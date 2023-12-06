with open("data.txt", "r") as inputFile:
    inputLines = inputFile.readlines()

# Regroup seeds in a list and initialize data dict
seeds = [int(n) for n in inputLines[0][:-1].split(": ")[1].split(" ")]
data = {}

# Parses different maps in a data dict
current_rule = None
for line in inputLines[2:]:
    if current_rule is None:
        current_rule = line.split(" ")[0]
        data[current_rule] = []
    elif line == "\n":
        current_rule = None
    else:
        map_rule = [int(n) for n in line[:-1].split(" ")]
        data[current_rule].append(map_rule)


# For each seed, convert it successively until finding the location
for i in range(len(seeds)):
    # Conversion rule by rule
    for mapping in data.values():
        for m in mapping:
            if m[1] <= seeds[i] < m[1] + m[2]:
                seeds[i] = m[0] + (seeds[i] - m[1])
                break
print(f"Lowest location member : {min(seeds)}")


