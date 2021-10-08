str_mas = input("Введите массив: ").split(' ')
int_mas = []
for i in str_mas:
    if i.lstrip('-').isdigit():
        int_mas.append(int(i))

de = 1

while True:
    status = True
    buf = [[] for i in range(20)]
    for num in int_mas:
        new_num = num // de
        if new_num > 0:
            status = False

        buf[new_num % 10 + 10 if new_num >= 0 else new_num % 10].append(num)
    if status:
        break

    int_mas = []
    for mas in buf:
        int_mas += mas

    de *= 10


otvet = []
print("Массив: " + " ".join(str(x) for x in int_mas))
