from typing import Never

__all__ = [
    "_not_implemented",
]


def _not_implemented(cate: str, t: type) -> Never:
    raise NotImplementedError(f"{cate} not implemented for type {t}")
