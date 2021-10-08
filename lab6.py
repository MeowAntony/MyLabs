str_mas = input("Введите массив: ").split(' ')
int_mas = []
for i in str_mas:
    if i.lstrip('-').isdigit():
        int_mas.append(int(i))

for i in range(0, len(int_mas)):
    minimum = int_mas[i]
    min_index = i
    for j in range(i + 1, len(int_mas)):
        if minimum > int_mas[j]:
            minimum = int_mas[j]
            min_index = j
        else:
            break
    int_mas[i], int_mas[min_index] = int_mas[min_index], int_mas[i]

print("Массив: " + " ".join(str(x) for x in int_mas))