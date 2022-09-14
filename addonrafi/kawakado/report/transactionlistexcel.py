from odoo import models ,fields
class PartnerXlsx(models.AbstractModel):
    _name = 'report.kawakado.report_kawakado.transaction_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    tgl_lap = fields.Date.today()
    def concator(self,obj):
        result = ""
        for i in obj:
            result += str(i.name)+", "
        return result
    def unpacker(self,obj):
        result = []
        for i in obj:
            result.append(i.name)
        return result
    def generate_xlsx_report(self, workbook, data, transaction):
        sheet = workbook.add_worksheet('transaction')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap),bold)
        sheet.write(1, 0, 'Order ID',bold)
        sheet.write(1, 1, 'Company Names',bold)
        sheet.write(1, 2, 'Items',bold)
        row = 2
        col = 0
        for obj in transaction:
            col = 0
            sheet.set_column(row, col, 50)
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, self.concator(obj.company_ids))
            sheet.write(row, col+2, self.concator(self.unpacker(obj.transaction_ids)))
            row += 1