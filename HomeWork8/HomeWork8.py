
# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал". Створіть об('єкт цього класу, '
# 'представляючи студента. Потім додайте метод до класу "Студент", ''який дозволяє змінювати середній бал студента.'
# "Виведіть інформацію про студента та змініть його середній бал)
class Students():
    def __init__(self,name, secondname, age, grade):
        self.name = name
        self.secondname = secondname
        self.age = age
        self.grade = grade

one_student = Students(name= 'Ivan', secondname='Golang', age = 21, grade = 10)
print( f"Name - {one_student.name},\nSoname - {one_student.secondname},\n"
       f"Age -{one_student.age},\nAverageGrade - {one_student.grade}")


