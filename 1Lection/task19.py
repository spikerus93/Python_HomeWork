# Задача No19. Решение в группах
# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3 Output: [4, 5, 1, 2, 3]

import time

lst = [1, 2, 3, 4, 5]
k = 100
x = time.time()
for i in range (len(k % lst[i])):
    last_el = lst.pop()
    lst.insert(0, last_el)
y = time.time()
print(lst)
print(y-x)

# lst = [1, 2, 3, 4, 5]
# shift = 2
# for i in range(shift):
#     lst.insert(0, lst.pop())
# print(lst)

# lst = [1, 2, 3, 4, 5]
# shift = 3
# for i in range(shift%len(lst)):
#     lst.insert(0, lst.pop())
# print(lst)
# Так вроде тоже работает 