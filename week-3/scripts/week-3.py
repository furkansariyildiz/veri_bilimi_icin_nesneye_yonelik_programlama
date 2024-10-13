#!/usr/bin/env python3



class Human:
    """
    Human class
    """
    def __init__(self, name: str, age: int):
        """
        Constructor of Human class.

        **Args**:
            name (str): Name of the human.
            age (int): Age of the human.
        """
        self.name_ = name
        self.age_ = age


    
    def talk(self):
        """
        Talk method of Human class.

        **Args**:
            None
        """
        print(f"Hello, my name is {self.name_} and I am {self.age_} years old.")



class Teacher(Human):
    """
    Teacher class
    """
    def __init__(self, name: str, age: int, department: str):
        """
        Constructor of Teacher class. Inherits from Human class.

        **Args**:
            name (str): Name of the teacher.
            age (int): Age of the teacher.
            department (str): Department of the teacher.
        """
        Human.__init__(self, name, age)
        self.department_ = department



    def talk(self):
        """
        Talk method of Teacher class.

        **Args**:
            None
        """
        print(f"Hello, my name is {self.name_} and I am {self.age_} years old. I am a teacher in {self.department_} department.")



    def teach(self):
        """
        Teach method of Teacher class.

        **Args**:
            None
        """
        print("I am teaching.")



class Student(Human):
    """
    Student class
    """
    def __init__(self, name: str, age: int, department: str, university_club: str):
        """
        Constructor of Student class. Inherits from Human class.

        **Args**:
            name (str): Name of the student.
            age (int): Age of the student.
            department (str): Department of the student.
        """
        Human.__init__(self, name, age)
        self.department_ = department
        self.university_club_ = university_club



    def talk(self):
        """
        Talk method of Student class.

        **Args**:
            None
        """
        print(f"Hello, my name is {self.name_} and I am {self.age_} years old. I am a student in {self.department_} department. I am a member of {self.university_club_} club.")    



    def study(self):
        """
        Study method of Student class.

        **Args**:
            None
        """
        print("I am studying.")



class Secretary(Human):
    """
    Secretary class
    """
    def __init__(self, name: str, age: int, department: str, office: str):
        """
        Constructor of Secretary class. Inherits from Human class.

        **Args**:
            name (str): Name of the secretary.
            age (int): Age of the secretary.
            department (str): Department of the secretary.
            office (str): Office of the secretary.
        """
        Human.__init__(self, name, age)
        self.department_ = department
        self.office_ = office


    
    def talk(self):
        """
        Talk method of Secretary class.

        **Args**:
            None
        """
        print(f"Hello, my name is {self.name_} and I am {self.age_} years old. I am a secretary in {self.department_} department. My office is {self.office_}.")



    def organize(self):
        """
        Organize method of Secretary class.

        **Args**:
            None
        """
        print("I am organizing.")



if __name__ == '__main__':
    human = Human("Furkan", 28)
    human.talk()

    print("------------------------------------\n")

    teacher = Teacher("Ali", 35, "Computer Engineering")
    teacher.talk()
    teacher.teach()

    print("------------------------------------\n")

    student = Student("Ayse", 22, "Computer Engineering", "Robotics Club")
    student.talk()
    student.study()

    print("------------------------------------\n")
    
    secretary = Secretary("Mehmet", 30, "Computer Engineering", "C-101")
    secretary.talk()
    secretary.organize()
    