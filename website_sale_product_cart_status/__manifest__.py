# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    'name': 'Product Cart Status',
    'version': '11.0.1.0.0',
    'author': 'Quartile Limited',
    'website': 'https://www.quartile.co',
    'category': 'Website',
    'license': "AGPL-3",
    'description': """
This module adds cart_in field to product and update the field when the 
product is being added to cart.
    """,
    'depends': [
        'website_sale',
        'stock_quant_list_view',
    ],
    'data': [
        'views/stock_quant_views.xml',
    ],
    'installable': True,
}
