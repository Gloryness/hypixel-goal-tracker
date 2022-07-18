
def getSpeedUhcLevel(score):
    scores = [0, 50, 300, 1050, 2550, 5550, 15_550, 30_550, 55_550, 85_550]
    for x in scores:
        if x - score > 0:
            return scores.index(x)
    return len(scores)

def getFormattedSpeedUhcLevel(level):
    return f"&d[{level}❋]"