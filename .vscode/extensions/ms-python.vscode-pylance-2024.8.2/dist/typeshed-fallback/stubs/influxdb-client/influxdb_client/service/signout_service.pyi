from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class SignoutService(_BaseService):
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    def post_signout(self, **kwargs): ...
    def post_signout_with_http_info(self, **kwargs): ...
    async def post_signout_async(self, **kwargs): ...
