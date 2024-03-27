class student():
    """descip of students(name,surname,age,year)"""
    def __init__(self,name,surname,age,year):
        self.name = name
        self.surname = surname
        self.age = age
        self.year = year
    
    def review(self):
        """printing data of student"""
        print("Student " + self.surname + " " + self.name + " " + str(self.age) + " years old currently on " + str(self.year) + " year of edu")

input_data = input("Введите данные студента (имя фамилия возраст курс): ")
name, surname, age, year = input_data.split()
student1 = student(name, surname, int(age), int(year))

student1.review()