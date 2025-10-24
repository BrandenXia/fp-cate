from fp_cate.cates import fmap, bind

print(fmap(lambda x: x + 1, [1, 2, 3]))
print(bind([1, 2, 3], lambda x: [x, x * 10]))
