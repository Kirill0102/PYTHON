# Найдите сумму цифр трехзначного числа. 

# num = 123

# a = 123 % 10
# b = 123 % 100 // 10 
# c = 123 // 100

# print(a + b + c)




# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# S = int(input("Введите число"))    # 8
# PetyAndSereza = S // 2
# Katya = S - PetyAndSereza
# print(PetyAndSereza // 2, Katya, PetyAndSereza // 2)




# # Вы пользуетесь общественным транспортом? Вероятно, вы
# # расплачивались за проезд и получали билет с номером. Счастливым
# # билетом называют такой билет с шестизначным номером, где сумма
# # первых трех цифр равна сумме последних трех. Т.е. билет с номером
# # 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# # программу, которая проверяет счастливость билета.

# S = int(input("ВВедите шестизначное число ")) # 385916

# A = S // 1000
# B = S % 1000

# Q = A % 10 + A % 100 // 10 + A // 100
# W = B % 10 + B % 100 // 10 + B // 100

# if Q == W :
#     print("Билет счастливый")
# else:
#     print("Билет не счастливый")



# Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).



n = int(input("Введите число "))
m = int(input("Введите число "))
k = int(input("Введите число "))

if (n * m - k) % 2 == 0 :
    print("yes")
else:
    print("no")
