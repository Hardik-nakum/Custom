# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'author': 'Hardik Nakum',
    'category': 'Hospital',
    'summary': 'Hospital Management System',
    'description': """Hospital Management""",
    'depends': [
        'mail'
    ],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'views/doctor_view.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'application': True,
    'sequence': -200,
}
