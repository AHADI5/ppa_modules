from email.policy import default

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Project(models.Model):
    _inherit = 'project.project'

    # Model Constraints
    _sql_constraints = [
        ('check_allocated_amount_positive', 'CHECK (allocated_amount > 0.00)',
         'The project amount must be Strictly Positive')
    ]

    allocated_amount = fields.Monetary(string='Allocated Amount')
    department_id = fields.Many2one('hr.department', string='Department' , required= True)
    user_id = fields.Many2one('res.users', compute = '_set_project_manager' , readonly = True)
    currency_id = fields.Many2one('res.currency')

    @api.depends('department_id')
    def _set_project_manager(self):
        """When a department is set its manager is set as the Project manager of that project"""
        employee_id  = self.department_id.manager_id
        self.user_id = employee_id.user_id

        if self.department_id and (not self.department_id.manager_id ):
            raise ValidationError("The department has no manager , please set it first")

        if  self.department_id  and not self.department_id.manager_id.user_id :
            raise ValidationError("Please Associate the existing Manager with a valid User")




