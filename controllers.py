# -*- coding: utf-8 -*-
from openerp import http

# class Chasqui(http.Controller):
#     @http.route('/chasqui/chasqui/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/chasqui/chasqui/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('chasqui.listing', {
#             'root': '/chasqui/chasqui',
#             'objects': http.request.env['chasqui.chasqui'].search([]),
#         })

#     @http.route('/chasqui/chasqui/objects/<model("chasqui.chasqui"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('chasqui.object', {
#             'object': obj
#         })