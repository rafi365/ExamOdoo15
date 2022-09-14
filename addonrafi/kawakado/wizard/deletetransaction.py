from odoo import api, fields, models

class DeleteTransaction(models.TransientModel):
    _name = 'kawakado.deletetransaction'

    transaction_id = fields.Many2one(comodel_name='kawakado.transaction', string='Transaction', required=True)

    def button_transaction_delete(self):
        for line in self:
            self.env['kawakado.transaction'].search([('id', '=', line.transaction_id.id)]).unlink()