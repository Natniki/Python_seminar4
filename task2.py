"""Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
находясь перед некоторым кустом заданной во входном файле грядки."""

N = int(input("количество кустов: "))

list1 = list()

for i in range(N):

    k = list1.append(int(input("сколько ягод на кусте: ")))

print(list1)


myList = list()

for i in range(len(list1)):

    myList.append(int(list1[i-2]+ list1[i-1]+ list1[i]))

print(max(*myList))