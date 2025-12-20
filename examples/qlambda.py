from fp_cate.qlambda import _1, _2


def test(a):
    return 10 - a * 20


print((_1 + _2 + test(_2))(9, 2))
