from _typeshed import Incomplete

from braintree.add_on import AddOn
from braintree.discount import Discount
from braintree.resource import Resource

class Plan(Resource):
    add_ons: list[AddOn]
    discounts: list[Discount]
    def __init__(self, gateway, attributes) -> None: ...
    @staticmethod
    def all(): ...
    @staticmethod
    def create(params: Incomplete | None = None): ...
    @staticmethod
    def find(subscription_id): ...
    @staticmethod
    def update(subscription_id, params: Incomplete | None = None): ...
    @staticmethod
    def create_signature(): ...
    @staticmethod
    def update_signature(): ...
