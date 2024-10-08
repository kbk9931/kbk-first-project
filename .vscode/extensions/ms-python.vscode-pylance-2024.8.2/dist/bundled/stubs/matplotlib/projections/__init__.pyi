from typing import Callable

class ProjectionRegistry:
    def __init__(self) -> None: ...
    def register(self, *projections) -> None: ...
    def get_projection_class(self, name): ...
    def get_projection_names(self) -> list: ...

projection_registry: ProjectionRegistry = ...

def register_projection(cls) -> None: ...
def get_projection_class(projection=...): ...

get_projection_names: Callable = ...
