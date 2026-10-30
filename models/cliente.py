# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError


class Cliente(models.Model):
   
    _name = "concesionario.cliente"
    _description = "Cliente del concesionario"

    #CAMPOS
    name = fields.Char(string="Nombre completo", required=True, help="Nombre y apellidos del cliente")
   
    dni = fields.Char(string="DNI", required=True, help="DNI del cliente")
    
    telefono = fields.Char(string="Teléfono")
    
    email = fields.Char(string="Email")

    tipo_cliente = fields.Selection(
        selection=[("particular", "Particular"), ("empresa", "Empresa")],
        string="Tipo de cliente", required=True, default="particular")

    fecha_nacimiento = fields.Date(string="Fecha de nacimiento")               
    fecha_registro = fields.Datetime(string="Fecha de registro",               
                                     default=fields.Datetime.now)
    foto = fields.Binary(string="Foto")                                                                     

    edad = fields.Integer(string="Edad")
    

   