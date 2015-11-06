#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""module for correlating two related data sets"""


def sum_orders(customers, orders):
    """combines two data sets into a single dictionary.

    Args:
        customers (dict): A dictionary of customers keyed by customer_id.
        orders (dict): A dictionary of orders keyed by order id.

    Returns:
        cust_dict: A dictionary of customers and orders.

    Examples:
        >>> ORDERS = {1: {'customer_id': 2, 'total': 10},
              3: {'customer_id': 2, 'total': 10},
              4: {'customer_id': 3, 'total': 15}}
        >>> CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
                 3: {'name': 'Person Two', 'email': 'email@two.com'}}
        >>> sum_orders(customers=CUSTOMERS, orders=ORDERS)
        {2: {'name': 'Person One',
        'email': 'email@one.com',
        'orders': 2,
        'total': 20}
         3: {'name': 'Person Two',
             'email': 'email@two.com',
             'orders': 1,
             'total': 15}}
    """
    customer_dict = {}
    for customer_key, customer_value in customers.iteritems():
        total_orders = 0
        num_orders = 0
        for order in orders.values():
            if customer_key == order['customer_id']:
                total_orders += order['total']
                num_orders += 1
                customer_dict[customer_key] = {'name': customer_value['name'],
                                               'email': customer_value['email'],
                                               'orders': num_orders,
                                               'total': total_orders}
    return customer_dict
