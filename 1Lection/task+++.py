# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать все зараженные холодильники.
# Для каждого холодильника существует строка с данными, состоящая из строчных букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника, нумерация начинается с единицы
# Формат входных данных
# В первой строке подаётся число n – количество холодильников. В последующих # n строках вводятся строки, содержащие латинские строчные буквы и цифры, в каждой строке от 
# 5 до 100 символов.
# Формат выходных данных
# Программа должна вывести номера зараженных холодильников через пробел. Если таких холодильников нет, ничего выводить не нужно.

# Sample Input 1:
# 6 # 222anton456 # a1n1t1o1n1 # 0000a0000n00t00000o000000n # gylfole # richard # ant0n
# Sample Output 1:
# 1 2 3
# Sample Input 2:
# 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen
# anton
# aoooooooooontooooo
# elelelelelelelelelel
# ntoneeee
# tonee
# 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon
# unton
# Sample Output 2:
# 1 2 7 8

import re   # Импорт модуля Regular для преобразования строки в список.

count = int(input("Введите количество холодильников: "))
virus = 'anton' # Значение вируса
vir_list = re.findall(r'\w', virus) #Преобразование строки в список
result = []

print(vir_list)

for n in range(count):
   fridge_str = input("Задайте строки с данными: ")
   try:                      # Метод с исключением ошибки                   
      pos_end = -1
      for i in vir_list:
         pos_end = fridge_str.index(i, pos_end + 1)
      result.append(n+1)
   except: ValueError
   continue
print(*result)