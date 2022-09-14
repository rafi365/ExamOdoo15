from odoo import api, fields, models


class FanMail(models.Model):
    _inherit = 'res.partner'
    _description = 'Fan Mailing list'

    is_sub = fields.Boolean(string='is Subscribe to mailing list?')
    
