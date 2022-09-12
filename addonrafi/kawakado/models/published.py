from odoo import api, fields, models


class Published(models.Model):
    _name = 'kawakado.published'
    _description = 'Published Works'

    name = fields.Char(string='Title')
    type = fields.Selection(string='Type', selection=[('anime', 'Anime'), ('manga', 'Manga'),])
    character_id = fields.Many2one('kawakado.character', string='character')
    status = fields.Selection([
        ('inproduction', 'In Production'),
        ('cancelled', 'Cancelled'),
        ('published', 'Published'),
        ('hiatus', 'Hiatus'),
    ], string='status')
    publish_date = fields.Date('Publish Date')
    company_ids = fields.Many2many('kawakado.company', string='Produced By')
    items_sold = fields.Integer('Items Sold')
    # cover image?
    # staff involved?