## A rewrite of https://github.com/Statsify/statsify/blob/main/packages/schemas/src/player/gamemodes/skywars/util.ts but in Python.

import math

def getSkyWarsLevel(xp):
    totalXp = [0, 2, 7, 15, 25, 50, 100, 200, 350, 600, 1000, 1500]
    if xp >= 15_000:
        return math.floor((xp - 15_000) / 10_000 + 12)

    for x in totalXp:
        if x * 10 - xp > 0:
            return totalXp.index(x)

def getSkyWarsExp(lvl):
    totalXp = [0, 2, 7, 15, 25, 50, 100, 200, 350, 600, 1000, 1500]
    if lvl >= 12:
        return 15_000 + (10_000 * (lvl - 12))

    return totalXp[lvl - 1] * 10

def applyFormat(prestigeColors, level, star):
    rounded = int(math.floor(level / 5.0)) * 5
    for index, prestige in enumerate(prestigeColors):
        if rounded >= prestige['req'] and (rounded < prestigeColors[index+1]['req'] if index+1 != len(prestigeColors) else True):
            return prestige['format'](str(level), star)
    return prestigeColors[-1]['format'](str(level), star)

def getFormattedSkyWarsLevel(level, star):
    level = math.floor(level)

    prestigeColors = [
        {"req": 0, "format": lambda n, m: f"&7[{n}{m}]"},
        {"req": 5, "format": lambda n, m: f"&f[{n}{m}]"},
        {"req": 10, "format": lambda n, m: f"&6[{n}{m}]"},
        {"req": 15, "format": lambda n, m: f"&b[{n}{m}]"},
        {"req": 20, "format": lambda n, m: f"&2[{n}{m}]"},
        {"req": 25, "format": lambda n, m: f"&3[{n}{m}]"},
        {"req": 30, "format": lambda n, m: f"&4[{n}{m}]"},
        {"req": 35, "format": lambda n, m: f"&d[{n}{m}]"},
        {"req": 40, "format": lambda n, m: f"&9[{n}{m}]"},
        {"req": 45, "format": lambda n, m: f"&5[{n}{m}]"},
        {"req": 50, "format": lambda n, m: f"&c[&6{n[0]}&e{n[1]}&b{m[0]}&a{m[1]}&d{m[2]}&5]" if len(m) == 3 else f"&c[&6{n[0]}&e{n[1]}&b{m}&a]"},
        {"req": 100, "format": lambda n, m: f"&c[&6{n[0]}&e{n[1]}&a{n[2]}&b{m[0]}&d{m[1]}&5{m[2]}&c]" if len(m) == 3 else f"&c[&6{n[0]}&e{n[1]}&a{n[2]}&b{m}&d]"},
    ]

    return applyFormat(prestigeColors, level, star)