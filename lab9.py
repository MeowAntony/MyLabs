str_mas = input("Введите массив: ").split(' ')
int_mas = []
for i in str_mas:
    if i.lstrip('-').isdigit():
        int_mas.append(int(i))

not_sorted = len(int_mas)
lenght = len(int_mas)


def sort_down(index):
    if index * 2 + 1 < not_sorted:
        if index * 2 + 2 < not_sorted:
            if int_mas[index * 2 + 2] <= int_mas[index * 2 + 1] >= int_mas[index]:
                int_mas[index], int_mas[index * 2 + 1] = int_mas[index * 2 + 1], int_mas[index]
                sort_down(index * 2 + 1)
            elif int_mas[index * 2 + 1] <= int_mas[index * 2 + 2] >= int_mas[index]:
                int_mas[index], int_mas[index * 2 + 2] = int_mas[index * 2 + 2], int_mas[index]
                sort_down(index * 2 + 2)

        elif int_mas[index * 2 + 1] > int_mas[index]:
            int_mas[index], int_mas[index * 2 + 1] = int_mas[index * 2 + 1], int_mas[index]
            sort_down(index * 2 + 1)


# изначальная сортировка дерева
for i in range(lenght - 1, -1, -1):
    sort_down(i)

# сортировка каждого элемента
for i in range(lenght - 1):
    int_mas[0], int_mas[not_sorted - 1] = int_mas[not_sorted - 1], int_mas[0]
    not_sorted -= 1
    sort_down(0)

print("Массив: " + " ".join(str(x) for x in int_mas))
