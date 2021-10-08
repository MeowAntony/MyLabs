str_mas = input("Введите массив: ").split(' ')
int_mas = []
for i in str_mas:
    if i.lstrip('-').isdigit():
        int_mas.append(int(i))


def req_sort(left_max_index, right_max_index):
    if right_max_index - left_max_index < 1:
        return
    pivot_index = left_max_index
    now_index = right_max_index
    direction = -1
    while pivot_index != now_index:
        if int_mas[pivot_index] < int_mas[now_index] and direction == 1 \
                or int_mas[pivot_index] > int_mas[now_index] and direction == -1:
            int_mas[pivot_index], int_mas[now_index] = int_mas[now_index], int_mas[pivot_index]
            pivot_index, now_index = now_index, pivot_index
            direction *= -1
        now_index += direction

    req_sort(left_max_index, pivot_index - 1)
    req_sort(pivot_index + 1, right_max_index)


req_sort(0, len(int_mas) - 1)
print("Массив: " + " ".join(str(x) for x in int_mas))
