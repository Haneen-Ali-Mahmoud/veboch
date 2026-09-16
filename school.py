class Person :
    def __init__(self, name, email):
        self.name=name
        self.email= email
    def introduce(self):
        print (f"Hi , I am {self.name}")

class Student(Person):
    total_Students= 0
    def __init__(self, name, email, grade):
        super().__init__(name, email)
        self.__grade=grade
        self.courses=[]
        Student.total_Students += 1

    @property
    def grade(self):
        return self.__grade
    @grade.setter 
    def grade(self,value):
        if 0 <= value <= 100:
            self.__grade= value
        else:
            print("grade must be between 0 and 100 ")
    def add_course(self, course):
        self.courses.append(course)

    def introduce(self):
        print(
            f"Hi , I am {self.name}"
            f"I am a student and my grade is {self.grade}"
        )

class teacher (Person):
    def __init__(self, name, email,subject):
        super().__init__(name,email)
        self.subject= subject
        self.courses=[]

    def add_course(self, course):
        self.courses.append(course)

    def introduce(self):
        super().introduce()
        print(f"I am teaching {self.subject}")

class Course:
    total_courses = 0

    def __init__(self,name,teacher):
        self.name = name
        self.teacher= teacher
        self.students = []
        Course.total_courses +=1

    def add_student (self, student):

        if student not in self.students:
            self.students.append(student)
            
            print(f"{student.name} enrolled in {self.name}")
        else:
            print(f"{student.name} is already enrolles in {self.name}")
    def show_student(self):
        print(f"\nStudents in {self.name}: ")

        if len (self.students) ==0 :
            print("No students enrolled ")
            return
        for student in self.students:
            print(f"- {student.name}"
                  f"(Grade : {student.grade})")

Student.total_Students=0
Course.total_courses=0

print("===== school system ========")
t1= teacher("DR Ahmed", "ahmed@gmail.com", "CS")
c1=Course("python", t1)
t1.add_course(c1)