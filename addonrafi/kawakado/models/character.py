from odoo import api, fields, models


class Character(models.Model):
    _name = 'kawakado.character'
    _description = 'character class'

    name = fields.Char(string='Character Name')
    desc = fields.Text(string='Character Description')
    va_id = fields.Many2one('kawakado.voiceactor', string='Voice Actor')
    published_ids = fields.Many2many('kawakado.published', string='Featured In')
    
