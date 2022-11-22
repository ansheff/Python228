# name = "Anton"
# age = 20
# print("Hello,", name)
# print(age)
# print(type(name))
# print(type(age))
# a = 4
# b = 5
# print(a)
# a = b
# print(id(a))  # комментарий ставится через два пробела, а после решётки ещё один пробел
# print(id(b))
# ============================================
# a = b = c = 1
# print(a, b, c)
# ==========================================
# a, b, c = 5, "Hello", 9.2
# print(a, b, c)
# ==========================================
# _name_New_2 = "Bob"  # переменная не может начинаться с цифры
# print(_name_New_2)  # символ дефиса не допускается
# =====================================
# PI = 3.14  # "Константа"
# print(PI)
# PI = 2
# print(PI)  # В Питоне констант нет, переменные указанные в верхнем регистре изменять не нужно
# ============================================
# a = "Hello"  # Неявная типизпция
# print(type(a))
# a = 3
# print(type(a))  # Динамическая типизация
# ==========================================
# name = "Anton"
# age = 40
# print("Меня зовут: " + name + ". Мне " + str(age) + " лет")  # Сильная типизация
# print("Меня зовут: ", name, ". Мне ", age, " лет")
# ========================================================
# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# # c = a
# # a = b
# # b = c
# a, b = b, a
# придумать способ, как поменять местами значения переменных без использования третьей переменной и без использования этих двух способов
# =======================================================
# print("строка "
#       "символов")  # делает одну строку
# print('строка \
# символов')  # перевод на другую строку
#
# print("Документ \"script.py\" находится \rпо заданному пути \n\tD:\\\Python\\project") # Экранирование
# ============================================================
# s1 = "Hello"
# s2 = "Python"
# s3 = s1 + ", " + s2 + "!\t\t"
# print(s3 * 3)  # умножение строк может быть на целочисленное
# print("*" * 40)
# ======================================================
# print(352323458728489523)
# print(2.42348237897325472034)  # выводит только 15 символов после точки
# ============================================================
# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)  # 3.0 float
# print(7 / 2)  # 3.5 float
# print(6 // 2)  # целочисленное деление
# print(7 // 2)
# print(7 % 2)  # Остаток от деления
# print(7 ** 2)  # возведение в степень
# ==================================================================

# Следующее занятие

# number = 6 + 4 * 5 ** 2 + 7  # Сначала возведение в степень, потом умножение, а потом сумма слева направо
# print(number)  # 113
# ===============================================
# num = 10
# num += 5  # num = num + 5
# print(num)  # 15
# ===============================================
# num = 4321
# a = num % 10
# # print(a)
# num = num // 10
# # print(num)
# b = num % 10
# # print(b)
# num = num // 10
# # print(num)
# c = num % 10
# # print(c)
# num = num // 10
# # print(num)
# d = num % 10
# # print(d)
# e = a * 1000 + b * 100 + c * 10 + d
# print(e)
#
# num1 = 4321
# print(num1)
# res = (num1 % 10) * 1000  # 1000
# num1 = num1 // 10
# res += (num1 % 10) * 100
# num1 = num1 // 10
# res += (num1 % 10) * 10
# num1 = num1 // 10
# res += (num1 % 10)
# print(res)

# ========================================================
# int() - преобразовывает к целочисленному типу данных

# num1 = "2"
# num2 = 3
# res = int(num1) + num2
# print(res)
#
# print(int(3.8))  # отбросит всё после точки
# print(round(3.82))  # округление
# print(round(3.891, 2))  # два символа после точки округление

# ==================================

# a = 5 / 3
# print(round(a, 2))

# =====================================
# float() - преобразует к вещественному типу данных

# a = '5.2'
# b = 10
# c = float(a) + b
# d = round(c)
# print(type(d))

# ======================================

# a = 1
# b = 2
# print("a:", a, "\nb:", b)
# =====================================
# str() - преобразовывает к строковому типу данных

# name = "Виктор"
# age = 20
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep="---", end=" ")  # separator - разделитель
# print("Я учу Python.", end="\n\n")
# print("qqq")
# print(5 + 2, 3 + 4)  # 7 7
# ===============================================

# name = input("Ваше имя: ")
# city = input("Ваш город: ")
# print(name, city)

# ============================================

# num = input("Введите число: ")  # input всегда возвращает строковые данные
# stp = input("Введите степень: ")
# num = int(num)
# stp = int(stp)
# sum1 = num ** stp
# print("Число", num, "в степени", stp, "равно:", sum1)

# =====================================================

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# d = int(input("Введите четвёртое число: "))
# sum1 = a + b
# sum2 = c + d
# ch = sum1 / sum2
# print("Результат: ", round(ch, 2))

# =========================================================

# a = True
# b = False
# print(a + 5)  # 1 + 5
# print(b * 5)  # 0 * 5

# =====================================

# bool() - преобразует к булеву типу данных
# False = "", 0, False, None

# print(bool("python"))  # True
# print(bool(""))  # False
# print(bool(" "))  # True
# print(bool(0))  # False
# print(bool(1))  # True
# print(bool(-5))  # True
# print(bool(False))  # False
# print(bool(None))  # False

# ===============================================
# None
# test = None
# print(test)
# test = 5
# print(test)
# ================================================
# Операторы сравнения
# print(7 == 7)  # True
# print(2 + 5 != 7)
# print(8 > 7)  # True
# print(8 < 7)  # False
# print(8 <= 7)  # False
# print("привет" == "Привет")  # False
# ==================================================
# print(2 < 4 < 9)  # True
# print(2 * 5 > 7 >= 4 + 3)  # True
# print(9 * 3 <= 7 >= 2)  # False
# ====================================================
# a = 10
# b = 5
# c = a == b
# print(a, b, c)  # 10, 5, False
# =================================================
# Логические операторы (or, and, not)
# print(5 - 3 == 2 and 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 and 1 + 3 < 4)  # False (True : False)
# print(5 - 3 > 2 and 1 + 3 == 4)  # False (False : True)
# print(5 - 3 > 2 and 1 + 3 < 4)  # False (False : False)
#
# print(5 - 3 == 2 or 1 + 3 == 4)  # True (True : True)
# print(5 - 3 == 2 or 1 + 3 < 4)  # True (True : False)
# print(5 - 3 > 2 or 1 + 3 == 4)  # True (False : True)
# print(5 - 3 > 2 or 1 + 3 < 4)  # False (False : False)

# print(not 9 - 7)  # False
# print(not 7 - 7)  # True

# ==================================================
# IF

# cnt = 5
# if cnt < 10:
#     cnt += 1
# print(cnt)  # 6

# ====================================

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешён")
# else:
#     print("Давай, до свидания")

# =================================================

# a = 15
# b = 15
# if a > b:
#     print("a > b")
# elif a < b:
#     print("b > a")
# else:
#     print("b == a")

# =================================================

# a = int(input("Введите первую сторону: "))
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите третью сторону: "))
#
# if a == b == c:
#     print("Трегуольник равносторонний")
# elif a == b or a == c or b == c:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# ================================================

# m = int(input("Введите номер месяца: "))
# # if (m >= 1) and (m <= 12):
# if 1 <= m <= 12:  # диапазон
#     if m == 1 or m == 2 or m == 12:
#         print("Зима")
#     if m == 3 or m == 4 or m == 5:
#         print("Весна")
#     if m == 6 or m == 7 or m == 8:
#         print("Лето")
#     if m == 9 or m == 10 or m == 11:
#         print("Осень")
# else:
#     print("Ошибка ввода данных")

# СЛЕДУЮЩЕЕ ЗАНЯТИЕ

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:  # day >= 1 and day <= 5
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресение")
# else:
#     print("Такого дня недели нет")

# ========================================================

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ", end="")
#     if n == 1:
#         print(n, "ворона")
#     if 2 <= n <= 4:
#         print(n, "вороны")
#     if 5 <= n <= 9 or n == 0:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# =================================================

# Тернарное выражение

# a, b = 30, 20
# minim = a if a < b else b
# print(minim)

# =================================

# a, b = 30, 40
# # print("a == b" if a == b else "a > b" if a > b else "b > a")
#
# if a == b:
#     print("a == b")
# else:
#     if a > b:
#         print("a > b")
#     else:
#         print("b > a")

# ======================================

# a, b = 1, 0
# if b == 0:
#     print("На ноль делить нельзя")
# else:
#     print(a / b)

# print("На ноль делить нельзя" if b == 0 else a / b)

# ======================================

# Исключения

# print("Код выше")
# a = 5
# b = 0
# print(a / b)
# print("Код далее")

# ========================================

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")
# print("Код далее")

# ==========================================

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")

# ==============================================

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки")
#     print("Нельзя делить на ноль")
# else:  # Когда в блоке try не возникло исключение
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выполняется в любом случае
#     print("Конец программы")

# ====================================================

# n = input("Введите первое число: ")  # 9
# m = input("Введите второе число: ")  # "a"
# try:
#     n = int(n)  # 9
#     m = int(m)  # 'a' !!!
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)  # '9' + 'a'

# =======================================================

# ЦИКЛЫ

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# ==============================

# i = 1
# while i <= 21:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1

# =============================

# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# =====================================

# n = int(input("Укажите количество символов: "))
# while n > 0:
#     print("*", end="")
#     n -= 1

# =================================

# СЛЕДУЮЩЕЕ ЗАНЯТИЕ

# ==================================

# n = input("Введите целое число: ")
# print(type(n))
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число нецелое")
#         n = input("Введите целое число")
# if n %2 == 0:
#     print("Чётное")
# else:
#     print("Нечётное")

# ===========================================================

# i = 0
# while i < 10:  # True
#     print(i, end=" ")
#     if i == 5:
#         break  # После break ничего не выводится
#     i += 1
# print("\nЦикл звершён")

# =======================================================

# i = 0
# while i < 10:  # True
#     if i == 3:
#         i += 1
#         continue  # пропустит тройку и не выводит всё, что ниже
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл звершён")

# ============================================================

# while True:  # Бесконечный цикл
#     n = int(input("Введите положительное число: "))
#     if n > 0:
#         break  # Условие выхода

# ================================================

# sum1 = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     sum1 *= n
# print(sum1)

# ====================================

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i, end=" ")
#     i += 1
# else:  # Только в Питоне есть else в цикле while
#     print("\nЦикл окончен, i =", i)

# ============================================

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВложенный цикл: j =", j)
#         j += 1
#     i += 1

# =================================================

# Таблица умножения

# i = 1
# while i <= 9:
#     j = 1
#     while j <= 9:
#         print(i, '*', j, '=', i * j, end="\t")
#         j += 1
#     print()  # перенос на другую строку
#     i += 1

# ====================================================

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print('^', end='')
#         j += 1
#     print()
#     i += 1

# =============================================

# i = 1
# while i <= 5:
#     j = 0
#     while j < 20:
#         if i % 2 != 0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1

# ========================================

# Цикл FOR

# for element in collection:
#     print(element)

# for i in 'Hello!':
#     print(i)

# for color in 'red', 'orange', 'yellow':
#     print("color:", color)

# ========================================

# for i in range(n):
#     Тело цикла

# ==========================================

# range(start, stop, step)

# for i in range(2, 9, 2):
#     print(i, end=" ")
#
# print()
#
# j = 2
# while j < 9:
#     print(j, end=" ")
#     j += 2

# ==================================================

# for i in range(9, 0, -1):  # range работает только с интами
#     print(i, end=" ")
#
# print()
#
# j = 9
# while j > 0:
#     print(j, end=" ")
#     j -= 1

# =======================================================

# a = int(input("Введите целое число: "))
# for i in range(1, a):
#     if a % i == 0:
#         print(i, end=" ")

# ===================================================

# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=" ")

# ====================================================

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')

# ====================================================

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")

# ====================================================

# w = int(input("Введите длину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
#
# for i in range(h):
#     print('*' * w)

# ====================================================

# a = int(input("высота прямоугольника: "))
# b = int(input("Ширина прямоугольника: "))
# for i in range(a):
#     print()
#     for j in range(b):
#         if 0 < i < a - 1 and 0 < j < b - 1:
#             print(" ", end="")
#         else:
#             print("*", end="")

# ====================================================

# =================== домашнее задание №3==============
# a = 2
# b = 15
# res = 0
# # if a > b:
# #     a, b = b, a
# a, b = (a, b) if a < b else (b, a)
# while a <= b:
#     if a % 2:
#         res += a
#     a += 1
# print(res)
# # else:
# #     while b <= a:
# #         if b % 2:
# #             res += b
# #         b += 1
# #     print(res)
# =====================конец дз =========================

# =======================================================
# СЛЕДУюЩЕЕ занятие

# a = [i * 2 for i in "Hello"]
# print(a)
# =======================================================
# num = [i for i in range(30) if i % 2 == 0]
# print(num)
# =======================================================
# СПИСКИ

# num = [8, 3, "one", 3.2, [1, 2, 3]]
# print(num)
# print(type(num))
# print(num[1])  # 3
# print(num[4][1])  # 2
# print(num[-1][1])  # 2
# print(num[-2])  # 3.2
# num[2] = 256  # добавит в список 256 вместо строки "one"
# print(num)
# num[1] += 100  # прибавит 100 к 3
# print(num)
# num[-1] = 2
# print(num)
# =======================================================
# num = [8, 3, "one", 3.2, [1, 2, 3]]
# print("Длина списка:", len(num))  # Длина спсика 5
# =======================================================
# s = []  # Пустой список
# print(type(s))
# b = list("Hello")  # Создаёт список
# print(b)
# =======================================================

# s = [5] * 6
# print(s)
# =======================================================
# n = list(range(2, 10, 2))
# print(n)
# n2 = [2, 4, 6, 8]
# print(n2)
# if n == n2:
#     print("списки равны")  # но по адресам памяти разные
# else:
#     print("спсики разные")
# =======================================================

# [выражение for переменная in последовательность]

# a = [0 for i in range(5)]  # [0, 0, 0, 0, 0]
# print(a)

# =======================================================
# n = 5
# a = [i ** 2 for i in range(1, n + 1)]  # [1, 4, 9, 16, 25]
# print(a)
# =======================================================

# a = [1, 2, 3]
# b = [5, 6]
# c = b + a
# print(c)  # [5, 6, 1, 2, 3]
# d = c * 2  # только на целочисленное можем умножать
# print(d)  # [5, 6, 1, 2, 3, 5, 6, 1, 2, 3]

# =======================================================
# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)
# =======================================================
# a = [int(input("-> ")) for i in range(int(input("Количество элементов: ")))]
# print(a)
# =======================================================
# a = [4, 8, 9, 3, 2]
# for i in range(len(a)):  # i - индексы
#     # print(i)
#     print(a[i], end=" ")
# print()
# for elem in a:  # elem - элементы
#     print(elem, end=" ")
# =======================================================
# lst = ['один', 'два', 'три']
# for elem in lst:
#     print(elem * 2, end=" ")
# print()
# for i in range(len(lst)):
#     print(lst[i] * 2, end=" ")
# =======================================================

# sum1 = 0
# a = [0] * int(input("Введите количество элементов списка: "))
# for i in range(len(a)):
#     a[i] = int(input("-> "))
#     if a[i] < 0:
#         sum1 += a[i]
# print(sum1)

# =======================================================
# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Количсевто чётных элементов:", k)
# print("Количсевто нечётных элементов:", s)
# print()
# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in n:
#     if i % 2:
#         s += i
#     else:
#         k += 1
# print("количество четных : ", k)
# print("сумма нечетных", s)
# =======================================================
# a = [int(input('-> '))for i in range(int(input('Введите количество элементов: ')))]
# count = 0
# summa = 0
# for i in a:
#     summa += i
#     count += 1 if i != 0 else 0
# print('Среднее арифметическое: ', summa/count)
# print()
# n = 3
# zero_elem = 0
# sum = 0
# lst = [int(input('-> ')) for _ in range(n)]
# for i in lst:
#     if i == 0:
#         zero_elem += 1
#     sum += i
# print('Среднее арифметическое: ', sum / (n - zero_elem))
# =======================================================
# a = [int(input('-> ')) for i in range(int(input('Введите количество элементов: ')))]
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=' ')
# =======================================================
# a = [7, 8, 2, 1, 17]
# print(a)
# a[0], a[-1] = a[-1], a[0]
# print(a)

# =======================================================
# NEXT LESSON
# =======================================================
# Разбор ДЗ

# size = int(input("Введите размер поля: "))
# symbol = int(input("Введите количество символов: "))
# for i in range(size):
#     for j in range(symbol):
#         for n in range(size):
#             for m in range(symbol):
#                 print("  " if (i + n) % 2 else "* ", end="")
#         print()
#
# for i in range(5):
#     for n in range(5):
#         if (i + n) % 2 == 0:
#             print("+", end="")
#         else:
#             print("-", end="")
#     print()
# =======================================================

# СРЕЗЫ

# Список[start:stop:step]
# s= [5, 9, 3, 7, 1, 8]
# print(s[1:4])  # [9, 3, 7]
# print(s[2:])  # [3, 7, 1, 8]
# print(s[:2])  # [5, 9]
# print(s[1::2])  # [9, 7, 8]
# print(s[::-1])  # [8, 1, 7, 3, 9, 5]
# print(s[-2:2:-1])  # [1, 7]
# print(s[1:4:-1])  # []
# =======================================================
# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[:])
# # print(s[::-1])
# # print(s[::2])
# # print(s[1::2])
# # print(s[1::2])
# # print(s[:1])
# # print(s[-1:])
# # print(s[3:4])
# # print(s[4:])
# # print(s[-3:1:-1])
# # print(s[2:5])
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[3] = [30]  # [1, 20, 0, [30], 0, 4, 5, 6, 7]
# print(s)
# =======================================================
# МЕТОДЫ СПИСКОВ

# s = [1, 20, 0, 30, 4, 5, 6, 7]
# print(s)
# s.append(99)  # добавляет только один элемент в конец списка
# print(s)
# s.append([99, 7])  # добавляет вложеный список в конец списка
# print(s)
# s.extend([9, 8, 7])  # добавляет множество элементов в конец списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(1, 100)  # добавляет заданное значение(второй параметр) по указанному индексу (первый параметр)
# print(s)
# =======================================================
# s = []
# for i in range(1, 11):
#     s.extend([i ** 2])
# print(s)
# =======================================================
# lst = []
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # lst.append(x)
#     # lst.extend([x])
#     lst.insert(-1, x)
# print(lst)
# =======================================================
# n = int(input('Введите количество элементов списка: '))
# i = 0
# lst = []
# while i < n:
#     x = int(input('Ввведите число кратное 3: '))
#     if x % 3 != 0:
#         print(x, 'число не делится на 3 без остатка')
#     else:
#         lst.append(x)
#     i += 1
# print(lst)
# =======================================================
# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)
# =======================================================
# a = [1, 2, 3, 4, 2]
# b = [11, 22, 33]
# c = []
# print("a =", a)
# print("b =", b)
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):  # range(3, 5)
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(b[i])
#         c.append(a[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# =======================================================
# s = [1, 20, 0, 30, 4, 5, 6, 7]
# # s[4:] = []  # [1, 20, 0, 30]
# # s[2:6] = []
# if 20 in s:
#     s.remove(0)  # Удаляет первый найденный конкретный элемент списка
# print(s)
# last = s.pop()  # удаляет последний элемент из списка и возвращает удаляемый элемент
# print(last)
# print(s)
# second = s.pop(-2)  # Удаляет элемент по индексу
# print(s)
# # s.clear()  # Очищает список
# # del s[:]  # Очищает список
# del s[2]  # Удаляет конкретный элемент списка по индексу
# print(s)
# =======================================================
# s = []
# [s.append(int(input('-> '))) for i in range(int(input('Введите количество элементов: ')))]
# s = []
# s = [int(input('-> ')) for i in range(int(input('Введите количество элементов: ')))]
# print(s)
# k = int(input('Введите индекс: '))
# # del s[k]
# s.pop(k)
# print(s)
# =======================================================

# NEXT LESSON

# =======================================================

# print(dir(list))  # метод dir показывает методы у любого типа данных
# =======================================================

# s = [1, 20, 0, 30, 4, 0, 5, 6, 7, 0, 2]
# num = s.count(0)  # считает сколько нулей в списке
# print(num)
#
# ind = s.index(0, 6, -1)  # возвращает положение первого индекса с заданным значением
# print(ind)
#
# print(dir(list))

# =======================================================
# a = [1, 2, 3]
# b = a
# s_copy = a.copy()  # Возвращает копию списка, расположенную по другому адресу
# print("a = ", a)
# print("b = ", b)
# print("s_copy = ", s_copy)
# a.append(20)
# b.append(4)
# s_copy.append(444)
# print("a = ", a)
# print("b = ", b)
# print("s_copy = ", s_copy)
# print(id(a))
# print(id(b))
# print(id(s_copy))
# =======================================================
# s = [1, 20, 0, 30, 4, 0, 5, 6, 7, 0, 2]
# s.reverse()  # разворачивает список наоборот
# print(s)
# s.sort(reverse=True)  # reverse=True - сортировка по убыванию
# print(s)
#
# s2 = ["Виталий", "Сергей", "Александр", "Анна"]
# s2.sort(key=len, reverse=True)  # Сортирует по количеству символов в значениях списка
# print(s2)

# srt = sorted(s)  # делает дубликат и сортирует
# print(srt)
# print(s)
# print(id(srt))
# print(id(s))
# =======================================================

# Генератор случайных данных

# import random as r  # импортируем модуль random, как псевдоним r
# print(r.random())  # возвращает случайное число от нулья до единицы, не включая 1
# print(r.randint(2, 9))  # от 2 до 9 включительно
# print(r.randrange(0, 10, 2))  # диапазон start stop step

from random import *
# print(randint(2, 9))  # от 2 до 9 включительно, обязательно два значения
# print(randrange(0, 10, 2))  # диапазон start stop step
# print(uniform(10.5, 25.5))  # генерирует случайное десятичное число в диапазоне от a до b
# print(round(uniform(10.5, 25.5), 2))  # округлили до двух знаков после точки
#
# s = [55, 66, 77, 88, 99, 20, 30, 80, 90]
# print(choice(s))  # возвращает одно значение из списка любого типа данных
# print(choices(s, k=5))  # количество элементов слуайных
# print(s)
# shuffle(s)  # перемешивание элементов случайным образом
# print(s)

# =======================================================

# mas = [randint(0, 37) for i in range(36)]
# print(mas)

# =======================================================

# # lst = [5, 3, 2, 4, 1]
# lst = ['s', 'a', 'r']
# print(len(lst))
# # print(sum(lst))  # сумма элементов списка, работает и с int и float
# print(min(lst))  # находит минимальное значение среди элементов списка
# print(max(lst))  # находит макисмальное значение среди элементов списка

# =======================================================

# lst = [randint(0, 100) for i in range(10)]
# max_ = max(lst)
# print(lst)
# print(max_)
# lst.remove(max_)
# lst.insert(0, max_)
# print(lst)

# =======================================================

# lst = [randint(-20, 20) for i in range(10)]
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# =======================================================

# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# print('Min:', min(lst))
# l = lst.index(min(lst))
# print('index min:', l)
# lst[:l] = []
# print(lst)

# =======================================================

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)  # True
# print('e' in x)  # False
# print('a' not in x)  # False
# print('e' not in x)  # True

# lst = []
# # if len(lst) == 0:
# print(bool(lst))
# if not lst:
#     print("Список пустой")

# =======================================================

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений: ", c)
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общие для двух списков: ", c)
# c = [min(a), min(b), max(a), max(b)]
# print(c)
# =======================================================

# k = int(input("размер списка: "))  # 6
# s = []
# while len(s) < k:
#     n = randint(1, k)  # с 1 по 6
#     if n not in s:
#         s.append(n)
# print(s)


# =======================================================

# NEXT LESSON

# =======================================================

# m = [
#     [1, 2, 3, 4, 5],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12, 7, 8]
# ]
# print(m)
# print(m[1][2])
# print(m[1])

# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t')
#     print()

# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end='\t')
#     print()

# =======================================================

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# for row in m:
#     for x in row:
#         print(x, end='\t')
#     print()
# print()
#
# q = [[x ** 2 for x in row] for row in m]
#
# for row in q:
#     for x in row:
#         print(x, end='\t\t')
#     print()

# =======================================================

# n, m = int(input('Введите высоту матрицы: ')), int(input('Введите ширину матрицы: '))
# matr = [[0 for i in range(m)] for j in range(n)]
# for row in matr:
#     for x in row:
#         print(x, end='\t')
#     print()

# =======================================================
# a = [[1, 2], [3, 4], [5, 6], [7, 8]]
# for x, y in a:
#     print(x, "+", y, "=", x + y)
# =======================================================
# w, h = 5, 4
# matrix = [[randint(1, 30) for x in range(w)]for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()
# =======================================================
# w, h = 3, 4
# matrix = [[randint(-20, 10) for i in range(w)] for j in range(h)]
# count = 0
# for row in matrix:
#     for x in row:
#         if x <0:
#             count +=1
#         print(x, end='\t')
#     print()
# print('Количество отрицательных элементов: ', count)
# =======================================================
# w, h = 3, 4
# matrix = [[randint(0, 4) for i in range(w)] for j in range(h)]
# count = 1
# for row in matrix:
#     for x in row:
#         if x > 0:
#             count *= x
#         print(x, end='\t')
#     print()
# print('Произведение: ', count)
# =======================================================

# w, h = 6, 6
# matrix = [[randint(0, 10) for i in range(w)] for j in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()
# print()
#
# for row in range(len(matrix)):
#     if row % 2 == 0:
#         for col in range(len(matrix[row])):
#             print(matrix[row + 1][col], end='\t')
#         print()
#         for col in range(len(matrix[row])):
#             print(matrix[row][col], end='\t')
#         print()

# =======================================================

import math

# print(dir(math))
# num1 = math.sqrt(3)  # корень квадратный
# print(num1)
# print(3 * 3 ** (-1/2))
# num2 = math.ceil(3.2)  # округление вверх при любых обстоятельствах
# print(num2)
# num3 = math.floor(3.8)  # округляет вниз при любых обстоятельствах
# print(num3)
# print(math.pi)  # Число Пи
#
# radius = 2
# print('Площадь окружности с радиусом', radius, "=>", math.pi * radius ** 2)
# =======================================================

import time

# second = time.time()
# print("Секунды с начала эпохи: ", second)
# localtime = time.ctime(413310500)
# print(localtime)
# res = time.localtime(second)
# print(res)
# print(res.tm_year)
# print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("%m/%d/%Y, %H:%M:%S", time.localtime(435543535)))
# =======================================================
# pause = 5
# print("Program started...")
# time.sleep(pause)
# print(pause, "seconds.")
# =======================================================

# test = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time *= 60
# time.sleep(local_time)
# print(test)
# =======================================================
# start = time.monotonic()
# time.sleep(3)
# finish = time.monotonic()
# res = finish - start
# print(res)
# =======================================================

# import locale
# locale.setlocale(locale.LC_ALL, 'ru')
# print(time.strftime("Сегодня: %B %d, %Y"))

# =======================================================

# FUNCTIONS

# def hello(name, word):
#     print("Hello,", name, "Say", word)
#
#
# hello("Anton", 'hi')
# hello("Ivan", 'hello')

# =======================================================


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# n, m = 7, 9
# get_sum(n, m)
# get_sum('abc', 'def')
# get_sum(2.5, 4.3)
# =======================================================


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end='')
#         else:
#             print(b, end='')
#
#
# symbol(9, '+', '-')
# print()
# symbol(7, 'X', '0')
# =======================================================


# def get_sum(a, b):
#     return a + b
#
#
# x, y = 2, 5
# res = get_sum(x, y)
# print(res)
# print(get_sum(1, 8))


# =======================================================


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 16))

# =======================================================

# def result(one, two):
#     if one > two:
#         return one - two
#     else:
#         return one + two
#
#
# a, b = int(input("Введите первое число: ")), int(input("Введите второе число: "))
# print(result(a, b))

# =======================================================

# NEXT LESSON

# =======================================================


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['c', 'л', 'о', 'н']))

# =======================================================


# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(5, 10))
# =======================================================


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:  #
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надёжный пароль")
# else:
#     print("Это ненадёжный пароль")
# =======================================================


# def get_sum(a, b, c, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 3))
# =======================================================


# def line(a=20, b='-'):
#     print(b * a)
#
#
# line(10, '*')
# line()

# =======================================================


# def digit_sum(n, even=True):  # 123
#     s = 0
#     while n > 0:
#         cur_digit = n % 10  # 3 2 1
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10  # 12 1
#     return s
#
#
# print("Сумма четных цифр:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("Сумма нечетных цифр:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))

# =======================================================


# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Ira", 23)
# display_info(age=23, name="Ira")

# =======================================================

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)  # True
# print(lt1 is lt2)  # False
#
# a = 'Hello'
# b = 'Hello'
# print(a == b)  # True
# print(a is b)  # True


# =======================================================

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# lt1.pop(1)
# print(lt1)
# lt1[1] = 'Hello'
# print(lt1)
# print(id(lt1[1]))
# print(id(lt1))

# =======================================================

# s = "Hello"
# print(id(s))
# s += 'World'
# print(s)
# print(id(s))

# =======================================================

# a = 5
# print(id(a))
# a += 1
# print(a)
# print(id(a))

# =======================================================

# s = "Hello"
# # s[1] = 'a'
# print(id(s))
# s = s[1:-1]
# print(s)
# print(id(s))
#
#
# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1 = lt1[1:-1]
# print(lt1)
# print(id(lt1))

# lt1 = [1, 2, 3]
# print(id(lt1))
# # lt1 = lt1[1:-1]
# lt1 = lt1 + [4, 5]
# print(lt1)
# print(id(lt1))

# =======================================================

# КОРТЕЖ (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# =======================================================

# a = 1, 2, 3, 4, 5
# print(type(a))
# print(a)
# b = tuple((1, 2, 3, 4, 5))
# print(type(b))
#
# c = tuple("Hello")
# print(c)
# c = list("Hello")
# print(c)
# =======================================================

# t = (1,)
# print(t)
# print(type(t))

# =======================================================

# b = tuple((1, 2, 3, 4, 5))
# print(b)
#
# print(b[3])
# print(b[1:3])
# print(id(b))
# print(id(b[3]))

# =======================================================

# s = tuple(int(input("-> ")) for i in range(3))
# print(s)

# =======================================================

# s = input("Строка: ")
# a = tuple(s)
# print(a)

# =======================================================

# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# tpl = tuple(mas)
# print(tpl)
#
# print(tuple(randint(0, 100) for _ in range(10)))
# =======================================================

# print(tuple(2 ** i for i in range(1, 13)))

# =======================================================

# t1 = tuple('Hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)
# # print(len(t3))
# # print(t3.count('l'))  # 3
# # print(t3.count('a'))
# # print(t3.index('l'))
# # print(t3.index('l', 3))
# for i in t3:
#     print(i, end=' ')

# =======================================================

# NEXT LESSON

# =======================================================

# lst = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# # row = 0
# col = 0
# for row in lst:
#     for col in row:
#         print(col, end='\t')
#     print()
# # print("---------------")
# # print(row)
# # print("---------------")
# i = 0
# for col in row:
#     # print("*" * 5)
#     # print(col)
#     # print("*" * 5)
#     for row in lst:
#         print("=" * 10)
#         print(row)
#         print("=" * 10)
#         print(row[i], end='\t')
#     i += 1
#     print()

# =======================================================

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# =======================================================

# def ran(a, b):
#     return tuple(randint(a, b) for _ in range(10))
#
#
# tpl1 = ran(0, 5)
# tpl2 = ran(-5, 0)
# print(tpl1)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print('0 =', tpl3.count(0))

# =======================================================

# a = 123456
# s = str(a)
# lst = list(s)
# lst1 = []
# for i in lst:
#     lst1.append(int(i))
# print(lst1)

# =======================================================

# t = (10, 11, [1, 2, 3], (4, 5, 6), ['hello', 'world'])
# print(t, id(t))
# t[-1][0] = 'new'
# t[4].append('hi')
# print(t, id(t))

# =======================================================

# def set_element(lst):
#     return lst
#
#
# print(set_element())

# =======================================================

# РАСПАКОВКА КОРТЕЖА

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)

# =======================================================

# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# print(user[0])
# name1, age1, is_marries1 = user
# print(name1)

# =======================================================

# a = (1, 2, 3)
# # del a
# print(a)
# lst = list(a)
# lst.append(4)
# print(lst)
# tpl = tuple(lst)
# print(tpl)

# =======================================================

# countries = (
#     ('Германия', 80.2, (('Берлин', 3.326), ('Гамбург', 1.718))),
#     ('Франция', 66, (('Париж', 2.2), ('Марсель', 1.6)))
# )
# print(countries, end='\n\n')
# for country in countries:
#     # print(country)
#     countryName, countryPopulation, cities = country
#     print("\nСтрана:", countryName, "население = ", countryPopulation)
#     for city in cities:
#         # print(city)
#         cityName, cityPopulation = city
#         print('\tГород', cityName, 'население =', cityPopulation)
# =======================================================

# МНОЖЕСТВО (set)

# s = {'banana', 'apple', 'orange', 'apple'}
# print(type(s))
# print(len(s))
# =======================================================
#
# c = ['hello', 'world']
# a = set(c)
# print(a)
# =======================================================
# s = {x * x for x in range(10)}
# print(s)

# =======================================================
# num = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# print(num)
# # num = set(num)
# # print(num)
# # num = list(num)
# num = list(set(num))
# print(num)


# =======================================================


# def to_set(element):
#     return set(element), len(set(element))
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))
# =======================================================

# t = {'red', 'green', 'blue'}
# # print('green' not in t)
# for i in t:
#     print(i)

# =======================================================

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r }
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)

# =======================================================

# NEXT LESSON

# =======================================================

# a = {'Tom', 'Bob', 'Alice'}
# a.add('Ann')
# print(a)
# a.remove('Tom')
# print(a)
# user = 'Tom'
# if user in a:
#     a.remove(user)
# print(a)
# a.discard('Bob')
# print(a)
# a.pop()
# print(a)

# =======================================================

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# c = a | b
# print(c)

# =======================================================
# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # a.update(b)
# a |= b
# print(a)
# =======================================================
# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a & b
# print(c)
# =======================================================
# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a - b
# c = a ^ b
# print(c)
# =======================================================

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))
# print(sum(s))
# =======================================================
# s1 = "Hello"
# s2 = "How are you"
# s = set(s1) & set(s2)
# print(s)
# =======================================================
# s1 = "Python"
# s2 = "Programming language"
# s = set(s1) - set(s2)
# print(s)
# =======================================================

# drawing = {'Marina', 'Jenya', 'Sveta'}
# music = {'Kostya', 'Jenya', 'Ilya'}
# only = drawing ^ music
# print('Одно хобби: ', only)
#
# both = drawing & music
# print('Два хобби: ', both)
# drawing = drawing - both
# print('Один кружок: ', drawing)

# =======================================================
# s = frozenset([1, 2, 3, 4, 5, 4])
# print(s)
# c = [0, 1, 2]
# s1 = frozenset(c)
# print(s1)
# s -= s1
# print(s)
# # a = frozenset(["hello", "world"])
# # print(a)
# =======================================================

# СЛОВАРИ (dict)

# s = ['one', 'two']
# print(s[0])
# d = {1: 'one', 2: 'two'}
# print(d)
# print(d[1])

# d = {'one': 1, 'two': 2}
# print(d)
# print(type(d))
#
# d1 = dict(one=1, two=2)
# print(d1)
# print(type(d1))

# =======================================================

# УСНУЛ НА ПЕРЕМЕНЕ

# =======================================================

# NEXT LESSON

# =======================================================

# d = {'a': 1, 'b': 2, 'c': 3}
# print(d['b'])
# value = d.get('e', 'False')  # Что бы не выдавалась ошибка
# print(value)
# print(d)
# item = d.items()  # Кортеж?
# print(item)
# key = d.keys()  #
# print(key)
# value = d.values()  # Значения..
# print(value)
#
# for i, j in d.items():
#     print(i, "-> ", j)
# d.clear()

# item = d.pop('b', 5)
# print(item)
# it = d.popitem()
# print(it)

# item = d.setdefault('e', 5)
# print(item)

# d.update([('a', 7), ('q', 9)])
# print(d)

# d2 = d.copy()
# # d2 = d
# print("D =", d)
# print("D2 =", d2)
# d['e'] = 7
# d2['b'] = 5
# print("D =", d)
# print("D2 =", d2)

# =======================================================
# a = {'a': 1, 'b': 2}
# b = {'b': 3, 'c': 4}
# # c = a.copy()
# # c.update(b)
# c = a | b
# print(c)
# =======================================================
# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# d['location'] = d.pop('city')
# print(d)
# new_d = dict()
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
# print(d)
# print(new_d)

# =======================================================
# a = {
#     'First': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'Second':{
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y, ": ", a[x][y], sep="")

# =======================================================
# d = {'Один': 1, 'Два': 2, 'Три': 3, 'Четыре': 4}
# a = {key: value for key, value in d.items() if value <= 2}
# print(a)

# =======================================================
# # a = {i: i * 5 for i in "Hello"}
# # print(a)
# value = int(input('-> '))
# # lt = [1, 2, 3, 4, 5]
# a = {i: value for i in range(1, 9)}
# print(a)
# =======================================================
# d = dict.fromkeys(['a', 'b'], 100)
# print(d)
# =======================================================

# list()

# figures = {1: 'Rectangle', 2: 'Triangle', 3: 'Circle'}
# # value = list(figures.keys())
# # value = list(figures.values())
# value = list(figures.items())
# print(value)

# =======================================================
# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = dict()
# s = None
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i  # 'one'
#     else:
#         d[s].append(i)
# print(d)
# =======================================================

# zip()

# d = dict(zip([12, 1, 2], ['Dec', 'Jan', 'Feb']))
# print(d)

# a = [12, 1, 2]
# b = ['Dec', 'Jan', 'Feb']
# f = {k: v for k, v in zip(a, b)}
# print(f)

# =======================================================
# a = [1, 2, 3]
# print(list(zip(a)))
# =======================================================
# print(list(zip(range(5), range(100))))
# =======================================================
# a = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# b = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
# c = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
# for (k1, v1), (k2, v2), (k3, v3) in zip(a.items(), b.items(), c.items()):
#     print(k1, ' -> ', v1, ", ", v2, ", ", v3, sep="")
#     # print(k1, '-> ', v1)
#     # print(k2, '-> ', v2)
# =======================================================
# a = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# x, y = zip(*a)
# print(x)
# print(y)

# lt1 = [2, 1, 4, 3]
# lt2 = ['d', 'a', 'c', 'b']
# a1 = list(zip(lt2, lt1))
# print(a1)
# a1.sort()
# print(a1)

# =======================================================

# month = ['January', 'February', 'March']
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
# for sales, cost, m in zip(total_sales, prod_cost, month):
#     res = sales - cost
#     print("Чистая прибыль в", m, "=", res)

# =======================================================
# one = {'apple': 0.4, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two})
#
# for k, v in {**one, **two}.items():
#     print(k, "-> ", v)

# =======================================================
# NEXT LESSON
# =======================================================
# n = int(input("Количество студентов: "))
# stud = {}
# s = 0
# for i in range(n):
#     name = input(str(i+1) + "-й студент: ")
#     point = int(input("Балл: "))
#     stud[name] = point
#     s += point
# avrq = s / n
# print("Средний балл: ", round(avrq, 1))
# print("Студенты с баллом выше среднего: ")
# for i in stud:
#     if stud[i] > avrq:
#         print(i)
# =======================================================
# en = ["red", "green", "blue"]
# j = 1
# for i in en:
#     print(j, "-й цвет: ", i, sep="")
#     j += 1

# en = ["red", "green", "blue"]
# for j, i in enumerate(en, 1):
#     print(j, "-й цвет: ", i, sep="")
#     j += 1

# =======================================================
# en = {0: 1, 1: 2, 2: 3}
#
# for i, j in enumerate(en):
#     print(i, ": ", j, "->", en[j], sep="")
# =======================================================
# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)
# =======================================================
# def func(*args):
#     return args
#
#
# print(func(1))
# print(func(1, 2, 3, "abc"))
# print(func())
# =======================================================
# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# num1 = summa(1, 2, 3, 4, 5, 6, 7, 8)
# num2 = summa(6, 7, 8)
# print(num1)
# print(num2)
# =======================================================
# def to_dict(*args):
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('gray', (2, 17), 3.11, -4))

# =======================================================

# def func(*num):
#     lst = []
#     a = sum(num) / len(num)
#     print(a)
#     for i in num:
#         if i < a:
#             lst.append(i)
#     return lst
#
#
# print(func(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(func(3, 6, 1, 9, 5))
# =======================================================
# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))
# =======================================================
# def print_scores(stud, *scores):
#     print("Student name: ", stud)
#     for score in scores:
#         print(score, end=" ")
#     print()
#
# print_scores("Jonatan", 100, 95, 88, 92, 99)
# print_scores("Rick", 96, 20, 33)

# =======================================================
# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_odd=False):
#     res = []
#     for i in args:
#         if not only_odd or (only_odd and i % 2):
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))
# =======================================================
# def func(**kwargs):  # key word args
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a='Python'))
# =======================================================
# def info(**data):
#     for k, v in data.items():
#         print(k, "->", v)
#     print('*' * 20)
#
# info(first_name="Irina", last_name="Petrova", age=22, phone=1234567890)
# info(first_name="Igor", last_name="Ivanov", age=36, email='igor@gmail.com', country='Russia', phone=6789012345)

# =======================================================
# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='gray')
# print("my_dict =", my_dict)
# =======================================================
# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
#
# func1(1 ,2, 3, 4, 5)
# func2(one=123, two=456)
# =======================================================
# def func(a, *args, one=True, **kwargs):
#     return a, args, kwargs, one
#
#
# print(func(5, 9, 7, 8, 6, one=False, b=2, c=3, d=4))

# =======================================================

# Область видимости (scope)

# for i in range(5):
#     a = 5
#     print(i)

# if True:
#     a = 5
#
# print("a =", a)

# =======================================================

# name = "Tom"
#
# def hi():
#     print("Hello", name)
#
#
# def bye():
#     global name
#     name = "Bob"
#     print("Good bye", name)
#
#
# def func():
#     global surname
#     name = "Nick"
#     surname = "Ivanov"
#     print("name:", name)
#
#
# hi()
# bye()
# func()
# print(name)
# print(surname)
# =======================================================
# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()  # 5
# =======================================================

# def add_two(a):
#     x = 2
#     return a + x
#
#
# print(add_two(3))
# # print(x)

# =======================================================
# def func(a):
#     x = 2
#
#     def inner():
#         print("x =", x)
#         return a + x
#
#     return inner()
#
#
# print(func(5))  # 7
# =======================================================
# import builtins
#
# print(dir(builtins))
# =======================================================

# NEXT LESSON

# =======================================================

# Вложенные функции

# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#
#     inner_func()
#
#
# outer_func("world!")

# =======================================================
# def func1():
#     a = 6  # 2 строка
#
#     def func2(b):
#         a = 4  # 5 строка
#         print("Сумма: ", a + b)  # 6 строка
#
#     print("а:", a)  # 3 строка
#     func2(4)  # 4 строка
#
#
# func1()  # 1 строка
# =======================================================
# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#     print("global:", x)  # 25
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("nonlocal:", a)  # 35
#
#     inner()
#     print(a)
#     t = a
#
#
# fn()
# z = x + t  # 25 + 35 = 60
# print('results:', z)
# =======================================================
# x = 5
#
#
# def fn1():
#     x = 25
#
#     def fn2():
#         # x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x =', x)
#
#     fn2()
#     print('fn1.x =', x)
#
#
# fn1()
# print('x =', x)
# =======================================================
# def outer(a1, b1, a2, b2):
#     a = b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)

# =======================================================

# def increment(number):
#     def inner():
#         return number + 1
#     return inner()
#
#
# print(increment(10))
# =======================================================

# ЗАМЫКАНИЯ

# def outer(n):
#     def inner(x):
#         return n + x
#     return inner
#
#
# print(outer(5)(10))
#
# # res = outer(5)
# # print(res(10))
# # print(res(2))
# #
# # res2 = outer(7)
# # print(res2(5))

# =======================================================

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())
# =======================================================

# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
#
# res2 = func("Сочи")
# res2()
# res2()
# res2()
# res1()

# =======================================================
# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Elise': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make_classifier(lower, upper):
#     def classify_student(exam):
#         return {k: v for k, v in exam.items() if lower <= v <= upper}
#
#     return classify_student
#
#
# A = make_classifier(80, 100)
# B = make_classifier(70, 80)
# C = make_classifier(50, 70)
# D = make_classifier(0, 50)
# print(A(students))
# print(B(students))
# print(C(students))
# print(D(students))
# =======================================================
# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         print()
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())
# =======================================================

# NEXT LESSON

# =======================================================

# Анонимные функции, lambda-выражения

# =======================================================
# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func('a', 'b'))

# =======================================================
# print((lambda x, y: x ** 2 + y ** 2)(1, 2))

# =======================================================
# summ = lambda  a=1, b=2, c=3: a + b + c
# print(summ())
# print(summ(10))

# =======================================================
# func1 = lambda *args: args
#
# print(func1(1, 2, 3, 4))
# print(func1('a', 'b'))
# =======================================================
# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
# for t in c:
#     print(t("abc_"))
# =======================================================
# def inc1(n):
#     def wrap(x):
#         return x + n
#
#     return wrap
#
#
# f1 = inc1(42)
# print(f1(3))
#
#
# def inc(n):
#     return lambda x: x + n
#
#
# f = inc(42)
# print(f(3))
#
#
# inc2 = (lambda n: (lambda x: x + n))
# # f2 = inc2(42)
# # print(f2(3))
# print(inc2(42)(3))
#
# print((lambda n: (lambda x: x + n))(42)(3))
# =======================================================
# print((lambda a: (lambda b: (lambda c: a + b + c)))(2)(4)(6))
# =======================================================
# def func(i):
#     return i[1]
#
#
# d = {'b': 15, 'a': 10, 'c': 24}
# lst = list(d.items())
# print(lst)
# # lst.sort(key=lambda i: i[1], reverse=True)
# lst.sort(key=func, reverse=True)
# print(lst)
# dict1 = dict(lst)
# print(dict1)
# =======================================================
# players = [{'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#            {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#            {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#            {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}]
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# players.sort(key=lambda item: item['raiting'], reverse=True)
# print(players)
# =======================================================
# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[2](12, 5)
# print(b)
# =======================================================
# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 2]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))
# =======================================================
# d = {
#     1: (lambda: print('Понедельник')),
#     2: (lambda: print('Вторник')),
#     3: (lambda: print('Среда')),
#     4: (lambda: print('Четверг')),
#     5: (lambda: print('Пятница')),
#     6: (lambda: print('Суббота')),
#     7: (lambda: print('Воскресение'))
# }
#
# d[4]()
# =======================================================
# maximum = (lambda a, b: a if a > b else b)
# print(maximum(15, 13))
# =======================================================
# minimun = (lambda a, b, c: a if a < b else b if b < c else c)
# print(minimun(9, 8, 15))
# =======================================================

# Функция map()

# =======================================================
# def multiple(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
#
# # print(list(map(multiple, lst)))
# print(list(map(lambda t: t * 2, range(2, 10))))
# =======================================================
# t = 2.88, -1.75, 100.55
# print(list(map(lambda x: str(x), t)))
#
# a = ['2.88', '-1.75', '100.55']
# print(list(map(float, a)))

# =======================================================
# areas = [3.578945, 5.789456, 7.456789, 56.4123456, 9.0123456, 32.7789456]
# print(list(map(round, areas, range(1, 3))))

# =======================================================
# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
# lst = list(map(lambda x, y: (x, y), st, num))
# print(lst)
# tp = dict(lst)
# print(tp)
# =======================================================

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda x, y: (x + y), l1, l2)))

# =======================================================

# NEXT LESSON

# =======================================================

# filter(func, iterable)

# =======================================================
# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
#
# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: 75 < s < 88, b))
# print(res)
# =======================================================

# lst = [randint(1, 40) for i in range(10)]
# print(lst)
# res = list(filter(lambda s: 10 <= s <= 20, lst))
# print(res)

# =======================================================
# lst = [45, 55, 60, 37, 100, 105, 220]
# res = list(filter(lambda s: s % 15 == 0, lst))
# print(res)
# =======================================================

# ДЕКОРАТОРЫ

# =======================================================

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super_func'")
#     print(func())
#
#
# super_func(hello)
#
# test = hello
# print(test())

# =======================================================
# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
#
# def func_test():
#     print("Hello, I am func 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# =======================================================

# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print('Code before')
#         func()
#         print('Code after')
#     return wrap
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'func_test'")
#
# @my_decorator
# def hello():
#     print('Hello, I am func "func_test"')
#
# func_test()
# print()
# hello()
# =======================================================

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())

# =======================================================
# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции: ", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# =======================================================
# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("*" * 50)
#         fn(arg1, arg2)
#         print("*" * 50)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Лаврова")

# =======================================================
# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         fn(*args, **kwargs)
#         print("*" * 50)
#         print("args:", args)
#         print("kwargs:", kwargs)
#         print("*" * 50)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study='Python'):
#     print(a, b, c, "изучают", study)
#
#
# print_full_name("Ирина", "Борис", "Светлана", study="JavaScript")
# print()
# print_full_name("Владимир", "Екатерина", "Виктор")
# =======================================================
# def decor(*args):
#     def args_dec(fn):
#         def wrap(*x):
#             print(args[0], x[0], args[1], x[1], "=", end=" ")
#             fn(*x)
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)
# =======================================================
# def multiply(n):
#     def return_mult(fn):
#         def wrap(num):
#             return 'Результат:' + str(fn(num) * n)
#         return wrap
#
#     return return_mult
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))
# =======================================================
# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных")
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных")
#             return fn(*f_args, **f_kwargs)
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello! "):
#     return (x + y) * z
#
#
# # print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "Doge"))
# # print(typed_fn2("Hello, ", "World", "!"))
# # print(typed_fn3("Hello, ", "World. ", z=5))
# print(typed_fn3("Hello, ", "World", z="!!!"))

# =======================================================

# NEXT LESSON

# =======================================================
# def decor(tx=None, decor_text=''):
#     def wrapper(fn):
#         def wrap(*args):
#             print(decor_text, end="")
#             fn(*args)
#
#         return wrap
#
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
#
# @decor
# def hello_world2(text):
#     print(text)
#
#
# @decor(decor_text="Hello, ")
# def hello_world(text):
#     print(text)
#
#
# hello_world2("Hi!")
# hello_world("world!")
# =======================================================

# print(int('100', 2))  # 4
# print(int('100', 8))  # 64
# print(int('100', 16))  # 256
# print(int('100', 10))  # 100
# print(int('100'))  # 100

# =======================================================

# СИСТЕМЫ ИСЧИСЛЕНИЙ

# print(bin(18))  # 0b10010  # 0B
# print(oct(18))  # 0o22     # 0O
# print(hex(18))  # 0x12     # 0X
#
# print(0b100)  # 4
# print(0o20)  # 16
# print(0x11)
# =======================================================
# q = 'Pyt'
# w = 'hon'
# e = q + w
# print(e)
# # print(e * 3)
# # print('e' in e)
# # print(e[-1::-1])
# e = e[:3] + 't' + e[4:]
# print(e)
# =======================================================
# def change_char(s, c_old, c_new):
#     s2 = ""
#     for i in s:
#         if i != c_old:
#             s2 += i
#         else:
#             s2 += c_new
#
#     return s2
#
#
# st = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования"
# st2 = change_char(st, 'N', 'P')
# print("st1 =", st)
# print("st2 =", st2)
# =======================================================
# print(u"Привет")  # Строки в юникоде
# print(r'C:\file.txt')  # "сырые" строки, игнорируют спецсимволы
# print('C:\\file.txt')
# print(r'C:\file.txt\\'[:-1])
# print(r'C:\file.txt' + "\\")
# print('C:\\file.txt\\')

# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет")
# print("Меня зовут ", name, ". Мне ", age, " лет", sep="")
# print(f"Меня зовут {name}. Мне {age} лет")  # f - строка
#
# print(f"{round(2.356789, 2)}")  # 2.36
# print(f"{2.356789:.2f}")  # 2.36
# =======================================================
# x = 10
# y = 5
# print(f"{x} x {y} / 2 = {int(x * y / 2)}"
#       f" - выражение")
# =======================================================
# d = 74
# print(f"{{d}}")
# =======================================================
# dir_name = 'doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# print("home\\" + dir_name + "\\" + file_name)
# =======================================================
# s = """<div>
#     <a href="#">content</a>
# </div>
# """
# print(s)
# s1 = '''<div>
#     <a href="#">content</a>
# </div>
# '''
# print(s1)
# =======================================================
# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""  # данный комментарий должен быть только первой строкой
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)  # Выведет документацию (комментарий функции), если она есть
# __doc__ - магическая переменная
# =======================================================
# def cylinder(r, h):
#     """
#     Здесь краткое описание функции.
#
#     Здесь полное описание функции.
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# =======================================================

# NEXT LESSON

# =======================================================
# print(ord('a'))  # показывает порядковый номер символа в юникоде
# print(ord('ш'))  # первые 128 символов это символы из ASCII

# =======================================================
# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break
# =======================================================
# my_str = "Testeee string for me"
# arr = [ord(x) for x in my_str]
# print(arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print(arr)
# arr += [x for x in [ord(x) for x in input("-> ")[:3]] if x not in arr]  # [:6:2] - пробелы
# print(arr)
# if arr[-1] in arr[:-1]:
#     print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)
# =======================================================
# print(chr(97))  # из кода символов получаем сам символ
# print(chr(35))  # - #
# print(chr(8364))  # - символ валюты евро
# =======================================================
# a = 122
# b = 97
# while b <= a:
#     print(chr(b), "", end="")
#     b += 1

# =======================================================
# print('apple' == 'Apple')  # False
# print('apple' > 'Apple')  # True
# print(ord('a'))  # 97
# print(ord('A'))  # 65
# =======================================================
# SHORTEST = 6
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     res = ""
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += random_char
#     return res
#
#
# print("Ваш случайный пароль:", random_password())

# =======================================================
# print(dir(str))
# =======================================================
# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# print(s.title())  # Hello, World! I Am Learning Python.
#
# print(s.count("l", 3))  # подсчитывает количество вхождений подстроки в строку, подстрокой считается то, что мы ищем
# print(s.find("Python1"))  # ищет в строке заданную подстроку, если она найдена, то возвращает индекс первого
# # вхождения подстроки, если нет - то возвращает "-1"
# =======================================================
# a = "один два"
# b = a[:a.find(" ")]
# c = a[a.find(" ") + 1:]
# print(c + " " + b)
# =======================================================
# a = 'ab12c59p7dq'
# digits = []
#
# # for i in a:
# #     if i in '1234567890':
# #         digits.append(int(i))
# # print(digits)
#
# for i in a:
#     if '1234567890'.find(i) != -1:
#         digits.append(int(i))
# print(digits)
# =======================================================
# s = "hello, WORLD! I am learning Python."
# print(s)
# # print(s.index("Python1"))  # ищет в строке заданную подстроку, если она найдена, то возвращает индекс первого
# # вхождения подстроки, если нет - то возвращает исключение ValueError
#
# print(s.rfind('h'))
# print(s.rindex('h'))
# =======================================================
# s = "hello, WORLD! I am learning Python."
# first = s.find('h')
# last = s.rindex('h')+1
# print(s[:first] + s[last:])
# =======================================================
# print('abc123'.isalnum())  # определяет состоит ли строка из цифр или букв
# print('ABCabc'.isalpha())  # определяет состоит ли строка из букв
# print('123'.isdigit())  # определяет состоит ли строка из цифр
# print('abc2'.islower())  # определяет состоит ли строка из строчных букв
# print('ACDC1'.isupper())  # определяет состоит ли строка из заглавных букв
# =======================================================
# print('py'.center(9, "-"))  # выводит по центру текст относительно заданного количества цифр
# print(' py '.center(30, "*"))  # выводит по центру текст относительно заданного количества цифр
# =======================================================
# print("   py".lstrip())  # удаляет пробелы с левой стороны
# print("py   ".rstrip())  # удаляет пробелы с правой стороны
# print("     py   ".strip())  # удаляет пробелы и справа и слева
#
# print("https://www.python.org".lstrip('/:pths'))
# print("py.$$$;".rstrip(';$.'))
#
# print("https://www.python.org".lstrip('htps:/').rstrip("org."))
# print("https://www.python.org".strip('htps:/worg.'))
#
# print("https://www.python.org".strip('/:pthsworg').strip('.'))
# =======================================================

# NEXT LESSON

# =======================================================
# s = "11 23 44 55 23 22"
# s_old = input("Заменяемая подстрока: ")
# s_new = input("Новая подстрока: ")
# i = s.find(s_old)
# # print(i)
# while i != -1:
#     ll = len(s_old)
#     s = s[0:i] + s_new + s[i+ll:]
#     i = s.find(s_old)
# print(s)
# =======================================================
# st = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(st)
# print(st.replace("Nython", "Python", 2))  # заменяет вхождение подстроки
# =======================================================
# s = "-"
# seq = ("a", "b", "c")
# print(s.join(seq))  # a-b-c
# =======================================================
# print("..".join(['1', '2']))  # метод объединяет итерируемую последовательность (список, кортеж, другая строка) в одну
# # строку через заданный символ разделитель
#
# print(":".join("Hello"))
# =======================================================
# print("Строка разделённая пробелами".split())  # метод делит строку на список из подстрок
# # print("Строка_разделённая_пробелами".split("_"))
# # print("Строка разделённая пробелами".split("а"))
# =======================================================
# print('www.python.org.ru'.split(".", 1))
# =======================================================
# a = list(map(int, input("-> ").split()))
# print(a)
# print(type(a[0]))
# =======================================================
# a = input('Введите ФИО: ').split()
# print(a[0], ' ', a[1][0], '.', a[2][0], '.', sep='')
#
# s = input('ФИО: ').split()
# print(f'{s[0]} {s[1][0]}. {s[2][0]}.')
# =======================================================
# print('www.python.org.ru.'.split(".", 2))
# print('www.python.org.ru.'.rsplit(".", 2))
#
# print('www...python...org'.split("."))
# =======================================================
# s = "В строке заменить пробелы символом"
# s = s.split(" ")
# s = "*".join(s)
# print(s)
# =======================================================

# РЕГУЛЯРНЫЕ ВЫРАЖЕНИЯ

# =======================================================

import re

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'\.'  # r поадваляет двойные бекслеши
#
# print(s.find(reg))
# print(re.findall(reg, s))  # ['я', 'я']  возвращает список, содержащий все совпадения
# print(re.findall('12', s))  # []
#
# print(re.search(reg, s))  # метод находит месторасположение первого объекта
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# =======================================================
# print(re.match(reg, s))  # поиск по заданному шаблону в начле строки
# =======================================================
# print(re.split(reg, s, 1))  # возвращает список, в котором строка разбита по шаблону

# =======================================================
# print("C:\\folder\\file.txt")
# print(r"C:\folder\file.txt")
# =======================================================
# print(re.sub(reg, "!", s, 1))  # поиск и замена
# =======================================================
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9578 19_4 5"
# reg = r'[А-яё.]'  # [А-Яа-яЁё]
# reg = r'[^0-9]'  # всё что угодно кроме цифр
# reg = r'[^039]'  # всё что угодно кроме 0, 3 и 9
# reg = r'\d'  # ищет совпадения с цифрами от 0 до 9
# reg = r'\w'  # смотри описание в специальных парах символах
# reg = r'\W'  # смотри описание в специальных парах символах
# reg = r'\A\w\s\w'  # Я и
# reg = r'\w\s\w\Z'  # 4 5
# reg = r'\b\w\s\w'  #
# ПОВТОРЕНИЯ
# reg = r'\w+'  # + от 1 до бесконечности
# reg = r'\w*'  # * от 0 до бесконечности
# reg = r'\w?'  # ? или 0 или 1
# reg = r'[12][90][0-9][0-9]'

# print(re.findall(reg, s))

# s1 = "Ели[-ели]."
# pattern = r'[А-яё.\[\]-]'
# print(re.findall(pattern, s1))
# =======================================================
# s1 = "Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09."
# pattern = '[0-2][0-]:[0-9][0-9]'
# print(re.findall(pattern, s1))
# =======================================================

# NEXT LESSON

# =======================================================
# s1 = "Цифры: 7, +17, -42, 0013, 0.3"
# pattern = r'[+-]?\d+[.\d]*'
# print(re.findall(pattern, s1))
# =======================================================
# s1 = "05-03-1987 # Дата рождения"
# print('Дата рождения:', re.sub(r'-', '.', re.sub(r'#.*', '', s1)))
# =======================================================
# s1 = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# pattern = r'\w+\s*=[^;]+'
# print(re.findall(pattern, s1))
# =======================================================
# s1 = '12 сентября 2021 года'
# reg1 = r'\d{2,4}'
# print(re.findall(reg1, s1))
# =======================================================
# test = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# print(re.findall(r'\+?7\d{10}', test))
# =======================================================
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта. 9578 19_4 5"
# # reg = r'^\w+\s\w+'
# reg = r'\w+\s\w+$'
# print(re.findall(reg, s))
# =======================================================


# def login(a):
#     return re.findall(r'^[\w!@#$-]{8,25}$', a)
#
#
# print(login('admin_admin'))
# print(login('admin!_admin'))
# =======================================================
# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))

# print(re.findall(r'[а-я]', 'Я я', re.I))
# =======================================================
# text = """
# one
# two
# """
# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, re.MULTILINE))  # работает только с многострочным текстом
# =======================================================
# text = """
# one
# two
# """
# print(re.findall(r'one.\w+', text))
# print(re.findall(r'one.\w+', text, re.DOTALL))
# =======================================================

# NEXT LESSON

# =======================================================
# print(re.findall("""
# [A-z.-]+   # part 1
# @          # поиск символа @
# [a-z_.-]+  # part 2
# """, 'test@mail.ru', re.VERBOSE))
# =======================================================
# text = 'hello world'
# print(re.findall(r'\w\+', text, re.DEBUG))
# =======================================================
# text = """Python,
# python,
# PYTHON"""
# reg = "(?im)^python"
# print(re.findall(reg, text))  # flags=re.IGNORECASE + re.MULTILINE
# =======================================================
# s = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru."
# reg = r'[\w.-]+@[\w.]+[^., ]'
# print(re.findall(reg, s))
# =======================================================
# text = "<body>Пример жадного соответствия регульярных выражений</body>"
# print(re.findall("<.+?>", text))
#
# # *?, +?, ??
# # {m,n}?, {,n}, {m,}?
#
# t = "2324 786 22 4569"
# reg = r'\d{1,3}?'
# print(re.findall(reg, t))
# =======================================================
# s = "<p>Изображение <img src='bg.jpg alt='картинка'> - фон страницы</p>"
# reg = r'<img\s+[^>]*?src\s*=\s*[^>]+>'
# print(re.findall(reg, s))  # <img src='bg.jpg>
# =======================================================
# s = "Python (в русском языке встречается название питон[16] или пайтон[17]) - высокоуровневый язык программирования " \
#     "общего назначения с динамической строгой типизацией и автоматическим управлением памятью[18][19]"
# print(re.findall(r'\[\d+]', s))
# =======================================================
# s = 'Пётр и Ольга отлично учатся!'
# reg = 'Пётр|Виталий|Ольга'
# print(re.findall(reg, s))
# =======================================================
# s = "int = 4, float = 4.0, double = 8.0f"
# # reg = r"int+\s*=\s*\d[.\w+]*|double\s*=\s*\d+[.\w+]*"
# reg = r"(?:int|double)\s*=\s*\d[.\w+]*"
# print(re.findall(reg, s))
#
# # () - группирующая скобка, сохраняющая
# # (?:) - группирующая скобка, не сохраняющая
# =======================================================
# # 192.168.255.255
# s = '127.0.0.1'
# # reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}(?:\d{1,3})'
# print(re.findall(reg, s))
# =======================================================
# s = "Word2016, PS6, AI5"
# reg = r'(([A-z]+)(\d*))'
# print(re.findall(reg, s))
# =======================================================
# s = "5 + 7*2 - 4"
# # reg = r'\s*[+*-]\s*'  # ['5', '7', '2', '4']
# # reg = r'\s*([+*-])\s*'  # ['5', '+', '7', '*', '2', '-', '4']
# reg = r'[^+* -]'
# print(re.split(reg, s))
# =======================================================
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[1])  # вернулось то, что в первой круглой скобке
# print(m[2])
# print(m[0])  # вернулось всё регулярное выражение
# =======================================================
# print("Hello")  # GitHub
# =======================================================

# NEXT LESSON

# =======================================================
# print("Vnesli izmeneniya")  # GitHub
# =======================================================
# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[1])  # вернулось то, что в первой круглой скобке
# print(m[2])
# print(m[0])  # вернулось всё регулярное выражение
# print(re.search(reg, s).group(3))
# =======================================================
# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
#
# def replace_find(m):  # в m попадает результат регулярного выражения
#     global count
#     count += 1
#     return f"<option value='{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r"\s*(\w+)\s*", replace_find, text))
# =======================================================
# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# reg = r'<img\s+[^>]*src=([\'"])(.+)\1>'
# print(re.findall(reg, s))
# =======================================================
# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# reg = r'<img\s+[^>]*src=(?P<q>[\'"])(.+)(?P=q)>'  # задали имя для круглой скобки и обратились к ней
# print(re.findall(reg, s))
# =======================================================
# s = "Самолёт прилетает 10/23/2023. Будем рады вас вас видеть после 10/24/2023."
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.findall(reg, s))
# print(re.sub(reg, r'\2.\1.\3', s))  # Если укажем имена круглых скобок, то работать не будет
# =======================================================
s = "google.com and google.ru"
reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
print(re.findall(reg, s))  # Возвращает кортеж из всех совпадений
print(re.sub(reg, r"http://\1", s))  # нулевых скобок не бывает
# =======================================================

# =======================================================
# =======================================================
