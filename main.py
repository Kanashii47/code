class student():
    """descip of students(name,surname,age,year)"""
    def __init__(self,name,surname,age,year):
        self.name = name
        self.surname = surname
        self.age = age
        self.year = year
    
    def review(self):
        """printing data of student"""
        print("Student " + self.surname + self.name + "and" + self.age + "years old currently on" + self.year + "year of edu")
student1 = student(input(str()),)
