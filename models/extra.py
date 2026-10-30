# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields


class Extra(models.Model):
    #Clase EXTRA, se puede añadir extras al coche
    _name = "concesionario.extra"
    _description = "Extra para vehículos"

    name = fields.Char(string="Nombre", required=True, help="Nombre del extra")
    codigo = fields.Char(string="Código", help="Código interno del extra")
    categoria = fields.Selection(
        selection=[("seguridad", "Seguridad"), ("confort", "Confort"), ("tecnologia", "Tecnología")],
        string="Categoría", required=True, default="confort")
    descripcion = fields.Text(string="Descripción")
    precio = fields.Float(string="Precio", help="Precio del extra")