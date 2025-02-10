from email.policy import default

from odoo import models, fields, api
from odoo.exceptions import RedirectWarning, ValidationError


class Project(models.Model):
    _inherit = 'project.project'

    # Model Constraints
    _sql_constraints = [
        ('check_allocated_amount_positive', 'CHECK (allocated_amount > 0.00)',
         'The project amount must be Strictly Positive')
    ]

    allocated_amount = fields.Monetary(string='Allocated Amount')
    department_id = fields.Many2one('hr.department', string='Department')
    user_id = fields.Many2one('res.users', compute = '_set_project_manager' , readonly = True)
    currency_id = fields.Many2one('res.currency')

    @api.depends('department_id')
    def _set_project_manager(self):
        """When a department is set its manager is set as the Project manager of that project"""
        employee_id  = self.department_id.manager_id
        self.user_id = employee_id.user_id
        print("Related manager user set successfully", employee_id.user_id)

    @api.constrains('department_id')
    def _check_department_manager(self):
        """If the department exists and has no manager assigned ,
         invite the user to setit using RedirectWarning"""

        action = self.env.ref('av_project.department_manager_setup_action').id
        if self.department_id and (not self.department_id.manager_id or not self.department_id.manager_id.user_id):
            raise RedirectWarning(
                "No manager Set , Please try to assign the selected department with a manager of if set , "
                "try to associate the manager with an existing user" ,
                action,
                "Set Manager" ,
                {'active_id': self.department_id.id}
            )

