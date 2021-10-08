str_mas = input("Введите массив: ").split(' ')
int_mas = []
for i in str_mas:
    if i.lstrip('-').isdigit():
        int_mas.append(int(i))

step = len(int_mas) // 2
while step > 0:
    for i in range(step, len(int_mas)):
        now = i
        for j in range(now, step - 1, -step):
            if int_mas[j] < int_mas[j - step]:
                int_mas[j], int_mas[j - step] = int_mas[j - step], int_mas[j]
            else:
                break

    step //= 2

print("Массив: " + " ".join(str(x) for x in int_mas))
