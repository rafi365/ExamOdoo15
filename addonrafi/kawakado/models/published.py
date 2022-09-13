from odoo import api, fields, models


class Published(models.Model):
    _name = 'kawakado.published'
    _description = 'Published Works'

    name = fields.Char(string='Title')
    works_type_id = fields.Many2one('kawakado.published_types', string='Type',ondelete='cascade')
    character_ids = fields.Many2many('kawakado.character', string='Characters')
    status = fields.Selection([
        ('inproduction', 'In Production'),
        ('cancelled', 'Cancelled'),
        ('published', 'Published'),
        ('hiatus', 'Hiatus'),
    ], string='status')
    publish_date = fields.Date('Publish Date')
    company_ids = fields.Many2many('kawakado.company', string='Produced By')
    items_sold = fields.Integer('Items Sold')
    transaction_detail_ids = fields.One2many('kawakado.transaction_details', 'name', string='Transaction Detail')
    # cover image?
    # staff involved?

class Published_Types(models.Model):
    _name = 'kawakado.published_types'
    _description = 'types of published work'

    name = fields.Char(string='Type Name')
    desc = fields.Char(string='Description')
    published_ids = fields.One2many('kawakado.published', 'works_type_id', string='Works')
    
