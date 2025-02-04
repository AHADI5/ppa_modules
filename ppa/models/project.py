

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
    employee_id = fields.Many2one('hr.employee', string='Project Manager', compute='_set_project_manager')
    currency_id = fields.Many2one('res.currency')

    @api.depends('department_id')
    def _set_project_manager(self):
        """When a department is set it's manager is set as the Project manager of that project"""
        self.employee_id = self.department_id.manager_id

    @api.constrains('department_id')
    def _check_department_manager(self):
        """If the department exists and has no manager assigned ,
         invite the user to setit using RedirectWarning"""

        action = self.env.ref('ppa.department_manager_setup_action').id
        if self.department_id and not self.department_id.manager_id:
            raise RedirectWarning(
                "No manager Set" ,
                action,
                "Set Manager" ,
                {'active_id': self.department_id.id}
            )

