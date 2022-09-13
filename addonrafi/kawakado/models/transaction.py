from odoo import api, fields, models


class Transaction(models.Model):
    _name = 'kawakado.transaction'
    _description = 'Transact model'

    name = fields.Char(string='order id')
    company_ids = fields.Many2many('kawakado.company', string='Buying Company')
    transaction_ids = fields.One2many('kawakado.transaction_details', 'transaction_id', string='Transaction')

class TransactionDetails(models.Model):
    _name = 'kawakado.transaction_details'
    _description = 'detail of transaction'

    name = fields.Many2one('kawakado.published', string='Title')
    transaction_id = fields.Many2one('kawakado.transaction', string='Transaction')
    amount = fields.Integer(string='Amount')
    
