import _win32typing

def CreateEnvironmentBlock(Token: int, Inherit): ...
def DeleteProfile(SidString: str, ProfilePath: str | None = ..., ComputerName: str | None = ...) -> None: ...
def ExpandEnvironmentStringsForUser(Token: int, Src: str) -> str: ...
def GetAllUsersProfileDirectory() -> str: ...
def GetDefaultUserProfileDirectory() -> str: ...
def GetEnvironmentStrings(): ...
def GetProfilesDirectory() -> str: ...
def GetProfileType(): ...
def GetUserProfileDirectory(Token: int) -> str: ...
def LoadUserProfile(hToken: int, ProfileInfo: _win32typing.PyPROFILEINFO) -> _win32typing.PyHKEY: ...
def UnloadUserProfile(Token: int, Profile: _win32typing.PyHKEY) -> None: ...

PI_APPLYPOLICY: int
PI_NOUI: int
PT_MANDATORY: int
PT_ROAMING: int
PT_TEMPORARY: int
