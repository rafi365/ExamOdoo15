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

    def write(self, vals):
        for i in self:
            for line in i:
                penjualan = i.env['kawakado.transaction_details'].search(
                    [('transaction_id', '=', line.id)])

            for ob in penjualan:
                ob.name.items_sold -= ob.amount
      
        line = super(Transaction, self).write(vals)
        
        for line in self:
            data_setelah_edit = self.env['kawakado.transaction_details'].search(
                    [('transaction_id', '=', line.id)])
            for data_baru in data_setelah_edit:
                if data_baru in penjualan:
                    data_baru.name.items_sold += data_baru.amount
                else:
                    pass

        return line

    def unlink(self):
        for i in self:
            if i.transaction_ids:
                penjualan = []
                for line in i:
                    penjualan = i.env['kawakado.transaction_details'].search(
                        [('transaction_id', '=', line.id)])

                for ob in penjualan:
                    ob.name.items_sold -= ob.amount

        line = super(Transaction, self).unlink()
        return line
    

class TransactionDetails(models.Model):
    _name = 'kawakado.transaction_details'
    _description = 'detail of transaction'

    name = fields.Many2one('kawakado.published', string='Title')
    transaction_id = fields.Many2one('kawakado.transaction', string='Transaction')
    amount = fields.Integer(string='Amount')
    @api.model
    def create(self, vals):
        line = super(TransactionDetails, self).create(vals)
        if line.amount:
            # Mendapatkan data berdasarkan ID pada barang_id
            self.env['kawakado.published'].search(
                [('id', '=', line.name.id)]
            ).write({'items_sold': line.name.items_sold + line.amount})
        return line
    
    
