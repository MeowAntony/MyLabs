from PIL import Image, ImageDraw, ImageFont


class Cell:
    def __init__(self, value, left, right, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def generate_tree(mas, index, cell_now):
    cell_left = Cell(mas[index * 2 + 1], None, None, parent=cell_now) if len(mas) > index * 2 + 1 else None
    cell_right = Cell(mas[index * 2 + 2], None, None, parent=cell_now) if len(mas) > index * 2 + 2 else None
    cell_now.left = cell_left
    cell_now.right = cell_right
    if cell_left:
        generate_tree(mas, index * 2 + 1, cell_left)
    if cell_right:
        generate_tree(mas, index * 2 + 2, cell_right)


def get_glubina(cell_now: Cell):
    if cell_now is None:
        return 0
    return 1 + max(get_glubina(cell_now.left), get_glubina(cell_now.right))


def get_x_y(diameter, level_now, level_max, index_element):
    """
    Получаем x и y для клеточки

    :param diameter: Дисаметр
    :param level_now: какой сейчас уровень (сверху вниз)
    :param level_max: максимальный уровень
    :param index_element: индекс элемента на строке
    :return: x и y
    """
    for_x = 0
    for i in range(level_max - level_now):
        for_x = for_x * 2 + 1
    x_plus = (diameter * 3 / 4) * for_x
    x = 100 + x_plus + index_element * ((diameter * 3 // 2) * (2 ** (level_max - level_now)))
    y = 50 + (diameter * 3 / 2) * level_now
    return x, y


def draw_pole(draw, diameter, level_now, level_max, index_element, cell_now: Cell):
    """
    Рисуем наше деревко

    :param draw: Рисовалка
    :param diameter: Дисаметр
    :param level_now: какой сейчас уровень (сверху вниз)
    :param level_max: максимальный уровень
    :param index_element: индекс элемента на строке
    :param cell_now: текущая клеточка
    """

    x, y = get_x_y(diameter, level_now, level_max, index_element)

    if cell_now.left is not None:
        x_left, y_left = get_x_y(diameter, level_now + 1, level_max, index_element * 2)

        draw.line((x + diameter // 2, y + diameter // 2,
                   x_left + diameter // 2, y_left + diameter // 2), fill=(80, 209, 235),
                  width=diameter // 20)

        draw_pole(draw, diameter, level_now + 1, level_max, index_element * 2, cell_now.left)

    if cell_now.right is not None:
        x_right, y_right = get_x_y(diameter, level_now + 1, level_max, index_element * 2 + 1)

        draw.line((x + diameter // 2, y + diameter // 2,
                   x_right + diameter // 2, y_right + diameter // 2), fill=(80, 209, 235),
                  width=diameter // 20)

        draw_pole(draw, diameter, level_now + 1, level_max, index_element * 2 + 1, cell_now.right)

    draw.ellipse((x, y, x + diameter, y + diameter), fill=(80, 209, 235))
    font = ImageFont.truetype("./123.ttf",
                              diameter // 2)  # FIXME вот тут шрифт задавать, можно контролировать в зависимости от числа
    draw.text((x + diameter // 2, y + diameter // 2),
              str(cell_now.value) if cell_now.value else "", anchor="mm", font=font, fill=(0, 0, 0))


def main(cell: Cell):
    glubina = get_glubina(cell) - 1
    diam = 100
    img = Image.new("RGBA", (200 + diam + ((2 ** glubina) - 1) * (diam * 3 // 2),
                             100 + diam + (diam * 3 // 2) * glubina), 'grey')
    draw_img = ImageDraw.Draw(img)

    draw_pole(draw_img, diam, 0, glubina, 0, cell)

    img.show()
# for i in range(4):
#     draw_img.ellipse((100 + i * (d * 1.5), 100 + (d * 3 / 2) * 2,
#                       100 + d + i * (d * 1.5), 100 + (d * 3 / 2) * 2 + d))
#
# for i in range(2):#75 1
#     draw_img.ellipse((100 + d * 3 // 4 + i * (d * 1.5) * 2, 100 + (d * 3 / 2) * 1,
#                       100 + d + d * 3 // 4 + i * (d * 1.5) * 2, 100 + (d * 3 / 2) * 1 + d))
#     pass
# for i in range(1):#150 3
#     draw_img.ellipse((100 + (d * 3 // 4) * 3 + i * (d * 1.5) * 2, 100,
#                       100 + d + (d * 3 // 4) * 3 + i * (d * 1.5) * 2, 100 + d))
#     pass
# for i in range(2):#300 7
#     draw.ellipse((100 + 525 + i * 1200, 250, 725 + i * 1200, 350))
#     pass
# for i in range(1):#600 15
#     draw.ellipse((100 + 1125 + i * 2400, 100, 1350 + i * 2400, 200))
#     pass
