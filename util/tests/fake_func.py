from time import sleep


def pow_a(n: int) -> int:
    return n ** n


def pow_b(n: int) -> int:
    sleep(0.5)
    return pow(n, n)


def pow_c(n: str) -> int:
    num = int(n)
    return num ** num


def pow_d(base: int, exp: int) -> int:
    sleep(0.1)
    return base ** exp
