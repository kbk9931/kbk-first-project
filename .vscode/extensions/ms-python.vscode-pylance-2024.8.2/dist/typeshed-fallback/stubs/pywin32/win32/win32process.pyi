from _typeshed import Incomplete

import _win32typing
from win32.lib.pywintypes import error as error

def STARTUPINFO() -> _win32typing.PySTARTUPINFO: ...
def beginthreadex(sa: _win32typing.PySECURITY_ATTRIBUTES, stackSize, entryPoint, args, flags, /) -> tuple[int, Incomplete]: ...
def CreateRemoteThread(
    hprocess: int, sa: _win32typing.PySECURITY_ATTRIBUTES, stackSize, entryPoint, Parameter, flags, /
) -> tuple[int, Incomplete]: ...
def CreateProcess(
    appName: str | None,
    commandLine: str,
    processAttributes: _win32typing.PySECURITY_ATTRIBUTES | None,
    threadAttributes: _win32typing.PySECURITY_ATTRIBUTES | None,
    bInheritHandles: int | bool,
    dwCreationFlags: int,
    newEnvironment: dict[str, str] | None,
    currentDirectory: str | None,
    startupinfo: _win32typing.PySTARTUPINFO,
    /,
) -> tuple[int, int, Incomplete, Incomplete]: ...
def CreateProcessAsUser(
    hToken: int,
    appName: str,
    commandLine: str,
    processAttributes: _win32typing.PySECURITY_ATTRIBUTES,
    threadAttributes: _win32typing.PySECURITY_ATTRIBUTES,
    bInheritHandles,
    dwCreationFlags,
    newEnvironment,
    currentDirectory: str,
    startupinfo: _win32typing.PySTARTUPINFO,
    /,
) -> tuple[int, int, Incomplete, Incomplete]: ...
def GetCurrentProcess() -> int: ...
def GetProcessVersion(processId, /): ...
def GetCurrentProcessId(): ...
def GetStartupInfo() -> _win32typing.PySTARTUPINFO: ...
def GetPriorityClass(handle: int, /): ...
def GetExitCodeThread(handle: int, /): ...
def GetExitCodeProcess(handle: int, /) -> int: ...
def GetWindowThreadProcessId(hwnd: int | None, /) -> tuple[int, int]: ...
def SetThreadPriority(handle: int, nPriority, /) -> None: ...
def GetThreadPriority(handle: int, /): ...
def GetProcessPriorityBoost(Process: int, /): ...
def SetProcessPriorityBoost(Process: int, DisablePriorityBoost, /) -> None: ...
def GetThreadPriorityBoost(Thread: int, /): ...
def SetThreadPriorityBoost(Thread: int, DisablePriorityBoost, /) -> None: ...
def GetThreadIOPendingFlag(Thread: int, /): ...
def GetThreadTimes(Thread: int, /): ...
def GetProcessId(Process: int, /): ...
def SetPriorityClass(handle: int, dwPriorityClass: int, /) -> None: ...
def AttachThreadInput(idAttach, idAttachTo, Attach, /) -> None: ...
def SetThreadIdealProcessor(handle: int, dwIdealProcessor, /): ...
def GetProcessAffinityMask(hProcess: int, /) -> tuple[Incomplete, Incomplete]: ...
def SetProcessAffinityMask(hProcess: int, mask, /) -> None: ...
def SetThreadAffinityMask(hThread: int, ThreadAffinityMask, /): ...
def SuspendThread(handle: int, /): ...
def ResumeThread(handle: int, /): ...
def TerminateProcess(handle: int, exitCode: int, /) -> None: ...
def ExitProcess(exitCode, /) -> None: ...
def EnumProcesses() -> tuple[Incomplete, Incomplete]: ...
def EnumProcessModules(hProcess: int, /) -> tuple[Incomplete, Incomplete]: ...
def EnumProcessModulesEx(hProcess: int, FilterFlag, /) -> tuple[Incomplete, Incomplete]: ...
def GetModuleFileNameEx(hProcess: int, hModule: int, /): ...
def GetProcessMemoryInfo(hProcess: int, /): ...
def GetProcessTimes(hProcess: int, /): ...
def GetProcessIoCounters(hProcess: int, /): ...
def GetProcessWindowStation() -> None: ...
def GetProcessWorkingSetSize(hProcess: int, /) -> tuple[Incomplete, Incomplete]: ...
def SetProcessWorkingSetSize(hProcess: int, MinimumWorkingSetSize, MaximumWorkingSetSize, /) -> None: ...
def GetProcessShutdownParameters() -> tuple[Incomplete, Incomplete]: ...
def SetProcessShutdownParameters(Level, Flags, /) -> None: ...
def GetGuiResources(Process: int, Flags, /): ...
def IsWow64Process(Process: int | None = ..., /) -> bool: ...
def ReadProcessMemory(*args): ...  # incomplete
def VirtualAllocEx(*args): ...  # incomplete
def VirtualFreeEx(*args): ...  # incomplete
def WriteProcessMemory(*args): ...  # incomplete

ABOVE_NORMAL_PRIORITY_CLASS: int
BELOW_NORMAL_PRIORITY_CLASS: int
CREATE_BREAKAWAY_FROM_JOB: int
CREATE_DEFAULT_ERROR_MODE: int
CREATE_NEW_CONSOLE: int
CREATE_NEW_PROCESS_GROUP: int
CREATE_NO_WINDOW: int
CREATE_PRESERVE_CODE_AUTHZ_LEVEL: int
CREATE_SEPARATE_WOW_VDM: int
CREATE_SHARED_WOW_VDM: int
CREATE_SUSPENDED: int
CREATE_UNICODE_ENVIRONMENT: int
DEBUG_ONLY_THIS_PROCESS: int
DEBUG_PROCESS: int
DETACHED_PROCESS: int
HIGH_PRIORITY_CLASS: int
IDLE_PRIORITY_CLASS: int
MAXIMUM_PROCESSORS: int
NORMAL_PRIORITY_CLASS: int
REALTIME_PRIORITY_CLASS: int
STARTF_FORCEOFFFEEDBACK: int
STARTF_FORCEONFEEDBACK: int
STARTF_RUNFULLSCREEN: int
STARTF_USECOUNTCHARS: int
STARTF_USEFILLATTRIBUTE: int
STARTF_USEPOSITION: int
STARTF_USESHOWWINDOW: int
STARTF_USESIZE: int
STARTF_USESTDHANDLES: int
THREAD_MODE_BACKGROUND_BEGIN: int
THREAD_MODE_BACKGROUND_END: int
THREAD_PRIORITY_ABOVE_NORMAL: int
THREAD_PRIORITY_BELOW_NORMAL: int
THREAD_PRIORITY_HIGHEST: int
THREAD_PRIORITY_IDLE: int
THREAD_PRIORITY_LOWEST: int
THREAD_PRIORITY_NORMAL: int
THREAD_PRIORITY_TIME_CRITICAL: int
LIST_MODULES_32BIT: int
LIST_MODULES_64BIT: int
LIST_MODULES_ALL: int
LIST_MODULES_DEFAULT: int
UNICODE: int
