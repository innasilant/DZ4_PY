# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# some_list1 = []
# n = int(input('Введите кол-во целых чисел первого набора: '))
# for a in range(n):
#     number1 = int(input())
#     some_list1.append(number1)

# some_list2 = []
# m = int(input('Введите кол-во целых чисел второго набора: '))
# for b in range(m):
#     number2 = int(input())
#     some_list2.append(number2)

# some_set1 = set(some_list1)
# some_set2 = set(some_list2)
# some_set1.intersection_update(some_set2)

# new_set = sorted(some_set1)

# print(new_set)


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
# на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, 
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

some_list = []
N = int(input('Введите кол-во кустов: '))
for a in range(N):
    berry = int(input())
    some_list.append(berry)

new_list = []
for i in range(len(some_list)):
       new_list.append(some_list[i-2] + some_list[i-1] + some_list[i])

print(max(new_list))