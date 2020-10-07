from fractions import Fraction


def choose(n, k):
    if n > k:
        q = 1
        if k > n // 2:
            k = n - k
        for i in range(1, k + 1):
            q *= Fraction(n - i + 1, i)
        return int(q)
    elif n == k:
        return 1
    else:
        return 0
