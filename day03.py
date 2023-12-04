with open("data.txt", "r") as inputFile:
    inputLines = inputFile.readlines()

########### PART 1 ###########
ignored_symbols = {'.', '\n'}
sum_part = 0
for n, line in enumerate(inputLines):
    valid_number = []
    current = ""
    included = False
    for k, c in enumerate(line):
        if not c.isdigit():
            if included is True:
                sum_part += int(current)
                valid_number.append(int(current))
                print(f"\u001b[32;1m{current}\u001b[37m", end='')
            else:
                print(f"\u001b[31;1m{current}\u001b[37m", end='')
            if c != '.':
                print(f"\u001b[33;1m{c}\u001b[37m", end='')
            else:
                print(c, end='')
            current = ""
            included = False
        else:
            current = current + c
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    try:
                        if not (inputLines[n + i][k + j]).isdigit() and inputLines[n + i][k + j] not in ignored_symbols:
                            included = True
                    except IndexError as e:
                        pass

print(sum_part)

########### PART 2 ###########
ignored_symbols = {'.', '\n'}
gears = {'current': []}
sum_part = 0
for n, line in enumerate(inputLines):
    valid_number = []
    current = ""
    for k, c in enumerate(line):
        if not c.isdigit():
            for engine in gears["current"]:
                if engine not in gears.keys():
                    gears[engine] = [int(current)]
                else:
                    gears[engine].append(int(current))
            gears['current'] = []
            current = ""
        else:
            current = current + c
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    try:
                        if inputLines[n + i][k + j] == "*" and f"{n+i};{k+j}" not in gears['current']:
                            gears["current"].append(f"{n+i};{k+j}")
                    except IndexError as e:
                        pass
for g in gears.values():
    if len(g) == 2:
        sum_part += g[0]*g[1]

print(gears)
print(sum_part)

