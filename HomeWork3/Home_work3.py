from pydoc import resolve

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland_1:str = (
'Would you tell me, please, which way I ought to go from here?'
'"\n"That depends a good deal on where you want to get to, said the Cat.'
'\n"I don t much care where ——" said Alice.'
'\n"Then it doesn t matter which way you go," said the Cat.'
'\n"—— so long as I get somewhere, Alice added as an explanation.'
'\n"Oh, you re sure to do that, said the Cat, if you only walk long enough.')
print( f"Task:01____________ \n {alice_in_wonderland_1}" )

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
alice_in_wonderland_2_and_3 = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I "don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
# task 03 == Виведіть змінну alice_in_wonderland на друк
print( f"Task:02 and 03________________ \n {alice_in_wonderland_2_and_3}" )


#     # Задачі 04 -10:
#     # Переведіть задачі з книги "Математика, 5 клас"
#     # на мову пітон і виведіть відповідь, так, щоб було
#     # зрозуміло дитині, що навчається в п'ятому класі

# task 04
# Площа Чорного моря становить 436 402 км2, а площа Азовського
# моря становить 37 800 км2. Яку площу займають Чорне та Азов-
# ське моря разом?

black_sea = 436402
azov_sea = 37800
vol = "km2"
Result = black_sea + azov_sea
print("Task:04___________________")
print (f'{Result} {vol}')

# # task 05
# Мережа супермаркетів має 3 склади, де всього розміщено
# 375 291 товар. На першому та другому складах перебуває
# 250 449 товарів. На другому та третьому – 222 950 товарів.
# Знайдіть кількість товарів, що розміщені на кожному складі.
sum_items_all = 375291
Sum_items_1and2 = 250449
sum_items_2and3 = 222950

Result = sum_items_all - Sum_items_1and2
Result2 = sum_items_all - sum_items_2and3
Result3 = sum_items_all - Result - Result2
# if sum_items_all is Result+Result2+Result3 == sum_items_all:
print("Task:05___________________")
print(f'sum_items_all = {sum_items_all}')
print (f'{Result3} - supermarket2')
print (f'{Result} - supermarket3')
print (f'{Result3} - supermarket1')
print (f'{Result2} + {Result} + {Result3} = {sum_items_all}')


# task 06
# Михайло разом з батьками вирішили купити комп’ютер, ско-
# риставшись послугою «Оплата частинами». Відомо, що сплачу-
# вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
# вартість комп’ютера.
long = 18
sum_per_m = 1179
Result = long * sum_per_m
print("Task:06___________________")
print(f'{Result} cost of comp')


# # task 07
# """
# Знайди остачу від діленя чисел:
# a) 8019 : 8     d) 7248 : 6
# b) 9907 : 9     e) 7128 : 5
# c) 2789 : 5     f) 19224 : 9
a_div = 8019
b_div = 8
# Results = a_div % b_div
print("Task:07___________________")
print (f'a = {a_div % b_div}, b = {9907 % 9}, c = {2789 % 5}, d = {7248 % 6}, e = {7128 % 5}, f = {19224 % 9}')

# # task 08
# Іринка, готуючись до свого дня народження, склала список того,
# що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
# для даного її замовлення.
# Назва товару    Кількість   Ціна
# Піца велика     4           274 грн
# Піца середня    2           218 грн
# Сік             4           35 грн
# Торт            1           350 грн
# Вода            3           21 грн
pizza_big = 274
pizza_items_big = 4
Results = pizza_big * pizza_items_big
pizza_midl = 218
pizza_items_midl = 2
Results_2 = pizza_midl * pizza_items_midl
jus = 35
jus_items = 4
Results_3 = jus * jus
cake = 350
cake_items = 1
Results_4 = cake * cake_items
water = 21
water_items = 3
Results_5 = water * water
print("Task:08___________________")
print (f'{Results + Results_2 + Results_3+ Results_4 + Results_5}грн. ')

# # task 09
# """
# Ігор займається фотографією. Він вирішив зібрати всі свої 232
# фотографії та вклеїти в альбом. На одній сторінці може бути
# розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
# Ігорю, щоб вклеїти всі фото?

all_photo = 232
one_list = 8
print("Task:09___________________")
print(f'{232 / 8} lists')


# # task 10
# """
# Родина зібралася в автомобільну подорож із Харкова в Буда-
# пешт. Відстань між цими містами становить 1600 км. Відомо,
# що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
# становить 48 літрів.
# 1) Скільки літрів бензину знадобиться для такої подорожі?
# 2) Скільки щонайменше разів родині необхідно заїхати на зап-
# равку під час цієї подорожі, кожного разу заправляючи пов-
# ний бак?
road = 1600
petrol =  9
tank = 48
Result_r = (road / 100) * petrol
Results_t = (Result_r / tank)

print("Task:10___________________")
print (f'{Result_r} litr')
print (f'{Results_t} times')