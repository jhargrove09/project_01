from employee import Employee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

def main():
    my_company = Company()

    employee1 = Employee1('Eren', 'Yeager', '50000')
    my_company.add_employee(employee1)
    employee2= Employee2('Gon', 'Freese', '60000')
    my_company.add_employee(employee2)
    employee3= Employee3('Ichigo', 'Kurosaki', '70000')
    my_company.add_employee(employee3)

    print(my_company.employees)
