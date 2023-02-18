# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class proyecto2(models.Model):
#     _name = 'proyecto2.proyecto2'
#     _description = 'proyecto2.proyecto2'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api
from odoo.exceptions import ValidationError

Class studio(models.model):
    _name='proyecto2.studio'
    name = fields.Char('nombre', required=True)


Class generos(models.model):
    _name='proyecto2.generos'
    _descrption ='Permite registrar el nombre de la pelicula'

    name = fields.Char('nombre', required=True)
    description = fields.Char('descripción', required=True)
    
Class peliculas(models.model):
    _name='proyecto2.peliculas'
    _description='Permite definir el tipo de pelicula'
    _order='name'
    
    name = fields.Char('categoria', required=True)
    categoria = fields.Char('categoria', required = True)
    #store=True
    fecha = fields.Date('fecha',compute='_get fecha', store=True)
    
    @api.constrains('fecha')
    def get_fecha(self):
        for peliculas in self:
            if peliculas.fecha > datetime.today())
                raise ValidationError("Esta pelicula no se encuentra disponible: %s" % peliculas.fecha)
            
    
            