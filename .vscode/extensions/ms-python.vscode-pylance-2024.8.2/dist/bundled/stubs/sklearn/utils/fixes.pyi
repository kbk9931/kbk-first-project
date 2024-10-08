import sys
from importlib import resources as resources
from typing import Literal, Mapping

import numpy as np
import scipy
import scipy.stats
import sklearn
import threadpoolctl
from numpy import percentile as percentile
from scipy.linalg import eigh as _eigh
from scipy.optimize.linesearch import line_search_wolfe1 as line_search_wolfe1, line_search_wolfe2 as line_search_wolfe2
from threadpoolctl import _ThreadpoolLimiter

from ..externals._lobpcg import lobpcg as lobpcg
from ..externals._packaging.version import parse as parse_version
from .deprecation import deprecated
from .parallel import delayed

np_version = ...
sp_version = ...

class loguniform(scipy.stats.reciprocal): ...

def threadpool_limits(
    limits: None | Mapping | str | int = None,
    user_api: None | Literal["blas", "openmp"] = None,
) -> _ThreadpoolLimiter: ...

threadpool_limits.__doc__ = ...

def threadpool_info() -> list[dict[str, int | str] | dict[str, str | None | int]]: ...

threadpool_info.__doc__ = ...

@deprecated(
    "The function `delayed` has been moved from `sklearn.utils.fixes` to "
    "`sklearn.utils.parallel`. This import path will be removed in 1.5."
)
def delayed(function): ...
