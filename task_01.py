#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is task_01 docstring."""


def sum_orders(customers, orders):
    """This is the sum_orders docstring.

    This function creates searches in two given dictionaries, customers{}
    and orders{} as an argument, and returns another dictionary, which
    contains the total number and amount of order a customer has placed.

    Args:
        customers (dict): A dictionary of the form:
                          {1: {'name': 'Joe', 'email': 'joe@email.com'}}
        orders (dict): A dictionary of the form:
                       {1: {'customer_id': 1, 'total': 8}}

    Returns:
        sum_orders (dict): A dictionary with the sum of customer orders.

    Example:
        >>> ORDERS = {1: {'customer_id': 1, 'total': 8},
     2: {'customer_id': 2, 'total': 12},
     3: {'customer_id': 2, 'total': 36},
     4: {'customer_id': 3, 'total': 22}}

        >>> CUSTOMERS = {1: {'name': 'Joe', 'email': 'joe@email.com'},
     2: {'name': 'Jack', 'email': 'jack@email.com'},
     3: {'name': 'Jill', 'email': 'jill@email.com'},
     4: {'name': 'paco', 'email': 'paco@email.com'}}

        >>> sum_orders(CUSTOMERS, ORDERS)
    {1: {'orders': 1, 'total': 8, 'name': 'Joe', 'email': 'joe@email.com'},
     2: {'orders': 2, 'total': 48, 'name': 'Jack', 'email': 'jack@email.com'},
     3: {'orders': 1, 'total': 22, 'name': 'Jill', 'email': 'jill@email.com'}}
"""
    my_dict = {}
    for cust_key, cust_value in customers.iteritems():
        total_orders = 0
        num_orders = 0
        for order in orders.values():
            if cust_key == order['customer_id']:
                total_orders += order['total']
                num_orders += 1
                my_dict[cust_key] = {'name': cust_value['name'],
                                     'email': cust_value['email'],
                                     'orders': num_orders,
                                     'total': total_orders}
    return my_dict
