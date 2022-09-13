from odoo import api, fields, models
import random

class Transaction(models.Model):
    _name = 'kawakado.transaction'
    _description = 'Transact model'

    def get_orderID(self):
        tgl_lap = fields.Date.today()
        return tgl_lap.strftime("%d/%m/%Y")+"/"+hex(random.getrandbits(24)).lstrip("0x").rstrip("L")

    name = fields.Char(string='order id',default=get_orderID)
    company_ids = fields.Many2many('kawakado.company', string='Buying Company')
    transaction_ids = fields.One2many('kawakado.transaction_details', 'transaction_id', string='Transaction')

class TransactionDetails(models.Model):
    _name = 'kawakado.transaction_details'
    _description = 'detail of transaction'

    name = fields.Many2one('kawakado.published', string='Title')
    transaction_id = fields.Many2one('kawakado.transaction', string='Transaction')
    amount = fields.Integer(string='Amount')
    
