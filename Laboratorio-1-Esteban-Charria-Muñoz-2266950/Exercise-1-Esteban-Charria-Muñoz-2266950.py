# Enunciado

# Se requiere crear un aplicativo que permita determinar y mostrar la fecha límite para 
# el pago del impuesto vehicular el presente año (2021). Para determinar la fecha límite 
# de pago de un vehículo automotor se tienen en cuenta el siguiente calendario: 
# a. Durante el periodo gravable 2020, los vehículos con placas comprendidas 
# entre 000 y 333, podrán declarar y pagar el impuesto automotor hasta el 30 de 
# abril del 2021, sin sanción o intereses por mora. 
# b. Durante el periodo gravable 2020, los vehículos con placas comprendidas 
# entre 334 y 666, podrán declarar y pagar el impuesto automotor hasta el 31 de 
# mayo del 2021, sin sanción o intereses por mora.
# c. Durante el periodo gravable 2020, los vehículos con placas comprendidas 
# entre 667 y 999 podrán declarar y pagar el impuesto automotor hasta el 30 de 
# junio de 2021, sin sanción o intereses por mora.
# d. Motocicletas con cilindraje superior 125cc podrán declarar y pagar el 
# impuesto automotor hasta el 30 de junio de 2021, sin sanción o intereses por 
# mora. Las motocicletas de cilindraje menor a 125 C.C. no pagan impuesto 
# vehicular en Cali.

# Programadores Novatos

# Definición de datos:
# isMotorcycle: valor booleano que define si el vehiculo es una moto
# isMotorcycleInput: valor numerico entero que selecciona el usuario para definir si su vehiculo es una moto o un carro y si es una mato si el cilindraje es mayor a 125cc o es menor
# plateNumber: cadena alfanumerica que contiene la placa del vehiculo
# messageResult: 
    # cadena alfanumerica que contiene el mensaje con la fecha limite del pago de inpuesto Ej: 'Su fecha limite de pago es hasta el 30 de Junio 2021' 
    # o 
    # cadena de texto que contiene el mesaje que no tiene que pagar inpuestos por su vehiculo Ej: 'No tiene necesidad de pagar impuesto'
    # o 
    # cadena de texto que contiene el mesaje que el numero de su placa es invalido Ej: 'Su placa no es valida'

# Firma y propósito:
# Firma (entradas y salidas):
    # Entrada: isMotorcycle, plateNumber
    # Salida: messageResult 
# Propósito: encontar la fecha limite para el pago de impuesto vehicular en el año 2021 en cali

# Ejemplos funcionales, pruebas en base al calendario:
#Si es una moto con un cilindraje mayor a 125cc La fecha limite de pago de impuesto es el el 30 de Junio 2021
#Si es una moto con un cilindraje menor a 125cc No tiene que pagar impuestos
#Si el numero de la placa es 123 La fecha limite de pago de impuesto es el el 30 de Abril 2021
#Si el numero de la placa es 345 La fecha limite de pago de impuesto es el 31 de Mayo 2021
#Si el numero de la placa es 678 La fecha limite de pago de impuesto es el 30 de Junio 2021
#Si el numero de la placa es 91011 la placa no seria valida

# Código del programa:

#Creamos una funcion para determinar la fecha limite 
def limitDate(isMotorcycle, plateNumberInput):
    messageResult  = ''
    if(isMotorcycle):
        messageResult  = 'Su fecha limite de pago es hasta el 30 de Junio 2021'
    elif(not isMotorcycle and plateNumberInput == 0):
        messageResult  = 'No tiene necesidad de pagar impuesto'
    elif(plateNumberInput <= '333'):
        messageResult  = 'Su fecha limite de pago es hasta el 30 de Abril 2021'
    elif(plateNumberInput <= '666'):
        messageResult  = 'Su fecha limite de pago es hasta el 31 de Mayo 2021'
    elif(plateNumberInput <= '999'):
        messageResult  = 'Su fecha limite de pago es hasta el 30 de Junio 2021'
    else:
        messageResult  = 'Su placa no es valida'
    return messageResult 

isMotorcycle = False
plateNumberInput = 0
isMotorcycleInput = int(input("""
    ¿Su Vehiculo es una moto:?
    1 - SI
    2 - NO
    Elige una opción:
    """))
if(isMotorcycleInput == 1):
    isMotorcycleInput = int(input("""
        ¿El cilindraje de su moto es mayor a 125cc:?
        1 - SI
        2 - NO
        Elige una opción:
        """))
    if(isMotorcycleInput == 1):
        isMotorcycle = True
    else:
        isMotorcycle = False
elif(isMotorcycleInput == 2):
    plateNumberInput = input('Digite el numero de la placa de su vehiculo:')

messageResult  = limitDate(isMotorcycle, plateNumberInput)

print(messageResult )
# Probar el programa:
#Prueba #1 Si ingresamos en el primer input un '1' y en el segundo input un '1' da como resultado que la fecha limite de pago es hasta el 30 de Junio 2021
    #isMotorcycle = True
    #plateNumberInput = 0
    #messageResult  = 'Su fecha limite de pago es hasta el 30 de Junio 2021'
#Prueba #2 Si ingresamos en el primer input un '1' y en el segundo input un '2' da como resultado que Su Vehiculo no tiene que pagar impuestos
    #isMotorcycle = False
    #plateNumberInput = 0
    #messageResult  = 'No tiene necesidad de pagar impuesto'
#Prueba #3 Si ingresamos en el primer input un '2' y en el segundo input la placa es '123' da como resultado que la fecha limite de pago es hasta el 30 de Abril 2021 
    #isMotorcycle = False
    #plateNumberInput = 123
    #messageResult  = 'Su fecha limite de pago es hasta el 30 de Abril 2021'
#Prueba #4 Si ingresamos en el primer input un '2' y en el segundo input la placa es '345' da como resultado que la fecha limite de pago es hasta el 31 de Mayo 202 
    #isMotorcycle = False
    #plateNumberInput = 345
    #messageResult  = 'Su fecha limite de pago es hasta el 31 de Mayo 2021'
#Prueba #5 Si ingresamos en el primer input un '2' y en el segundo input la placa es '678' da como resultado que la fecha limite de pago es hasta el 30 de Junio 2021 
    #isMotorcycle = False
    #plateNumberInput = 678
    #messageResult  = 'Su fecha limite de pago es hasta el 30 de Junio 2021'
#Prueba #6 Si ingresamos en el primer input un '2' y en el segundo input la placa es '91011' da como resultado que la placa no es valida 
    #isMotorcycle = False
    #plateNumberInput = 91011
    #messageResult  = 'Su placa no es valida'