# Enunciado

# Se requiere crear un aplicativo que permita determinar y mostrar la fecha límite para 
# el pago de la declaración de renta de las personas naturales en el presente año (2021). 
# Para determinar la fecha límite de pago de la declaración de renta de una persona 
# natural en el año 2021 se debe tener en cuenta el calendario tributario de la DIAN, el 
# cual puede consultar en la siguiente página (link). Se le pide a usted aplicar la 
# metodología vista en el curso para crear un programa que le permita a un usuario 
# conocer la fecha límite para el pago de la declaración de renta de una persona natural 
# dado el número de su cédula.

# Programadores Novatos

# Definición de datos:
# CC: cadena de texto alfanumerica que contiene los 2 ultimos digitos del CC(Cedula de Cuidadania) 
# message: cadena de texto que contiene el siguiente texto 'Su fecha limite para hacer la declaracion de renta es el: '
# month: cadena de texto que contiene el nombre del mes de la fecha limite(Este varia dependiendo del CC ingresado Ej: 'Agosto', 'Septiembre', 'Octubre')
# date: cadena de texto alfanumerico que contiene el dia del mes de la fecha limite(Este varia dependiendo del CC ingresado) 
# age: cadena de texto alfanumerico que contiene el año actual 
# resulMesaage: cadena de texto alfanumerico que concatena el message + date + "/" + month + "/" + age'(Este varia dependiendo de la cedula ingresada) Ej: Su fecha limite es el 19 Agosto 2021



# Firma y propósito:
# Firma (entradas y salidas):
    # Entrada: CC
    # Salida: resulMesaage
# Propósito: Determinar la fecha limite para hacer la declaracion de renta de una persona natural en el 2021

# Ejemplos funcionales, Probar diferentes CC:
# '1107837809', para este CC la fecha limite del usuario para hacer la declaracion de renta es el 16 de Agosto.
# '1107837835', para este CC la fecha limite del usuario para hacer la declaracion de renta es e 2 de Septiempre.
# '1107837895', para este CC la fecha limite del usuario para hacer la declaracion de renta es e 14 de Ocutibre.
# '1107837800', para este CC la fecha limite del usuario para hacer la declaracion de renta es e 19 de Ocutibre.

# Código del programa:

# se crea la funcipn

def dateLimit(CC):
    message = 'Su fecha limite para hacer la declaracion de renta es el: '
    month = ''
    date = ''
    age = '2021'
    #Se valida si la fecha limite se encuentra en agosto
    #Agust
    if(CC <= '32' and CC > '00'):
        month = 'Agosto'
        if(CC <= '02'):
            date = '9'
        elif(CC <= '04'):
            date = '10'
        elif(CC <= '06'):
            date = '11' 
        elif(CC <= '08'):
            date = '12' 
        elif(CC <= '10'):
            date = '16' 
        elif(CC <= '12'):
            date = '17' 
        elif(CC <= '14'):
            date = '18' 
        elif(CC <= '16'):
            date = '19' 
        elif(CC <= '18'):
            date = '22' 
        elif(CC <= '20'):
            date = '23' 
        elif(CC <= '22'):
            date = '25' 
        elif(CC <= '24'):
            date = '25' 
        elif(CC <= '26'):
            date = '26' 
        elif(CC <= '28'):
            date = '29' 
        elif(CC <= '30'):
            date = '30' 
        elif(CC <= '32'):
            date = '31' 
    #Se valida si la fecha limite se encuentra en Septiembre
    #September
    elif(CC <= '64' and CC > '00'):
        month = 'Septiembre'
        if(CC <= '34'):
            date = '1'
        elif(CC <= '36'):
            date = '2'
        elif(CC <= '38'):
            date = '5'
        elif(CC <= '40'):
            date = '6'
        elif(CC <= '42'):
            date = '7'
        elif(CC <= '44'):
            date = '8'
        elif(CC <= '46'):
            date = '9'
        elif(CC <= '48'):
            date = '12'
        elif(CC <= '50'):
            date = '13'
        elif(CC <= '52'):
            date = '14'
        elif(CC <= '54'):
            date = '15'
        elif(CC <= '56'):
            date = '16'
        elif(CC <= '58'):
            date = '19'
        elif(CC <= '60'):
            date = '20'
        elif(CC <= '62'):
            date = '21'
        elif(CC <= '64'):
            date = '22'
        elif(CC <= '66'):
            date = '23'
        elif(CC <= '68'):
            date = '26'
        elif(CC <= '70'):
            date = '27'
        elif(CC <= '72'):
            date = '28'
        elif(CC <= '74'):
            date = '29'
        elif(CC <= '76'):
            date = '30'
    #Se valida si la fecha limite se encuentra en Octubre
    #October
    elif(CC <= '99'):
        month = 'Octubre'
        if(CC <= '78'  and CC > '00'):
            date = '3'
        elif(CC <= '80' and CC > '00'):
            date = '4'
        elif(CC <= '82' and CC > '00'):
            date = '5'
        elif(CC <= '84' and CC > '00'):
            date = '6'
        elif(CC <= '86' and CC > '00'):
            date = '7'
        elif(CC <= '88' and CC > '00'):
            date = '10'
        elif(CC <= '90' and CC > '00'):
            date = '11'
        elif(CC <= '92' and CC > '00'):
            date = '12'
        elif(CC <= '94' and CC > '00'):
            date = '13'
        elif(CC <= '96' and CC > '00'):
            date = '14'
        elif(CC <= '98' and CC > '00'):
            date = '18'
        elif(CC <= '99' or CC <= '00'):
            date = '19'
    messageResult  = message + date + '/' + month + '/' + age
    return messageResult 

#Pedimos al usuario su cedula de ciudadania
CC = input('Digite su Cedula de Ciudadania:')
#Sacamos los 2 ultimos digitos de Cedula
CC = CC[-2:]
print(CC)

messageResult  = dateLimit(CC)
print(messageResult )

# Probar el programa:
#PRUEBA #1: Si ingresa el valor al programa '11078378509', da como resultado que la fecha limite para hacer la declaracion de renta es el 16 de Agosto del 2021.
    #CC = '09'
    #resulMesaage = 'Su fecha limite para hacer la declaracion de renta es el: 16/Agosto/2021'

#PRUEBA #2: Si ingresa el valor al programa '11078378535', da como resultado que la fecha limite para hacer la declaracion de renta es el 2 de Septiempre del 2021.
    #CC = '35'
    #resulMesaage = 'Su fecha limite para hacer la declaracion de renta es el: 2/Septiembre/2021'

#PRUEBA #3: Si ingresa el valor al programa '11078378595', da como resultado que la fecha limite para hacer la declaracion de renta es el 14 de Octubre del 2021.
    #CC = '95'
    #resulMesaage = 'Su fecha limite para hacer la declaracion de renta es el: 14/Octubre/2021'

#PRUEBA #4: Si ingresa el valor al programa '11078378500', da como resultado que la fecha limite para hacer la declaracion de renta es el 19 de Octubre del 2021.
    #CC = '00'
    #resulMesaage = 'Su fecha limite para hacer la declaracion de renta es el: 19/Octubre/2021'
