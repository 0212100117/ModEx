class Employee:

    def __init__(self, first_name, last_name, email_add, salary):
        self.first = first_name
        self.last = last_name
        self.email = email_add
        self.salary = salary

    def describe_employee(self):
        print(" First Name    : ", self.first, "\n",
              "Last Name     : ", self.last, "\n",
              "Email Address : ", self.email, "\n",
              "Salary        : ", self.salary, "\n")

    def greet_employee(self):
        print(" Good Evening", self.first, "\n")


emp1 = Employee("Neb", "Balina", "neb@gmail.com", 100000)

emp2 = Employee("Norman", "Acain", "norman@gmail.com", 100000)

emp3 = Employee("Jayson", "Trinidad", "jayson@gmail.com", 100000)

emp1.describe_employee()
emp1.greet_employee()
emp2.describe_employee()
emp2.greet_employee()
emp3.describe_employee()
emp3.greet_employee()
