# -*- coding: utf-8 -*-
{
    'name': "My project ",
    'summary': """My project model""",
    'description': """Managing project information""",
    'author': "myCompany.info",
    'website': "https://www.tma.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'product',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/my_project_views.xml',
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}