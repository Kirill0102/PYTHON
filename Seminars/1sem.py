# введите два числа и определите большее

# первый вариант решения задачи:
# first = int(input("first "))
# second = int(input("second "))

# if first > second:
#     print("первое число больше второго")

# if first < second:
#     print("второе число больше первого")

# if first == second:
#     print('числа равны')

    
# второй вариант решения задачи:
# first = int(input("first "))
# second = int(input("second "))

# print(max(first,second))

# 3 вариант решения задачи
# в питоне 0 - булевое значение False,а остальные числа это True в условии
# first = int(input("first "))     
# second = int(input("second "))

# print(first > second)
# if 0:
#     print(first)

# if 12332:
#     print(second)

# 4 вариант решения задачи
# first = int(input("first "))     
# second = int(input("second "))

# if first == second:
#     print("=")
# elif first > second:
#     print(first)
# else:
#     print(second)

# print(18//8) # - целочисленное деление
# print(18%8) # - остаток от деления - остаток 2

# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# n = 700
# m = 750

# m = m * -1
# print((m//n) * -1)

# print ((m+n-1) // n) # для случая если m and n равны меду собой



# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых 
# математических класса и оборудовать кабинеты для 
# них новыми партами. За каждой партой может сидеть 
# два учащихся. Известно количество учащихся в 
# каждом из трех классов. Выведите наименьшее 
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# a = 20 
# b = 21 
# c = 22 

# print(a//2 + (-b // 2 * -1) + c // 2 )


# Задача №5. Решение в группах
# Вагоны в электричке пронумерованы натуральными 
# числами, начиная с 1 (при этом иногда вагоны 
# нумеруются от «головы» поезда, а иногда – с 
# «хвоста»; это зависит от того, в какую сторону едет 
# электричка). В каждом вагоне написан его номер. 
# Витя сел в i-й вагон от головы поезда и обнаружил, 
# что его вагон имеет номер j. Он хочет определить, 
# сколько всего вагонов в электричке. Напишите 
# программу, которая будет это делать или сообщать, 
# что без дополнительной информации это сделать 
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# i = 3 #  вагон по счету от головы поезда
# j = 4 #  номер вагона

# print(i + j -1)


# Задача №7. Решение в группах
# Дано натуральное число. Требуется определить, 
# является ли год с данным номером високосным. Если 
# год является високосным, то выведите YES, иначе 
# выведите NO. Напомним, что в соответствии с 
# григорианским календарем, год является 
# високосным, если его номер кратен 4, но не кратен 
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

# a = 2016
# if a // 4 == 0 and a //100 != 0 and a // 400 == 0:
#     print("YES")
# else:
#     print("NO")






