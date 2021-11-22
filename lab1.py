msg = input('Введите строку: ')

d = {'}': '{', ']': '[', ')': '('}
stack = []
for ch in msg:
    if ch in list(d.values()):
        stack.append(ch)
    else:
        if not stack or ch not in d or d[ch] != stack.pop(-1):
            exit('Ошибка скобочной последовательности')

if stack:
    exit('Ошибка скобочной последовательности')
else:
    print('Скобочная последовательность составлена правильно')