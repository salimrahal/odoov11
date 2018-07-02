# -*- coding: utf-8 -*-
{
    'name': "Quotation Approval Level",

    'summary': """ 
    Append Approval level to quotation workflow: draft->approved->confirmed.
    The User should be added to the group: Approve quotation, in order to approve the quotation
    """
    ,
    'description': """
    
    """,

    'author': "salim.rahal@jcyared.com",
     "contributors": [
        "Salim Rahal <salim.rahal@jcyared.com>, Ali Atwi <Ali.atwi@jcyared.com>",
    ],
    'website': "www.jcyared.com",
    'price':'100',
    'currency': 'USD',
    "version": "8.0.1.0",
    'category': 'Sales',
    "license": "AGPL-3",
    'images': ['static/description/banner.png'],
    
    'depends': [
             'base', 'sale'],
    'installable':True,
    # always loaded
    'data': [
    'security/grp_approv.xml',
    #'security/ir.model.access.csv',
    'views/sale_order_extension.xml',
    #no longer exists in 11 'views/sale_order_workflow.xml'
    ],
     
    # only loaded in demonstration mode
    'demo': [
    ],
}
