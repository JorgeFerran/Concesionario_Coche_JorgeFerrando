# -*- coding: utf-8 -*-
{
    'name': "Concesionario",
    'summary': "Gestión  concesionario de coches y motos",
    'description': "Aplicación para gestionar vehículos, clientes, ventas y extras",
    'author': "Jorge Ferrando Lafarga",
    'category': "Tools",
    'version': '0.1',
    'license': 'LGPL-3',

    # Módulos
    'depends': ['base'],

    
    'data': [
        'security/ir.model.access.csv',
        'views/concesionario_view.xml',
    ],

    # Datos de prueba 
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
}
