# instantiation of parent class with attributes
class Person:
    name = "Corey Tran"
    user = "Ctran.prosper@gmail.com"
    password = "8675309"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_user = input("Enter your user: ")
        entry_password = input("Enter your password: ")
        if (entry_user == self.user and entry_password == self.password):
            print("Login complete, {}".format(entry_name))
        else:
            print("The user or password is incorrect.")

# Child class with attributes


class Student(Person):
    course_name = "Python"
    enrollment_weeks = "15 weeks"
    program_code = "1234"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_user = input("Enter your user: ")
        entry_code = input("Enter your code: ")
        if (entry_user == self.user and entry_code == self.program_code):
            print("Login complete, {}".format(entry_name))
        else:
            print("User or code is incorrect")

    instructor = Person()
    instructor.getLoginInfo()

    pupil = Student()
    pupil.getLoginInfo()
