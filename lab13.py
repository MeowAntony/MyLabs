import codecs
import re

MAX_NUMBER = 10000
ALL_NUMBERS = [num for num in range(MAX_NUMBER + 1)]
prime_numbers = []


def get_key(value: str):
    answer = 0
    for index, ch in enumerate(value):
        answer += (index + 1) * ord(ch)
    return answer


class HashTable:
    def __init__(self):
        self.index_prime_number = 0
        self.now_size = 0
        self.size = prime_numbers[self.index_prime_number]
        self.data = [None] * self.size

    def resize_table(self, increase: bool):
        self.index_prime_number += 1 if increase else -1
        self.now_size = 0
        self.size = prime_numbers[self.index_prime_number]
        data_timed = self.data
        self.data = [None] * self.size
        for value in data_timed:
            if value is not None:
                self.add_value(value)

    def print_hash_table(self):
        print("\n====TABLE====")
        for key, value in enumerate(self.data):
            print(f"{key}: {value}")
        print("=============\n")

    def add_value(self, value: str):
        key = get_key(value)
        hashvalue = self.hashfunction(key)
        if self.data[hashvalue] is None:
            self.data[hashvalue] = value
            self.now_size += 1
        elif self.data[hashvalue] != value:
            nexthashvalue = self.rehash(hashvalue)
            while self.data[nexthashvalue] is not None and self.data[hashvalue] != value:
                nexthashvalue = self.rehash(nexthashvalue)

            if self.data[nexthashvalue] is None:
                self.now_size += 1
                self.data[nexthashvalue] = value

        if self.now_size == self.size:
            self.resize_table(True)

    def delete_value(self, value):
        key = get_key(value)
        hashvalue = self.hashfunction(key)
        if self.data[hashvalue] == value:
            self.data[hashvalue] = None
        elif self.data[hashvalue] is not None:
            starthashvalue = hashvalue
            nexthashvalue = self.rehash(hashvalue)
            while self.data[nexthashvalue] is not None and self.data[hashvalue] != value and starthashvalue != nowhashvalue:
                nexthashvalue = self.rehash(nexthashvalue)
            if self.data[nexthashvalue] is None or starthashvalue == nexthashvalue:
                raise ValueError(f"Not found value ({value})")
            self.data[nexthashvalue] = None
        else:
            raise ValueError(f"Not found value ({value})")
        self.now_size -= 1

        if self.size > self.now_size * self.now_size:
            self.resize_table(False)

    def check_value(self, value):
        key = get_key(value)
        hashvalue = self.hashfunction(key)
        if self.data[hashvalue] == value:
            print(f"Found value ({value})")
        elif self.data[hashvalue] is not None:
            starthashvalue = hashvalue
            nexthashvalue = self.rehash(hashvalue)
            while self.data[nexthashvalue] is not None and self.data[nexthashvalue] != value and starthashvalue != nexthashvalue:
                nexthashvalue = self.rehash(nexthashvalue)
            if self.data[nexthashvalue] is None or starthashvalue == nexthashvalue:
                raise ValueError(f"Not found value ({value})")
            print(f"Found value ({value}). HashKey: {nexthashvalue}")
        else:
            raise ValueError(f"Not found value ({value})")

    def hashfunction(self, key):
        return key % self.size

    def rehash(self, oldhash):
        return (oldhash + self.size // 2) % self.size


if __name__ == '__main__':
    left_degree_2 = 2 ** 0
    right_degree_2 = 2 ** 1

    now_num = 2
    while now_num <= MAX_NUMBER:
        if ALL_NUMBERS[now_num] != 0:
            while now_num > right_degree_2:
                left_degree_2 *= 2
                right_degree_2 *= 2
            if now_num >= 11 and now_num / left_degree_2 > 1.2 and right_degree_2 / now_num > 1.2:
                prime_numbers.append(ALL_NUMBERS[now_num])
            for j in range(now_num, MAX_NUMBER + 1, now_num):
                ALL_NUMBERS[j] = 0
        now_num += 1

    with codecs.open("text.txt", encoding='utf-8') as file:
        text = file.read().lower()
        words = re.findall(r"(?<=\s)[a-zA-Zа-яА-ЯёЁ][\-a-zA-Zа-яА-ЯёЁ\d]+(?=\s|$|)", " " + text)

    hashtable = HashTable()
    for word in words:
        hashtable.add_value(word)
    hashtable.print_hash_table()
    hashtable.check_value('зимний')
