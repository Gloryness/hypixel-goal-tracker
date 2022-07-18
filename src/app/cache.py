import os
import json

class Cache:
    def __init__(self, folder, filename):
        self.folder = os.path.abspath(folder)
        self.filename = self.folder + f'\\{filename}'

        self.layout = {
            "goals": [],
            "completed_goals": [],
            "goal_organiser": {
                "api_gamemode_name": "Hypixel",
                "gamemode": "Hypixel",
                "api_goal_name": "quests",
                "goal": "Quests Completed",
                "milestone": 1,
                "sort_by": "Name"
            },
            "milestone": False
        }

        if not os.path.exists(self.folder): # making sure all the folders exist to avoid errors
            os.makedirs(self.folder)

        if not os.path.isfile(self.filename):
            with open(self.filename, 'w') as f:
                json.dump(self.layout, f, indent=3)

    def _test_if_empty(self):
        try:
            with open(self.filename) as f:
                json.load(f)
        except: # If the file is 0 bytes or there is a syntax error in the .json file
            with open(self.filename, 'w') as f:
                json.dump(self.layout, f, indent=3)
            return True
        return False

    def cached(self, key):
        """
        Check if the question has already been stored.
        """
        empty = self._test_if_empty()
        if empty: return False

        with open(self.filename) as f:
            data = json.load(f)
        if key in data.keys():
            return True
        return False

    def store(self, dictionary):
        """
        Add to the database.
        """
        empty = self._test_if_empty()
        if empty: return {}

        with open(self.filename) as f:
            data = json.load(f)

        data.update(dictionary)

        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=3)

    def get(self, key, *keys):
        """
        Retrieve values in the database.
        :param key: A required key to get from the database
        :param keys: Optional other keys to get stacking up from the first key
        For example: get('1', '2', 3) is equal to data['1']['2'][3]
        """
        keys = list(keys)
        keys.insert(0, key)
        with open(self.filename) as f:
            data = json.load(f)
        if not self.cached(key):
            return ""
        evalulated = 'data' + ''.join([f'[{ascii(keyy) if type(keyy) == str else keyy}]' for keyy in keys])
        return eval(evalulated)

    def all(self):
        empty = self._test_if_empty()
        if empty: return {}

        with open(self.filename) as f:
            data = json.load(f)

        return data

    def clear(self):
        empty = self._test_if_empty()
        if empty: return {}

        with open(self.filename) as f:
            json.dump(self.layout, f, indent=3)