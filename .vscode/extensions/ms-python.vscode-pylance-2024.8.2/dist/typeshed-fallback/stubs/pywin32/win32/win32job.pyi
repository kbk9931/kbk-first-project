import _win32typing
from win32.lib.pywintypes import error as error

def AssignProcessToJobObject(hJob: int, hProcess: int, /) -> None: ...
def CreateJobObject(jobAttributes: _win32typing.PySECURITY_ATTRIBUTES | None, name: str, /) -> None: ...
def OpenJobObject(desiredAccess, inheritHandles, name, /) -> None: ...
def TerminateJobObject(hJob: int, exitCode, /) -> None: ...
def UserHandleGrantAccess(hUserHandle: int, hJob: int, grant, /) -> None: ...
def IsProcessInJob(hProcess: int, hJob: int, /): ...
def QueryInformationJobObject(Job: int, JobObjectInfoClass, /): ...
def SetInformationJobObject(Job: int, JobObjectInfoClass, JobObjectInfo, /) -> None: ...

JOB_OBJECT_ALL_ACCESS: int
JOB_OBJECT_ASSIGN_PROCESS: int
JOB_OBJECT_BASIC_LIMIT_VALID_FLAGS: int
JOB_OBJECT_EXTENDED_LIMIT_VALID_FLAGS: int
JOB_OBJECT_LIMIT_ACTIVE_PROCESS: int
JOB_OBJECT_LIMIT_AFFINITY: int
JOB_OBJECT_LIMIT_BREAKAWAY_OK: int
JOB_OBJECT_LIMIT_DIE_ON_UNHANDLED_EXCEPTION: int
JOB_OBJECT_LIMIT_JOB_MEMORY: int
JOB_OBJECT_LIMIT_JOB_TIME: int
JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE: int
JOB_OBJECT_LIMIT_PRESERVE_JOB_TIME: int
JOB_OBJECT_LIMIT_PRIORITY_CLASS: int
JOB_OBJECT_LIMIT_PROCESS_MEMORY: int
JOB_OBJECT_LIMIT_PROCESS_TIME: int
JOB_OBJECT_LIMIT_SCHEDULING_CLASS: int
JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK: int
JOB_OBJECT_LIMIT_VALID_FLAGS: int
JOB_OBJECT_LIMIT_WORKINGSET: int
JOB_OBJECT_MSG_ABNORMAL_EXIT_PROCESS: int
JOB_OBJECT_MSG_ACTIVE_PROCESS_LIMIT: int
JOB_OBJECT_MSG_ACTIVE_PROCESS_ZERO: int
JOB_OBJECT_MSG_END_OF_JOB_TIME: int
JOB_OBJECT_MSG_END_OF_PROCESS_TIME: int
JOB_OBJECT_MSG_EXIT_PROCESS: int
JOB_OBJECT_MSG_JOB_MEMORY_LIMIT: int
JOB_OBJECT_MSG_NEW_PROCESS: int
JOB_OBJECT_MSG_PROCESS_MEMORY_LIMIT: int
JOB_OBJECT_POST_AT_END_OF_JOB: int
JOB_OBJECT_QUERY: int
JOB_OBJECT_SECURITY_FILTER_TOKENS: int
JOB_OBJECT_SECURITY_NO_ADMIN: int
JOB_OBJECT_SECURITY_ONLY_TOKEN: int
JOB_OBJECT_SECURITY_RESTRICTED_TOKEN: int
JOB_OBJECT_SECURITY_VALID_FLAGS: int
JOB_OBJECT_SET_ATTRIBUTES: int
JOB_OBJECT_SET_SECURITY_ATTRIBUTES: int
JOB_OBJECT_TERMINATE: int
JOB_OBJECT_TERMINATE_AT_END_OF_JOB: int
JOB_OBJECT_UI_VALID_FLAGS: int
JOB_OBJECT_UILIMIT_ALL: int
JOB_OBJECT_UILIMIT_DESKTOP: int
JOB_OBJECT_UILIMIT_DISPLAYSETTINGS: int
JOB_OBJECT_UILIMIT_EXITWINDOWS: int
JOB_OBJECT_UILIMIT_GLOBALATOMS: int
JOB_OBJECT_UILIMIT_HANDLES: int
JOB_OBJECT_UILIMIT_NONE: int
JOB_OBJECT_UILIMIT_READCLIPBOARD: int
JOB_OBJECT_UILIMIT_SYSTEMPARAMETERS: int
JOB_OBJECT_UILIMIT_WRITECLIPBOARD: int
JobObjectAssociateCompletionPortInformation: int
JobObjectBasicAccountingInformation: int
JobObjectBasicAndIoAccountingInformation: int
JobObjectBasicLimitInformation: int
JobObjectBasicUIRestrictions: int
JobObjectEndOfJobTimeInformation: int
JobObjectExtendedLimitInformation: int
JobObjectJobSetInformation: int
JobObjectSecurityLimitInformation: int
MaxJobObjectInfoClass: int
JobObjectBasicProcessIdList: int
UNICODE: int
