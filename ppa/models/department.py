from odoo import models, fields


class  Department(models.Model) :
    _inherit = 'hr.department'
    project_ids  = fields.One2many('project.project', 'department_id', string='Projects')


