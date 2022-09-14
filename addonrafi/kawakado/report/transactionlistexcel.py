from odoo import models ,fields
from datetime import timedelta
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
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, self.concator(obj.company_ids))
            sheet.write(row, col+2, self.concator(self.unpacker(obj.transaction_ids)))
            # for xxx in obj.detailtransaction_ids:
            #     sheet.set_column(col+5, col+5, 50)
            #     sheet.set_row(row, 100)  # Set the height of Row 1 to 20.
            #     sheet.write(row, col+4, f"""Name : {xxx.barang_id.name}
            #     qty : {xxx.qty}
            #     subtotal : {xxx.subtotal}
            #     """)
            #     col += 1
            row += 1