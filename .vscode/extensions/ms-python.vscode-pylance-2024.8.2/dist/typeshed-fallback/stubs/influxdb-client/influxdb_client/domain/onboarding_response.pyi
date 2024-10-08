from _typeshed import Incomplete

class OnboardingResponse:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(
        self,
        user: Incomplete | None = None,
        org: Incomplete | None = None,
        bucket: Incomplete | None = None,
        auth: Incomplete | None = None,
    ) -> None: ...
    @property
    def user(self): ...
    @user.setter
    def user(self, user) -> None: ...
    @property
    def org(self): ...
    @org.setter
    def org(self, org) -> None: ...
    @property
    def bucket(self): ...
    @bucket.setter
    def bucket(self, bucket) -> None: ...
    @property
    def auth(self): ...
    @auth.setter
    def auth(self, auth) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
