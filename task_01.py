#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Getting four pieces of information about a single customer"""


import data


def sum_orders(customers, orders):
    """This function will calculate customer orders.

    Args:
        It takes two arguments; customers and orders.

    Returns:
        A dictionary

    Examples:
        >>>
        {'email': 'evorsoisson@komarr.net', 'total': 1287, 'orders': 3,...)
    """
    new_dict = {}
    for outer_key, outer_value in customers.iteritems():
        new_key = outer_key
        new_value = outer_value
        temp_dict = {}
        real_orders = 0
        total_sum = 0
        for inner_value in orders.itervalues():
            inner_dict = inner_value
            customer_id = inner_dict['customer_id']
            if customer_id is new_key:
                real_orders = real_orders + 1
                total_sum = total_sum + inner_dict['total']
        temp_dict['orders'] = real_orders
        temp_dict['total'] = total_sum
        temp_dict['name'] = new_value['name']
        temp_dict['email'] = new_value['email']
        new_dict[new_key] = temp_dict
    return new_dict
sum_orders(data.CUSTOMERS, data.ORDERS)
