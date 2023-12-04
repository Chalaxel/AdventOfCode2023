with open("data.txt", "r") as inputFile:
    inputLines = inputFile.readlines()

########### PART 1 ###########
sumValue = 0
for line in inputLines:
    digits = [c for c in line if c.isdigit()]
    sumValue += int(digits[0] + digits[-1])
print(sumValue)

########### PART 2 ###########
sumValue = 0
letterDigits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
                "six": "6", "seven": "7", "eight": "8", "nine": "9"}
for line in inputLines:
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        else:
            for length in range(3,6):
                if line[i:i+length] in letterDigits.keys():
                    digits.append(letterDigits[line[i:i+length]])
    sumValue += int(digits[0] + digits[-1])
print(sumValue)
