#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 10 synthesizing task_01."""


def sum_orders(customers, orders):
    """This function will combine data into single dictionary.

    This function will be correlating two related data sets and combined
    into single dictionary.

    Args:
        customers (dict): A dictionary of customers keyed by customer_id.
        orders (dict): A dictionary of orders keyed by order id.

    Returns:
        Returns combined dictionary.

    Examples:
        >>> ORDERS = {1: {'customer_id': 2, 'total': 10},
              3: {'customer_id': 2, 'total': 10},
              4: {'customer_id': 3, 'total': 15}}
        >>> CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
                 3: {'name': 'Person Two', 'email': 'email@two.com'}}
        >>> sum_orders(customers=CUSTOMERS, orders=ORDERS){
        2: {'name': 'Person One',
        'email': 'email@one.com',
        'orders': 2,
        'total': 20}
        3: {'name': 'Person Two',
        'email': 'email@two.com',
        'orders': 1,
        'total': 15}}
    """

    combine_dict = {}
    for key in orders.values():
        cid = key['customer_id']
        total = key['total']
        if cid in combine_dict:
            combine_dict[cid]['total'] += total
            combine_dict[cid]['orders'] += 1
        else:
            combine_dict.update({cid: {'total': total}})
            combine_dict[cid].update({'orders': 0})
            combine_dict[cid]['orders'] += 1
            combine_dict[cid].update(customers[cid])
    return combine_dict
