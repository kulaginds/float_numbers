import converters


def info(num: float):
    i = converters.float_to_int_data(num)

    print(bin(i))

    # S sign  E exponent            M fraction
    #     63  62 (11 b-bits)        52 (52 n-bits)                  0

    # sign
    S = (i >> 63) & 2 ** 0
    print("S", bin(S))

    # exponent
    E = (i >> 52) & 2 ** 11 - 1
    print("E", bin(E))

    # fraction
    M = i & (2 ** 52 - 1)
    print("fract", bin(M))

    # Для нормализованного числа:
    #                 b - 1
    #     S     (E - 2      + 1)   (1 + M)
    # (-1)   * 2                  * ------
    #                                 n
    #                                2
    b = 11
    n = 52

    new_num = (-1) ** S * 2 ** (E - 2 ** (b - 1) + 1) * (1 + M / 2 ** n)
    print(new_num)

    # Для денормализованного числа:
    #                 b - 1
    #     S     (E - 2      + 2)     M
    # (-1)   * 2                  * ---
    #                                 n
    #                                2
    # Как определить float нормализован или нет - хз, в стандарте не определено.
    # new_num = (-1) ** S * 2 ** (E - 2 ** (b - 1) + 2) * (M / 2 ** n)
    # print(new_num)


if __name__ == '__main__':
    a = 41016.98 * 100.0
    b = 4101698.0
    c = 0.1

    info(a)
    print("==========")
    info(b)
    print("==========")
    info(c)
