# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Vehiculo(models.Model):
    # Cada registro es un coche o una moto que tiene el concesionario
    _name = "concesionario.vehiculo"
    _description = "Vehículo del concesionario"

    # CAMPOS
    name = fields.Char(string="Modelo", required=True, help="Modelo del vehículo")
    marca = fields.Char(string="Marca", required=True, help="Marca del vehículo")
    matricula = fields.Char(string="Matrícula", help="Matrícula del vehículo")

    #Selection
    tipo = fields.Selection(
        selection=[("coche", "Coche"), ("moto", "Moto")],
        string="Tipo", required=True, default="coche")
   
    estado = fields.Selection(
        selection=[("disponible", "Disponible"), ("reservado", "Reservado"), ("vendido", "Vendido")],
        string="Estado", required=True, default="disponible")
    combustible = fields.Selection(
        selection=[("gasolina", "Gasolina"), ("diesel", "Diésel"),
                   ("electrico", "Eléctrico"), ("hibrido", "Híbrido")],
        string="Combustible", default="gasolina")

    fecha_matriculacion = fields.Date(string="Fecha de matriculación")      
    fecha_alta = fields.Datetime(string="Fecha de alta en el concesionario",  
                                 default=fields.Datetime.now)
    