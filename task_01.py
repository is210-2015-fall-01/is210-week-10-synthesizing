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
        >>> Orders
    """
    customers_new = customers.copy()
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
            customers_new[cid]['orders'] = 1
            customers_new[cid]['total'] = order['total']
    return customers_new

if __name__ == "__main__":
    ORDERS = {1: {'customer_id': 2, 'total': 10},
              3: {'customer_id': 2, 'total': 10},
              4: {'customer_id': 3, 'total': 15}}
    CUSTOMERS = {2: {'name': 'Person One', 'email': 'email@one.com'},
                 3: {'name': 'Person Two', 'email': 'email@two.com'}}
    ORDER_SUM = sum_orders(customers=CUSTOMERS, orders=ORDERS)
    print ORDER_SUM
