import math

OPERATIONS = {'=': 0, '+': 1, '-': 1, '*': 2, '/': 2}


def reduc(num, den):
    dell = math.gcd(num, den)
    return [num // dell, den // dell]


def op():
    global numbers, chars

    if len(numbers) >= 2 and len(chars) >= 1:
        if chars[-1] == '+':
            num = numbers[-2][0] * numbers[-1][1] + numbers[-1][0] * numbers[-2][1]
            den = numbers[-1][1] * numbers[-2][1]

            num, den = reduc(num, den)
            numbers = numbers[:-2] + [[num, den]]
            chars.pop()
        elif chars[-1] == '-':
            num = numbers[-2][0] * numbers[-1][1] - numbers[-1][0] * numbers[-2][1]
            den = numbers[-1][1] * numbers[-2][1]

            num, den = reduc(num, den)
            numbers = numbers[:-2] + [[num, den]]
            chars.pop()
        elif chars[-1] == '*':
            num = numbers[-2][0] * numbers[-1][0]
            den = numbers[-1][1] * numbers[-2][1]

            num, den = reduc(num, den)
            numbers = numbers[:-2] + [[num, den]]
            chars.pop()
        elif chars[-1] == '/':
            if numbers[-1][0] == 0:
                exit("Деление на ноль")
            else:
                num = numbers[-2][0] * numbers[-1][1]
                den = numbers[-2][1] * numbers[-1][0]

                num, den = reduc(num, den)
                numbers = numbers[:-2] + [[num, den]]
                chars.pop()

    else:
        exit("Неправильное выражение")


chars = []
numbers = []
timed = None

exp = input("Введите выражение: ")

if '=' not in exp:
    exit("Нету знака '='")

for ch in exp:
    if ch == ' ':
        continue
    elif ch.isdigit():
        if timed is None:
            timed = 0
        timed = timed * 10 + int(ch)
        continue

    if timed is not None:
        numbers.append([timed, 1])
        timed = None

    if ch == '(':
        chars.append(ch)
    elif ch == ')':
        while chars and chars[-1] != '(':
            op()
        if not chars or chars[-1] != '(':
            exit("Недостаточно открывающих скобок")
        chars.pop()
    elif ch in OPERATIONS:
        while chars and chars[-1] in OPERATIONS and OPERATIONS[chars[-1]] >= OPERATIONS[ch]:
            op()
        if ch != '=':
            chars.append(ch)

if len(numbers) != 1 or chars:
    exit("Неправильное выражение")
else:
    print(f"Ответ: {numbers[0][0] if numbers[0][1] == 1 else numbers[0][0] / numbers[0][1]}")
