from _typeshed import Incomplete

class TemplateExportByID:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self, stack_id: Incomplete | None = None, org_ids: Incomplete | None = None, resources: Incomplete | None = None
    ) -> None: ...
    @property
    def stack_id(self): ...
    @stack_id.setter
    def stack_id(self, stack_id) -> None: ...
    @property
    def org_ids(self): ...
    @org_ids.setter
    def org_ids(self, org_ids) -> None: ...
    @property
    def resources(self): ...
    @resources.setter
    def resources(self, resources) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
