#!user/bin/env python
# -*- coding: utf-8 -*-
"""Week 10 Synthesizing"""


def sum_orders(customers, orders):
    """Sorts information from two different dictionaroes to make new dictionary
       and sum orders
    Args:
        customers (dict): Dict with cust number as key, with 'name' and 'email'
        as keys of nested dict.
        orders (dict): Dict containing order number, customer ID corresponding
        to ID in customers and order total
    Returns:
        New dictionary with combined information and sum of order totals and
        number of orders per cust.
    Example:
        ORDERS = {1: {'customer_id': 1, 'total': 20},
                  3: {'customer_id': 1, 'total': 40},
                  4: {'customer_id': 5, 'total': 55}}
        CUSTOMERS = {1: {'name': 'Alex', 'email': 'email1@gmail.com'},
                     5: {'name': 'Nick', 'email': 'email2@gmail.com'}}
        >>>{1: {'orders': 2, 'total': 60, 'name': 'Alex', 'email':
                'email1@gmail.com'}, 5: {'orders': 1, 'total': 55, 'name':
                'Nick', 'email': 'email2@gmail.com'}}
        """
    newdict = {}
    for dummy, value in orders.iteritems():  # dummy becuase variable not used
        custkey = value['customer_id']
        if custkey not in newdict:
            newdict[custkey] = {}
            newdict[custkey]['name'] = customers[custkey]['name']
            newdict[custkey]['email'] = customers[custkey]['email']
            newdict[custkey]['total'] = value['total']  # first declare of value
            newdict[custkey]['orders'] = 1
        else:
            newdict[custkey]['total'] += value['total']  # accumulate values
            newdict[custkey]['orders'] += 1              # 2+ times through loop

    return newdict
