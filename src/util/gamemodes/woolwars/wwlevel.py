## A rewrite of https://github.com/Statsify/statsify/blob/main/packages/schemas/src/player/gamemodes/woolwars/util.ts but in Python.

import math

def getExpReq(level):
    progress = level % 100
    if progress > 4:
        return 5000

    levels = [5000 if level >= 100 else 0, 1000, 2000, 3000, 4000]

    return levels[progress]

def getWoolWarsLevel(exp):
    prestiges = math.floor(exp / 490_000)
    level = prestiges * 100
    remainingExp = exp - prestiges * 490_000

    for i in range(5):
        expForNextLevel = getExpReq(i)
        if remainingExp < expForNextLevel:
            break
        level += 1
        remainingExp -= expForNextLevel

    return level + remainingExp / getExpReq(level + 1)

def applyFormat(prestigeColors, star):
    rounded = int(math.floor(star / 100.0)) * 100
    for prestige in prestigeColors:
        if prestige['req'] == rounded:
            return prestige['format'](str(star))
    return prestigeColors[-1]['format'](str(star))

def getFormattedWoolWarsLevel(level):
    star = math.floor(level)

    prestigeColors = [
        {"req": 0, "format": lambda n: f"&7[{n}✫]"},
        {"req": 100, "format": lambda n: f"&f[{n}✫]"},
        {"req": 200, "format": lambda n: f"&c[{n}✫]"},
        {"req": 300, "format": lambda n: f"&6[{n}✫]"},
        {"req": 400, "format": lambda n: f"&9[{n}✫]"}
    ]

    return applyFormat(prestigeColors, star)