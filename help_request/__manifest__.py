# -*- coding: utf-8 -*-

{
    'name': 'Help request',
    'version': '1.0',
    'author': 'DSquare Net',
    'sequence': 80,
    'summary': 'Requests for help sent by company staff.',
    'license': 'OPL-1',
    'price':   25,
    'currency':   'EUR',
    'description': """
Help request Management
==================================
Help request is an obligatory solution in every company with a large number of employees and not only. 
There are difficulties, problems, questions everywhere. This module helps to manage requests and simplifies the process of solving problems. 
The submitter has an overview of the current status of the request. When the problem is solved, the employee will be informed about it.

The tool is designed primarily for IT Support, but it can also be used by other departments within the company.

Main features
-------------
* help requests
* status of the request
* easy management of the requests
* easy to send request

""",
    'category': 'Tool',
    'depends': [
        'base',
        'hr',
    ],
    'data': [
        'views/help_request_view.xml',
        'security/help_request_security.xml',
        'security/ir.model.access.csv',
    ],
    # 'images': ['static/description/it_dev.jpg'],
    'auto_install': False,
    'application': True,
    'installable': True,
}
