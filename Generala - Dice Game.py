mport re
import collections

def points(dice):
    if collections.Counter(dice).most_common()[0][1] >= 4:
        return collections.Counter(dice).most_common()[0][1]*10
    if collections.Counter(dice).most_common()[0][1] == 3 and collections.Counter(dice).most_common()[1][1] == 2:
        return 30
    x = 1 if int(sorted(list(dice))[0]) == 1 else 0
    for i in range(x, 4):
        if int(sorted(list(dice))[i]) + 1 != int(sorted(list(dice))[i+1]) or int(sorted(list(dice))[1]) == 0:
            return 0
    else:
        return 20
