from odoo import api, fields, models


class VoiceActor(models.Model):
    _name = 'kawakado.voiceactor'
    _description = 'voiceactor class'

    name = fields.Char(string='VA Name')
    gender = fields.Selection(string='Gender', selection=[('male', 'Male'), ('female', 'Female'),])
    desc = fields.Text(string='Description')
    character_ids = fields.One2many('kawakado.character', 'va_id', string='character')

