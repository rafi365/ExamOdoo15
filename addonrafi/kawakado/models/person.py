from odoo import api, fields, models


class Person(models.Model):
    _name = 'kawakado.person'
    _description = 'New Description'

    name = fields.Char(string='Name')
    alamat = fields.Char(string='Address')
    tgl_lahir = fields.Datetime(string='BirthDate')
    useless = fields.Char(string='onchange')
    uselessv2 = fields.Char(string='compute',compute="_oncomp")

    @api.onchange('name')
    def _onnamechange(self):
        for i in self:
            i.useless = i.name

    @api.depends('name')
    def _oncomp(self):
        for i in self:
            i.uselessv2 = i.name
    


class Ceo(models.Model):
    _name = 'kawakado.ceo'
    _inherit = 'kawakado.person'
    _description = 'New Description'

    id_ceo = fields.Char(string='ID CEO')


class CleaningService(models.Model):
    _name = 'kawakado.cleaningservice'
    _inherit = 'kawakado.person'
    _description = 'New Description'

    id_cln = fields.Char(string='ID Cleaning Service')