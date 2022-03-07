class Person:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

class Employee(Person):
    def __init__(self, first, last, age, wage):
        super().__init__(first, last, age)

class Customer:
    def __init__(self, first, last, order_no):
        self.first = first
        self.last = last
        self.order_no = order_no

    def info(self):
        return f"my name is {self.first}, and my last name is {self.last}"

p_1 = Person('joe', 'Bloggs', 1)
p_2 = Person('Sara', 'Stone', 1)

emp_1 = Employee('elle', 'donland', 23, 100)
print(p_1.first)
print(emp_1.last)

customer1 = Customer('Jade', 'Row', 2344)
print(customer1.first)

print(customer1.info())

