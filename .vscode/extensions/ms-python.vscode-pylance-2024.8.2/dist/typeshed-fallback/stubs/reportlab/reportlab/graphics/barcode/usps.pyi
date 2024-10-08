from _typeshed import Incomplete

from reportlab.graphics.barcode.common import Barcode

class FIM(Barcode):
    barWidth: Incomplete
    spaceWidth: Incomplete
    barHeight: Incomplete
    rquiet: Incomplete
    lquiet: Incomplete
    quiet: int
    def __init__(self, value: str = "", **args) -> None: ...
    valid: int
    validated: str
    def validate(self): ...
    decomposed: str
    def decompose(self): ...
    def computeSize(self) -> None: ...
    def draw(self) -> None: ...

class POSTNET(Barcode):
    quiet: int
    shortHeight: Incomplete
    barHeight: Incomplete
    barWidth: Incomplete
    spaceWidth: Incomplete
    def __init__(self, value: str = "", **args) -> None: ...
    validated: str
    valid: int
    def validate(self): ...
    encoded: str
    def encode(self): ...
    decomposed: str
    def decompose(self): ...
    def computeSize(self) -> None: ...
    def draw(self) -> None: ...
