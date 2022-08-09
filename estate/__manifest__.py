{
    'name': 'Real Estate',
    'version': '1.0.0',
    'author': 'Hardik',
    'sequence': -100,
    'description': "Real estate module",
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'depends':['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_menus.xml',
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag_views.xml',
    ],
}
