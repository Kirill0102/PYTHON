# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120


# n = int(input("Введите целое число")) # --- input 5
# i = 1
# Factorials = 1 
# while i <= n :
#     Factorials *= i
#     i = i + 1
#     print(Factorials) 



# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по 
# счету числом Фибоначчи оно является, то есть 
# выведите такое число n, что φ(n)=A. Если А не 
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6



# n = int(input())

# n0 = 0
# n1 = 0
# n2 = 1
# i = 2

# while n0 < n:
#     n0 = n1 + n2
#     n1 = n2
#     n2 = n0
#     i += 1
# if n0 > n:
#     i = -1

# print(i)




# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю 
# наблюдений за погодой. Они обратились к синоптикам, а те, в 
# свою очередь, занялись исследованиями статистики за 
# прошлые годы. Их интересует, сколько дней длилась самая 
# длинная оттепель. Оттепелью они называют период, в 
# который среднесуточная температура ежедневно превышала 
# 0 градусов Цельсия. Напишите программу, помогающую 
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2


# N = int(input("Введите общее количество рассматриваемых дней на промежутке 1 ≤ N ≤ 100: "))
# nBolsheNulya = 0

# for i in range(N):
#     t = int(input("Введите температуру "))
#     if t > 0:
#         nBolsheNulya = nBolsheNulya + 1
#     elif t < 0:
#         nBolsheNulya = nBolsheNulya + 0


# print(nBolsheNulya)



# n = int(input())
# d=0
# t=0
# for i in range(1,n+1):
#           s=int(input())
#           if s>0:
#                     d=d+1
#           elif d>t :
#                     t=d
#                     d=0
# print(t)











# 15. Иван Васильевич пришел на рынок и решил 
# купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз 
# потяжелей, а для тещи полегче. Но вот незадача: 
# арбузов слишком много и он не знает как же выбрать 
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза


# numA = 4 #колличество арбузов
# w = int(input())
# ma = w
# mi = w

# for i in range(numA-1):
#     w = int(input()) #вес каждого из арбузов
# if w > ma:
#     ma = w
# elif w < mi:
#     mi = w
# print(ma,mi)





    