from typing import Any

from sympy.assumptions.relation.binrel import BinaryRelation

__all__ = [
    "EqualityPredicate",
    "UnequalityPredicate",
    "StrictGreaterThanPredicate",
    "GreaterThanPredicate",
    "StrictLessThanPredicate",
    "LessThanPredicate",
]

class EqualityPredicate(BinaryRelation):
    is_reflexive = ...
    is_symmetric = ...
    name = ...
    handler = ...
    @property
    def negated(self) -> Any: ...
    def eval(self, args, assumptions=...): ...

class UnequalityPredicate(BinaryRelation):
    is_reflexive = ...
    is_symmetric = ...
    name = ...
    handler = ...
    @property
    def negated(self) -> Any: ...
    def eval(self, args, assumptions=...): ...

class StrictGreaterThanPredicate(BinaryRelation):
    is_reflexive = ...
    is_symmetric = ...
    name = ...
    handler = ...
    @property
    def reversed(self) -> Any: ...
    @property
    def negated(self) -> Any: ...
    def eval(self, args, assumptions=...): ...

class GreaterThanPredicate(BinaryRelation):
    is_reflexive = ...
    is_symmetric = ...
    name = ...
    handler = ...
    @property
    def reversed(self) -> Any: ...
    @property
    def negated(self) -> Any: ...
    def eval(self, args, assumptions=...): ...

class StrictLessThanPredicate(BinaryRelation):
    is_reflexive = ...
    is_symmetric = ...
    name = ...
    handler = ...
    @property
    def reversed(self) -> Any: ...
    @property
    def negated(self) -> Any: ...
    def eval(self, args, assumptions=...): ...

class LessThanPredicate(BinaryRelation):
    is_reflexive = ...
    is_symmetric = ...
    name = ...
    handler = ...
    @property
    def reversed(self) -> Any: ...
    @property
    def negated(self) -> Any: ...
    def eval(self, args, assumptions=...): ...
