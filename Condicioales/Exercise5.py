# Enunciado

# Se requiere crear un aplicativo que permita determinar y mostrar la nota definitiva de 
# un estudiante y si aprueba o no una asignatura. Para determinar la nota de una 
# asignatura se debe tener en cuenta lo siguiente:
# a. La asignatura puede ser matemáticas, física o química.
# b. Cada asignatura se evalúa con la nota del examen y las notas de tres tareas 
# así: 
#  La calificación de Matemáticas se obtiene de la siguiente manera: 
# Examen 90% y el promedio de las tareas 10%.
#  La calificación de Física se obtiene de la siguiente manera: Examen 
# 80% y el promedio de las tareas 20%.
#  La calificación de Química se obtiene de la siguiente manera: Examen 
# 85% y el promedio de las tareas 15%.
# Se le pide a usted aplicar la metodología vista en el curso para crear un programa que 
# le permita a un usuario conocer la nota definitiva de una de las asignaturas 
# (Matemáticas, Física o Química) y saber si aprobó o no la asignatura.

# Programadores Novatos

# Definición de datos:
# matterInput valor numerico entero que permite determinar que materia se va a evaluar
# matter cadena de texto con la materia seleccionada Ej: 'matematicas', 'quimica', 'fisica'
# homeworkNote1 valor numerico decimal que contiene la nota de la primera tarea
# homeworkNote2 valor numerico decimal que contiene la nota de la segunda tarea
# homeworkNote3 valor numerico decimal que contiene la nota de la tercera tarea
# noteTest valor numero decimal que contiene la nota del examen
# totalHomeworkNotes valor numero decimal que contiene el promedio de las 3 notas(homeworkNote1, homeworkNote2, homeworkNote3)
# finalNote  cadena alfanumerica que contiene la nota final del estudiante
# messageResult  cadena alfanumerica que contiene si el estudiante paso o no paso la materia y la nota defiinitiva

# Firma y propósito:
# Firma (entradas y salidas):
    # Entrada: matter, homeworkNote1, homeworkNote2, homeworkNote3, noteTest
    # Salida: messageResult
# Propósito: Definir si un estudiando aprobo o reprobo una materia y mostrarle su respectiva nota

# Ejemplos funcionales, pruebas con diferentes notas y materias:
# Si la materia es matematicas y las notas de las 3 tareas son 5.0, 4.5, 5.0 y la nota del examen es 5.0 el estudiante aprobaria la materia y su nota definitiva seria 4.0
# Si la materia es matematicas y las notas de las 3 tareas son 1.0, 2.0, 2.0 y la nota del examen es 3.0 el estudiante reprobaria la materia y su nota definitiva seria 2.9
# Si la materia es fisica y las notas de las 3 tareas son 4.0, 4.5, 3.0 y la nota del examen es 5.0 el estudiante aprobaria la materia y su nota definitiva seria 4.8
# Si la materia es fisica y las notas de las 3 tareas son 1.0, 1.5, 1.0 y la nota del examen es 2.0 el estudiante reprobaria la materia y su nota definitiva seria 1.8
# Si la materia es quimica y las notas de las 3 tareas son 3.0, 3.5, 3.0 y la nota del examen es 3.0 el estudiante aprobaria la materia y su nota definitiva seria 3.0
# Si la materia es quimica y las notas de las 3 tareas son 1.0, 3.0, 2.0 y la nota del examen es 2.0 el estudiante reprobaria la materia y su nota definitiva seria 2.0

# Código del programa:

def qualificationTotal(matter, noteTest, homeworkNote1, homeworkNote2, homeworkNote3) :
    totalHomeworkNotes = (homeworkNote1 + homeworkNote2 + homeworkNote3) / 3
    messageResult = '' 
    finalNote = 0
    if(matter == 'matematicas'):
        finalNote = (noteTest * .90) + (totalHomeworkNotes * .10)
    elif(matter == 'fisica'):
        finalNote = (noteTest * .80) + (totalHomeworkNotes * .20)     
    elif(matter == 'quimica'):
        finalNote = (noteTest * .85) + (totalHomeworkNotes * .15)

    if(finalNote >= 3):
        messageResult = '¡Felicidades usted APROBO ' + matter + '! Su nota definitiva es ' + str(round(finalNote, 1))
    else: messageResult = 'Lo lamento usted Reprobo ' + matter + ' Su nota definitiva es ' + str(round(finalNote, 1))
    return messageResult

matterInput = int(input("""
    ¿Que Materia desea consultar su nota final?
    1 - Matematicas
    2 - Fisica
    3 - Quimica
    Elige una opción:
    """))

matter = ''
if(matterInput == 1):
    matter = 'matematicas'
elif(matterInput == 2):
    matter = 'fisica'
elif(matterInput == 3):
    matter = 'quimica'

homeworkNote1 = float(input('Digite su primera nota de ' + matter + ':'))
homeworkNote2 = float(input('Digite su segunda nota de ' + matter + ':'))
homeworkNote3 = float(input('Digite su tercera nota de ' + matter + ':'))
noteTest = float(input('Digite su nota del examen de ' + matter + ':'))

messageResult = qualificationTotal(matter, noteTest, homeworkNote1, homeworkNote2, homeworkNote3)
print(messageResult)




# Probar el programa:
#Prueba #1 Si ingresamos en el primer input un '1' y digitamos las siguientes notas de tareas 5.0, 4.5, 5.0 y en la nota del examen ponemos 5.0 el resultado seria '¡Felicidades usted APROBO matematicas! Su nota definitiva es de 4.0' 
    # matter = matematicas
    # homeworkNote1 = 5.0
    # homeworkNote2 = 4.5
    # homeworkNote3 = 5.0
    # noteTest = 5.0
    # messageResult = '¡Felicidades usted APROBO matematicas! Su nota definitiva es de 4.0'
    
#Prueba #2 Si ingresamos en el primer input un '1' y digitamos las siguientes notas de tareas 1.0, 2.0, 2.0 y en la nota del examen ponemos 3.0 el resultado seria 'Lo lamento usted Reprobo matematicas Su nota definitiva es 2.9' 
    # matter = matematicas
    # homeworkNote1 = 1.0
    # homeworkNote2 = 2.5
    # homeworkNote3 = 2.0
    # noteTest = 2.9
    # messageResult = 'Lo lamento usted Reprobo matematicas Su nota definitiva es 2.9'

#Prueba #3 Si ingresamos en el primer input un '2' y digitamos las siguientes notas de tareas 4.0, 4.5, 3.0 y en la nota del examen ponemos 5.0 el resultado seria ¡Felicidades usted APROBO fisica! Su nota definitiva es de 4.8
    # matter = fisica
    # homeworkNote1 = 4.0
    # homeworkNote2 = 4.5
    # homeworkNote3 = 3.0
    # noteTest = 5.0
    # messageResult = '¡Felicidades usted APROBO fisica! Su nota definitiva es de 4.0'

#Prueba #4 Si ingresamos en el primer input un '2' y digitamos las siguientes notas de tareas 1.0, 1.5, 1.0 y en la nota del examen ponemos 2.0 el resultado seria Lo lamento usted Reprobo fisica Su nota definitiva es 1.8
    # matter = fisica
    # homeworkNote1 = 1.0
    # homeworkNote2 = 1.5
    # homeworkNote3 = 1.0
    # noteTest = 2.0
    # messageResult = 'Lo lamento usted Reprobo fisica Su nota definitiva es 1.8'

#Prueba #5 Si ingresamos en el primer input un '1' y digitamos las siguientes notas de tareas 3.0, 3.5, 3.0 y en la nota del examen ponemos 3.0 el resultado seria ¡Felicidades usted APROBO quimica! Su nota definitiva es 3.0 
    # matter = quimica
    # homeworkNote1 = 3.0
    # homeworkNote2 = 3.5
    # homeworkNote3 = 3.0
    # noteTest = 3.0
    # messageResult = '¡Felicidades usted APROBO quimica! Su nota definitiva es 3.0'
#Prueba #6 Si ingresamos en el primer input un '1' y digitamos las siguientes notas de tareas 1.0, 3.0, 2.0 y en la nota del examen ponemos 2.0 el resultado seria 'Lo lamento usted Reprobo quimica Su nota definitiva es 2.0' 
    # matter = quimica
    # homeworkNote1 = 1.0
    # homeworkNote2 = 3.0
    # homeworkNote3 = 2.0
    # noteTest = 2.0
    # messageResult = 'Lo lamento usted Reprobo quimica Su nota definitiva es 2.0'




