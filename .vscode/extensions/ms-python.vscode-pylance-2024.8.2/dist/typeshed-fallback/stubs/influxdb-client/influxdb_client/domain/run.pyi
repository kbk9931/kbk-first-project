from _typeshed import Incomplete

class Run:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        id: Incomplete | None = None,
        task_id: Incomplete | None = None,
        status: Incomplete | None = None,
        scheduled_for: Incomplete | None = None,
        log: Incomplete | None = None,
        flux: str | None = None,
        started_at: Incomplete | None = None,
        finished_at: Incomplete | None = None,
        requested_at: Incomplete | None = None,
        links: Incomplete | None = None,
    ) -> None: ...
    @property
    def id(self): ...
    @id.setter
    def id(self, id) -> None: ...
    @property
    def task_id(self): ...
    @task_id.setter
    def task_id(self, task_id) -> None: ...
    @property
    def status(self): ...
    @status.setter
    def status(self, status) -> None: ...
    @property
    def scheduled_for(self): ...
    @scheduled_for.setter
    def scheduled_for(self, scheduled_for) -> None: ...
    @property
    def log(self): ...
    @log.setter
    def log(self, log) -> None: ...
    flux: str | None
    @property
    def started_at(self): ...
    @started_at.setter
    def started_at(self, started_at) -> None: ...
    @property
    def finished_at(self): ...
    @finished_at.setter
    def finished_at(self, finished_at) -> None: ...
    @property
    def requested_at(self): ...
    @requested_at.setter
    def requested_at(self, requested_at) -> None: ...
    @property
    def links(self): ...
    @links.setter
    def links(self, links) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
