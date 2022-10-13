def run():
    messageResult = ''
    numberStudents = 4
    topTime1 = 0
    topName1 = ""
    topTime2 = 0
    topName2 = ""
    topTime3 = 0
    topName3 = ""
    for i in range(numberStudents):
        isRegistered = int(input("""
            ¿El esudiante esta matriculado?
            (1) si
            (2) no
            Elige una opcion: """))
        if(isRegistered == 1):
            isMen = int(input("""
            ¿El estudiante es hombre o mujer ?
            (1) Hombre
            (2) Mujer
            Elige una opcion: """))
            if(isMen == 1):
                yearStudent = int(input('¿Cuantos años tiene el estudiante?: '))
                if(yearStudent >= 24):
                    nameStudent = input('Digite el nombre del estudiante: ')
                    timeStudent = int(input('Digite el tiempo en recorrer los 100mts'))
                    #1:1 #2:2 #3:3
                    #top1 = 1
                    #top2 = 0
                    #top3 = 0
                    if(timeStudent > topTime1):
                        topTime3 = topTime2
                        topName3 = topName2
                        topTime2 = topTime1
                        topName2 = topName1
                        topTime1 = timeStudent
                        topName1 = nameStudent
                        print('1')
                    elif(timeStudent > topTime2):
                        topTime3 = topTime2
                        topName3 = topName2
                        topTime2 = timeStudent
                        print('2')
                        topName2 = nameStudent
                    elif(timeStudent > topTime3):
                        topName3 = nameStudent
                        topTime3 = timeStudent
                        print('3')
                else:
                    messageResult = 'Si el estudiante es menor de 24 años no puede participar'
                print(topTime1, topTime2, topTime3)
            else:
                messageResult = 'Si el estudiante es mujer no puede parcipar'
        else:
            messageResult = 'Si el estudiante no esta matriculado no puede participar'
    print(messageResult)

run()