from employee_project import Employee, SalaryEmployee, HourlyEmployee 

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

    employee1 = SalaryEmployee('Eren', 'Yeager', '50000')
    my_company.add_employee(employee1)
    employee2= HourlyEmployee('Gon', 'Freese', '20', '50')
    my_company.add_employee(employee2)
    employee3= HourlyEmployee('Ichigo', 'Kurosaki', '40', '15')
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.pay_employees()

main()

