import re

with open("data.txt", "r") as inputFile:
    inputLines = inputFile.readlines()


########### PART 1 ###########
def possible_set(set_list):  # [['2', 'green'], ['5', 'blue']
    if False in [True if int(ss[0]) <= cube_number[ss[1]] else False for ss in set_list]:
        return False
    else:
        return True


cube_number = {'red': 12, 'green': 13, 'blue': 14}
possible_games = []
power_sets = []
for line in inputLines:
    min_set = {'red': 0, 'green': 0, 'blue': 0}
    line_split = re.split(': |; ', line[:-1])
    game_nb, sets = line_split[0], line_split[1:]
    sl = [[sss.split(' ') for sss in ss] for ss in [s.split(', ') for s in sets]]
    possible_sets = [True if possible_set(s) else False for s in sl]
    if False not in possible_sets:
        possible_games.append(int(game_nb.split(' ')[-1]))
    for s in sl:
        for color in s:
            if int(color[0]) > min_set[color[1]]:
                min_set[color[1]] = int(color[0])
    mul = 1
    for c in min_set.values():
        mul = mul * c
    power_sets.append(mul)
print(sum(possible_games))
print(sum(power_sets))

########### PART 2 ###########
