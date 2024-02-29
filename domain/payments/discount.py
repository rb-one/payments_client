"""Discounts Module"""


class Discounts:
    def __init__(self):
        self.discount_list = []

    def add_discount(self, reason, discount_type, value):
        discount = {
            "reason": reason,
            "discount_type": discount_type,
            "value": value,
        }
        self.discount_list.append(discount)

    def generate_discounts_list(self):
        return self.discount_list
