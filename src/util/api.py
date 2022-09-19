import requests
import time
import math
import re
import threading

from PyQt5.QtCore import QObject

class API(QObject):
    """
    Handles sending requests to the Hypixel API and retreiving the data.
    """
    def __init__(self, uuid, api_key, parent=None):
        super().__init__(parent)
        self.uuid = uuid
        self.api_key = api_key

    def getPlayerStats(self):
        return requests.get(f'https://api.hypixel.net/player?uuid={self.uuid}&key={self.api_key}').json()['player']

    def getFriends(self):
        return requests.get(f'https://api.hypixel.net/friends?uuid={self.uuid}&key={self.api_key}').json()['records']

class APISync:
    """
    Used to store data from requests and update it every second (peforms in a seperate thread)
    This was made to avoid sending a unique request for each goal otherwise it would of exceeded the key throttle limit.
    """
    def __init__(self, api, goals, statistics, request_wait=1.50, request_step=0.05):
        self.api = api
        self.goals = goals
        self.statistics = statistics[0]
        self.realtime = statistics[1]
        self.request_wait = request_wait
        self.request_step = request_step
        self.syncing = False # Controls whether the session is active or not.
        self.player_stats = {}
        self.friend_stats = {}

        self.endpoints = {
            "player": False,
            "friends": False
        }

    def player_endpoint(self, limit=False, friends_req=False):
        return (limit and not friends_req) or any(list(map(lambda k: k['api_goal_name'] != "records", self.goals))) and not all(list(map(lambda k: k['status'] in ['PAUSED', 'COMPLETE'], self.goals)))

    def friends_endpoint(self, limit=False, friends_req=False):
        # any goal that contains the friends api goal name AND that every goal doesnt contain 'PAUSED' or 'COMPLETE'
        if limit and not friends_req:
            return False
        return friends_req or any(list(map(lambda k: k['api_goal_name'] == "records", self.goals))) and not all(list(map(lambda k: k['status'] in ['PAUSED', 'COMPLETE'], self.goals)))

    def start_session_sync(self, limit=None, friends_req=False):
        self.thread = threading.Thread(target=self.start_session, kwargs={'limit': limit, 'friends_req': friends_req})
        self.thread.start()

    def start_session(self, limit=None, friends_req=False):
        temp = False

        if limit is True and self.syncing and friends_req and (any(list(map(lambda k: k['goal'] == "records", self.goals))) and not all(list(map(lambda k: k['status'] in ['PAUSED', 'COMPLETE'], self.goals)))):
            time.sleep(0.5)
            return

        elif limit is True and self.syncing and self.endpoints['player'] and not friends_req:
            time.sleep(0.5)
            return

        elif limit is True and not self.syncing:
            temp = True

        elif limit is None and self.syncing:
            return

        self.syncing = True

        while self.syncing:
            step = self.request_step

            if not limit:
                if not (not self.player_endpoint(limit=limit, friends_req=friends_req) and not self.friends_endpoint(limit=limit, friends_req=friends_req)):
                    self.realtime.setText("<html/></head><body><p>"
                                          "<span style=\"color: white\">Next Hypixel API Request: </span>"
                                          f"<span style=\"color: cyan\">Updating...</span>"
                                          "</p></body></html>")
            try:
                if self.player_endpoint(limit=limit, friends_req=friends_req):
                    if not limit:
                        self.endpoints["player"] = True
                        self.realtime.setText("<html/></head><body><p>"
                                              "<span style=\"color: white\">Next Hypixel API Request: </span>"
                                              f"<span style=\"color: cyan\">Updating with </span>"
                                              f"<span style=\"color: green\">/player </span>"
                                              f"<span style=\"color: cyan\">endpoint...</span>"
                                              "</p></body></html>")
                    self.player_stats = self.api.getPlayerStats()
                else:
                    if not limit:
                        self.endpoints["player"] = False

                if self.friends_endpoint(limit=limit, friends_req=friends_req):
                    if not limit:
                        self.endpoints["friends"] = True
                        self.realtime.setText("<html/></head><body><p>"
                                              "<span style=\"color: white\">Next Hypixel API Request: </span>"
                                              f"<span style=\"color: cyan\">Updating with </span>"
                                              f"<span style=\"color: green\">/friends </span>"
                                              f"<span style=\"color: cyan\">endpoint...</span>"
                                              "</p></body></html>")
                    self.friend_stats = self.api.getFriends()
                else:
                    if not limit:
                        self.endpoints["friends"] = False
            except KeyError:
                if not limit:
                    self.realtime.setText("<html/></head><body><p>"
                                          "<span style=\"color: white\">Next Hypixel API Request: </span>"
                                          f"<span style=\"color: red\">Error: Exceeded limit of 120 API requests/min </span>"
                                          f"<span style=\"color: cyan\">(waiting 20.0s)</span>"
                                          "</p></body></html>")
                    num = 20.0
                    for i in range(math.ceil(20.0 / step)):
                        if not self.syncing:
                            return
                        number = num if not re.search(".+\.\d$", str(num)) else str(num) + '0'
                        self.realtime.setText("<html/></head><body><p>"
                                              "<span style=\"color: white\">Next Hypixel API Request: </span>"
                                              "<span style=\"color: red\">Error: Exceeded limit of 120 API requests/min </span>"
                                              f"<span style=\"color: cyan\">(waiting {number}s)</span>"
                                              "</p></body></html>")
                        num -= step
                        num = round(num, 2)
                        time.sleep(20.0 // step)
                else:
                    time.sleep(20.0)
                continue
            except Exception:
                import traceback
                print(traceback.format_exc())
                print(f"API Sync --> Unknown error (waiting 3.0s)")
                time.sleep(3.0)
                continue

            if limit:
                break

            rw = self.request_wait if not re.search(".+\.\d$", str(self.request_wait)) else str(self.request_wait) + '0'

            self.statistics.setText("<html/></head><body><p>"
                                      "<span style=\"color: white\">Statistics: </span>"
                                      f"<span style=\"color: aqua\">Request Wait Time: {rw}s</span>"
                                      "<span style=\"color: white\"> // </span>"
                                      f"<span style=\"color: gold\">Requests/min: {round(60/self.request_wait, 2)*len(list(filter(bool, self.endpoints.values())))}</span>"
                                      "<span style=\"color: white\"> // </span>"
                                      f"<span style=\"color: grey\">API Endpoints:</span> <span style=\"color: {'green' if self.endpoints['player'] else 'red'}\">/player</span> <span style=\"color: {'green' if self.endpoints['friends'] else 'red'}\">/friends</span>"
                                      "</p></body></html>")

            if not (not self.player_endpoint(limit=limit, friends_req=friends_req) and not self.friends_endpoint(limit=limit, friends_req=friends_req)) and not limit:
                num = self.request_wait
                for i in range(math.ceil(self.request_wait / step)):
                    if not self.syncing:
                        return
                    number = num if not re.search(".+\.\d$", str(num)) else str(num) + '0'
                    self.realtime.setText("<html/></head><body><p>"
                                          "<span style=\"color: white\">Next Hypixel API Request: </span>"
                                          f"<span style=\"color: cyan\">{number}s</span>"
                                          "</p></body></html>")
                    num -= step
                    num = round(num, 2)
                    time.sleep(step)
            else:
                time.sleep(self.request_wait)
            self.realtime.setText("<html/></head><body><p>"
                                  "<span style=\"color: white\">Next Hypixel API Request: </span>"
                                  f"<span style=\"color: cyan\">0.00s</span>"
                                  "</p></body></html>")
        if temp:
            self.syncing = False

    def end_session(self):
        self.syncing = False
        self.endpoints["player"] = False
        self.endpoints["friends"] = False

        rw = self.request_wait if not re.search(".+\.\d$", str(self.request_wait)) else str(self.request_wait) + '0'

        self.statistics.setText("<html/></head><body><p>"
                                "<span style=\"color: white\">Statistics: </span>"
                                f"<span style=\"color: aqua\">Request Wait Time: {rw}s</span>"
                                "<span style=\"color: white\"> // </span>"
                                f"<span style=\"color: gold\">Requests/min: {round(60 / self.request_wait, 2) * len(list(filter(bool, self.endpoints.values())))}</span>"
                                "<span style=\"color: white\"> // </span>"
                                f"<span style=\"color: grey\">API Endpoints:</span> <span style=\"color: {'green' if self.endpoints['player'] else 'red'}\">/player</span> <span style=\"color: {'green' if self.endpoints['friends'] else 'red'}\">/friends</span>"
                                "</p></body></html>")
        self.realtime.setText("<html/></head><body><p>"
                              "<span style=\"color: white\">Next Hypixel API Request: </span>"
                              f"<span style=\"color: cyan\">0.00s</span>"
                              "</p></body></html>")

        print("API Sync --> Ending session")

class Test(QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

    def test_user(self, username):
        try:
            headers = {
                'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                'Accept-Encoding': "gzip, deflate, br",
                'Accept-Language': "en-GB, en;q=0.5",
                'Host': 'hypixel.net',
                'Scheme': 'https',
                'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
            }
            player = requests.get(f'https://hypixel.net/player/{username}', headers=headers) # Seeing if a user has joined Hypixel or not without using the API
            if len(player.text) <= 7500:
                return False
            return True
        except:
            return False

    def test_key(self, api_key):
        response = requests.get(f'https://api.hypixel.net/key?&key={api_key}').json()
        return response['success']