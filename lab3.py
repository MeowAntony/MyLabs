mas = []


def req(a, b, c, n):
    global mas
    num = 3 ** a * 5 ** b * 7 ** c
    if num > n:
        return
    elif num not in mas:
        mas.append(num)
    req(a + 1, b, c, n)
    req(a, b + 1, c, n)
    req(a, b, c + 1, n)


n = int(input("Введите X: "))
req(0, 0, 0, n)
mas.sort()
print("Числа: " + " ".join(str(x) for x in mas))
