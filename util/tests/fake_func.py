from time import sleep


def fast_fake(n: int) -> int:
    return n * n * 100


def medium_fake(n: int) -> int:
    sleep(0.01)
    return n * n * 100


def slow_fake(n: int) -> int:
    sleep(1)
    return n * n * 100


def fake_A(n: int) -> int:
    return n ** n * 100


def fake_B(n: int, m: str) -> int:
    return pow(n, n) * int(m)


def fake_C(base: int, exp: int) -> int:
    return base ** exp * 100


def sleep_A():
    sleep(0.001)


def sleep_B():
    sleep(0.01)


def sleep_C():
    sleep(0.1)


def sleep_D():
    sleep(1.0)
