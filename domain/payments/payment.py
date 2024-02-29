"""Payment Module"""
import uuid
from domain.payments.discount import Discounts


class Payment:
    def __init__(self, payment_method, amount):
        self.reference = str(uuid.uuid4())
        self.payment_method = payment_method
        self.amount = amount
        self.discounts = Discounts()

    def add_discount(self, reason, discount_type, value):
        self.discounts.add_discount(reason, discount_type, value)

    def generate_payment(self):
        payment_dict = {
            "reference": self.reference,
            "payment_method": self.payment_method,
            "amount": self.amount,
            "discounts": self.discounts.generate_discounts_list(),
        }
        return payment_dict

    def __repr__(self):
        return str(self.generate_payment())
