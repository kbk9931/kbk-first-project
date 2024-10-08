from _typeshed import Incomplete

from influxdb_client.domain.expression import Expression

class CallExpression(Expression):
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, type: Incomplete | None = None, callee: Incomplete | None = None, arguments: Incomplete | None = None
    ) -> None: ...
    @property
    def type(self): ...
    @type.setter
    def type(self, type) -> None: ...
    @property
    def callee(self): ...
    @callee.setter
    def callee(self, callee) -> None: ...
    @property
    def arguments(self): ...
    @arguments.setter
    def arguments(self, arguments) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
