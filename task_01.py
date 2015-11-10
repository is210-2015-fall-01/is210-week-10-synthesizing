# usr/bin/env/python
# -*- coding: utf-8 -*-
"""dictionaries"""


def sum_orders(customers, orders):
    """Docstring explaining what each arguments mean.

    Args:
        customers (dict): A dictionary of customers keyed by customer_id.
        orders (dict): A dictionary of orders keyed by order id.

    Returns:
        (dict): the combined dictionary of customers and orders.
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
    customer_list = {}
    for key, value in customers.iteritems():
        total_orders = 0
        number_orders = 0
        for request in orders.values():
            if key == request['customer_id']:
                total_orders += request['total']
                number_orders += 1
                customer_list[key] = {'name': value['name'],
                                      'email': value['email'],
                                      'orders': number_orders,
                                      'total': total_orders}
    return customer_list
