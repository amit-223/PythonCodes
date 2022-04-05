class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def change(self, name, surname):
        self.fname = name
        self.lname = surname

    def display(self):
        print(self.fname + " " + self.lname)


# class Student(Person):
#     pass
class Student(Person):
    def __init__(self, fname, lname):
        # Person.__init__(self, fname, lname) # here Person. is inherit the child class properties
        super().__init__(fname, lname)  # super is inherit the child class properties


o = Person("Ashneer", "Grover")
o1 = Student("Anupam", "Mittal")
o1.display()
o1.change("Vineeta", "singh")
o1.display()
