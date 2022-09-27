def count(n):
    currentYear = 2022
    counter = 0
    for i in range(n):
        studentYear = int(input('Escribe las edades de los estudiantes'))
        currentAgeStudent = currentYear - studentYear
        if(currentAgeStudent >= 18):
            counter += 1
    return counter

counterStudent = int(input('¿Cuantos estudiantes son?'))

print(count(counterStudent))    
