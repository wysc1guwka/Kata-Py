def square_digits(num):
    num = list(str(num))
    for i in range(0, len(num)):
        num[i] = str(int(num[i]) ** 2)
    return int("".join(num))
