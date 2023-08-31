n = int(input("input lenght of list: "))

list1 = []

for i in range(n):

    k = list1.append(input("input number: "))

print(set(list1))

m = int(input("input lenght of list: "))

list2 = []

for i in range(m):

    k = list2.append(input("input number: "))

print(set(list2))

mylist =print(*sorted(set(list1).intersection(set(list2))))





