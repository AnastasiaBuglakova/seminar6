# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на
# угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки
# # исчерпаны.
# from random import choice
#
# def stor_of_puzzles():
#     dict_puzzle = {"Зимой и летом одним цветом!": ['елка', 'ель', 'елочка'],
#                           'Висит груша нельзя скушать': ['lamp', 'лампа', 'лампочка']}
#
#     result = choice(list(dict_puzzle))
#     return result, dict_puzzle[result]
#
#
# def guess(tries):
#     puzzle, answers = stor_of_puzzles()
#     print(puzzle)
#     while tries > 0:
#         user_answer = input('Please input your answer: ').lower()
#         if user_answer in answers:
#             print(f"You are lucky! {tries}")
#             break
#         else:
#             print('Wrong answer, try again')
#         tries -= 1
#     else:
#         print(f"Game over! You are loser(Answer was {answers[0]}")
#
# guess(4)



# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
#
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
#
# Для формирования результатов используйте генераторное выражение.
# def score(cf, scores):
#     for i in scores:
#         print(cf * i)
#
# cf = 0.2
# scores = [4,5,4]
# score(cf, scores)


l = [0,9,7,6]
print(type(*l))