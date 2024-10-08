from ctypes import Structure
from typing import Any

logger: Any

def load_geos() -> Any: ...

NOTICEFUNC: Any

def notice_h(fmt: Any, lst: Any) -> None: ...

ERRORFUNC: Any

def error_h(fmt: Any, lst: Any) -> None: ...

class GEOSGeom_t(Structure): ...
class GEOSPrepGeom_t(Structure): ...
class GEOSCoordSeq_t(Structure): ...
class GEOSContextHandle_t(Structure): ...

GEOM_PTR: Any
PREPGEOM_PTR: Any
CS_PTR: Any
CONTEXT_PTR: Any
lgeos: Any

class GEOSFuncFactory:
    argtypes: Any = ...
    restype: Any = ...
    errcheck: Any = ...
    func_name: Any = ...
    def __init__(
        self,
        func_name: Any,
        *,
        restype: Any | None = ...,
        errcheck: Any | None = ...,
        argtypes: Any | None = ...
    ) -> None: ...
    def __call__(self, *args: Any) -> Any: ...
    def func(self) -> Any: ...

def geos_version() -> Any: ...
def geos_version_tuple() -> Any: ...
