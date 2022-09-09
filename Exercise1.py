def isOlder(currentYear, studentYear):
    currentAgeStudent = currentYear - studentYear
    if(currentAgeStudent >= 18):
        return True
    else:
        return False

def run():
    messageIsOlder = ''
    currentYear = 2022
    studentYear =  int(input('Escribe su año de nacimiento:'))
    isOlderStudent = isOlder(currentYear, studentYear)
    if isOlderStudent:
        messageIsOlder = 'Eres Mayor'
    else:
        messageIsOlder = 'Eres Menor'
    return print(messageIsOlder)

if __name__ == '__main__':
    run()
