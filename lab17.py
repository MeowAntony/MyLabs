class Cell:
    def __init__(self, value=None, left=None, right=None, parent=None):
        self.value = value
        self.left: Cell = left
        self.right: Cell = right
        self.parent: Cell = parent



def construction_tree(cell_now, tree_str: str) -> Cell:
    if '(' in tree_str:
        left_index = tree_str.find('(')
        cell_now.value = int(tree_str[:left_index])
        tree_str = tree_str[left_index + 1:-1]
    else:
        cell_now.value = int(tree_str)
    if ',' in tree_str:
        index_start = 0
        index_comma = tree_str.find(',', index_start)
        while tree_str.count('(', 0, index_comma) != tree_str.count(')', 0, index_comma):
            # print("tree: ", tree_str)
            # print(tree_str.count('(', 0, index_comma), tree_str.count(')', 0, index_comma))
            # print(index_start, index_comma)
            # print()
            index_start = index_comma + 1
            index_comma = tree_str.find(',', index_start)
        left_tree = tree_str[:index_comma]
        right_tree = tree_str[index_comma + 1:]
        if left_tree:
            cell_now.left = Cell(parent=cell_now)
            construction_tree(cell_now.left, left_tree)
        if right_tree:
            cell_now.right = Cell(parent=cell_now)
            construction_tree(cell_now.right, right_tree)

def search_value_tree(cell_tree: Cell, value):
    if cell_tree is not None and
if __name__ == '__main__':  # 8 (3 (1, 6 (4,7)), 10 (, 14(13,)))
    tree = input("Введите дерево в виде линейно-скобочной записи: \n").replace(' ', '')
    cell_tree = Cell()
    construction_tree(cell_tree, tree)
    while True:
        choose = input("""
        Выберите действие:\n
        1) Поиск элемента
        2) Добавить элемент
        3) Удалить элемент
        4) Показать дерево (строчный вариант)
        5) Показать дерево (картинка)
        6) Выход
        """)

        if choose == "1":

