from typing import Callable, TypeVar
from functools import singledispatch

from .. import curry
from ._internal import _not_implemented


__all__ = ["mempty", "mappend", "register_monoid"]


T = TypeVar("T")


@singledispatch
def _mempty(v: T) -> T:
    return _not_implemented("mempty", type(v))


mempty = _mempty


@singledispatch
def _mappend(a: T, _: T) -> T:
    return _not_implemented("mappend", type(a))


mappend = curry(_mappend)


def register_monoid(t: type[T], /, mempty: T, mappend: Callable[[T, T], T]) -> None:
    _mempty.register(t)(lambda _: mempty)
    _mappend.register(t)(mappend)
