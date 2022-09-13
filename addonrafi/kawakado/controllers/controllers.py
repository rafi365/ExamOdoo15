# -*- coding: utf-8 -*-
# from odoo import http
from odoo import http,models,fields
from odoo.http import request
import json
from datetime import timedelta
class Kawakado(http.Controller):
    @http.route('/kawakado/listcatalogue', auth='public',method=['GET'])
    def getCatalogue(self, **kw):
        publ = request.env['kawakado.published'].search([])
        isi = []
        for bb in publ:
            isi.append({
                'Title' : bb.name,
                'Type' : bb.works_type_id.name,
                'status' : bb.status,
                'publish_date':(bb.publish_date+ timedelta(hours=7)).strftime("%d/%m/%Y"),
                'sold' : bb.items_sold,
            })
        return json.dumps(isi)


# class Kawakado(http.Controller):
#     @http.route('/kawakado/kawakado', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/kawakado/kawakado/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('kawakado.listing', {
#             'root': '/kawakado/kawakado',
#             'objects': http.request.env['kawakado.kawakado'].search([]),
#         })

#     @http.route('/kawakado/kawakado/objects/<model("kawakado.kawakado"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('kawakado.object', {
#             'object': obj
#         })
