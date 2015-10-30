#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module correlates two related data sets."""


def sum_orders(customers, orders):
    """Combines the two datasets--customers & orders--into a single dictionary.

    Args:
        customers (dict): A dictionary of customers keyed by customer_id
        orders (dict): A dictionary of orders keyed by order id

    Returns:
        cust_dict: a dictionary created by combining customers and orders

    Examples:
        ORDERS = {1: {'customer_id': 2, 'total': 10},
              3: {'customer_id': 2, 'total': 10},
              4: {'customer_id': 3, 'total': 15}}
        CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
                 3: {'name': 'Person Two', 'email': 'email@two.com'}}
        >>> pprint.pprint(sum_orders(data.CUSTOMERS, data.ORDERS))
        {2: {'email': 'email@one.com', 'name': 'Person One', 'orders': 2,
        'total': 20},
         3: {'email': 'email@two.com', 'name': 'Person Two', 'orders': 1,
        'total': 15}}
    """
    cust_dict = {}  # initialize cust_dict
    for cust_id1, cust_info in customers.iteritems():
        num_orders = 0
        running_total = 0
        for order in orders.itervalues():
            if cust_id1 == order.get('customer_id'):
                num_orders += 1
                running_total += order.get('total')
        if num_orders > 0:  # only use customers who've placed orders
            cust_dict[cust_id1] = {'name': cust_info.get('name'),
                                   'email': cust_info.get('email'),
                                   'orders': num_orders,
                                   'total': running_total}
    return cust_dict
