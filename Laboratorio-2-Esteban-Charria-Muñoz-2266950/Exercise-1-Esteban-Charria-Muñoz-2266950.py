# Enunciado

# Se requiere crear un aplicativo que permita calcular el promedio de tasa metabólica basal de 
# un grupo de estudiantes de un curso determinado, el cual tiene un número determinado de 
# estudiantes. El programa de tener en cuenta la captura de los datos y como resultado debe 
# mostrar el nombre de la asignatura y su promedio. Como referencia, use el siguiente link.

# Programadores Novatos

#Funcion #1: calculateTMB

# Definición de datos:
# gender: valor numerico entero que contiene el identificador si es hombre o mujer (este es variado)
# height: valor numerico decimal que contiene la altura del estudiante (este es variado)
# weight: valor numerico decimal que contiene el peso del estudiante (este es variado)
# age: valor enetero que contiene la edad del estudiante (este es variado)
# TMB: valor decimal que contiene el TMB del estudiante (este es variado)

# Firma y propósito:
# Firma (entradas y salidas):
    # Entrada: gender, height, weight, age
    # Salida: TMB
# Propósito: Calcular el TMB de los estudiantes de un curso en una asignatura

# Ejemplos funcionales, pruebas con diferentes generos, alturas, pesos y años:
# si el estudiante es hombre(gender=1), su altura es de 170cm(height=170), su peso es de 70kg(weight=70) y tiene 17 años(age=17) su TMB seria 1682.5
# si el estudiante es mujer(gender=2), su altura es de 170cm(height=170), su peso es de 70kg(weight=70) y tiene 17 años(age=17) su TMB seria 1516.5
# si el estudiante es hombre(gender=1), su altura es de 150cm(height=150), su peso es de 55kg(weight=55) y tiene 21 años(age=21) su TMB seria 1387.5
# si el estudiante es mujer(gender=2), su altura es de 150cm(height=150), su peso es de 55kg(weight=55) y tiene 21 años(age=21) su TMB seria 1221.5
# si el estudiante es hombre(gender=1), su altura es de 200cm(height=200), su peso es de 60kg(weight=70) y tiene 15 años(age=15) su TMB seria 1780.0
# si el estudiante es mujer(gender=2), su altura es de 200cm(height=200), su peso es de 60kg(weight=70) y tiene 15 años(age=15) su TMB seria 1614.0

# Código del programa:

def calculateTMB(gender, weight, height, age):
    TMB = 0
    if(gender == 1):
        TMB = (10 * weight) + (6.25 * height) - (5 * age) +  5
    else:
        TMB = (10 * weight) + (6.25 * height) - (5 * age) - 161
    return TMB

# Probar el programa:
#Prueba #1 Si el valor de gender = 1, el valor de height = 170, el valor de wight = 70, y el valor de age = 17 el valor de TMB es 1682.5
#Prueba #2 Si el valor de gender = 2, el valor de height = 170, el valor de wight = 70, y el valor de age = 17 el valor de TMB es 1516.5
#Prueba #3 Si el valor de gender = 1, el valor de height = 150, el valor de wight = 55, y el valor de age = 21 el valor de TMB es 1387.5
#Prueba #4 Si el valor de gender = 2, el valor de height = 150, el valor de wight = 55, y el valor de age = 21 el valor de TMB es 1221.5
#Prueba #5 Si el valor de gender = 1, el valor de height = 200, el valor de wight = 60, y el valor de age = 15 el valor de TMB es 1780.0
#Prueba #6 Si el valor de gender = 2, el valor de height = 200, el valor de wight = 60, y el valor de age = 15 el valor de TMB es 1614.0


#Funcion #2: courseAverageTMB

# Definición de datos:
# numberStudents: valor numerico entero que contiene la cantidad de estudiantes que hay en el curso (este es variado)
# accumulatorTMB: valor decimal que contiene la acumulacion de todos los TMB de los estudiantes
# totalAverage: valor decimal que contiene el promedio de totalTMB

# Firma y propósito:
# Firma (entradas y salidas):
    # Entrada: accumulatorTMB, numberStudents
    # Salida: totalAverage
# Propósito: Calcular del promedio TMB de todos los estudiantes de un curso en una asignatura

# Ejemplos funcionales, pruebas con diferentes valores para accumulatorTMB, numberStudents
# Si el acumulado total es 1682.5(accumulatorTMB=1682.5) y la cantidad de estudiantes es 1(numberStudents = 1) el promedio total seria 1682.5(totalAverage=1682.5)
# Si el acumulado total es 3199(accumulatorTMB=3199) y la cantidad de estudiantes es 2(numberStudents = 2) el promedio total seria 1682.5(totalAverage=1599,5)
    # 1682.5 + 1516.5 = 3199 
# Si el acumulado total es 4586,5(accumulatorTMB=4586,5) y la cantidad de estudiantes es 3(numberStudents = 3) el promedio total seria 1682.5(totalAverage=2293,25)
    # 1682.5 + 1516.5 + 1387.5 = 4586,5 
# Si el acumulado total es 5808(accumulatorTMB=5808) y la cantidad de estudiantes es 4(numberStudents = 4) el promedio total seria 1682.5(totalAverage=1452)
    # 1682.5 + 1516.5 + 1387.5 + 1221.5 = 5808 
# Si el acumulado total es 7588(accumulatorTMB=7588) y la cantidad de estudiantes es 5(numberStudents = 5) el promedio total seria 1682.5(totalAverage=1517,6)
    # 1682.5 + 1516.5 + 1387.5 + 1221.5 + 1780.0 = 7588 
# Si el acumulado total es 9202(accumulatorTMB=9202) y la cantidad de estudiantes es 6(numberStudents = 6) el promedio total seria 1682.5(totalAverage=1533,6)
    # 1682.5 + 1516.5 + 1387.5 + 1221.5 + 1780.0 + 1614.0 = 9202

# Código del programa:

def courseAverageTMB(accumulatorTMB, numberStudents):
    totalAverage = accumulatorTMB / numberStudents
    return totalAverage

# Probar el programa:
#Prueba #1 Si el valor de accumulatorTMB = 1682.5 y numberStudents = 1 el prometio total es totalAverage = 1682.5
#Prueba #2 Si el valor de accumulatorTMB = 3199 y numberStudents = 2 el prometio total es totalAverage = 1599,5
    # 1682.5 + 1516.5 = 3199 
#Prueba #3 Si el valor de accumulatorTMB = 4586,5 y numberStudents = 3 el prometio total es totalAverage = 2293,25
    # 1682.5 + 1516.5 + 1387.5 = 4586,5 
#Prueba #4 Si el valor de accumulatorTMB = 5808 y numberStudents = 4 el prometio total es totalAverage = 1452
    # 1682.5 + 1516.5 + 1387.5 + 1221.5 = 5808 
#Prueba #5 Si el valor de accumulatorTMB = 7588 y numberStudents = 5 el prometio total es totalAverage = 1517,6
    # 1682.5 + 1516.5 + 1387.5 + 1221.5 + 1780.0 = 7588 
#Prueba #6 Si el valor de accumulatorTMB = 9202 y numberStudents = 6 el prometio total es totalAverage = 1533,6
    # 1682.5 + 1516.5 + 1387.5 + 1221.5 + 1780.0 + 1614.0 = 9202

#Funcion #3: run

# Definición de datos:
# numberStudents: valor numerico entero que contiene la cantidad de estudiantes que hay en el curso (este es variado)
# asignatureName: Cadena de texto que contiene el nombre de la asignatura(este es variado)
# accumulatorTMB: valor decimal que contiene el acumulado de todos los TMB de los estudiantes
# studentGender: valor numerico entero que contiene el identificador si es hombre o mujer (este es variado)
# studentHeight: valor numerico decimal que contiene la altura del estudiante (este es variado)
# studentWeight: valor numerico decimal que contiene el peso del estudiante (este es variado)
# studentAge: valor enetero que contiene la edad del estudiante (este es variado)
# percentageTMBTotal: valor decimal que contiene el promedio total del acumulado de todos los TMB de los estudiantes
# messageResult: cadena alfanumerica que contiene este mensaje 'El promedio de tasa metabólica basal(TMB) de los estudiantes del curso en la asignatura ' + asignatureName + ' es de: ' + percentageTMBTotal
# i : valor numerico entero que itera en el ciclo for

# Firma y propósito:
# Firma (entradas y salidas):
    # Entrada: asignatureName, numberStudents, studentGender, studentAge, studentWeight studentHeight 
    # Salida: messageResult
# Propósito: Definir los valores bases para poder sacar el promedio de tasa metabólica basal de un grupo de estudiantes de un curso determinado

# Ejemplos funcionales, pruebas con diferentes asignaturas, sexo, estatura, peso, edad
#1
#  Si numberStudents = 1, asignatureName = 'matematica' 
#   Estudiante #1
#       studentGender = 1, studentHeight = 170, studentWeight = 70, studentAge = 17, 
#   accumulatorTMB = 1682.5
#   percentageTMBTotal = 1682.5
#   messageResult = 'El promedio de tasa metabólica basal(TMB) de los estudiantes del curso en la asignatura matematica es de: 1682.5'
#2
#  Si numberStudents = 2, asignatureName = 'quimica', 
#   Estudiante #1
#       studentGender = 1 studentHeight = 170, studentWeight = 70, studentAge = 17, 
#   Estudiante #2
#       studentGender = 2 studentHeight = 170, studentWeight = 70, studentAge = 17, 
#   accumulatorTMB = 3199
#   percentageTMBTotal = 1599,5
#   messageResult = 'El promedio de tasa metabólica basal(TMB) de los estudiantes del curso en la asignatura quimica es de: 1599,5'
#3
#  Si numberStudents = 3, asignatureName = 'fisica', 
#   Estudiante #1
#       studentGender = 1 studentHeight = 170, studentWeight = 70, studentAge = 17, 
#   Estudiante #2
#       studentGender = 2 studentHeight = 170, studentWeight = 70, studentAge = 17, 
#   Estudiante #3
#       studentGender = 1 studentHeight = 150, studentWeight = 55, studentAge = 21, 
#   accumulatorTMB = 4586,5 
#   percentageTMBTotal = 2293,25
#   messageResult = 'El promedio de tasa metabólica basal(TMB) de los estudiantes del curso en la asignatura fisica es de: 2293,25'
# Código del programa: 
#4
#  Si numberStudents = 4, asignatureName = 'artes', 
#   Estudiante #1
#       studentGender = 1 studentHeight = 170, studentWeight = 70, studentAge = 17, 
#   Estudiante #2
#       studentGender = 2 studentHeight = 170, studentWeight = 70, studentAge = 17, 
#   Estudiante #3
#       studentGender = 1 studentHeight = 150, studentWeight = 55, studentAge = 21, 
#   Estudiante #4
#       studentGender = 2 studentHeight = 150, studentWeight = 55, studentAge = 21, 
#   accumulatorTMB = 5808 
#   percentageTMBTotal = 1452
#   messageResult = 'El promedio de tasa metabólica basal(TMB) de los estudiantes del curso en la asignatura artes es de: 1452'
#5
#  Si numberStudents = 5, asignatureName = 'tecnologia', 
#   Estudiante #1
#       studentGender = 1 studentHeight = 170, studentWeight = 70, studentAge = 17, 
#   Estudiante #2
#       studentGender = 2 studentHeight = 170, studentWeight = 70, studentAge = 17, 
#   Estudiante #3
#       studentGender = 1 studentHeight = 150, studentWeight = 55, studentAge = 21, 
#   Estudiante #4
#       studentGender = 2 studentHeight = 150, studentWeight = 55, studentAge = 21, 
#   Estudiante #5
#       studentGender = 1 studentHeight = 200, studentWeight = 60, studentAge = 15, 
#   accumulatorTMB = 7588
#   percentageTMBTotal = 1517,6
#   messageResult = 'El promedio de tasa metabólica basal(TMB) de los estudiantes del curso en la asignatura tecnologia es de: 1517,6'
# Código del programa: 
#6
#  Si numberStudents = 6, asignatureName = 'etica', 
#   Estudiante #1
#       studentGender = 1 studentHeight = 170, studentWeight = 70, studentAge = 17, 
#   Estudiante #2
#       studentGender = 2 studentHeight = 170, studentWeight = 70, studentAge = 17, 
#   Estudiante #3
#       studentGender = 1 studentHeight = 150, studentWeight = 55, studentAge = 21, 
#   Estudiante #4
#       studentGender = 2 studentHeight = 150, studentWeight = 55, studentAge = 21, 
#   Estudiante #5
#       studentGender = 1 studentHeight = 200, studentWeight = 60, studentAge = 15, 
#   Estudiante #6
#       studentGender = 2 studentHeight = 200, studentWeight = 60, studentAge = 15, 
#   accumulatorTMB = 9202
#   percentageTMBTotal = 1533,6
#   messageResult = 'El promedio de tasa metabólica basal(TMB) de los estudiantes del curso en la asignatura etica es de: 1533,6'
# Código del programa: 

def run():
    numberStudents = int(input("""
        ¿Cuantos estudiantes son?
        (0) Para Salir
        Digite la cantidad de estudiantes:"""
    ))
    messageResult = ''
    if(numberStudents == 0):
        messageResult = 'Chao :)'
        print(messageResult)
    else:
        asignatureName = input('Digite el nombre de la asignatura: ')
        accumulatorTMB = 0
        for i in range(numberStudents):
            print('Estudiante ' + str(i+1))
            studentGender = int(input("""
                ¿Cual es su sexo?
                (1) - Hombre
                (2) - Mujer
                Elija una opcion:"""
            ))
            studentHeight = float(input('Digite la altura del estudiante en "cm" ' + str(i+1) + ': '))
            studentWeight = float(input('Digite el peso del estudiante en "kg" ' + str(i+1) + ': '))
            studentAge = int(input('Digite la edad del estudiante ' + str(i+1) + ': '))
            accumulatorTMB += calculateTMB(studentGender, studentWeight, studentHeight, studentAge)
        percentageTMBTotal = courseAverageTMB(accumulatorTMB, numberStudents)
        messageResult = 'El promedio de tasa metabólica basal(TMB) de los estudiantes del curso en la asignatura ' + asignatureName + ' es de: ' + str(round(percentageTMBTotal, 1))
        print(messageResult)
run()

# Probar el programa:
#Prueba #1 
