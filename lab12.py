with open("a.txt", "w+"):
    pass
with open("b.txt", "w+"):
    pass
with open("c.txt", "w+"):
    pass
with open("d.txt", "w+"):
    pass

count_numbers = 0
with open("mas.txt", "r") as file_mas:
    file_a = open("a.txt", "a+")
    file_b = open("b.txt", "a+")
    num_str = ""
    file_select = "a"
    ch = file_mas.read(1)
    while True:
        if ch in " ":
            if file_select == "a":
                file_a.write((num_str + " ") if ch else num_str)
                file_select = "b"
            else:
                file_b.write((num_str + " ") if ch else num_str)
                file_select = "a"
            count_numbers += 1
            if not ch:
                break
            ch = file_mas.read(1)
            num_str = ""
        else:
            num_str += ch
            ch = file_mas.read(1)
    file_a.close()
    file_b.close()

count = 1
file_read_1_name = "a"
file_read_2_name = "b"
file_write_1_name = "c"
file_write_2_name = "d"
while True:  # до того, пока 3 файла не окажутся пустыми
    file_1_read = open(f"{file_read_1_name}.txt", "r")
    file_2_read = open(f"{file_read_2_name}.txt", "r")
    active_file_write = 1
    with open(f"{file_write_1_name}.txt", "w+"):
        pass
    with open(f"{file_write_2_name}.txt", "w+"):
        pass
    file_1_write = open(f"{file_write_1_name}.txt", "a+")
    file_2_write = open(f"{file_write_2_name}.txt", "a+")
    while True:  # пока два считывающий файла ещё не проверены
        read_index_1 = read_index_2 = 0
        num1_int = num2_int = 0
        ch1 = ""
        ch2 = ""
        num1_str = ""
        num2_str = ""
        while read_index_1 < count and read_index_2 < count:  # считываем, пока можно ещё сравнивать
            if num1_str == "":
                ch1 = file_1_read.read(1)
                if ch1 in " ":
                    read_index_1 = count
                    break
                while ch1 not in " ":
                    num1_str += ch1
                    ch1 = file_1_read.read(1)
                num1_int = int(num1_str)
            if num2_str == "":
                ch2 = file_2_read.read(1)
                if ch2 in " ":
                    read_index_2 = count
                    break
                num2_str = ""
                while ch2 not in " ":
                    num2_str += ch2
                    ch2 = file_2_read.read(1)
                num2_int = int(num2_str)
            if num1_int <= num2_int:
                read_index_1 += 1
                if active_file_write == 1:
                    file_1_write.write(num1_str + " ")
                else:
                    file_2_write.write(num1_str + " ")
                num1_str = ""
            else:
                read_index_2 += 1
                if active_file_write == 1:
                    file_1_write.write(num2_str + " ")
                else:
                    file_2_write.write(num2_str + " ")
                num2_str = ""
        if read_index_1 < count:
            if active_file_write == 1:
                file_1_write.write(num1_str + " ")
            else:
                file_2_write.write(num1_str + " ")
            num1_str = ""
            read_index_1 += 1
        while read_index_1 < count:
            ch1 = file_1_read.read(1)
            while ch1 not in " ":
                num1_str += ch1
                ch1 = file_1_read.read(1)
            if active_file_write == 1:
                file_1_write.write(num1_str + " " )
            else:
                file_2_write.write(num1_str + " ")
            read_index_1 += 1
            num1_str = ""

        if read_index_2 < count:
            if active_file_write == 1:
                file_1_write.write(num2_str + " ")
            else:
                file_2_write.write(num2_str + " ")
            num2_str = ""
            read_index_2 += 1
        while read_index_2 < count:
            ch2 = file_2_read.read(1)
            while ch2 not in " ":
                num2_str += ch2
                ch2 = file_2_read.read(1)
            if active_file_write == 1:
                file_1_write.write(num2_str + " ")
            else:
                file_2_write.write(num2_str + " " )
            read_index_2 += 1
            num2_str = ""

        if ch1 == "" and ch2 == "":
            break
        active_file_write = 1 if active_file_write == 2 else 2
    count *= 2
    if count >= count_numbers:
        print(f"Массив расположен в файле: {file_write_1_name if active_file_write == 2 else file_write_2_name}")
        break
    file_1_read.close()
    file_2_read.close()
    file_1_write.close()
    file_2_write.close()
    file_read_1_name = "a" if file_read_1_name == "c" else "c"
    file_read_2_name = "b" if file_read_2_name == "d" else "d"
    file_write_1_name = "c" if file_write_1_name == "a" else "a"
    file_write_2_name = "d" if file_write_2_name == "b" else "b"
