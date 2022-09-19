import threading
import time
import os

from app.cache import Cache
from util.goalmanager import GoalManager
from util.api import API

class ThreadManager:
    def __init__(self, info, mainwindow):
        self.goals = info
        self.end_cache = False
        self.managers = {}
        cache = Cache(f'{os.environ["USERPROFILE"]}/AppData/Local/hypixel-goal-tracker', 'data.json')
        self.api = API(uuid=cache.get('uuid'), api_key=cache.get('api-key'))
        self.api_sync = mainwindow.api_sync
        self.main = mainwindow

    def load(self, data):
        if len(self.managers) == 0:
            self.api_sync.start_session_sync()
        self.managers[data['index']] = GoalManager(self.goals, self.main.clock_sync)
        manager = self.managers[data['index']]
        self.load_thread = threading.Thread(target=lambda: manager.begin_process(data))
        self.load_thread.start()

    def manage(self, data):
        manager = self.managers[data['index']]
        self.manage_thread = threading.Thread(target=lambda: manager.manage_process(data, self.main))
        self.manage_thread.start()

    def cache(self, goals, completed_goals, goal_organiser):
        self.cache_thread = threading.Thread(target=lambda: self.cache_processes(goals, completed_goals, goal_organiser))
        self.cache_thread.start()

    def delete(self, index, temp=False):
        manager = self.managers[index]
        manager.deleted = True
        self.managers.pop(index)

        if not temp:
            if len(self.managers) == 0: # End if all goals have been deleted
                self.api_sync.end_session()

    def cache_processes(self, goals, completed_goals, goal_organiser):
        cache = Cache(f'{os.environ["USERPROFILE"]}/AppData/Local/hypixel-goal-tracker', 'data.json')
        while True:
            if self.end_cache:
                break

            if self.main.inside_settings:
                time.sleep(1.0)
                continue

            if not cache.cached('uuid'):
                time.sleep(2)
                continue

            cache.store({'goals': goals, 'completed_goals': completed_goals, 'goal_organiser': goal_organiser})

            self.main.clock_sync.wait_for_sync()

    def sync(self):
        self.load_thread.join(0)
        self.manage_thread.join(0)