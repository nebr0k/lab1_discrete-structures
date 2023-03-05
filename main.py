def first(p, q):
    con = p and q
    print("Кон'юнкція p і q:", con)

    dis = p or q
    print("Диз'юнкція p і q:", dis)

    xor = p != q
    print("Альтернативне «або» p і q:", xor)

    imp = not p or q
    print("Імплікація p на q:", imp)

    equiv = p == q
    print("Еквівалентність p і q:", equiv)


def second(a, b):
    n = len(a)

    or_result = ""
    for i in range(n):
        or_result += str(int(a[i]) or int(b[i]))
    print("OR рядків a і b:", or_result)

    and_result = ""
    for i in range(n):
        and_result += str(int(a[i]) and int(b[i]))
    print("AND рядків a і b:", and_result)

    xor_result = ""
    for i in range(n):
        xor_result += str(int(a[i]) ^ int(b[i]))
    print("XOR рядків a і b:", xor_result)


if __name__ == "__main__":
    p = True
    q = False
    first(p, q)

    a = "11001100"
    b = "10101011"
    second(a, b)
