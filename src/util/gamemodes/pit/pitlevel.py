## A rewrite of https://github.com/PitPanda/PitPandaProduction/blob/master/structures/Pit.js but in Python.
import math

PRESTIGE_MULTIPLIERS = [
    {"Multiplier": 1, "TotalXp": 65950, "SumXp": 65950},
    {"Multiplier": 1.1, "TotalXp": 72560, "SumXp": 138510},
    {"Multiplier": 1.2, "TotalXp": 79170, "SumXp": 217680},
    {"Multiplier": 1.3, "TotalXp": 85750, "SumXp": 303430},
    {"Multiplier": 1.4, "TotalXp": 92330, "SumXp": 395760},
    {"Multiplier": 1.5, "TotalXp": 98940, "SumXp": 494700},
    {"Multiplier": 1.75, "TotalXp": 115440, "SumXp": 610140},
    {"Multiplier": 2, "TotalXp": 131900, "SumXp": 742040},
    {"Multiplier": 2.5, "TotalXp": 164890, "SumXp": 906930},
    {"Multiplier": 3, "TotalXp": 197850, "SumXp": 1104780},
    {"Multiplier": 4, "TotalXp": 263800, "SumXp": 1368580},
    {"Multiplier": 5, "TotalXp": 329750, "SumXp": 1698330},
    {"Multiplier": 6, "TotalXp": 395700, "SumXp": 2094030},
    {"Multiplier": 7, "TotalXp": 461650, "SumXp": 2555680},
    {"Multiplier": 8, "TotalXp": 527600, "SumXp": 3083280},
    {"Multiplier": 9, "TotalXp": 593550, "SumXp": 3676830},
    {"Multiplier": 10, "TotalXp": 659500, "SumXp": 4336330},
    {"Multiplier": 12, "TotalXp": 791400, "SumXp": 5127730},
    {"Multiplier": 14, "TotalXp": 923300, "SumXp": 6051030},
    {"Multiplier": 16, "TotalXp": 1055200, "SumXp": 7106230},
    {"Multiplier": 18, "TotalXp": 1187100, "SumXp": 8293330},
    {"Multiplier": 20, "TotalXp": 1319000, "SumXp": 9612330},
    {"Multiplier": 24, "TotalXp": 1582800, "SumXp": 11195130},
    {"Multiplier": 28, "TotalXp": 1846600, "SumXp": 13041730},
    {"Multiplier": 32, "TotalXp": 2110400, "SumXp": 15152130},
    {"Multiplier": 36, "TotalXp": 2374200, "SumXp": 17526330},
    {"Multiplier": 40, "TotalXp": 2638000, "SumXp": 20164330},
    {"Multiplier": 45, "TotalXp": 2967750, "SumXp": 23132080},
    {"Multiplier": 50, "TotalXp": 3297500, "SumXp": 26429580},
    {"Multiplier": 75, "TotalXp": 4946250, "SumXp": 31375830},
    {"Multiplier": 100, "TotalXp": 6595000, "SumXp": 37970830},
    {"Multiplier": 101, "TotalXp": 6660950, "SumXp": 44631780},
    {"Multiplier": 101, "TotalXp": 6660950, "SumXp": 51292730},
    {"Multiplier": 101, "TotalXp": 6660950, "SumXp": 57953680},
    {"Multiplier": 101, "TotalXp": 6660950, "SumXp": 64614630},
    {"Multiplier": 101, "TotalXp": 6660950, "SumXp": 71275580},
    {"Multiplier": 200, "TotalXp": 13190000, "SumXp": 84465580},
    {"Multiplier": 300, "TotalXp": 19785000, "SumXp": 104250580},
    {"Multiplier": 400, "TotalXp": 26380000, "SumXp": 130630580},
    {"Multiplier": 500, "TotalXp": 32975000, "SumXp": 163605580},
    {"Multiplier": 750, "TotalXp": 49462500, "SumXp": 213068080},
    {"Multiplier": 1000, "TotalXp": 65950000, "SumXp": 279018080},
    {"Multiplier": 1250, "TotalXp": 82437500, "SumXp": 361455580},
    {"Multiplier": 1500, "TotalXp": 98925000, "SumXp": 460380580},
    {"Multiplier": 1750, "TotalXp": 115412500, "SumXp": 575793080},
    {"Multiplier": 2000, "TotalXp": 131900000, "SumXp": 707693080},
    {"Multiplier": 3000, "TotalXp": 197850000, "SumXp": 905543080},
    {"Multiplier": 5000, "TotalXp": 329750000, "SumXp": 1235293080},
    {"Multiplier": 10000, "TotalXp": 659500000, "SumXp": 1894793080},
    {"Multiplier": 50000, "TotalXp": 3297500000, "SumXp": 5192293080},
    {"Multiplier": 100000, "TotalXp": 6595000000, "SumXp": 11787293080}
]

LEVEL_REQUIREMENTS = [
    15,
    30,
    50,
    75,
    125,
    300,
    600,
    800,
    900,
    1000,
    1200,
    1500,
    0
]

def getPitLevel(prestige, xp):
    if prestige > 0:
        xp = xp - PRESTIGE_MULTIPLIERS[prestige-1]['SumXp']
    else:
        xp = xp

    multiplier = PRESTIGE_MULTIPLIERS[prestige]['Multiplier']
    level = 0

    while xp > 0 and level < 120:
        levelXp = LEVEL_REQUIREMENTS[math.floor(level / 10)] * multiplier
        if (xp >= levelXp * 10):
            xp -= levelXp * 10
            level += 10
        else:
            gain = math.floor(xp / levelXp)
            level += gain
            xp -= gain * levelXp
            xp = 0
    return level

def getRomanNumeral(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12

    numeral = []

    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            numeral.append(sym[i])
            div -= 1
        i -= 1
    return ''.join(numeral)

def getFormattedPitLevel(prestige, level):
    prestigeColors = {
        0: lambda n, m: f"&7[&e{n}&7-{m}&7]",
        1: lambda n, m: f"&9[&e{n}&9-{m}&9]",
        5: lambda n, m: f"&e[&e{n}&e-{m}&e]",
        10: lambda n, m: f"&6[&e{n}&6-{m}&6]",
        15: lambda n, m: f"&c[&e{n}&c-{m}&c]",
        20: lambda n, m: f"&5[&e{n}&5-{m}&5]",
        25: lambda n, m: f"&d[&e{n}&d-{m}&d]",
        30: lambda n, m: f"&f[&e{n}&f-{m}&f]",
        35: lambda n, m: f"&b[&e{n}&b-{m}&b]",
        40: lambda n, m: f"&1[&e{n}&1-{m}&1]",
        45: lambda n, m: f"&0[&e{n}&0-{m}&0]",
        50: lambda n, m: f"&3[&e{n}&3-{m}&3]",
    }

    levelColors = {
        0: lambda n: f"&7{n}",
        10: lambda n: f"&9{n}",
        20: lambda n: f"&3{n}",
        30: lambda n: f"&4{n}",
        40: lambda n: f"&a{n}",
        50: lambda n: f"&e{n}",
        60: lambda n: f"&6{n}",
        70: lambda n: f"&c{n}",
        80: lambda n: f"&4{n}",
        90: lambda n: f"&5{n}",
        100: lambda n: f"&d{n}",
        110: lambda n: f"&f{n}",
        120: lambda n: f"&b{n}"
    }

    for req in levelColors:
        if req - level > 0:
            levelFormatted = list(levelColors.keys())[list(levelColors.keys()).index(req) - 1]
            break
    try:
        levelFormatted
    except:
        levelFormatted = 120

    for req in prestigeColors:
        if req - prestige > 0:
            prestigeFormatted = list(prestigeColors.keys())[list(prestigeColors.keys()).index(req) - 1]
            break
    try:
        prestigeFormatted
    except:
        prestigeFormatted = list(prestigeColors.keys())[-1]

    return prestigeColors[prestigeFormatted](getRomanNumeral(prestige), levelColors[levelFormatted](level))