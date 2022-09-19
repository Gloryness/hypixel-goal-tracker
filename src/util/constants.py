class summarise:
    def __init__(self, *args):
        self.args = list(args)

    def result(self, player):
        if -1 != self.args[-1]:
            arr = []
            for arg in self.args:
                arr.append(0 if arg not in player else player[arg])
            return sum(arr)
        else:
            arr = []
            for arg in self.args[:-1]:
                arr.append("0" if arg not in player else f"{player[arg]}")
            return eval('-'.join(arr))

def add(*args):
    return [*args]

def sub(*args):
    return [*args, -1]

KNOWN_MANUALS = [
    "networkExp",
    "networkExpp",
    "quests",
    "records",
    "prestiges",
    "woolwars_level",
    "speeduhc_level",
    "uhc_level",
    "pit_level",
    "Experience",
    "levelFormatted",
    "winsArcade",
    "fortune",
    "superluck",
    "endurance",
    "transfusion",
    "godfather",
    "headstart",
    "adrenaline",
    "general_challenger",
    add
]

COLOUR_CODES = {
    "&0": (0, 0, 0),
    "&1": (0, 0, 170),
    "&2": (0, 170, 0),
    "&3": (0, 170, 170),
    "&4": (170, 0, 0),
    "&5": (170, 0, 170),
    "&6": (255, 170, 0),
    "&7": (170, 170, 170),
    "&8": (85, 85, 85),
    "&9": (85, 85, 255),
    "&a": (85, 255, 85),
    "&b": (85, 255, 255),
    "&c": (255, 85, 85),
    "&d": (255, 85, 255),
    "&e": (255, 255, 85),
    "&f": (255, 255, 255),
}

hypixel = [
    {
        'Hypixel Level': 'networkExpp',
        'Network EXP': 'networkExp',
        'Karma': 'karma',
        'Achievement Points': 'achievementPoints',
        'Quests Completed': 'quests',
        'Challenges Completed': 'general_challenger'
    },
    {
        'Friends': 'records',
        'Total Daily Rewards Claimed': 'totalDailyRewards',
        'Daily Reward Streak': 'rewardStreak',
        'Daily Reward Best Streak': 'rewardHighScore'
    }
]

arcade = [
    {
        'Coins': 'coins',
        'Wins': 'winsArcade',
        'Hypixel Says Wins': add('wins_simon_says', 'wins_santa_says'),
        'Hypixel Says Points': add('rounds_simon_says', 'rounds_santa_says'),
        'Hypixel Says Round Wins': add('round_wins_simon_says', 'round_wins_santa_says'),
        'Hypixel Says Top Score': 'top_score_simon_says'
    },
    {
        'Seasonal Wins': add('wins_easter_simulator', 'wins_grinch_simulator_v2', 'wins_halloween_simulator', 'wins_scuba_simulator'),
        'Easter Simulator Wins': 'wins_easter_simulator',
        'Grinch Simulator Wins': 'wins_grinch_simulator_v2',
        'Halloween Simulator Wins': 'wins_halloween_simulator',
        'Scuba Simulator Wins': 'wins_scuba_simulator'
    },
    {
        'Mini Walls Wins': 'wins_mini_walls',
        'Mini Walls Kills': 'kills_mini_walls',
        'Mini Walls Final Kills': 'final_kills_mini_walls',
        'Football Wins': 'wins_soccer',
        'Football Goals': 'goals_soccer'
    },
    {
        'Party Game Wins': 'wins_party',
        'Hole In The Wall Wins': 'wins_hole_in_the_wall',
        'Hole In The Wall Rounds Played': 'rounds_hole_in_the_wall',
        'Hole In The Wall Best Qualification Score': 'hitw_record_q',
        'Hole In The Wall Best Finals Score': 'hitw_record_f'
    },
    {
        'Hide And Seek Wins': add('hider_wins_hide_and_seek', 'seeker_wins_hide_and_seek'),
        'Hide And Seek Hider Wins': 'hider_wins_hide_and_seek',
        'Hide And Seek Seeker Wins': 'seeker_wins_hide_and_seek'
    },
    {
        'Pixel Painter Wins': 'wins_draw_their_thing',
        'Throw Out Wins': 'wins_throw_out',
        'Throw Out Kills': 'kills_throw_out',
        'Galaxy Wars Wins': 'sw_game_wins',
        'Galaxy Wars Kills': 'sw_kills'
    },
    {
        'Farm Hunt Wins': 'wins_farm_hunt',
        'Farm Hunt Poop Collected': 'poop_collected',
        'Ender Spleef Wins': 'wins_ender',
        'Dragon Wars Wins': 'wins_dragonwars2',
        'Dragon Wars Kills': 'kills_dragonwars2'
    },
    {
        'Bounty Hunter Wins': 'wins_oneinthequiver',
        'Bounty Hunter Kills': 'kills_oneinthequiver',
        'Blocking Dead Wins': 'wins_dayone',
        'Blocking Dead Kills': 'kills_dayone',
        'Blocking Dead Headshots': 'headshots_dayone'
    },
    {
        'Zombies Wins': 'wins_zombies',
        'Zombies Rounds Survived': 'total_rounds_survived_zombies',
        'Zombies Best Round': 'best_round_zombies',
        'Zombies Zombie Kills': 'zombie_kills_zombies',
        'Zombies Players Revived': 'players_revived_zombies'
    }
]

arena = [
    {
        'Coins': 'coins',
        'Keys': 'keys',
        'Wins': 'wins'
    },
    {
        '1v1 Kills': 'kills_1v1',
        '1v1 Wins': 'wins_1v1'
    },
    {
        '2v2 Kills': 'kills_2v2',
        '2v2 Wins': 'wins_2v2'
    },
    {
        '4v4 Kills': 'kills_4v4',
        '4v4 Wins': 'wins_4v4'
    }
]

bedwars = [
    {
        'Coins': 'coins',
        'Level': 'Experience',
        'Wins': 'wins_bedwars',
        'Winstreak': 'winstreak',
        'Gamed Played': 'games_played_bedwars'
    },
    {
        'Kills': 'kills_bedwars',
        'Void Kills': 'void_kills_bedwars',
        'Final Kills': 'final_kills_bedwars',
        'Beds Broken': 'beds_broken_bedwars'
    },
    {
        'Solo Kills': 'eight_one_kills_bedwars',
        'Solo Wins': 'eight_one_wins_bedwars',
        'Solo Winstreak': 'eight_one_winstreak',
        'Doubles Kills': 'eight_two_kills_bedwars',
        'Doubles Wins': 'eight_two_wins_bedwars',
        'Doubles Winstreak': 'eight_two_winstreak'
    },
    {
        '3v3v3v3 Kills': 'four_three_kills_bedwars',
        '3v3v3v3 Wins': 'four_three_wins_bedwars',
        '3v3v3v3 Winstreak': 'four_three_winstreak',
        '4v4v4v4 Kills': 'four_four_kills_bedwars',
        '4v4v4v4 Wins': 'four_four_wins_bedwars',
        '4v4v4v4 Winstreak': 'four_four_winstreak'
    },
    {
        '4v4 Kills': 'two_four_kills_bedwars',
        '4v4 Wins': 'two_four_wins_bedwars',
        '4v4 Winstreak': 'two_four_winstreak',
        'Lucky Block 4v4v4v4 Wins': 'four_four_lucky_wins_bedwars',
        'Lucky Block 4v4v4v4 Winstreak': 'four_four_lucky_winstreak',
        'Castle Kills': 'castle_kills_bedwars',
        'Castle Wins': 'castle_wins_bedwars',
        'Castle Winstreak': 'castle_winstreak'
    },
    {
        'Ultime Solo Wins': 'eight_one_ultimate_wins_bedwars',
        'Ultime Solo Winstreak': 'eight_one_ultimate_winstreak',
        'Ultimate Doubles Wins': 'eight_two_ultimate_wins_bedwars',
        'Ultimate Doubles Winstreak': 'eight_two_ultimate_winstreak',
        'Ultimate 4v4v4v4 Wins': 'four_four_ultimate_wins_bedwars',
        'Ultimate 4v4v4v4 Winstreak': 'four_four_ultimate_winstreak'
    }
]

buildbattle = [
    {
        'Coins': 'coins',
        'Score': 'score',
        'Games Played': 'games_played',
        'Total Votes': 'total_votes',
        'Correct Guesses': 'correct_guesses'
    },
    {
        'Wins': 'wins',
        'Wins Solo': 'wins_solo_normal',
        'Wins Teams': 'wins_teams_normal',
        'Wins Pro': 'wins_solo_pro',
        'Wins Guess The Build': 'wins_guess_the_build'
    }
]

mcgo = [
    {
        'Coins': 'coins',
        'Kills': 'kills',
        'Shots Fired': 'shots_fired',
        'Headshot Kills': 'headshot_kills',
        'Bombs Planted': 'bombs_planted',
        'Bombs Defused': 'bombs_defused'
    },
    {
        'Game Wins': 'game_wins',
        'Round Wins': 'round_wins',
        'Team Deathmatch Wins': 'game_wins_deathmatch',
        'Deathmatch Kills': 'kills_deathmatch',
        'Cop Kills': 'cop_kills',
        'Criminal Kills': 'criminal_kills',
    }
]

duels = [
    {
        'Coins': 'coins',
        'Games Played': 'games_played_duels',
        'Wins': 'wins',
        'Kills': 'kills',
        'Current Winstreak': 'current_winstreak',
        'Highest Winstreak': 'best_overall_winstreak'
    },
    {
        'Skywars 1v1 Wins': 'sw_duel_wins',
        'Skwyars 1v1 Current Winstreak': 'current_winstreak_mode_sw_duel',
        'Skywars 1v1 Highest Winstreak': 'best_winstreak_mode_sw_duel',
        'Skywars 2v2 Wins': 'sw_doubles_wins',
        'Skywars 2v2 Current Winstreak': 'current_winstreak_mode_sw_doubles',
        'Skywars 2v2 Highest Winstreak': 'best_winstreak_mode_sw_doubles'
    },
    {
        'UHC 1v1 Wins': 'uhc_duel_wins',
        'UHC 1v1 Current Winstreak': 'current_winstreak_mode_uhc_duel',
        'UHC 1v1 Highest Winstreak': 'best_winstreak_mode_uhc_duel',
        'UHC 2v2 Wins': 'uhc_doubles_wins',
        'UHC 2v2 Current Winstreak': 'current_winstreak_mode_uhc_doubles',
        'UHC 2v2 Highest Winstreak': 'best_winstreak_mode_uhc_doubles'
    },
    {
        'UHC 4v4 Wins': 'uhc_four_wins',
        'UHC 4v4 Current Winstreak': 'current_winstreak_mode_uhc_four',
        'UHC 4v4 Highest Winstreak': 'duels_winstreak_best_uhc_four',
        'UHC Deathmatch Wins': 'uhc_meetup_wins',
        'UHC Deathmatch Current Winstreak': 'current_winstreak_mode_uhc_meetup',
        'UHC Deathmatch Highest Winstreak': 'best_winstreak_mode_uhc_meetup'
    },
    {
        'OP 1v1 Wins': 'op_duel_wins',
        'OP 1v1 Current Winstreak': 'current_winstreak_mode_op_duel',
        'OP 1v1 Highest Winstreak': 'best_winstreak_mode_op_duel',
        'OP 2v2 Wins': 'op_doubles_wins',
        'OP 2v2 Current Winstreak': 'current_winstreak_mode_op_doubles',
        'OP 2v2 Highest Winstreak': 'best_winstreak_mode_op_doubles'
    },
    {
        'Bridge 1v1 Wins': 'bridge_duel_wins',
        'Bridge 1v1 Current Winstreak': 'current_winstreak_mode_bridge_duel',
        'Bridge 1v1 Highest Winstreak': 'best_winstreak_mode_bridge_duel',
        'Bridge 2v2 Wins': 'bridge_doubles_wins',
        'Bridge 2v2 Current Winstreak': 'current_winstreak_mode_bridge_doubles',
        'Bridge 2v2 Highest Winstreak': 'best_winstreak_mode_bridge_doubles'
    },
    {
        'Bridge 4v4 Wins': 'bridge_four_wins',
        'Bridge 4v4 Current Winstreak': 'current_winstreak_mode_bridge_four',
        'Bridge 4v4 Highest Winstreak': 'best_winstreak_mode_bridge_four',
        'Bridge 2v2v2 Wins': 'bridge_2v2v2v2_wins',
        'Bridge 2v2v2 Current Winstreak': 'current_winstreak_mode_bridge_2v2v2v2',
        'Bridge 2v2v2 Highest Winstreak': 'best_winstreak_mode_bridge_2v2v2v2'
    },
    {
        'Bridge 3v3v3 Wins': 'bridge_3v3v3v3_wins',
        'Bridge 3v3v3 Current Winstreak': 'current_winstreak_mode_bridge_3v3v3v3',
        'Bridge 3v3v3 Highest Winstreak': 'best_winstreak_mode_bridge_3v3v3v3',
        'Bridge Goals': 'goals',
        'Bow 1v1 Wins': 'bow_duel_wins',
        'Blitz 1v1 Wins': 'blitz_duel_wins'
    },
    {
        'Sumo 1v1 Wins': 'sumo_duel_wins',
        'Bow Spleef 1v1 Wins': 'bowspleef_duel_wins',
        'Classic 1v1 Wins': 'classic_duel_wins',
        'NoDebuff 1v1 Wins': 'potion_duel_wins',
        'Combo 1v1 Wins': 'combo_duel_wins'
    }
]

walls3 = [
    {
        'Coins': 'coins',
        'Mythic Favor': 'mythic_favor',
        'Games Played': 'games_played',
        'Wins': 'wins',
        'Kills': 'kills',
        'Assists': 'assists'
    },
    {
        'Final Kills': 'final_kills',
        'Final Assists': 'final_assists',
        'Damage Dealt': 'damage_dealt',
        'Blocks Placed': 'blocks_placed'
    }
]

murdermystery = [
    {
        'Coins': 'coins',
        'Games Played': 'games',
        'Kills': 'kills',
        'Bow Kills': 'bow_kills',
        'Knife Kills': 'knife_kills',
        'Trap Kills': 'trap_kills'
    },
    {
        'Wins': 'wins',
        'Kills as Murderer': 'kills_as_murderer',
        'Kills Classic': 'kills_MURDER_CLASSIC',
        'Kills Double Up': 'kills_MURDER_DOUBLE_UP',
        'Deaths': 'deaths'
    },
    {
        'Murderer Wins': 'murderer_wins',
        'Murderer Wins Classic': 'wins_MURDER_CLASSIC',
        'Murderer Wins Double Up': 'wins_MURDER_DOUBLE_UP'
    },
    {
        'Detective Wins': 'detective_wins',
        'Detective Wins Classic': 'detective_wins_MURDER_CLASSIC',
        'Detective Wins Double Up': 'detective_wins_MURDER_DOUBLE_UP'
    }
]

paintball = [
    {
        'Coins': 'coins',
        'Wins': 'wins',
        'Kills': 'kills',
        'Killstreaks': 'killstreaks',
        'Shots Fired': 'shots_fired'
    },
    {
        'Fortune Perk Level': 'fortune',
        'Superluck Perk Level': 'superluck',
        'Endurance Perk Level': 'endurance',
        'Transfusion Perk Level': 'transfusion'
    },
    {
        'Godfather Perk Level': 'godfather',
        'Headstart Perk Level': 'headstart',
        'Adrenaline Perk Level': 'adrenaline'
    }
]

pit = [
    {
        'Gold': 'cash',
        'Kills': 'kills',
        'Assists': 'assists',
        'Highest Streak': 'max_streak',
        'Left Clicks': 'left_clicks',
    },
    {
        'Sword Hits': 'sword_hits',
        'Arrow Hits': 'arrow_hits',
        'Contracts Started': 'contracts_started',
        'Contracts Completed': 'contracts_completed',
        'Golden Heads Eaten': 'ghead_eaten',
    },
    {
        'Jumps Into Pit': 'jumped_into_pit',
        'Chat Messages': 'chat_messages',
        'Damage Dealt': 'damage_dealt',
        'Damage Received': 'damage_received',
        'Ingots Picked Up': 'ingots_picked_up'
    },
    {
        'Playtime (Minutes)': 'playtime_minutes',
        'Enderchest opened': 'enderchest_opened',
        'Diamond Items Purchased': 'diamond_items_purchased',
        'Blocks Placed': 'blocks_placed',
        'Blocks Broken': 'blocks_broken',
        'Vampire Healed HP': 'vampire_healed_hp'
    },
    {
        'Rage Potatoes Eaten': 'rage_potatoes_eaten',
        'Wheat Farmed': 'wheat_farmed',
        'Fished Anything': 'fished_anything',
        'Fishes Fished': 'fishes_fished',
        'Rage Pants Crafted': 'rage_pants_crafted',
        'Launched by Launchers': 'launched_by_launchers'
    },
    {
        'Prestige': 'prestiges',
        'Level': 'pit_level',
        'Renown': 'renown',
        'XP': 'xp'
    }
]

quake = [
    {
        'Coins': 'coins',
        'Highest Killstreak': 'highest_killstreak',
        'Headshots': 'headshots',
        'Wins': add('wins', 'wins_team'),
        'Kills': add('kills', 'kills_team')
    },
    {
        'Solo Wins': 'wins',
        'Solo Kills': 'kills',
        'Team Wins': 'wins_teams',
        'Team Kills': 'kills_teams'
    },
    {
        'Killstreaks': add('killstreaks', 'killstreaks_teams'),
        'Solo Killstreaks': 'killstreaks',
        'Teams Killstreaks': 'killstreaks_teams'
    }
]

hungergames = [
    {
        'Coins': 'coins',
        'Games Played': 'games_played',
        'Chests Opened': 'chests_opened',
    },
    {
        'Kills': 'kills',
        'Kills Solo': sub('kills', 'kills_teams_normal'),
        'Kills Teams': 'kills_teams_normal'
    },
    {
        'Wins': add('wins_solo_normal', 'wins_teams_normal'),
        'Wins Solo': 'wins_solo_normal',
        'Wins Teams': 'wins_teams_normal'
    }
]

skywars = [
    {
        'Coins': 'coins',
        'Level': 'levelFormatted',
        'Experience': 'skywars_experience',
        'Souls': 'souls',
        'Heads': 'heads',
    },
    {
        'Shards': 'shard',
        'Opals': 'opals',
        'Games Played': 'games_played_skywars',
        'Kills': 'kills'
    },
    {
        'Void Kills': 'void_kills',
        'Solo Kills': 'kills_solo',
        'Solo Normal Kills': 'kills_solo_normal',
        'Solo Insane Kills': 'kills_solo_insane',
        'Team Kills': 'kills_team',
        'Team Normal Kills': 'kills_team_normal'
    },
    {
        'Team Insane Kills': 'kills_team_insane',
        'Wins': 'wins',
        'Solo Wins': 'wins_solo',
        'Solo Normal Wins': 'wins_solo_normal',
        'Solo Insane Wins': 'wins_solo_insane'
    },
    {
        'Team Wins': 'wins_team',
        'Team Normal Wins': 'wins_team_normal',
        'Team Insane Wins': 'wins_team_insane',
        'Ranked Wins': 'wins_ranked_normal',
        'Ranked Kills': 'kills_ranked_normal'
    },
    {
        'Mega Kills': 'kills_mega',
        'Mega Wins': 'wins_mega',
        'Laboratory Kills': 'kills_lab',
        'Laboratory Wins': 'wins_lab'
    }
]

supersmash = [
    {
        'Coins': 'coins',
        'Smash Level': 'smashLevel',
        'Kills': 'kills',
        'Solo Kills': 'kills_normal',
        'Double Kills': 'kills_2v2',
        'Team Kills': 'kills_teams'
    },
    {
        'Games Played': 'games',
        'Damage Dealt': 'damage_dealt',
        'Losses': 'losses',
        'Deaths': 'deaths',
        'Quits': 'quits'
    },
    {
        'Wins': 'wins',
        'Solo Wins': 'wins_normal',
        'Double Wins': 'wins_2v2',
        'Team Wins': 'wins_teams'
    }
]

speeduhc = [
    {
        'Coins': 'coins',
        'Level': 'speeduhc_level',
        'Score': 'score',
        'Highest Killstreak': 'highestKillstreak',
        'Survived Players': 'survived_players',
    },
    {
        'Kills': 'kills',
        'Kills Solo': 'kills_solo',
        'Kills Team': 'kills_team',
        'Wins': 'wins',
        'Wins Solo': 'wins_solo',
        'Wins Team': 'wins_team'
    }
]

tntgames = [
    {
        'Coins': 'coins',
        'Winstreak': 'winstreak',
        'Wins': 'wins',
        'TNT Run Wins': 'wins_tntrun',
        'PVP Run Wins': 'wins_pvprun',
        'PVP Run Kills': 'kills_pvprun'
    },
    {
        'Bow Spleef Wins': 'wins_bowspleef',
        'Bow Spleef Shots Fired': 'tags_bowspleef',
        'TNT Tag Wins': 'wins_tntag',
        'TNT Tag Kills': 'kills_tntag',
    },
    {
        'TNT Wizards Wins': 'wins_capture',
        'TNT Wizards Kills': 'kills_capture',
        'TNT Wizards Assists': 'assists_capture'
    }
]

gingerbread = [
    {
        'Coins': 'coins',
        'Coins Picked Up': 'coins_picked_up',
        'Box Pickups': 'box_pickups',
        'Laps Completed': 'laps_completed'
    },
    {
        'Total Trophies': 'wins',
        'Gold Trophies': 'gold_trophy',
        'Silver Trophies': 'silver_trophy',
        'Bronze Trophies': 'bronze_trophy'
    }
]

uhc = [
    {
        'Coins': 'coins',
        'Score': 'score',
        'Level': 'uhc_level',
        'Heads Eaten': add('heads_eaten_solo', 'heads_eaten'),
        'Heads Eaten Solo': 'heads_eaten_solo',
        'Heads Eaten Teams': 'heads_eaten',
    },
    {
        'Kills': add('kills_solo', 'kills'),
        'Kills Solo': 'kills_solo',
        'Kills Teams': 'kills',
        'Wins': add('wins_solo', 'wins'),
        'Wins Solo': 'wins_solo',
        'Wins Teams': 'wins'
    },
    {
        'Ultimates Crafted': add('ultimates_crafted_solo', 'ultimates_crafted'),
        'Ultimates Crafted Solo': 'ultimates_crafted_solo',
        'Ultimates Crafted Teams': 'ultimates_crafted',
        'Extra Ultimates': add('extra_ultimates_crafted_solo', 'extra_ultimates_crafted'),
        'Extra Ultimates Solo': 'extra_ultimates_crafted_solo',
        'Extra Ultimates Teams': 'extra_ultimates_crafted',

    }
]

vampirez = [
    {
        'Coins': 'coins',
        'Most Vampires Killed': 'most_vampire_kills_new',
        'Vampire Kills': 'vampire_kills',
        'Zombie Kills': 'zombie_kills',
        'Human Kills': 'human_kills'
    },
    {
        'Wins': add('human_wins', 'vampire_wins'),
        'Human Wins': 'human_wins',
        'Vampire Wins': 'vampire_wins'
    }
]

walls = [
    {
        'Coins': 'coins',
        'Wins': 'wins',
        'Kills': 'kills',
        'Assists': 'assists',
        'Deaths': 'deaths',
        'Losses': 'losses'
    }
]

battleground = [
    {
        'Coins': 'coins',
        'Kills': 'kills',
        'Assists': 'assists',
        'Wins': 'wins',
        'Wins CTF': 'wins_capturetheflag'
    },
    {
        'Wins Domination': 'wins_domination',
        'Wins Team Deathmatch': 'wins_teamdeathmatch',
        'Flags Captured': 'flag_conquer_self',
        'Flags Returned': 'flag_returns'
    }
]

woolgames = [
    {
        'Coins': 'coins',
        'Level': 'woolwars_level',
        'Wins': 'wins',
        'Kills': 'kills',
        'Assists': 'assists',
    },
    {
        'Games Played': 'games_played',
        'Blocks Broken': 'blocks_broken',
        'Wool Placed': 'wool_placed',
        'Powerups': 'powerups_gotten',
        'Layers': 'available_layers'
    }
]