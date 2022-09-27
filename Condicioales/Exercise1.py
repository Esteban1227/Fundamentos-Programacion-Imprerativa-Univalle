def isOlder(currentYear, studentYear):
    currentAgeStudent = currentYear - studentYear
    isOlderStudent = False
    if(currentAgeStudent >= 18):
        isOlderStudent = True
    else:
        isOlderStudent = False
    return isOlderStudent

def run():
    messageIsOlder = ''
    currentYear = 2022
    studentYear =  int(input('Escribe su año de nacimiento:'))
    isOlderStudent = isOlder(currentYear, studentYear)
    if isOlderStudent:
        messageIsOlder = 'Eres Mayor'
    else:
        messageIsOlder = 'Eres Menor'
    return messageIsOlder

if __name__ == '__main__':
    print(run())
