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
        'views/cliente_view.xml',
        'views/vehiculo_view.xml',
        'views/venta_view.xml',
        'views/extra_view.xml',
        'views/menu.xml',

    ],

    # Datos de prueba 
    'demo   ': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
}
