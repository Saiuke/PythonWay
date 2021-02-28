#
# We want make a package of goal kilos of chocolate.
# We have small bars (1 kilo each) and big bars (5 kilos each).
# Return the number of small bars to use, assuming we always use big bars before small bars.
# Return -1 if it can't be done.
#

def make_chocolate(small, big, goal):
    totalBig = big * 5
    smallNeeded = goal - totalBig
    if goal < 5 and small >= goal:
        return goal
    if smallNeeded > small or totalBig > goal:
        return -1
    else:
        return smallNeeded

