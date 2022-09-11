from odoo import api, fields, models


class Character(models.Model):
    _name = 'kawakado.character'
    _description = 'character class'

    name = fields.Char(string='Character Name')
    desc = fields.Char(string='Character Description')
    va_id = fields.Many2one('kawakado.voiceactor', string='Voice Actor')
    
