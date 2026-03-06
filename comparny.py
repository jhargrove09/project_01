from employee import Employee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current Employee:')
        for i in self.employees:
            print(i.fname,i.lname)
        print('_________________________')

    def pay_employees(self):
        print('Paying Employees:')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print('Amount:', i.calculate_paycheck())
            print('_________________________')


def main():
    my_company = Company()

    employee1 = Employee('Eren', 'Yeager', '50000')
    my_company.add_employee(employee1)
    employee2= Employee('Gon', 'Freese', '60000')
    my_company.add_employee(employee2)
    employee3= Employee('Ichigo', 'Kurosaki', '70000')
    my_company.add_employee(employee3)

    my_company.display_employees()

main()

