# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError



class Vehiculo(models.Model):
    # Cada registro es un coche o una moto que tiene el concesionario
    _name = "concesionario.vehiculo"
    _description = "Vehículo del concesionario"

    # CAMPOS
    name = fields.Char(string="Modelo", required=True, help="Modelo del vehículo")
    marca = fields.Char(string="Marca", required=True, help="Marca del vehículo")
    matricula = fields.Char(string="Matrícula", help="Matrícula del vehículo")

    
    tipo = fields.Selection(
        selection=[("coche", "Coche"), ("moto", "Moto")],
        string="Tipo", required=True, default="coche")
   
    estado = fields.Selection(
        selection=[("disponible", "Disponible"), ("reservado", "Reservado"), ("vendido", "Vendido")],
        string="Estado", required=True, default="disponible")
    kilometraje = fileds.Float(string="Kilometros", required=True, help="Kilometros de vehiculo")
    
    combustible = fields.Selection(
        selection=[("gasolina", "Gasolina"), ("diesel", "Diésel"),
                   ("electrico", "Eléctrico"), ("hibrido", "Híbrido")],
        string="Combustible", default="gasolina")

    fecha_matriculacion = fields.Date(string="Fecha de matriculación")      
    
    fecha_alta = fields.Datetime(string="Fecha de alta en el concesionario",  
                                 default=fields.Datetime.now)

    foto = fields.Binary(string="Foto")                                       
    
    precio = fields.Float(string="Precio", required=True)
    
    descuento = fields.Float(string="Descuento (%)", default=0.0)
    
    precio_final = fields.Float(string="Precio final", compute="_compute_precio_final", store=True)
    
    antiguedad = fields.Integer(string="Antigüedad (años)")
    
    #RELACIONES
        


    #METODOS
    @api.depends("precio", "descuento")
    def _compute_precio_final(self):
            # Calcula el precio final restando el descuentoSi el descuento no es válido lanza una excepción
            for record in self:
                if record.descuento < 0 or record.descuento > 100:
                    raise ValidationError("El descuento tiene que estar entre 0 y 100.")
                record.precio_final = record.precio - (record.precio * record.descuento / 100)
       