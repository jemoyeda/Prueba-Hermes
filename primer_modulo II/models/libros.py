from odoo import models, fields

#creando un modelo a partir de una clase
class Libros(models.Model):
    _name : 'libros'

    name = fields.Char(string="Nombre del libro")
    name = fields.Char(string="Categoria")
    name = fields.Float(string="precio de venta")
    
    
