# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

N = int(input('Введите число N: '))
factorial = 1
while N > 1:
    factorial *= N
    N -= 1

print (factorial)

# a = int(input('enter num: '))
# mylist = [0, 1]
# while fib < a:
#     fib = mylist[len(mylist) - 1] + mylist[len(mylist) - 2]
#     mylist.append(fib)
    
# print([-1, len(mylist)][fib == a])