from distutils.unixccompiler import UnixCCompiler
from distutils.version import LooseVersion
from re import Pattern
from typing import Literal

def get_msvcr() -> list[str] | None: ...

class CygwinCCompiler(UnixCCompiler): ...
class Mingw32CCompiler(CygwinCCompiler): ...

CONFIG_H_OK: str
CONFIG_H_NOTOK: str
CONFIG_H_UNCERTAIN: str

def check_config_h() -> tuple[Literal["ok", "not ok", "uncertain"], str]: ...

RE_VERSION: Pattern[bytes]

def get_versions() -> tuple[LooseVersion | None, ...]: ...
def is_cygwingcc() -> bool: ...
