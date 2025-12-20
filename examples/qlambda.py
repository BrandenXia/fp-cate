from fp_cate.qlambda import _1, _2


def test(a):
    return 10 - a * 20


print((_1 + _2 + test(_2))(9, 2))
print(sorted([(4, 3), (1, 2), (2, 1)], key=_1[0]))
print(sorted([(4, 3), (1, 2), (2, 1)], key=_1[1]))
print(len(list(filter(_1 % 2 == 0, range(10)))))
