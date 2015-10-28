#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01"""


def sum_orders(customers, orders):
    """Putting these dictionaries together

    Args:
        customers (dict): A dictionary of customers keyed by customer_id
        orders (dict): A dictionary of orders keyed by order id

        Returns:
            Return the combined dictionary
    """
    combination = {}
    for order in orders.itervalues():
        if order['customer_id'] not in combination:
            combination[order['customer_id']] = {'total': order['total']}
            combination[order['customer_id']]['orders'] = 1
            combination[order['customer_id']].update(customers
                                                     [order['customer_id']])
        else:
            combination[order['customer_id']]['total'] += order['total']
            combination[order['customer_id']]['orders'] += 1
    return combination
