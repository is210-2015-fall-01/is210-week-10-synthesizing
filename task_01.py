#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Wk 10 synthesizing."""


def sum_orders(customers, orders):
    """This function combines two dataset,
        into a single dictionary.
    Args:
        Customer(dict)
        orders(dict)
    Returns:
        Returns the combined dictionary.
    Examples:
            ORDERS = {1: {'customer_id': 2, 'total': 10},
            3: {'customer_id': 2, 'total': 10},
            4: {'customer_id': 3, 'total': 15}}
    """
    customers_new = {}
    for _, order in orders.items():
        cid = order['customer_id']
        if cid in customers_new:
            if 'orders' not in customers_new[cid]:
                customers_new[cid]['orders'] = 1
                customers_new[cid]['total'] = order['total']
            else:
                customers_new[cid]['orders'] += 1
                customers_new[cid]['total'] += order['total']
        else:
            customers_new[cid] = {}
            customers_new[cid]['email'] = customers[cid]['email']
            customers_new[cid]['name'] = customers[cid]['name']
            customers_new[cid]['orders'] = 1
            customers_new[cid]['total'] = order['total']
    return customers_new

if __name__ == "__main__":
    import data
    import pprint
    pprint.pprint(sum_orders(customers=data.CUSTOMERS, orders=data.ORDERS))
