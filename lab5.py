str_mas = input("Введите массив: ").split(' ')
int_mas = []
for i in str_mas:
    if i.lstrip('-').isdigit():
        int_mas.append(int(i))

for i in range(1, len(int_mas)):
    for j in range(i, 0, -1):
        if int_mas[j] < int_mas[j - 1]:
            int_mas[j], int_mas[j - 1] = int_mas[j - 1], int_mas[j]
        else:
            break

print("Массив: " + " ".join(str(x) for x in int_mas))