
from EmployeeClass import Employee
from PayrollDeductionClass import PayrollDeduction

emp = Employee('Jimmy Smith', 58475, 'Information Systems', 'Developer', 6800)
d1 = PayrollDeduction('food court', '8/14/2022', 22.50, 39119)
d2 = PayrollDeduction('gift contribution', '8/12/2022', 25.00, 58475)
d3 = PayrollDeduction('food court', '8/17/2022', 15.25, 21547)
d4 = PayrollDeduction('vending machine', '8/22/2022', 3.00, 58475)
d5 = PayrollDeduction('vending machine', '8/5/2022', 2.75, 58475)

print('*** Employee Pay ***')
print('Name: ', emp.getname())
print('ID Number: ', emp.getID())
print('Department: ', emp.getdept())
print('Gross Pay: $', emp.getsalary(), sep = '')
print('Net Pay: $', emp.getsalary() - d2.getamt() - d4.getamt() - d5.getamt(), sep = '')