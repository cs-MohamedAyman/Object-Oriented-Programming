class BasedClass:
    pass

class DerivedClass(BasedClass):
    pass


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'name: ' + self.name + '\n' + \
               'age: ' + str(self.age) + '\n'

class Employee(Human):
    def __init__(self, name, age, salary, department):
        Human.__init__(self, name, age)
        self.salary = salary
        self.department = department
    def __str__(self):
        return Human.__str__(self) + \
               'salary: ' + str(self.salary) + '\n' + \
               'department' + self.department + '\n'

x = Human('Jack', 24)
print(x)

y = Employee('Robert', 26, 4000, 'IT')
print(y)


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'name: ' + self.name + '\n' + \
               'age: ' + str(self.age) + '\n'

class Employee(Human):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age)
        self.salary = salary
        self.department = department
    def __str__(self):
        return super().__str__() + \
               'salary: ' + str(self.salary) + '\n' + \
               'department' + self.department + '\n'

x = Human('Jack', 24)
print(x)

y = Employee('Robert', 26, 4000, 'IT')
print(y)


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'name: ' + self.name + '\n' + \
               'age: ' + str(self.age) + '\n'

class Employee(Human):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age)
        self.salary = salary
        self.department = department
    def __str__(self):
        return super().__str__() + \
               'salary: ' + str(self.salary) + '\n' + \
               'department' + self.department + '\n'

x = Employee('Robert', 26, 4000, 'IT')
print(x.name, x.age, x.salary, x.department)


class Human:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    def __str__(self):
        return 'name: ' + self.name + '\n' + \
               'age: ' + str(self.age) + '\n'

class Employee(Human):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age)
        self.salary = salary
        self.department = department
    def __str__(self):
        return super().__str__() + \
               'salary: ' + str(self.salary) + '\n' + \
               'department' + self.department + '\n'

x = Employee('Robert', 26, 4000, 'IT')
print(x._name, x._age, x.salary, x.department)


class Human:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def __str__(self):
        return 'name: ' + self.name + '\n' + \
               'age: ' + str(self.age) + '\n'

class Employee(Human):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age)
        self.salary = salary
        self.department = department
    def __str__(self):
        return super().__str__() + \
               'salary: ' + str(self.salary) + '\n' + \
               'department' + self.department + '\n'

x = Employee('Robert', 26, 4000, 'IT')
print(x.__name, x.__age, x.salary, x.department)


class Parent:
    def __init__(self, name):
        self.parent_name = name
    def __str__(self):
        return 'name: ' + self.name + '\n'

class Child(Parent):
    def __init__(self, first_name, last_name):
        super().__init__(last_name)
        self.child_name = first_name
    def __str__(self):
        return self.child_name + ' ' + self.parent_name

x = Child('Mark', 'Bill')
print(x.get_name())


class Parent:
    def __init__(self, name):
        self.parent_name = name
    def __str__(self):
        return 'name: ' + self.name + '\n'

class Child(Parent):
    def __init__(self, first_name, last_name):
        super().__init__(last_name)
        self.child_name = first_name
    def __str__(self):
        return self.child_name + ' ' + self.parent_name

x = Child('Mark', 'Bill')
print(x.get_name())


class Human:
    def __init__(self, name):
        self.name = name
    def greeting(self):
        return 'Hi my name is ' + self.name + '\n'

class Employee(Human):
    def __init__(self, name, salary):
        super().__init__(name)
        self.child_name = first_name


x = Employee('Mark', 10000)
print(x.greeting())


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'name: ' + self.name + '\n' + \
               'age: ' + str(self.age) + '\n'

class Employee(Human):
    def __init__(self, name, age, salary, department):
        Human.__init__(self, name, age)
        self.salary = salary
        self.department = department
    def __str__(self):
        return Human.__str__(self) + \
               'salary: ' + str(self.salary) + '\n' + \
               'department' + self.department + '\n'

class Father:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'name: ' + self.name + '\n'

class Mother:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'name: ' + self.name + '\n'

class Child(Father, Mother):
    def __init__(self, father_name, mother_name, name):
        Father.__init__(self, father_name)
        Mother.__init__(self, mother_name)
        self.name = name
    def __str__(self):
        return Father.__str__(self) + \
               Mother.__str__(self) + \
               'name: ' + self.name + '\n'

x = Child('bill', 'jsica', 'adam')
print(x)


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return 'name: ' + self.name + '\n' + \
               'age: ' + str(self.age) + '\n'

class Employee(Human):
    def __init__(self, name, age, salary, department):
        Human.__init__(self, name, age)
        self.salary = salary
        self.department = department
    def __str__(self):
        return Human.__str__(self) + \
               'salary: ' + str(self.salary) + '\n' + \
               'department' + self.department + '\n'

class Leader(Employee):
    def __init__(self, name, age, salary, department, reports):
        Human.__init__(self, name, age)
        Employee.__init__(self, salary, department)
        self.reports = reports
    def __str__(self):
        return Human.__str__(self) + \
               Employee.__str__(self) + \
               'reports: ' + str(self.reports) + '\n' 

x = Leader('Manuel', 28, 20000, 'Research', ['R1', 'R2', 'R3'])
print(x)


class Human:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'name: ' + self.name + '\n'

class Father:
    def __init__(self, name, salary):
        Human.__init__(self, name)
        self.salary = salary
    def __str__(self):
        return Human.__str__(self) + \
               'salary: ' + str(self.salary) + '\n'

class Mother:
    def __init__(self, name, salary):
        Human.__init__(self, name)
        self.salary = salary
    def __str__(self):
        return Human.__str__(self) + \
               'salary: ' + str(self.salary) + '\n'

class Child(Father, Mother):
    def __init__(self, father_name, father_salary, mother_name, mother_salary, name):
        Father.__init__(self, father_name, father_salary)
        Mother.__init__(self, mother_name, mother_salary)
        self.name = name
    def __str__(self):
        return Father.__str__(self) + \
               Mother.__str__(self) + \
               'name: ' + self.name + '\n'

x = Child('bill', 'jsica', 'adam')
print(x)
