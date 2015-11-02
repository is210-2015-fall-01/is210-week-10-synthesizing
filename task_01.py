#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Correlates two related data sets."""


def sum_orders(customers, orders):
    """This function returns a combined dictionary with customer info.
    Args:
    customers (dict): dictionary of customers keyed by customer_id
    orders (dict): dicitonary of customers keyed by order id

    Returns:
    customer_id (dict): a combined dictionary that includes 'name',
                        'email', 'orders', 'total'

    Examples:
    >>> print sum_orders(customers = CUSTOMERS, orders = ORDERS)
    >>>
    {2: {'email': 'email@one.com', 'total': 20, 'orders': 2,
     'name': 'Person One'}, 3: {'email': 'email@two.com',
     'total': 15, 'orders': 1, 'name': 'Person Two'}}

    """
    cdict = {}
    for customer_id1, info1 in customers.iteritems():
        ordr_num = 0
        ordr_total = 0
        for ordr in orders.itervalues():
            if customer_id1 == ordr.get('customer_id'):
                ordr_num += 1
                ordr_total += ordr.get('total')
            cdict[customer_id1] = {'name': info1.get('name'),
                                   'email': info1.get('email'),
                                   'orders': ordr_num,
                                   'total': ordr_total}
        return cdict
    

ORDERS = {1: {'customer_id': 2, 'total': 10},
          3: {'customer_id': 2, 'total': 10},
          4: {'customer_id': 3, 'total': 15}}
CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
             3: {'name': 'Person Two', 'email': 'email@two.com'}}
print sum_orders(customers=CUSTOMERS, orders=ORDERS)
