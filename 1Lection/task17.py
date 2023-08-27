# Задача No17. Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4] Output: 6

array = [1, 1, 2, 0, -1, 3, 4, 4]
i = 0
j = len(array)-1
list1 = []

for i in range (len(array)):
    if array[i] not in list1:
        list1.append(array[i])
#print(list1, end= ',')
print(len(set(list1)))