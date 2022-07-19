import requests

from util.constants import KNOWN_MANUALS

class DManualSetup:
    """
    Determine if manual or automated setup is needed
    """

    def __init__(self, gamemode, goal):
        self.gamemode = gamemode
        self.goal = goal

    def is_manual_needed(self):
        try:
            _ = requests.head('https://www.google.com/', timeout=2.2)
        except:
            try:
                _ = requests.head('https://www.google.com/', timeout=10.0)
            except:
                return 'timeout'

        if self.goal in KNOWN_MANUALS or isinstance(self.goal, list):
            return True

        return False