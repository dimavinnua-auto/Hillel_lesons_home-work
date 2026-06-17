# # task 1
# """ Задача - надрукувати табличку множення на задане число, але
# лише до максимального значення для добутку - 25.
# Код майже готовий, треба знайти помилки та випраавити\доповнити.
# """

def multiplication_table(number):
    # Initialize the appropriate variable
    number = 25
    multiplier = 1

    # Complete the while loop condition.
    while multiplier <= number:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            pass
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(25)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# # task 2
# """Написати функцію, яка обчислює суму двох чисел."""
def sum (a, b):
    print(f"{a+b}")
sum(10, 20)

# # task 3
# """Написати функцію, яка розрахує середнє арифметичне списку чисел.
def arf (a,b,c):
    print(f"{(a+b)/c}")
arf(10,20,30)


# # task 4
# """Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
def revers(s):
    print(s[::-1])
revers("порядку")

# # task 5
# """Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
def long_word(text="Написати функцію яка приймає список слів"):
    words = text.split()
    return max(words, key=len)
print(long_word(text="Написати функцію яка приймає список слів"))



# # task 6
# """Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
# у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
# не є підрядком першого рядка."""

def find_substring(str1, str2):
    return -1
str1 = "Hello, world!"
str2 = "world"

print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"

print(find_substring(str1, str2)) # поверне -1

# # task 7
# # task 8
# # task 9
# # task 10
# """  Оберіть будь-які 4 таски з попередніх домашніх робіт та
# перетворіть їх у 4 функції, що отримують значення та повертають результат.
# Обоязково документуйте функції та дайте зрозумілі імена змінним.

#------>>>>> task 7 - 10
# Home_work1 (task 2, 4, 6,)

def sum1 (a, x):
    print(f"{a* x}")
sum1(2,4)


def sum2 (a,b,c,d):
    print(f"{a+b+c+d}")
sum2(2,3,4,5)


def sum3 (a,b):
    print(f"{a + b}!")
sum3("hello", "world")

apples_trees = 4
pear_trees = "x"
plum_trees = "y"
x = 5
y = 2

def sum4 (a = 4,b = x ,c = y):
    print(f"{a * b * c}")
sum4(4,5,8)






