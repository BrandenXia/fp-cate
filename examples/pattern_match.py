from dataclasses import dataclass

from fp_cate import pipe, match, case, matchV, _any, _rest, default


# works with any iterables
a = "test"
print(
    matchV(a)(
        case("tes") >> (lambda _: "one"),
        case(["a", _rest]) >> (lambda _, xs: f"list starts with a, rest is {xs}"),
        default >> "good",
    )
)
a = ["a", 1, 2, 3]
pipe(
    a,
    match(
        case([1, 2]) >> (lambda _: "one"),
        case(["a", _rest]) >> (lambda _, xs: f"list starts with a, rest is {xs}"),
    ),
    print,
)

# works with dicts
pipe(
    {"test": 1, "other": 2},
    match(
        case({"test": _any}) >> (lambda x: f"test is {x}"),
        case({"other": 2}) >> (lambda _: "other two"),
    ),
    print,
)


@dataclass
class Test:
    a: int
    b: bool


# works with dataclasses as well
pipe(
    Test(1, True),
    match(
        case({"a": 1}) >> "this is a good match",
        case({"b": False}) >> "this won't match",
        default >> "all other matches failed",
    ),
    print,
)
