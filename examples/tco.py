from fp_cate.optimize import TailCall, tco


@tco
def fib(n, acc=1):
    return TailCall(n - 1, n * acc) if n > 1 else acc


print(fib(1145))
