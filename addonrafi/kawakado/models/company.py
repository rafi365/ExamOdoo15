from odoo import api, fields, models


class Company(models.Model):
    _name = 'kawakado.company'
    _description = 'list of companies'

    name = fields.Char(string='Company Name')
    company_type = fields.Selection([
        ('studio', 'Studio'),
        ('publisher', 'Publisher')
    ], string='Company Type')
    address = fields.Char(string='Address')
    works_ids = fields.Many2many('kawakado.published', string='Published Work')
    

