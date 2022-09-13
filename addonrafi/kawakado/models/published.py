from odoo import api, fields, models


class Published(models.Model):
    _name = 'kawakado.published'
    _description = 'Published Works'

    name = fields.Char(string='Title')
    works_type = fields.Selection(string='Type', selection=[('anime', 'Anime'), ('manga', 'Manga'),])
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