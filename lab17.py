import tree_to_picture


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


def search_value_tree(cell_tree: Cell, value: int):
    if cell_tree is None or cell_tree.value == value:
        return cell_tree
    if value < cell_tree.value:
        return search_value_tree(cell_tree.left, value)
    else:
        return search_value_tree(cell_tree.right, value)


def add_value_tree(cell_tree: Cell, cell: Cell):
    if cell_tree.value > cell.value and not cell_tree.left:
        cell.parent = cell_tree
        cell_tree.left = cell
    elif cell_tree.value < cell.value and not cell_tree.right:
        cell.parent = cell_tree
        cell_tree.right = cell
    elif cell_tree.left and cell_tree.value > cell.value:
        add_value_tree(cell_tree.left, cell)
    elif cell_tree.right and cell_tree.value < cell.value:
        add_value_tree(cell_tree.right, cell)


def delete_value_tree(cell_tree: Cell, value):
    if cell_tree is None:
        return False
    if cell_tree.value > value:
        return delete_value_tree(cell_tree.left, value)
    elif cell_tree.value < value:
        return delete_value_tree(cell_tree.right, value)
    else:
        if cell_tree.left is None and cell_tree.right is None:
            if cell_tree == cell_tree.parent.left:
                cell_tree.parent.left = None
            else:
                cell_tree.parent.right = None
            del cell_tree
        elif cell_tree.left is None and cell_tree.right is not None:
            cell_tree.value = cell_tree.right.value
            cell_tree.left = cell_tree.right.left
            cell_tree.right = cell_tree.right.right
        elif cell_tree.left is not None and cell_tree.right is None:
            cell_tree.value = cell_tree.left.value
            cell_tree.right = cell_tree.left.right
            cell_tree.left = cell_tree.left.left
        else:
            if cell_tree.right.left is None:
                cell_tree.value = cell_tree.right.value
                cell_tree.right = cell_tree.right.right
            else:
                min_left = cell_tree.right.left
                while min_left.left is not None:
                    min_left = min_left.left
                cell_tree.value = min_left.value
                min_left.parent.left = min_left.right
        return True


if __name__ == '__main__':  # 8 (3 (1, 6 (4,7)), 10 (, 14(13,)))
    tree = input("Введите дерево в виде линейно-скобочной записи: \n").replace(' ', '')
    cell_tree = Cell()
    construction_tree(cell_tree, tree)
    while True:
        choose_text = """Выберите действие:
        1) Поиск элемента 
        2) Добавить элемент 
        3) Удалить элемент 
        4) Показать дерево (картинка) 
        5) Выход \n"""
        choose = input(choose_text)
        print()
        if choose == "1":
            search_value = int(input("Введите значение элемента: "))
            if search_value_tree(cell_tree, search_value) is not None:
                print("Данный элемент присутствует в дереве")
            else:
                print("Данный элемент не найден")
        elif choose == "2":
            add_value = int(input("Введите значение элемента: "))
            add_value_tree(cell_tree, Cell(add_value))
        elif choose == "3":
            delete_value = int(input("Введите значение элемента: "))
            if delete_value_tree(cell_tree, delete_value):
                print("Успешно удалён элемент")
            else:
                print("Данный элемент отсутствует")
        elif choose == "4":
            tree_to_picture.main(cell_tree)
        elif choose == "5":
            exit(1)
        else:
            continue
