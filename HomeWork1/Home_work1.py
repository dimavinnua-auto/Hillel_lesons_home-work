

# task 01 == Виправте синтаксичні помилки
print("task 01: Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"task 02: {hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print("task 03: Hello world!") # or ("letter")

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = "x"
x = 4
print(f'task 04: banana = {apples*x}')

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(f'task 06: {storona_1 + storona_2 + storona_3 + storona_4}')

# Задачі 07 -10:
# Переведіть задачі з книги "Математика, 2 клас"
# на мову пітон і виведіть відповідь, так, щоб було
# зрозуміло дитині, що навчається в другому класі

# task 07 == У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
# Скільки всього дерев посадили в саду?
apples_trees = 4
pear_trees = "x"
plum_trees = "y"
x = 5
y = 2

print(f'task 07: pear_trees {x * apples_trees}, plum_trees {apples_trees - y} ')

# task 08 == До обіда температура повітря була на 5 градусів вище нуля.
# Після обіду температура опустилася на 10 градусів.
# Надвечір потепліло на 4 градуси. Яка температура надвечір?
before = 5
after = 10
befor_night = 4
before_after = -5
morning = 0
print(f'task 08: До обіда температура повітря була {morning + before} , '
      f'Після обіду температура опустилася до {before - after},'
      f'температура надвечір {before_after+befor_night }')

# task 09 == Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
# 1 хлопчик захворів та 2 дівчинки не прийшли сьогодні. Скількі сьогодні дітей у театральному гуртку?
boys = 24
girls = 2
boy_ill = 1
two_girlmissing = 2
all_boys = 23
all_girls = 10
print(f'task 09: girl = {boys / girls}, present boy = {boys - boy_ill}, '
      f' present girl = {boys / girls - two_girlmissing},'
      f' all students {all_boys + all_girls}')

# task 10 Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
# а третя - як половина вартості першої та другої разом.
# Скільки будуть коштувати усі книги, якщо купити по одному примірнику?

first = 8
second = +2
thrd = "1.2*8"
print(f'task 10: second = {first + second}')
first = 8
second_b = 10
print(f'thrd = {first + second_b} / {3} ')
thrd = 18
print(f'thrd = {thrd / 3}')
thrd_c = 6
print(f'allbooks = {first+second_b+thrd_c}')
