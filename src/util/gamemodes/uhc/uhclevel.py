
def getUhcLevel(score):
    scores = [0, 10, 60, 210, 460, 960, 1710, 2710, 5210, 10_210, 13_210, 16_210, 19_210, 22_210, 25_210]
    for x in scores:
        if x - score > 0:
            return scores.index(x)
    return len(scores)

def getFormattedUhcLevel(level):
    return f"&6[{level}✫]"