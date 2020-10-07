def is_prime(num) -> bool:
    if num > 1:
        for p in range(2, int((num ** 0.5) + 1)):
            if num % p == 0:
                return False
        return True
    else:
        return False
