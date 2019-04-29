import random, string


def id_8(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def id_4_1(size=4, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def id_4_2(size=4, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def id_4_3(size=4, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def id_12(size=12, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def new_app_key():
    a_8 = id_8()
    b_4 = id_4_1()
    c_4 = id_4_2()
    d_4 = id_4_3()
    e_12 = id_12()

    key = a_8+b_4+c_4+d_4+e_12
    return key

