# if and else
#if  true
#is_rainy = True
#if is_rainy:
#    print('Беру зонт')
#    print('Надеть сапоги')
#else:
#    print('Не беру зонт')
#print('иду гцлять')
#is_rainy = False
#if is_rainy:
#    print('Беру зонт')
#    print('Надеть сапоги')
#else:
#    print('Не беру зонт')
#print('иду гцлять')
# if без else
# is_rainy = True
# if is_rainy:
#     print('Беру зонт')
# print('Иду гулять')
# is_rainy = False
# if is_rainy:
#     print('Беру зонт')
# print('Иду гулять')
# is_rainy = True
# heavy_rainy = True
# if is_rainy:
#     if heavy_rainy:
#         print('Беру зонт')
#     else:
#         print('Беру дождевик')
# else:
#     print('Не беру зонт')
# print('Иди гулять')
# print('Пять болше трех?', 7 != 12) # True
# print("Длина слова равна 1?", len("Hello") == 1) #False
# print("7 не равно 12?", 7 != 12) # True
# Посчитаем пример
# example = (2 > 3) and (2 < 2) or (1 != 5) and (not (5 < 3) or (3 == 1))
# my_result = False and False or True and (not False or False)
# my_result = False and False or True and (True or False)
# my_result = (False and False) or (True and True)
# my_result = False or True
# my_result = True
# print(example)
# print(my_result)
# print(example == my_result)
# str 1 = 'test'
# str 2 = "test"
# str 3 '''test'''
# str 4 = """test"""
# print(str_1 == str_2 == str_3 == str_4)
# print(
#      (str_1 == str_2)
#      and (str_2 == str_3)
#      and (str_3= str_4)
# )
# Плохо
# from test4 import a
#
# if a > 10:
#     print('a больше 10')
# else:
#     if a 10:
#         print('a меньше 10')
#     else:
#         print('a равно 10')
# Хорошо
# if a > 10:
#     print('a больше 10')
# elif a < 10:
#     print('a меньше 10')
# else:
#     print('a равно 10')