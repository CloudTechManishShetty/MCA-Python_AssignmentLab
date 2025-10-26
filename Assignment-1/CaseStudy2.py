employee_name = input("Enter Employee Name: ");
employee_id = input("Enter Employee ID: ");
basic_salary = float(input("Enter Basic Salary: "));

print("\nCalculating the Allowances i.e. HRA with 0.2 and DA with 0.5 rate....");
HRA = 0.2 * basic_salary;
DA = 0.5 * basic_salary;

print("\nCalculating Total Salary In-Hand...");
salary = basic_salary + HRA + DA;
print("Employee-ID: ",employee_id,"| Mr.",employee_name," Your Estimated Salary after adding all Allowances is: ",salary);

