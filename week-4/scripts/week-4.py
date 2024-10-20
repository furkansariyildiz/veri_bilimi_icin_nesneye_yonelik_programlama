#!/usr/bin/env python3



class Human:
    """
    Human class
    """
    def __init__(self, name: str, age: int, gender: str):
        """
        Constructor of Human class.

        **Args**:
            name (str): Name of the human.
            age (int): Age of the human
            genter (str): Gender of the human
        """
        self.name_ = name    
        self.__age = age
        self.gender_ = gender



    def get_age(self):
        """
        Getter method for age.

        **Args**:
            None
        """
        return self.__age
    

    def set_age(self, age: int):
        """
        Setter method for age.

        **Args**:
            age (int): Age of the human to be set private age value.
        """
        self.__age = age



    def give_info(self):
        """
        Give info method of Human class.

        **Args**:
            None
        """
        print(f"Name: {self.name_}, Age: {self.__age}, Gender: {self.gender_}")



class Teacher(Human):
    """
    Teacher class 
    """
    def __init__(self, name: str, age: int, gender: str, department: str):
        """
        Constructor of Teacher class. Inherits from Human class.

        **Args**:
            department (str): Department of the teacher.
        """
        super().__init__(name=name, age=age, gender=gender)
        self.department_ = department



    def talk(self):
        """
        Talk method of Teacher class.

        **Args**:
            None
        """
        print(f"{self.name_} is a teacher in {self.department_} department.")



class Student(Human):
    """
    Student class
    """
    def __init__(self, name: str, age: int, gender: str, lesson_class: str, number: int):
        """
        Constructor of Student class. Inherits from Human class.

        **Args**:
            lesson_class (str): Lesson class of the student.
            number (int): Number of the student.
        """
        super().__init__(name=name, age=age, gender=gender)
        self.lesson_class_ = lesson_class
        self.__number = number



    def get_number(self):
        """
        Getter method for number.

        **Args**:
            None
        """
        return self.__number
    


    def set_number(self, number: int):
        """
        Setter method for number.

        **Args**:
            number (int): Number of the student to be set private number value.
        """
        self.__number = number



    def join_lesson(self):
        """
        Join lesson method of Student class.

        **Args**:
            None
        """
        print(f"{self.name_} is joining the {self.lesson_class_} lesson.")


    
    def talk(self):
        """
        Talk method of Student class.

        **Args**:
            None
        """
        print(f"{self.name_} is a student in {self.lesson_class_} class.")



if __name__ == "__main__":
    human = Human("Alice", 25, "female")
    human.give_info()

    print("--------------------------------")

    teacher = Teacher("Bob", 35, "Male", "Computer Science")
    teacher.give_info()
    teacher.talk()

    print("--------------------------------")

    student = Student("Charlie", 20, "Male", "Math", 1812120)
    student.give_info()
    student.join_lesson()
    student.talk()

    print("--------------------------------")