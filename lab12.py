str_mas = input("Введите массив: ").split(' ')
int_mas = []
for i in str_mas:
    if i.lstrip('-').isdigit():
        int_mas.append(int(i))

count = 1
while count < len(int_mas):
    b = []
    c = []
    for num, index in enumerate(range(0, len(int_mas), count)):
        if num % 2 == 0:
            b += int_mas[index:index + count]
        else:
            c += int_mas[index:index + count]

    int_mas = []
    for i in range(len(b) // count + 1 if len(b) % count > 0 else len(b) // count):
        b_index = c_index = i * count
        return_mas = []
        while b_index < i * count + count > c_index and b_index < len(b) and c_index < len(c):
            if b[b_index] <= c[c_index]:
                int_mas.append(b[b_index])
                b_index += 1
            else:
                int_mas.append(c[c_index])
                c_index += 1
        if b_index < i * count + count and b_index < len(b):
            int_mas += b[b_index:i * count + count]
        else:
            int_mas += c[c_index:i * count + count]
    count *= 2

print("Массив: " + " ".join(str(x) for x in int_mas))



