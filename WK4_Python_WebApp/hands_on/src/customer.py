import json
from typing import List

from WK4_Python_WebApp.hands_on.src.order import Order


class Customer:
    def __init__(self, customer_id: int = None, orders: List[Order] = None):
        self.customer_id = customer_id
        self.orders = orders
        # add more attributes ...

    def to_json(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=4)

    # Add more functions here


if __name__ == '__main__':
    c = Customer(customer_id=1, orders=[Order(order_id=1)])
    print(c.to_json())