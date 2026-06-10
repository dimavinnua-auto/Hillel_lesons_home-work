
# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". Створіть об('єкт цього класу, '
# 'представляючи студента. Потім додайте метод до класу "Студент", ''який дозволяє змінювати середній бал студента.'
# "Виведіть інформацію про студента та змініть його середній бал)
class students():
    def __init__(self,name, secondname, age, grade):
        self.name = name
        self.secondname = secondname
        self.age = age
        self.grade = grade

one_students = students(name= 'Ivan', secondname='Golang', age = 21, grade = 10)
print( f"Name - {one_students.name},\nSoname - {one_students.secondname},\n"
       f"Age -{one_students.age},\nAverageGrade - {one_students.grade}")


