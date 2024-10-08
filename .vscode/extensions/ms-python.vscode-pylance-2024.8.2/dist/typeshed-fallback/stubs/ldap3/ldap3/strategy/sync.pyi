from typing import Any

from ..strategy.base import BaseStrategy

LDAP_MESSAGE_TEMPLATE: Any

class SyncStrategy(BaseStrategy):
    sync: bool
    no_real_dsa: bool
    pooled: bool
    can_stream: bool
    socket_size: Any
    def __init__(self, ldap_connection) -> None: ...
    def open(self, reset_usage: bool = True, read_server_info: bool = True) -> None: ...
    def receiving(self): ...
    def post_send_single_response(self, message_id): ...
    def post_send_search(self, message_id): ...
    def set_stream(self, value) -> None: ...
    def get_stream(self) -> None: ...
