#Function that loads the name, salary of an employee and saves it in a list
def load_employee():
  num_employee = int(input("How many employees would you like upload: "))
  employees = []
  n = 1
  while(num_employee >= n):
    name = input("Insert the name of the employee: ")
    salary = int(input("Insert the salary: "))
    employee = (name,salary)
    employees.append(employee)
    n += 1
  return employees

#Function that checks the employee with the highest salary
def biggest_salary(lst):
  salary = 0
  for n in lst:
    if n[1] > salary:
      salary = n[1]
      nanme = n[0]
  print(f"The employee with the highest salary is: {name}")


biggest_salary(load_employee())
