from typing import Any

class Future:
    info: Any
    def __init__(self, info: str = ...) -> None: ...
    def done(self): ...
    def running(self): ...
    def wait(self) -> None: ...
    def check_success(self) -> None: ...
    def set_result(self, result) -> None: ...
    def set_exception(self, exception) -> None: ...
    def result(self): ...
    get_result: Any
    def exception(self): ...
    get_exception: Any
    def get_traceback(self): ...
    def add_done_callback(self, callback) -> None: ...
    def cancel(self) -> None: ...
    def cancelled(self): ...
    @staticmethod
    def wait_any(futures): ...
    @staticmethod
    def wait_all(futures): ...

class _TaskletFuture(Future):
    generator: Any
    context: Any
    waiting_on: Any
    def __init__(self, generator, context, info: str = ...) -> None: ...
    def cancel(self) -> None: ...

class _MultiFuture(Future):
    def __init__(self, dependencies) -> None: ...
    def cancel(self) -> None: ...

def tasklet(wrapped): ...
def wait_any(futures): ...
def wait_all(futures) -> None: ...

class Return(Exception): ...

def sleep(seconds): ...
def add_flow_exception(*args, **kwargs) -> None: ...
def make_context(*args, **kwargs) -> None: ...
def make_default_context(*args, **kwargs) -> None: ...

class QueueFuture:
    def __init__(self, *args, **kwargs) -> None: ...

class ReducingFuture:
    def __init__(self, *args, **kwargs) -> None: ...

class SerialQueueFuture:
    def __init__(self, *args, **kwargs) -> None: ...

def set_context(*args, **kwargs) -> None: ...
def synctasklet(wrapped): ...
def toplevel(wrapped): ...
