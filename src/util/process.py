from util.gamemodes.hypixel.leveling import getExactLevel
from util.gamemodes.bedwars.bwlevel import getBedWarsLevel, getFormattedBedWarsLevel
from util.gamemodes.woolwars.wwlevel import getWoolWarsLevel, getFormattedWoolWarsLevel
from util.gamemodes.skywars.swlevel import getSkyWarsLevel, getFormattedSkyWarsLevel
from util.gamemodes.speeduhc.speedlevel import getSpeedUhcLevel, getFormattedSpeedUhcLevel
from util.gamemodes.uhc.uhclevel import getUhcLevel, getFormattedUhcLevel
from util.gamemodes.pit.pitlevel import getPitLevel, getFormattedPitLevel
from util.constants import COLOUR_CODES, summarise

import re
import math

def processManuals(goal, gamemode, api):
    if goal == "networkExp":
        player = api.player_stats
        xp = int(player[goal])
        return xp

    elif goal == "networkExpp": # network level
        player = api.player_stats
        xp = int(player["networkExp"])
        return round(getExactLevel(xp), 2)

    elif goal == "quests":
        quests = api.player_stats['quests']
        quests_completed = []
        for quest in quests:
            try:
                quests_completed.append(len(quests[quest]['completions']))
            except:
                pass
        return sum(quests_completed)

    elif goal == "general_challenger":
        return api.player_stats['achievements']['general_challenger']

    elif goal == "records":
        return len(api.friend_stats)

    elif goal == "prestiges":
        return len(api.player_stats['stats']['Pit']['profile']['prestiges'])

    elif goal == "Experience": # bedwars level
        player = api.player_stats['stats']['Bedwars']
        xp = int(player[goal])
        return math.floor(getBedWarsLevel(xp))

    elif goal == "woolwars_level": # woolwars level
        xp = api.player_stats['stats']['WoolGames']['progression']['experience']
        return math.floor(getWoolWarsLevel(xp))

    elif goal == "levelFormatted": # skywars level
        exp = api.player_stats['stats']['SkyWars']['skywars_experience']
        level = getSkyWarsLevel(exp)
        return level

    elif goal == "speeduhc_level": # speeduhc level
        score = api.player_stats['stats']['SpeedUHC']['score']
        level = getSpeedUhcLevel(score)
        return level

    elif goal == "uhc_level": # uhc level
        score = api.player_stats['stats']['UHC']['score']
        level = getUhcLevel(score)
        return level

    elif goal == "winsArcade":
        player = api.player_stats['stats']['Arcade']
        wins = [
            'wins_simon_says', 'wins_party', 'hider_wins_hide_and_seek', 'seeker_wins_hide_and_seek',
            'wins_mini_walls', 'wins_soccer', 'wins_ender', 'sw_game_wins', 'wins_farm_hunt', 'wins_dayone', 'wins_hole_in_the_wall',
            'wins_zombies', 'wins_oneinthequiver', 'wins_dragonwars2', 'wins_draw_their_thing', 'wins_throw_out', 'wins_easter_simulator',
            'wins_grinch_simulator_v2', 'wins_halloween_simulator', 'wins_scuba_simulator'
        ]
        win_count = []
        for win in wins:
            win_count.append(int(player[win]) if win in player else 0)
        return sum(win_count)

    elif isinstance(goal, list):
        player = api.player_stats['stats'][gamemode]
        add = summarise(*goal)
        return add.result(player)

    elif goal == "killsQuake":
        player = api.player_stats['stats']['Quake']
        solo_kills = player['kills']
        team_kills = player['kills_teams']
        return solo_kills + team_kills

    elif goal in ['fortune', 'superluck', 'endurance', 'transfusion', 'godfather', 'headstart', 'adrenaline']:
        player = api.player_stats['stats']['Paintball']
        return player[goal]+1

    elif goal == "pit_level":
        try: prestige = len(api.player_stats['stats']['Pit']['profile']['prestiges'])
        except: prestige = 0
        return getPitLevel(prestige, api.player_stats['stats']['Pit']['profile']['xp'])

    else:
        return 0

def processProgress(data, progress_design=False):
    if data['goal_amount'] == 'infinite':
        outOf = [data['mid_amount'], '∞']
    else:
        if data['milestone']:
            outOf = [data['current_amount'], data['goal_amount']]
        else:
            outOf = [data['mid_amount'], data['goal_amount']]

    prettier_goals = [
        "woolwars_level", "Experience", "levelFormatted", "smashLevel", "speeduhc_level", "uhc_level", "pit_level"
    ]

    if data['api_goal_name'] in prettier_goals and not progress_design:
        if data['api_goal_name'] == "Experience":
            formatted = getFormattedBedWarsLevel
        elif data['api_goal_name'] == "woolwars_level":
            formatted = getFormattedWoolWarsLevel
        elif data['api_goal_name'] == "levelFormatted":
            formatted = lambda k: getFormattedSkyWarsLevel(k, data['skywars_star'])
        elif data['api_goal_name'] == "smashLevel":
            formatted = lambda k: f"&b{k}&6✶"
        elif data['api_goal_name'] == "speeduhc_level":
            formatted = getFormattedSpeedUhcLevel
        elif data['api_goal_name'] == "uhc_level":
            formatted = getFormattedUhcLevel
        elif data['api_goal_name'] == "pit_level":
            formatted = lambda k: getFormattedPitLevel(data['pit_prestige'], k)

        if outOf[0] > outOf[1]:
            if data['milestone']:
                data['current_amount'] = data['goal_amount']
            else:
                data['mid_amount'] = data['goal_amount']
            outOf[0] = outOf[1]
        outOf[0] = computeHtml(formatted(outOf[0]))
        if outOf[1] != '∞':
            outOf[1] = computeHtml(formatted(outOf[1]))
    else:
        if outOf[1] != '∞':
            if outOf[0] > outOf[1]:
                if data['milestone']:
                    data['current_amount'] = data['goal_amount']
                else:
                    data['mid_amount'] = data['goal_amount']
                outOf[0] = outOf[1]
            outOf[1] = f"{outOf[1]:,}"
        outOf[0] = f"{outOf[0]:,}"


    return ' / '.join(outOf)

def computeHtml(text):
    colors = re.findall('&.', text)
    if len(colors) == 0:
        return text

    res = re.split('&.', text)

    for index, section in enumerate(res.copy()[:-1]):
        res[index] += f"<span style=\"color: rgb{COLOUR_CODES[colors[index]]}; font-size: 12pt\">"
        res[index+1] = res[index+1]+"</span>"

    return ''.join(res)