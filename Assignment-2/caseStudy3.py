def calculate_allowances_deductions(basic_salary):
    hra_percent = 0.30  # 30% of basic
    da_percent = 0.20   # 20% of basic
    pf_percent = 0.12   # 12% of basic

    hra = basic_salary * hra_percent
    da = basic_salary * da_percent
    pf = basic_salary * pf_percent
    
    return hra, da, pf

employee_basic_salary = int(input("Enter Employee Salary: "))

hra_amount, da_amount, pf_amount = calculate_allowances_deductions(employee_basic_salary)

calculate_net_salary = lambda basic, hra, da, pf: basic + hra + da - pf

net_salary = calculate_net_salary(employee_basic_salary, hra_amount, da_amount, pf_amount)

print("--- Employee Salary Slip ---")
print("Basic Salary : ",employee_basic_salary)
print("HRA (30%)    : ",hra_amount)
print("DA (20%)     : ",da_amount)
print("PF (12%)     : ",pf_amount)
print("-" * 28)
print("Net Salary   :  ",net_salary)
print("=" * 28)