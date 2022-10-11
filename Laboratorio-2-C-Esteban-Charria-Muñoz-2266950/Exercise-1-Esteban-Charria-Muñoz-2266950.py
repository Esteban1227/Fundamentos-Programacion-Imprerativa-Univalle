# Enunciado

# Se requiere crear un aplicativo que permita calcular el promedio de un curso, el cual tiene un
# número determinado de estudiantes, el curso solo tiene una asignatura, la nota definitiva de la
# asignatura se calcula de la siguiente manera: Examen1 40%, Examen2 30% y una tarea del
# 30%. El programa de tener en cuenta la captura de los datos para calcular el promedio del
# curso. Como resultado debe mostrar el nombre de la asignatura y su promedio.

# Programadores Novatos

#Funcion #1: courseSum

# Definición de datos:
# test1: valor numerico decimal que contiene la nota del examen 1 del estudiante (este es variado)
# test2: valor numerico decimal que contiene la nota del examen 2 del estudiante (este es variado)
# homework: valor numerico decimal que contiene la nota de la tarea del estudiante (este es variado)
# sumTotalNote: valor decimal que contiene la suma total de las notas del curso de la asignatura especificada

# Firma y propósito:
# Firma (entradas y salidas):
    # Entrada: test1, test2, homework
    # Salida: sumTotalNote
# Propósito: Definir el porcentaje respectivo de cada nota y la suma de todas las notas

# Ejemplos funcionales, pruebas con diferentes notas:
# si la nota del examen 1 es 5.0,la nota del examen 2 es 5.0, la nota de la tarea es 5.0 la suma total de las notas seria 5.0
# si la nota del examen 1 es 4.0,la nota del examen 2 es 4.5, la nota de la tarea es 4.0 la suma total de las notas seria 4.2
# si la nota del examen 1 es 3.5,la nota del examen 2 es 3.0, la nota de la tarea es 3.2 la suma total de las notas seria 3.3
# si la nota del examen 1 es 2.2,la nota del examen 2 es 2.0, la nota de la tarea es 2.9 la suma total de las notas seria 2.4
# si la nota del examen 1 es 1.0,la nota del examen 2 es 1.0, la nota de la tarea es 1.0 la suma total de las notas seria 1.0

# Código del programa:

def courseSum(test1, test2, homework):
    sumTotalNote = (test1 * .40) + (test2 * .30) + (homework * .30)
    sumTotalNote = round(sumTotalNote, 1)
    return sumTotalNote

# Probar el programa:
#Prueba #1 Si el valor de test1 es 5.0, el valor de test2 es 5.0 y el valor de homework es 5.0 el valor de sumaTotalNote seria 5.0
    # test1 = 5.0
    # test2 = 5.0
    # homework = 5.0
    # sumTotalNote = 5.0
#Prueba #2 Si el valor de test1 es 4.0, el valor de test2 es 4.5 y el valor de homework es 4.0 el valor de sumaTotalNote seria 4.2
    # test1 = 4.0
    # test2 = 4.5
    # homework = 4.0
    # sumTotalNote = 4.2
#Prueba #3 Si el valor de test1 es 3.5, el valor de test2 es 3.0 y el valor de homework es 3.2 el valor de sumaTotalNote seria 3.3
    # test1 = 3.5
    # test2 = 3.0
    # homework = 3.2
    # sumTotalNote = 3.3
#Prueba #4 Si el valor de test1 es 2.2, el valor de test2 es 2.0 y el valor de homework es 2.9 el valor de sumaTotalNote seria 2.4
    # test1 = 2.2
    # test2 = 2.0
    # homework = 2.9
    # sumTotalNote = 2.4
#Prueba #5 Si el valor de test1 es 1.0, el valor de test2 es 1.0 y el valor de homework es 1.0 el valor de sumaTotalNote seria 1.0
    # test1 = 1.0
    # test2 = 1.0
    # homework = 1.0
    # sumTotalNote = 1.0

#Funcion #2: courseAverage

# Definición de datos:
# numberStudents: valor numerico entero que contiene la cantidad de estudiantes que hay en el curso (este es variado)
# sumTotal: valor decimal que contiene la suma total de las notas del curso de la asignatura especificada
# percentageTotal: valor decimal que contiene el promedio total de las notas del curso de la asignatura especificada

# Firma y propósito:
# Firma (entradas y salidas):
    # Entrada: sumTotal, numberStudents
    # Salida: percentageTotal
# Propósito: Definir el promedio de la suma total de todas las notas

# Ejemplos funcionales, pruebas con diferentes notas y diferentes cantidades de estudiantes
# Si la suma total de las notas es 5.0 y es un solo estudiante el porcentaje total es 5.0
# Si la suma total de las notas es 10.0 y son 2 estudiantes el porcentaje total es 5.0
# Si la suma total de las notas es 12.6 y son 3 estudiantes el porcentaje total es 4.2
# Si la suma total de las notas es 13.2 y son 4 estudiantes el porcentaje total es 3.3
# Si la suma total de las notas es 12.0 y son 5 estudiantes el porcentaje total es 2.4
# Si la suma total de las notas es 6.0 y son 6 estudiantes el porcentaje total es 1.0

# Código del programa:

def courseAverage(sumTotal, numberStudents):
    percentageTotal = sumTotal / numberStudents
    return percentageTotal

# Probar el programa:
#Prueba #1 Si el valor de sumTotal es 5.0 y el valor de numberStudent es 1 el valor de percentageTotal seria 5.0
    # sumTotal = 5.0
    # numberStudent = 1
    # percentageTotal = 5.0
#Prueba #2 Si el valor de sumTotal es 10.0 y el valor de numberStudent es 2 el valor de percentageTotal seria 5.0
    # sumTotal = 10.0
    # numberStudent = 2
    # percentageTotal = 5.0
#Prueba #3 Si el valor de sumTotal es 12.6 y el valor de numberStudent es 3 el valor de percentageTotal seria 4.2
    # sumTotal = 12.6
    # numberStudent = 3
    # percentageTotal = 4.2
#Prueba #4 Si el valor de sumTotal es 13.2 y el valor de numberStudent es 4 el valor de percentageTotal seria 3.3
    # sumTotal = 13.2
    # numberStudent = 4
    # percentageTotal = 3.3
#Prueba #5 Si el valor de sumTotal es 12.0 y el valor de numberStudent es 5 el valor de percentageTotal seria 2.4
    # sumTotal = 12.0
    # numberStudent = 5
    # percentageTotal = 2.4
#Prueba #6 Si el valor de sumTotal es 6.0 y el valor de numberStudent es 6 el valor de percentageTotal seria 1.0
    # sumTotal = 6.0
    # numberStudent = 6
    # percentageTotal = 1.0

#Funcion #3: run

# Definición de datos:
# asignatureName: valor numerico entero que contiene la cantidad de estudiantes que hay en el curso (este es variado)
# numberStudents: valor numerico entero que contiene la cantidad de estudiantes que hay en el curso (este es variado)
# test1: valor numerico decimal que contiene la nota del examen 1 del estudiante (este es variado)
# test2: valor numerico decimal que contiene la nota del examen 2 del estudiante (este es variado)
# homework: valor numerico decimal que contiene la nota de la tarea del estudiante (este es variado)
# sumTotal: valor decimal que contiene la suma total de las notas del curso de la asignatura especificada
# percentageTotal: valor decimal que contiene el promedio total de las notas del curso de la asignatura especificada
# messageResult: cadena alfanumerica que contiene este mensaje 'El promedio de los estudiantes del curso en la asignatura ' + asignatureName + ' es de: ' + percentageTotal
# i : valor numerico entero que itera en el ciclo for

# Firma y propósito:
# Firma (entradas y salidas):
    # Entrada: asignatureName, numberStudents, test1, test2, homework, asignatureName
    # Salida: messageResult
# Propósito: Definir los valores bases para poder sacar el promedio de todas las notas de los estudiantes determinados

# Ejemplos funcionales, pruebas con diferentes notas, diferentes cantidades de alumnos, diferentes nombres de asignaturas:
#1
# Si el nombre de la asignatura es matematica y la cantidad de estudiantes es 1 y las notas son: 
    # Estudiante 1
        # examen 1 es 5.0,la nota del examen 2 es 5.0, la nota de la tarea es 5.0 
    # la suma total de las notas seria 5.0, el porcentaje total seria 5.0 y el mesaje final seria 'El promedio de los estudiantes del curso en la asignatura matematica es de 5.0'
#2
# Si el nombre de la asignatura es quimica y la cantidad de estudiantes es 2 y las notas son:
    # Estudiante 1 
        # examen 1 es 5.0,la nota del examen 2 es 5.0, la nota de la tarea es 5.0 
    # Estudiante 2 
        # examen 1 es 5.0,la nota del examen 2 es 5.0, la nota de la tarea es 5.0 
    # la suma total de las notas seria 10.0, el porcentaje total seria 5.0 y el mesaje final seria 'El promedio de los estudiantes del curso en la asignatura quimica es de 5.0'
#3
# Si el nombre de la asignatura es fisica y la cantidad de estudiantes es 3 y las notas son:
    # Estudiante 1 
        # examen 1 es 4.0,la nota del examen 2 es 4.0, la nota de la tarea es 4.5 
    # Estudiante 2 
        # examen 1 es 4.0,la nota del examen 2 es 4.5, la nota de la tarea es 4.0 
    # Estudiante 3 
        # examen 1 es 4.0,la nota del examen 2 es 4.0, la nota de la tarea es 4.5 
    # la suma total de las notas seria 12.6, el porcentaje total seria 4.2 y el mesaje final seria 'El promedio de los estudiantes del curso en la asignatura fisica es de 4.2'
#4
# Si el nombre de la asignatura es arte y la cantidad de estudiantes es 4 y las notas son:
    # Estudiante 1 
        # examen 1 es 3.5,la nota del examen 2 es 3.2, la nota de la tarea es 3.0
    # Estudiante 2 
        # examen 1 es 3.5,la nota del examen 2 es 3.0, la nota de la tarea es 3.2 
    # Estudiante 3 
        # examen 1 es 3.5,la nota del examen 2 es 3.0, la nota de la tarea es 3.2 
    # Estudiante 4
        # examen 1 es 3.5,la nota del examen 2 es 3.2, la nota de la tarea es 3.0 
    # la suma total de las notas seria 13.2, el porcentaje total seria 3.3 y el mesaje final seria 'El promedio de los estudiantes del curso en la asignatura arte es de 3.3'
#5
# Si el nombre de la asignatura es tecnologia y la cantidad de estudiantes es 5 y las notas son:
    # Estudiante 1 
        # examen 1 es 2.2,la nota del examen 2 es 2.9, la nota de la tarea es 2.0
    # Estudiante 2 
        # examen 1 es 2.2,la nota del examen 2 es 2.0, la nota de la tarea es 2.9 
    # Estudiante 3 
        # examen 1 es 2.2,la nota del examen 2 es 2.9, la nota de la tarea es 2.0 
    # Estudiante 4
        # examen 1 es 2.2,la nota del examen 2 es 2.0, la nota de la tarea es 2.9 
    # Estudiante 5
        # examen 1 es 2.2,la nota del examen 2 es 2.9, la nota de la tarea es 2.0
    # la suma total de las notas seria 12.0, el porcentaje total seria 2.4 y el mesaje final seria 'El promedio de los estudiantes del curso en la asignatura tecnologia es de 2.4'
#6
# Si el nombre de la asignatura es Religion y la cantidad de estudiantes es 6 y las notas son:
    # Estudiante 1 
        # examen 1 es 1.0,la nota del examen 2 es 1.0, la nota de la tarea es 1.0
    # Estudiante 2 
        # examen 1 es 1.0,la nota del examen 2 es 1.0, la nota de la tarea es 1.0 
    # Estudiante 3 
        # examen 1 es 1.0,la nota del examen 2 es 1.0, la nota de la tarea es 1.0 
    # Estudiante 4
        # examen 1 es 1.0,la nota del examen 2 es 1.0, la nota de la tarea es 1.0 
    # Estudiante 5
        # examen 1 es 1.0,la nota del examen 2 es 1.0, la nota de la tarea es 1.0
    # Estudiante 6
        # examen 1 es 1.0,la nota del examen 2 es 1.0, la nota de la tarea es 1.0
    # la suma total de las notas seria 6.0, el porcentaje total seria 1.0 y el mesaje final seria 'El promedio de los estudiantes del curso en la asignatura Religion es de 1.0'

# Código del programa:

def run():
    asignatureName = input('Digite el nombre de la asignatura: ')
    numberStudents = int(input('Digite el numero de estudiantes del curso: '))
    sumTotal = 0
    for i in range(numberStudents):
        print('Estudiante ' + str(i+1))
        test1 = float(input('Digite la nota de su primer Examen: '))
        test2 = float(input('Digite la nota de su segundo Examen: '))
        homework = float(input('Digite la nota de tarea: '))
        sumTotal += courseSum(test1, test2, homework)
    percentageTotal = courseAverage(sumTotal, numberStudents)
    messageResult = 'El promedio de los estudiantes del curso en la asignatura ' + asignatureName + ' es de: ' + str(round(percentageTotal, 1))
    return messageResult

print(run())

# Probar el programa:
#Prueba #1 Si el valor de asignatureName es matematica, el valor de numberStudents es 1, el valor de 
    #Estudiante 1
        # test1 es 5.0, el valor de test2 es 5.0 y el valor de homework es 5.0, 
    # la sumTotal seria 5.0, el percentageTotal seria 5.0 y el messageResult seria 'El promedio de los estudiantes del curso en la asignatura matematica es de 5.0'
    # asignatureName = matematica
    # numberStudents = 1
    # test1 = 5.0
    # test2 = 5.0
    # homework = 5.0
    # sumTotal = 5.0
    # percentageTotal = 5.0
    # messageResult = 'El promedio de los estudiantes del curso en la asignatura matematica es de 5.0'

#Prueba #2 Si el valor de asignatureName es quimica, el valor de numberStudents es 2, el valor de 
    #Estudiante 1
        # test1 es 5.0, el valor de test2 es 5.0 y el valor de homework es 5.0, 
    #Estudiante 2
        # test1 es 5.0, el valor de test2 es 5.0 y el valor de homework es 5.0, 
    # la sumTotal seria 10.0, el percentageTotal seria 5.0 y el messageResult seria 'El promedio de los estudiantes del curso en la asignatura quimica es de 5.0'
    # asignatureName = quimica
    # numberStudents = 2
    #Estudiante 1
        # test1 = 5.0
        # test2 = 5.0
        # homework = 5.0
    #Estudiante 2
        # test1 = 5.0
        # test2 = 5.0
        # homework = 5.0
    # sumTotal = 10.0
    # percentageTotal = 5.0
    # messageResult = 'El promedio de los estudiantes del curso en la asignatura quimica es de 5.0'

#Prueba #3 Si el valor de asignatureName es fisica, el valor de numberStudents es 3, el valor de 
    #Estudiante 1
        # test1 es 4.0, el valor de test2 es 4.5 y el valor de homework es 4.0, 
    #Estudiante 2
        # test1 es 4.0, el valor de test2 es 4.0 y el valor de homework es 4.5, 
    #Estudiante 3
        # test1 es 4.0, el valor de test2 es 4.5 y el valor de homework es 4.0, 
    # la sumTotal seria 12.6, el percentageTotal seria 4.2 y el messageResult seria 'El promedio de los estudiantes del curso en la asignatura fisica es de 4.2'
    # asignatureName = fisica
    # numberStudents = 3
    #Estudiante 1
        # test1 = 4.0
        # test2 = 4.5
        # homework = 4.0
    #Estudiante 2
        # test1 = 4.0
        # test2 = 4.0
        # homework = 4.5
    #Estudiante 3
        # test1 = 4.0
        # test2 = 4.5
        # homework = 4.0
    # sumTotal = 12.6
    # percentageTotal = 4.2
    # messageResult = 'El promedio de los estudiantes del curso en la asignatura fisica es de 4.2'

#Prueba #4 Si el valor de asignatureName es arte, el valor de numberStudents es 4, el valor de 
    #Estudiante 1
        # test1 es 3.5, el valor de test2 es 3.2 y el valor de homework es 3.0, 
    #Estudiante 2
        # test1 es 3.5, el valor de test2 es 3.0 y el valor de homework es 3.2, 
    #Estudiante 3
        # test1 es 3.5, el valor de test2 es 3.2 y el valor de homework es 3.0, 
    #Estudiante 4
        # test1 es 3.5, el valor de test2 es 3.2 y el valor de homework es 3.0, 
    # la sumTotal seria 13.2, el percentageTotal seria 3.3 y el messageResult seria 'El promedio de los estudiantes del curso en la asignatura arte es de 3.3'
    # asignatureName = arte
    # numberStudents = 4
    #Estudiante 1
        # test1 = 3.5
        # test2 = 3.2
        # homework = 3.0
    #Estudiante 2
        # test1 = 3.5
        # test2 = 3.0
        # homework = 3.2
    #Estudiante 3
        # test1 = 3.5
        # test2 = 3.2
        # homework = 3.0
    #Estudiante 4
        # test1 = 3.5
        # test2 = 3.2
        # homework = 3.0
    # sumTotal = 13.2
    # percentageTotal = 3.3
    # messageResult = 'El promedio de los estudiantes del curso en la asignatura arte es de 3.3'

#Prueba #5 Si el valor de asignatureName es tecnologia, el valor de numberStudents es 5, el valor de 
    #Estudiante 1
        # test1 es 2.2, el valor de test2 es 2.9 y el valor de homework es 2.0, 
    #Estudiante 2
        # test1 es 2.2, el valor de test2 es 2.0 y el valor de homework es 2.9, 
    #Estudiante 3
        # test1 es 2.2, el valor de test2 es 2.9 y el valor de homework es 2.0, 
    #Estudiante 4
        # test1 es 2.2, el valor de test2 es 2.0 y el valor de homework es 2.9, 
    #Estudiante 5
        # test1 es 2.2, el valor de test2 es 2.9 y el valor de homework es 2.0, 
    # la sumTotal seria 12.0, el percentageTotal seria 2.4 y el messageResult seria 'El promedio de los estudiantes del curso en la asignatura tecnologia es de 2.4'
    # asignatureName = tecnologia
    # numberStudents = 5
    #Estudiante 1
        # test1 = 2.2
        # test2 = 2.9
        # homework = 2.0
    #Estudiante 2
        # test1 = 2.2
        # test2 = 2.0
        # homework = 2.9
    #Estudiante 3
        # test1 = 2.2
        # test2 = 2.9
        # homework = 2.0
    #Estudiante 4
        # test1 = 2.2
        # test2 = 2.0
        # homework = 2.9
    #Estudiante 5
        # test1 = 2.2
        # test2 = 2.9
        # homework = 2.0
    # sumTotal = 12.0
    # percentageTotal = 2.4
    # messageResult = 'El promedio de los estudiantes del curso en la asignatura tecnologia es de 2.4'

#Prueba #5 Si el valor de asignatureName es religion, el valor de numberStudents es 6, el valor de 
    #Estudiante 1
        # test1 es 1.0, el valor de test2 es 1.0 y el valor de homework es 1.0, 
    #Estudiante 2
        # test1 es 1.0, el valor de test2 es 1.0 y el valor de homework es 1.0, 
    #Estudiante 3
        # test1 es 1.0, el valor de test2 es 1.0 y el valor de homework es 1.0, 
    #Estudiante 4
        # test1 es 1.0, el valor de test2 es 1.0 y el valor de homework es 1.0, 
    #Estudiante 5
        # test1 es 1.0, el valor de test2 es 1.0 y el valor de homework es 1.0, 
    #Estudiante 6
        # test1 es 1.0, el valor de test2 es 1.0 y el valor de homework es 1.0, 
    # la sumTotal seria 6.0, el percentageTotal seria 1.0 y el messageResult seria 'El promedio de los estudiantes del curso en la asignatura religion es de 1.0'
    # asignatureName = religion
    # numberStudents = 6
    #Estudiante 1
        # test1 = 1.0
        # test2 = 1.0
        # homework = 1.0
    #Estudiante 2
        # test1 = 1.0
        # test2 = 1.0
        # homework = 1.0
    #Estudiante 3
        # test1 = 1.0
        # test2 = 1.0
        # homework = 1.0
    #Estudiante 4
        # test1 = 1.0
        # test2 = 1.0
        # homework = 1.0
    #Estudiante 5
        # test1 = 1.0
        # test2 = 1.0
        # homework = 1.0
    #Estudiante 6
        # test1 = 1.0
        # test2 = 1.0
        # homework = 1.0
    # sumTotal = 6.0
    # percentageTotal = 1.0
    # messageResult = 'El promedio de los estudiantes del curso en la asignatura religion es de 1.0'