import json


class Order:
    def __init__(self, order_id: int):
        self.order_id = order_id
        ## add more attributes here

    def to_json(self):
        return json.dumps(self,
                          default=lambda o: o.__dict__,
                          sort_keys=True,
                          indent=4)

    # Add more functions here


if __name__ == '__main__':
    o = Order(order_id=1)
    print(o.to_json())
