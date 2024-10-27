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
            age (int): Age of the human
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
        super().__init__(name, age)
        self.__department = department


    def talk(self):
        """
        Talk method of Teacher class.

        **Args**:
            None
        """
        print(f"Hello, my name is {self.name_} and I am {self.age_} years old. I am a teacher in {self.__department} department.")




class Student(Human):
    """
    Student class
    """
    def __init__(self, name: str, age: int, faculty: str, number: int):
        """
        Constructor of Student class. Inherits from Human class.

        **Args**:
            name (str): Name of the student.
            age (int): Age of the student.
            faculty (str): Faculty of the student.
            number (int): Number of the student.
        """
        super().__init__(name, age)
        self.__faculty = faculty
        self.__number = number


    
    def talk(self):
        """
        Talk method of Student class.

        **Args**:
            None
        """
        print(f"Hello, my name is {self.name_} and I am {self.age_} years old. I am a student in {self.__faculty} faculty. Also my number is {self.__number}.")




class Worker:
    """
    Worker class
    """
    def __init__(self, name: str, age: int, salary: int, shift: int):
        """
        Constructor of Worker class.

        **Args**:
            name (str): Name of the worker.
            age (int): Age of the worker.
            salary (int): Salary of the worker.
            shift (int): Shift of the worker. 
        """
        self.name_ = name
        self.age_ = age
        self.salary_ = salary
        self.shift_ = shift


    
    def work(self):
        pass



    def CV(self):
        """
        CV method of Worker class.

        **Args**:
            None
        """
        return (f"Name: {self.name_}, Age: {self.age_}, Salary: {self.salary_}, Shift: {self.shift_}")




class BlueCollarWorker(Worker):
    """
    BlueCollarWorker class
    """
    def __init__(self, name: str, age: int, salary: int, shift: int, work_type: str):
        """
        Constructor of BlueCollarWorker class. Inherits from Worker class.

        **Args**:
            name (str): Name of the blue collar worker.
            age (int): Age of the blue collar worker.
            salary (int): Salary of the blue collar worker.
            shift (int): Shift of the blue collar worker.
            work_type (str): Work type of the blue collar worker.
        """
        super().__init__(name, age, salary, shift)
        self.__work_type = work_type



    def work(self):
        """
        Work method for blue collar workers.

        **Args**:
            None
        """
        print(f"{self.name_} is working as a {self.__work_type} worker.")



    def CV(self):
        """
        CV method of BlueCollarWorker class.

        **Args**:
            None
        """
        return super().CV() + f", Work Type: {self.__work_type}"



class WhiteCollarWorker(Worker):
    """
    WhileCollarWorker class
    """
    def __init__(self, name: str, age: int, salary: int, shift: int, work_type: str, education: str):
        """
        Constructor of WhiteCollarWorker class. Inherits from Worker class.

        **Args**:
            name (str): Name of the white collar worker.
            age (int): Age of the white collar worker.
            salary (int): Salary of the white collar worker.
            shift (int): Shift of the white collar worker.
            work_type (str): Work type of the white collar worker.
            education (str): Education of the white collar worker.
        """
        super().__init__(name, age, salary, shift)
        self.__work_type = work_type
        self.__education = education



    def work(self):
        """
        Work method for white collar workers.

        **Args**:
            None
        """
        print(f"{self.name_} is working as a {self.__work_type} worker.")



    
    def CV(self):
        """
        CV method of WhiteCollarWorker class.

        **Args**:
            None
        """
        return super().CV() + f", Work Type: {self.__work_type}, Education: {self.__education}"


class Week5:
    """
    Week5 class
    """
    def __init__(self):
        pass


    def question1(self):
        """
        We need to use 'def' keyword to create function.
        So answer is 'def'
        """


    def question2(self):
        """
        For converting input to integer, we can use int() function.
        So answer is 'int'
        """
        a = int(input("Enter your grade: "))
        print(a)
        print(a * 5)
        print(a + 5)



    def question3(self):
        """
        while, continue, if, elif, else and break are control statements.
        But 'def' keyword is used to create function.
        So answer is 'def'
        """


    def question4(self):
        """
        a) Encapsulation is a mechanism that restricts direct access to some of the object's components.
           With private keyword, we can restrict access to class members. 
        b) Inheritance is a mechanism that a new class is created from an existing class. 
           For example, Teacher class is created from Human class. 
        """


    def question5(self):
        """
        Creating classes and objects is the main concept of Object Oriented Programming.
        Human, Teacher and Student classes are created in this script.
        """
        human = Human("Ali", 32)
        human.talk()

        teacher = Teacher("Veli", 45, "Computer Science")
        teacher.talk()

        student = Student("Ayse", 22, "Computer Engineering", 171725425)
        student.talk()



    def question6(self):
        """
        Worker class is created in this script. BlueCollarWorker and WhiteCollarWorker classes are created from Worker class. (inheritance)
        CV method is overridden in BlueCollarWorker and WhiteCollarWorker classes. (polymorphism)
        work method is implemented in BlueCollarWorker and WhiteCollarWorker classes. 
        Private variables are used in Worker, BlueCollarWorker and WhiteCollarWorker classes. (encapsulation)

        **Args**:
            None
        """
        blue_collar_worker = BlueCollarWorker("Alice", 35, 5000, 1, "Factory Worker")
        white_collar_worker = WhiteCollarWorker("Bob", 40, 10000, 2, "Software Developer", "Computer Engineering")

        print(blue_collar_worker.CV())
        print(white_collar_worker.CV())

        blue_collar_worker.work()
        white_collar_worker.work()

    



if __name__ == '__main__':
    week5 = Week5()

    # Question 1
    # week5.question1()

    # Question 2
    # week5.question2()

    # Question 3
    # week5.question3()

    # Question 4
    # week5.question4()

    # Question 5
    # week5.question5()

    # Question 6
    week5.question6()