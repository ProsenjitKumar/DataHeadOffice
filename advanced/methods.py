class Employee:
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    @classmethod
    def another_stuff(cls, full_name):
        cls.full_name = full_name

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workkday(day):
        if day.weekday() == 5 or day.weekday() == 6: # saturday
            return False
        return True


import datetime
my_date = datetime.date(2019, 2, 22)
print(Employee.is_workkday(my_date))
print(my_date.weekday())


# emp_obj = Employee('Prosenjit', 'Das', 26980)
# emp_obj1 = Employee('Samoli', 'Das', 5688)

# emp_obj.another_stuff('Prosenjit Das')
# print(Employee.full_name)
# print(emp_obj.full_name)
# print(emp_obj1.full_name)

# emp_str_1 = 'Prosenjit-Das-85200'
# emp_str_2 = 'Jalil-Khan-56870'
# emp_str_3 = 'Suvo-Roy-87452'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.first_name)
# print(new_emp_1.pay)


