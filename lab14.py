import codecs
import re
from typing import List, Union


def get_key(value: str):
    answer = 0
    for index, ch in enumerate(value):
        answer += (index + 1) * ord(ch)
    return answer


class ValueClass:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class HashTable:
    def __init__(self):
        self.index_prime_number = 0
        self.size = 19
        self.data: List[Union[None, ValueClass]] = [None] * self.size

    def print_hash_table(self):
        print("\n====TABLE====")
        for key, value_class in enumerate(self.data):
            print(f"{key}:", end=' ')
            now_value_class = value_class
            while now_value_class is not None:
                print(now_value_class.value, end=' ')
                now_value_class = now_value_class.right
            print()
        print("=============\n")

    def add_value(self, value: str):
        key = get_key(value)
        hashvalue = self.hashfunction(key)
        if self.data[hashvalue] is None:
            self.data[hashvalue] = ValueClass(value)
        else:
            now_value_class = self.data[hashvalue]
            while now_value_class.right is not None:
                now_value_class = now_value_class.right
            now_value_class.right = ValueClass(value, left=now_value_class)

    def delete_value(self, value: str):
        key = get_key(value)
        hashvalue = self.hashfunction(key)
        if self.data[hashvalue] is not None:
            now_value_class = self.data[hashvalue]
            while now_value_class.value != value and now_value_class.right is not None:
                now_value_class = now_value_class.right
            if now_value_class.value == value:
                if now_value_class.left is not None:
                    now_value_class.left = now_value_class.right
                else:
                    self.data[hashvalue] = None
            else:
                raise ValueError(f"Not found value ({value})")
        else:
            raise ValueError(f"Not found value ({value})")

    def check_value(self, value: str):
        key = get_key(value)
        hashvalue = self.hashfunction(key)
        if self.data[hashvalue] is not None:
            now_value_class = self.data[hashvalue]
            while now_value_class.value != value and now_value_class.right is not None:
                now_value_class = now_value_class.right
            if now_value_class.value == value:
                print(f"Found value ({value}). HashKey: {hashvalue}")
            else:
                raise ValueError(f"Not found value ({value})")
        else:
            raise ValueError(f"Not found value ({value})")

    def hashfunction(self, key):
        return key % self.size


if __name__ == '__main__':
    with codecs.open("text.txt", encoding='utf-8') as file:
        text = file.read().lower()
        words = re.findall(r"(?<=\s)[a-zA-Zа-яА-ЯёЁ][\-a-zA-Zа-яА-ЯёЁ\d]+(?=\s|$|)", " " + text)

    hashtable = HashTable()
    for word in words:
        hashtable.add_value(word)
    hashtable.check_value('зимний')
    hashtable.print_hash_table()
