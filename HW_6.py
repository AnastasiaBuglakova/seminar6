import random

# 1 В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.
# год, номер которого кратен 400, — високосный;
# остальные годы, номер которых кратен 100, — невисокосные (например, годы 1700, 1800, 1900, 2100, 2200, 2300);
# остальные годы, номер которых кратен 4, — високосные[5];
# from sys import argv
#
# __all__ = ['check_date']
#
# def is_leapYear(year):
#     if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#         return True
#     else:
#         return False
#
#
# def check_date(date):
#     separator_set = {i for i in date if not i.isdigit()}
#     days_dict = {1: 31, 2: (28, 29), 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
#     separator = separator_set.pop()
#     day, mon, year = tuple(map(int, date.split(separator)))
#     if len(separator_set) > 1:
#         print(f'Wrong format of date: {date}, you have to use 1 separator.')
#     else:
#         if 0 < year < 10000:
#             if 0 < mon < 13:
#                 if mon == 2 and is_leapYear(year) and 0 < day <= days_dict[2][1]:
#                     return True
#                 elif mon == 2 and not is_leapYear(year) and 0 < day <= days_dict[2][0]:
#                     return True
#                 else:
#                     if 0 < day <= days_dict[mon]:
#                         return True
#             else:
#                 return False
#         else:
#             return False
#
#
# if __name__ == "__main__":
#     print(check_date("8:23:2023"))
# print(argv)
#
# check_date(argv[1])

# 2 Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

SIZE = 8


def fill_lines(gor, vert, chessboard_):
    res = []
    # // заполняем по горизонтали
    for i in range(8):
        if chessboard_[i][vert] == 0:
            chessboard_[i][vert] = 1
        elif chessboard_[i][vert] == '*' and i != gor:
            res.append(True)
    # // заполняем по вертикали
    for j in range(8):
        if chessboard_[gor][j] == 0:
            chessboard_[gor][j] = 1
        elif chessboard_[gor][j] == '*' and j != vert:
            res.append(True)
    # print_chessb(chessboard)

    # // заполняем по диагоналям
    for i in range(1, 8):
        if gor + i < 8 and vert + i < 8 and chessboard_[gor + i][vert + i] == 0:
            chessboard_[gor + i][vert + i] = 1
        elif gor + i < 8 and vert + i < 8 and chessboard_[gor + i][vert + i] == '*':
            res.append(True)
    for i in range(1, 8):
        if gor - i > -1 and vert - i > -1 and chessboard_[gor - i][vert - i] == 0:
            chessboard_[gor - i][vert - i] = 1
        elif gor - i > -1 and vert - i > -1 and chessboard_[gor - i][vert - i] == '*':
            res.append(True)
    for i in range(1, 8):
        if gor + i < 8 and vert - i > -1 and chessboard_[gor + i][vert - i] == 0:
            chessboard_[gor + i][vert - i] = 1
        elif gor + i < 8 and vert - i > -1 and chessboard_[gor + i][vert - i] == '*':
            res.append(True)
    for i in range(1, 8):
        if gor - i > -1 and vert + i < 8 and chessboard_[gor - i][vert + i] == 0:
            chessboard_[gor - i][vert + i] = 1
        elif gor - i > -1 and vert + i < 8 and chessboard_[gor - i][vert + i] == '*':
            res.append(True)

    return any(res)


def print_ch(chessboard_):
    for line in chessboard_:
        for item in line:
            print(f"{item}", end='  ')
        print()
    print("-" * 16)

# дана расстановка 8 ферзей на доске не бьющих друг друга
data1 = {(6, 2), (3, 4), (2, 7), (1, 1), (4, 6), (0, 3), (5, 0), (7, 5)}

# дана расстановка 8 ферзей на доске бьющих друг друга
data2 = {(6, 2), (6, 4), (2, 7), (1, 1), (4, 6), (0, 3), (5, 0), (7, 5)}

def check_chess(data_):
    chess_b = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
    for j in data_:
        chess_b[j[0]][j[1]] = '*'
        #     заполним единичками возможные линии хода ферзя, если на пути будет хоть одна * мы получим True из функции fill_lines
        if fill_lines(j[0], j[1], chess_b):
            print("Ферзи бьют друг друга ")
            return False
    else:
        print("Ферзи не бьют друг друга ")
        return True
    print(data)
    print_ch(chess_b)

check_chess(data1)
check_chess(data2)






#3 Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

#
# def print_chessb(chessboard_):
#     for line in chessboard_:
#         for item in line:
#             print(f"{item}", end='  ')
#         print()
#     print("-" * 16)
#
#
# def fillLines(gor, vert, chessboard_):
#     res = []
#     # // заполняем по горизонтали
#     for i in range(8):
#         if chessboard_[i][vert] == 0:
#             chessboard_[i][vert] = 1
#
#     # // заполняем по вертикали
#     for j in range(8):
#         if chessboard_[gor][j] == 0:
#             chessboard_[gor][j] = 1
#
#     # print_chessb(chessboard)
#
#     # // заполняем по диагоналям
#     for i in range(1, 8):
#         if gor + i < 8 and vert + i < 8 and chessboard_[gor + i][vert + i] == 0:
#             chessboard_[gor + i][vert + i] = 1
#
#     for i in range(1, 8):
#         if gor - i > -1 and vert - i > -1 and chessboard_[gor - i][vert - i] == 0:
#             chessboard_[gor - i][vert - i] = 1
#
#     for i in range(1, 8):
#         if gor + i < 8 and vert - i > -1 and chessboard_[gor + i][vert - i] == 0:
#             chessboard_[gor + i][vert - i] = 1
#         elif gor + i < 8 and vert - i > -1 and chessboard_[gor + i][vert - i] == '*':
#             res.append(True)
#     for i in range(1, 8):
#         if gor - i > -1 and vert + i < 8 and chessboard_[gor - i][vert + i] == 0:
#             chessboard_[gor - i][vert + i] = 1
#
#     return chessboard_
#
#
# chessboard = [[0 for _ in range(8)] for _ in range(8)]
# SIZE = 8
# all_comb = []
#
# def is_not_full(chessboard):
#     result = []
#     for line in chessboard:
#         result.append(False) if 0 in line else True
#     return not all(result)
#
#
# def all_combination():
#     while len(all_comb) < 92:
#         chessboard = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
#         ferzi = set()
#         while is_not_full(chessboard):
#             gor, vert = random.randint(0, SIZE - 1), random.randint(0, SIZE - 1)
#             if chessboard[gor][vert] == 0:
#                 chessboard[gor][vert] = '*'
#                 chessboard = fillLines(gor, vert, chessboard)
#                 ferzi.add((gor, vert))
#         if len(ferzi) >7 and ferzi not in all_comb:
#             all_comb.append(ferzi)
#     print(*all_comb, sep='\n')
#
#
# all_combination()
#
# # выводим случайных 4 расстановки
# M = 4
# for i in range(M):
#     chess = [[1 for _ in range(SIZE)] for _ in range(SIZE)]
#     for j in all_comb[i]:
#         chess[j[0]][j[1]] = '*'
#     print(all_comb[i])
#     print_chessb(chess)



