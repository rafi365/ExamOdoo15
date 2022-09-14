from odoo import api, fields, models


class Person(models.Model):
    _name = 'kawakado.person'
    _description = 'New Description'

    name = fields.Char(string='Name')
    alamat = fields.Char(string='Address')
    tgl_lahir = fields.Datetime(string='BirthDate')


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