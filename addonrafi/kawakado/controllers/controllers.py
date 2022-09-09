# -*- coding: utf-8 -*-
# from odoo import http


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
