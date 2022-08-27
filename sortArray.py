arrayNumbers = [4, 30, 7, 5, 9, 7, 2, 4, 1, 3, 2];
length = len(arrayNumbers)

for index in range(length-1):
    for subIndex in range(length-1):
        if arrayNumbers[subIndex]>arrayNumbers[subIndex+1]:
            swapElement=arrayNumbers[subIndex+1]
            arrayNumbers[subIndex+1]=arrayNumbers[subIndex]
            arrayNumbers[subIndex]=swapElement

print(arrayNumbers)