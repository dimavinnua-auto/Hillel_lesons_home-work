

adwentures_of_tom_sawer = """\n
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

#  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
# """ Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
# треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

new_row = adwentures_of_tom_sawer.replace("\n", " ")
print("task01_______________")
print(new_row)

# task 02 ==
# """ Замініть .... на пробіл
new_row2 = adwentures_of_tom_sawer.replace("....", " ")
print("task02_______________")
print(new_row2)

# # task 03 ==
# """ Зробіть так, щоб у тексті було не більше одного пробілу між словами.
new_row3 = adwentures_of_tom_sawer.strip(" ")
print("task03_______________")
print(new_row3)

# task 04
# """ Виведіть, скількі разів у тексті зустрічається літера "h"
new_row4 = adwentures_of_tom_sawer
a = adwentures_of_tom_sawer
print("task04_______________")
print(a.count('h'))

# # # task 05
# # """ Виведіть, скільки слів у тексті починається з Великої літери?
b = adwentures_of_tom_sawer.split()
count = 0
for word in b:
    if word[0].isupper():
        count += 1
print("task05_______________")
print(f"Слів, що починаються з великої літери: {count}")


# # # task 06
# # """ Виведіть позицію, на якій слово Tom зустрічається вдруге
words = adwentures_of_tom_sawer.split()
count = 0
idnnx = 0
for index, i in enumerate(words):
    if i == "Tom":
        count += 1
    if count == 2:
        idnnx = index
        break
print("task06_______________")
print(idnnx)

# # task 07
# """ Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
# Збережіть результат у змінній adwentures_of_tom_sawer_sentences
# adwentures_of_tom_sawer_sentences = None

b = adwentures_of_tom_sawer.rstrip()
print(b)




# # task 08
# """ Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
# Перетворіть рядок у нижній регістр.
# """
#
#
# # task 09
# """ Перевірте чи починається якесь речення з "By the time".
# """
#
#
# # task 10
# """ Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
# """
