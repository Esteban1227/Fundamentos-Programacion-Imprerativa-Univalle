def limitDate(plateNumber, isMotorcycle):
    message = ''
    if(isMotorcycle):
        message = 'Su fecha limite de pago es hasta el 30 de Junio 2021'
    elif(plateNumber >= 333):
        message = 'Su fecha limite de pago es hasta el 30 de Abril 2021'
    elif(plateNumber >= 666):
        message = 'Su fecha limite de pago es hasta el 31 de Mayo 2021'
    elif(plateNumber >= 999 ):
        message = 'Su fecha limite de pago es hasta el 30 de Junio 2021'
    return print(message)



def run():
    plateNumberInput = int(input('Digite el numero de la placa de su vehiculo:'))
    isMotorcycleInput = int(input("""
            ¿Su Vehiculo es una moto:?
            1 - SI
            2 - NO
            Elige una opción:
            """
        ))
    isMotorcycle = False
    if(isMotorcycleInput == 1):
        isMotorcycleCC = int(input("""
                ¿El cilindraje de su moto es mayor a 125cc:?
                1 - SI
                2 - NO
                Elige una opción:
                """
            ))
        if(isMotorcycleCC == 1):
            isMotorcycle = True
    
    limitDate(plateNumberInput, isMotorcycle)

if __name__ == '__main__':
    run()