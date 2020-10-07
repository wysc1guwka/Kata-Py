def is_prime(num: int) -> bool:
    if num > 1:
        for p in range(2, int((num ** 0.5) + 1)):
            if num % p == 0:
                return False
        return True
    else:
        return False


def solve(n: int):
    dif = 0
    prime = 2
    for m in range(n, 1, -1):
        if is_prime(m):
            prime = m
            dif = n-m
            break
    for m in range(n, n+dif):
        if is_prime(m):
            print(m)
            if (m-n) < dif:
                prime = m
            break
    return prime
