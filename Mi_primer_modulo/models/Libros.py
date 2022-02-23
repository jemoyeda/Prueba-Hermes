from odoo import models, fields

#creando un modelo a partir de una clase
class Libros(models.model):
    _name : 'Libros'

    name = fields.char(string="Nombre del libro")
    name = fields.char(string="Categoria")
    name = fields.float(string="precio de venta")
    
    
