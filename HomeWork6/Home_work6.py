

# #6.1
# # Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - вивести в консоль True,
# # інакше - False. Строку отримати за допомогою функції input()

text = input('how much - enter value - ')
unique_chars = set(text)
if len(text) > 10:
 print (True)
else:
 print (False)

# #6.2
# # Напишіть цикл, який буде вимагати від користувача ввести слово,
# # в якому є літера "h" (враховуються як великі так і маленькі).
# # Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

while True:
    word = input("Введіть слово, що містить літеру 'h': ")
    if 'h' in word.lower() or word.isupper():
        print("Дякую! Слово містить літеру 'h'.")
        break
    else:
        print("Помилка: слово не містить літери 'h'. Спробуйте ще раз.")


# 6.3
# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг,
# які присутні в lst1. Данні в лісті можуть бути будь якими

list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
list2 = []
for l in list1:
    if isinstance(l, str):
        list2.append(l)
print(list2)

# 6.4
# # Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
list_value = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_value_list = 0
list_value_sum = []

for num in list_value:
    if num % 2 == 0:
        sum_value_list += num
        list_value_sum.append(num)
print("Сума парних чисел:", sum_value_list)