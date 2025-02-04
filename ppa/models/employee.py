from odoo import  models , fields

class Employee (models.Model):
    _inherit = 'hr.employee'
    project_ids = fields.One2many('project.project', 'employee_id', string='Projects')
