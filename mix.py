calculated = set()


def calculate_sum(n, k):
    s = 0
    for i in range(1, n + 1):
        if i in calculated:
            continue
        val = f(i, k)
        j = k
        while i * j < n:
            calculated.add(i * j)
            s += val
            j *= k
        s += val
    return s


def f(a, k):
    while a % k == 0:
        a //= k
    return a


print(calculate_sum(66, 2))
