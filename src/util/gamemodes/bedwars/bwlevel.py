## A rewrite of https://github.com/Statsify/statsify/blob/main/packages/schemas/src/player/gamemodes/bedwars/util.ts but in Python.

import math

def getExpReq(level):
    progress = level % 100
    if progress > 3:
        return 5000

    levels = {
        0: 500,
        1: 1000,
        2: 2000,
        3: 3500
    }

    return levels[progress]

def getBedWarsLevel(exp):
    prestiges = math.floor(exp / 487_000)
    level = prestiges * 100
    remainingExp = exp - prestiges * 487_000

    for i in range(4):
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

def getFormattedBedWarsLevel(level):
    star = math.floor(level)

    prestigeColors = [
        {"req": 0, "format": lambda n: f"&7[{n}✫]"},
        {"req": 100, "format": lambda n: f"&f[{n}✫]"},
        {"req": 200, "format": lambda n: f"&6[{n}✫]"},
        {"req": 300, "format": lambda n: f"&b[{n}✫]"},
        {"req": 400, "format": lambda n: f"&2[{n}✫]"},
        {"req": 500, "format": lambda n: f"&3[{n}✫]"},
        {"req": 600, "format": lambda n: f"&4[{n}✫]"},
        {"req": 700, "format": lambda n: f"&d[{n}✫]"},
        {"req": 800, "format": lambda n: f"&9[{n}✫]"},
        {"req": 900, "format": lambda n: f"&5[{n}✫]"},
        {"req": 1000, "format": lambda n: f"&c[&6{n[0]}&e{n[1]}&a{n[2]}&b{n[3]}&d✫&5]"},
        {"req": 1100, "format": lambda n: f"&7[&f{n}&7✪]"},
        {"req": 1200, "format": lambda n: f"&7[&e{n}&6✪&7]"},
        {"req": 1300, "format": lambda n: f"&7[&b{n}&3✪&7]"},
        {"req": 1400, "format": lambda n: f"&7[&a{n}&2✪&7]"},
        {"req": 1500, "format": lambda n: f"&7[&3{n}&9✪&7]"},
        {"req": 1600, "format": lambda n: f"&7[&c{n}&4✪&7]"},
        {"req": 1700, "format": lambda n: f"&7[&d{n}&5✪&7]"},
        {"req": 1800, "format": lambda n: f"&7[&9{n}&1✪&7]"},
        {"req": 1900, "format": lambda n: f"&7[&5{n}&8✪&7]"},
        {"req": 2000, "format": lambda n: f"&8[&7{n[0]}&f{n[1]}{n[2]}&7{n[3]}&8✪]"},
        {"req": 2100, "format": lambda n: f"&f[{n[0]}&e{n[1]}{n[2]}&6{n[3]}⚝&6]"},
        {"req": 2200, "format": lambda n: f"&6[{n[0]}&f{n[1]}{n[2]}&b{n[3]}&3⚝&3]"},
        {"req": 2300, "format": lambda n: f"&5[{n[0]}&d{n[1]}{n[2]}&6{n[3]}&e⚝&e]"},
        {"req": 2400, "format": lambda n: f"&b[{n[0]}&f{n[1]}{n[2]}&7{n[3]}⚝&8]"},
        {"req": 2500, "format": lambda n: f"&f[{n[0]}&a{n[1]}{n[2]}&2{n[3]}⚝&2]"},
        {"req": 2600, "format": lambda n: f"&4[{n[0]}&c{n[1]}{n[2]}&d{n[3]}⚝&d]"},
        {"req": 2700, "format": lambda n: f"&e[{n[0]}&f{n[1]}{n[2]}&8{n[3]}⚝&8]"},
        {"req": 2800, "format": lambda n: f"&a[{n[0]}&2{n[1]}{n[2]}&6{n[3]}⚝&e]"},
        {"req": 2900, "format": lambda n: f"&b[{n[0]}&3{n[1]}{n[2]}&9{n[3]}⚝&1]"},
        {"req": 3000, "format": lambda n: f"&e[{n[0]}&6{n[1]}{n[2]}&c{n[3]}⚝&4]"},
    ]

    return applyFormat(prestigeColors, star)