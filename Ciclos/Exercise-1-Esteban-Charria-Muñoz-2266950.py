def salarySum(salary, extraHours):
    sumSalary = (salary + extraHours)
    percentage = sumSalary * .10
    totalResult = sumSalary - percentage
    return totalResult

sumTotalSalary = 0
companyName = input('¿Cual es el nombre de la empresa: ?')
numberEmployees = int(input('¿Cuantos de empleados son: ?'))

for i in range(numberEmployees):
    extraHours = 0
    salary = int(input('Digite los salarios: ')) 
    sumTotalSalary += salarySum(salary)

percentageTotalSalary = sumTotalSalary / numberEmployees

mensaje = 'el promedio del salario es ' + percentageTotalSalary + 'y el nombre de la empresa es ' + companyName


