# -*- coding: utf-8 -*-
# from odoo import http


# class ViseducatCore(http.Controller):
#     @http.route('/viseducat_core/viseducat_core/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/viseducat_core/viseducat_core/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('viseducat_core.listing', {
#             'root': '/viseducat_core/viseducat_core',
#             'objects': http.request.env['viseducat_core.viseducat_core'].search([]),
#         })

#     @http.route('/viseducat_core/viseducat_core/objects/<model("viseducat_core.viseducat_core"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('viseducat_core.object', {
#             'object': obj
#         })
