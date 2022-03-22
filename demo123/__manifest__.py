# -*- coding: utf-8 -*-
{
    'name': "odooapp",
    'version': '14.0.0.1',
    'summary': 'Demo Module',
    'description': """
     This is a demo Module
    """,
    'author': "DataElite",
    'website': "http://www.odoo.yenthevg.com",
    'category': 'Demo',
    'installable': True,
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/user_groups.xml',
        'security/ir.model.access.csv',
        'views/backup_view.xml',
        'data/backup_data.xml',
    ],
    'images': ['static/description/icon.png'],
    'auto_install': False,
    # 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
}
