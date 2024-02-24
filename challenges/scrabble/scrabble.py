import random
from datetime import datetime

def print_tile_set(tileset, scorelist):
    tilestring = 'Tiles  : '
    scorestring = 'Scores : '
    for alphabet in tileset:
        tilestring += alphabet + "  "
        score = scorelist[ord(alphabet) - 65]
        if score < 10:
            scorestring += str(score) + "  "
        else:
            scorestring += str(score) + " "
    print(tilestring)
    print(scorestring)

def prepare_score_list(filename):
    scorelist = [0] * 26
    f = open(filename, 'r')
    for line in f:
        alphabet_score_pair = line.strip().split()
        alphabet = alphabet_score_pair[0]
        score = int(alphabet_score_pair[1])
        scorelist[ord(alphabet) - 65] = score
    f.close()
    return scorelist

scorelist = prepare_score_list("scores.txt")

while True:
    userinput = input("Do you want to use random tiles (enter Y or N): ").upper()
    if userinput != "N" and userinput != "Y":
        continue
    if userinput == 'N':
        tileset = ['B', 'S', 'N', 'O', 'E', 'U', 'T']
    else:
        tileset = []
        for i in range(7):
            tileset.append(chr(65 + random.randint(0, 25)))
    break

print_tile_set(tileset, scorelist)

#####################################################################
#### Your code starts here                                       ####
#####################################################################

