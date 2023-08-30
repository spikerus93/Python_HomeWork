# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

list_1 = "a a a b c a a d c d d" 
list_2 = list_1.split() 
dict ={} 
 
for i in list_2: 
    if i in dict: 
        print(f'{i}_{dict[i]}', end=' ')  
    else:  
        print(i, end=' ') 
    #dict[i] = dict.get(i,0) +1 
    dict[i] = dict.setdefault(i, 0) +1