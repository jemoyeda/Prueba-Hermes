from odoo import models, fields

#creando un modelo a partir de una clase
class Libros(models.Model):
    _name = 'colores'

    color = fields.Char(string="Color")
    talla = fields.Char(string="Talla")
    
    
    
