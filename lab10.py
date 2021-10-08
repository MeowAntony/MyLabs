str_mas = input("Введите массив: ").split(' ')
int_mas = []
for i in str_mas:
    if i.lstrip('-').isdigit():
        int_mas.append(int(i))


def req_sort(mas):
    if len(mas) == 1 or len(mas) == 0:
        return mas
    left = req_sort(mas[0:len(mas) // 2])
    right = req_sort(mas[len(mas) // 2:])
    left_index = right_index = 0
    return_mas = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            return_mas.append(left[left_index])
            left_index += 1
        else:
            return_mas.append(right[right_index])
            right_index += 1

    if left_index < len(left):
        return_mas += left[left_index:]
    else:
        return_mas += right[right_index:]
    return return_mas


int_mas_sort = req_sort(int_mas)
print("Массив: " + " ".join(str(x) for x in int_mas_sort))
