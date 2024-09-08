from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class VariablesService(_BaseService):
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    def delete_variables_id(self, variable_id, **kwargs): ...
    def delete_variables_id_with_http_info(self, variable_id, **kwargs): ...
    async def delete_variables_id_async(self, variable_id, **kwargs): ...
    def delete_variables_id_labels_id(self, variable_id, label_id, **kwargs): ...
    def delete_variables_id_labels_id_with_http_info(self, variable_id, label_id, **kwargs): ...
    async def delete_variables_id_labels_id_async(self, variable_id, label_id, **kwargs): ...
    def get_variables(self, **kwargs): ...
    def get_variables_with_http_info(self, **kwargs): ...
    async def get_variables_async(self, **kwargs): ...
    def get_variables_id(self, variable_id, **kwargs): ...
    def get_variables_id_with_http_info(self, variable_id, **kwargs): ...
    async def get_variables_id_async(self, variable_id, **kwargs): ...
    def get_variables_id_labels(self, variable_id, **kwargs): ...
    def get_variables_id_labels_with_http_info(self, variable_id, **kwargs): ...
    async def get_variables_id_labels_async(self, variable_id, **kwargs): ...
    def patch_variables_id(self, variable_id, variable, **kwargs): ...
    def patch_variables_id_with_http_info(self, variable_id, variable, **kwargs): ...
    async def patch_variables_id_async(self, variable_id, variable, **kwargs): ...
    def post_variables(self, variable, **kwargs): ...
    def post_variables_with_http_info(self, variable, **kwargs): ...
    async def post_variables_async(self, variable, **kwargs): ...
    def post_variables_id_labels(self, variable_id, label_mapping, **kwargs): ...
    def post_variables_id_labels_with_http_info(self, variable_id, label_mapping, **kwargs): ...
    async def post_variables_id_labels_async(self, variable_id, label_mapping, **kwargs): ...
    def put_variables_id(self, variable_id, variable, **kwargs): ...
    def put_variables_id_with_http_info(self, variable_id, variable, **kwargs): ...
    async def put_variables_id_async(self, variable_id, variable, **kwargs): ...
