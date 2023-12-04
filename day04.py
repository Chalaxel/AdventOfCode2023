import re

with open("data.txt", "r") as inputFile:
    inputLines = inputFile.readlines()

score = 0
scratch_card_nb = [1 for n in inputLines]
for i, line in enumerate(inputLines):
    # Separating winning numbers and numbers we have
    card, winning_nb, nb_you_have = re.split(' \| |: ', line[:-1])
    winning_nb = [n for n in winning_nb.split(' ') if n.isdigit()]
    nb_you_have = [n for n in nb_you_have.split(' ') if n.isdigit()]

    # Finding the common numbers
    commun = [n for n in nb_you_have if n in winning_nb]

    # Adding the numbers of total card we got (Part 2)
    for k in range(scratch_card_nb[i]):
        for j in range(i+1, i+1+len(commun)):
            scratch_card_nb[j] += 1

    # Calculating and adding score of the card
    this_score = 2 ** len(commun) // 2
    score += this_score
print(f"Part 1 answer : {score}")
print(f"Part 2 answer : {sum(scratch_card_nb)}")

