from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'
     
    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        res = super(ProductTemplate, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        for access_id in self.env['ir.model'].sudo().search([('name','=','Product Template')]).access_ids:
            if access_id.group_id.name != "Create Product":
                access_id.sudo().write({'perm_create' : False})
        return res
 
class ProductProduct(models.Model):
    _inherit = 'product.product'
      
    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        res = super(ProductProduct, self).fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        for access_id in self.env['ir.model'].sudo().search([('name','=','Product')]).access_ids:
            if access_id.group_id.name != "Create Product":
                access_id.sudo().write({'perm_create' : False})
        return res