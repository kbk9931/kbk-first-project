from _typeshed import Incomplete

class TaskUpdateRequest:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        status: Incomplete | None = None,
        flux: Incomplete | None = None,
        name: Incomplete | None = None,
        every: Incomplete | None = None,
        cron: Incomplete | None = None,
        offset: Incomplete | None = None,
        description: Incomplete | None = None,
    ) -> None: ...
    @property
    def status(self): ...
    @status.setter
    def status(self, status) -> None: ...
    @property
    def flux(self): ...
    @flux.setter
    def flux(self, flux) -> None: ...
    @property
    def name(self): ...
    @name.setter
    def name(self, name) -> None: ...
    @property
    def every(self): ...
    @every.setter
    def every(self, every) -> None: ...
    @property
    def cron(self): ...
    @cron.setter
    def cron(self, cron) -> None: ...
    @property
    def offset(self): ...
    @offset.setter
    def offset(self, offset) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, description) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
