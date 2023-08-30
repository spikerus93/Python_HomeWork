# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
text1 = text.lower().replace("." , " ").split()
print(len(set(text1)))


# другое решение
# text_1 = 'She sells sea shells on the sea shore The shells' 
# text_2 = text_1.lower() 
# text_3 = text_2.replace(('.' and ';' ), '')  
# text_4 = text_3.split(' ' or '  ') 
# text_5 = set(text_4) 
# print(len(text_5))