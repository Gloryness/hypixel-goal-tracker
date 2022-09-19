from PyQt5.QtCore import QMetaObject, QSize, Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon, QBrush, QColor, QPalette
from PyQt5.QtWidgets import QFrame, QWidget, QScrollArea, QGridLayout, QLabel, QLayout, QToolButton, QVBoxLayout, QMainWindow, \
    QSplitter

from packaging import version
import subprocess
import datetime
import threading
import requests
import sys
import os
import re

from app import path, __version__, is_executable
from app.cache import Cache
from app.clock import Clock, ClockSync
from gui.setup import Setup
from gui.extract_info import Extractor
from gui.completed import CompletedGoals
from gui.best_goals import BestGoals
from gui.settings import Config
from gui.check_updates import UpdateCheck
from util.threadmanager import ThreadManager
from util.api import API, APISync
from util.process import processProgress, convert_to_time

class MainUI:
    def __init__(self, main_window: QMainWindow):
        self.win = main_window
    
    def setupUi(self):
        self.win.setWindowTitle("Hypixel Goal Tracker")
        self.win.setWindowIcon(QIcon(path('images', 'logo.png')))
        self.win.resize(1310, 406)
        self.win.setMinimumWidth(1306)

        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush = QBrush(QColor(11, 14, 7))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        self.win.setPalette(palette)

        self.centralwidget = QWidget(self.win)
        self.gridLayout_3 = QGridLayout(self.centralwidget)

        self.hypixel_logo = QLabel(self.centralwidget)
        self.hypixel_logo.setMinimumSize(QSize(351, 151))
        self.hypixel_logo.setMaximumSize(QSize(351, 151))
        self.hypixel_logo.setPixmap(QPixmap(path('images', 'banner.png')))
        self.hypixel_logo.setScaledContents(True)
        self.gridLayout_3.addWidget(self.hypixel_logo, 0, 0, 1, 1)

        self.outer_frame = QFrame(self.centralwidget)
        self.outer_frame.setFrameShape(QFrame.StyledPanel)
        self.outer_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.outer_frame)
        self.gridLayout_4.setSizeConstraint(QLayout.SetMinAndMaxSize)

        self.inner_frame = QFrame(self.outer_frame)
        self.inner_frame.setFrameShape(QFrame.StyledPanel)
        self.inner_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.inner_frame)
        self.gridLayout_2.setContentsMargins(0, 9, 9, 9)

        self.active_goals_line = QFrame(self.inner_frame)
        self.active_goals_line.setFrameShadow(QFrame.Raised)
        self.active_goals_line.setFrameShape(QFrame.HLine)
        self.gridLayout_2.addWidget(self.active_goals_line, 3, 0, 1, 3)

        self.main_frame = QFrame(self.inner_frame)
        palette = QPalette()
        brush = QBrush(QColor(11, 14, 7))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(18, 18, 18))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        self.main_frame.setPalette(palette)
        self.main_frame.setAutoFillBackground(True)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.main_frame)

        self.scrollArea = QScrollArea(self.main_frame)
        self.scrollArea.setFrameShape(QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(QFrame.Raised)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollAreaContents = QWidget()
        self.gridLayout_1 = QGridLayout(self.scrollAreaContents)
        self.gridLayout_1.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_1.setHorizontalSpacing(0)
        palette = QPalette()
        brush = QBrush(QColor(11, 14, 7))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(18, 18, 18))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        self.scrollAreaContents.setPalette(palette)

        self.splitter = QSplitter(self.scrollAreaContents)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(3)
        self.splitter.setChildrenCollapsible(False)
        # self.splitter.setStyleSheet("QSplitter::handle { background-color: rgba(20, 20, 20, 75%) }")

        ###########################################################

        line_palette = QPalette()
        brush = QBrush(QColor(170, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        line_palette.setBrush(QPalette.Active, QPalette.Light, brush)
        line_palette.setBrush(QPalette.Inactive, QPalette.Light, brush)

        palette = QPalette()
        brush = QBrush(QColor(85, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)

        font = QFont()
        font.setFamily("Nirmala UI")
        font.setBold(True)
        font.setWeight(75)

        ###########################################################

        self.gamemode_frame = QFrame(self.scrollAreaContents)
        self.gamemode_frame.setFrameShape(QFrame.StyledPanel)
        self.gamemode_frame.setFrameShadow(QFrame.Raised)
        self.gamemode_grid = QVBoxLayout(self.gamemode_frame)
        self.gamemode_grid.setContentsMargins(0, -1, 0, -1)
        self.gamemode_grid.setAlignment(Qt.AlignTop)

        self.gamemode_label = QLabel(self.gamemode_frame)
        self.gamemode_label.setPalette(palette)
        self.gamemode_label.setFont(font)
        self.gamemode_label.setText("#")
        self.gamemode_grid.addWidget(self.gamemode_label)

        self.line = QFrame(self.gamemode_frame)
        self.line.setPalette(line_palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.gamemode_grid.addWidget(self.line)
        self.gamemode_frame.setMaximumWidth(18)

        self.splitter.addWidget(self.gamemode_frame)

        ###########################################################

        self.name_frame = QFrame(self.scrollAreaContents)
        self.name_frame.setFrameShape(QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QFrame.Raised)
        self.name_grid = QVBoxLayout(self.name_frame)
        self.name_grid.setContentsMargins(0, -1, 0, -1)
        self.name_grid.setAlignment(Qt.AlignTop)

        self.name_label = QLabel(self.name_frame)
        self.name_label.setPalette(palette)
        self.name_label.setFont(font)
        self.name_grid.addWidget(self.name_label)

        self.line = QFrame(self.name_frame)
        self.line.setPalette(line_palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.name_grid.addWidget(self.line)

        self.splitter.addWidget(self.name_frame)

        ###########################################################

        self.goal_frame = QFrame(self.scrollAreaContents)
        self.goal_frame.setFrameShape(QFrame.StyledPanel)
        self.goal_frame.setFrameShadow(QFrame.Raised)
        self.goal_grid = QVBoxLayout(self.goal_frame)
        self.goal_grid.setContentsMargins(0, -1, 0, -1)
        self.goal_grid.setAlignment(Qt.AlignTop)

        self.goal_label = QLabel(self.goal_frame)
        self.goal_label.setPalette(palette)
        self.goal_label.setFont(font)
        self.goal_grid.addWidget(self.goal_label)

        self.line = QFrame(self.goal_frame)
        self.line.setPalette(line_palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.goal_grid.addWidget(self.line)

        self.splitter.addWidget(self.goal_frame)

        ###########################################################

        self.progress_frame = QFrame(self.scrollAreaContents)
        self.progress_frame.setFrameShape(QFrame.StyledPanel)
        self.progress_frame.setFrameShadow(QFrame.Raised)
        self.progress_grid = QVBoxLayout(self.progress_frame)
        self.progress_grid.setContentsMargins(0, -1, 0, -1)
        self.progress_grid.setAlignment(Qt.AlignTop)

        self.progress_label = QLabel(self.progress_frame)
        self.progress_label.setPalette(palette)
        self.progress_label.setFont(font)
        self.progress_grid.addWidget(self.progress_label)

        self.line = QFrame(self.progress_frame)
        self.line.setPalette(line_palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.progress_grid.addWidget(self.line)

        self.splitter.addWidget(self.progress_frame)

        ###########################################################

        self.requirement_frame = QFrame(self.scrollAreaContents)
        self.requirement_frame.setFrameShape(QFrame.StyledPanel)
        self.requirement_frame.setFrameShadow(QFrame.Raised)
        self.requirement_grid = QVBoxLayout(self.requirement_frame)
        self.requirement_grid.setContentsMargins(0, -1, 0, -1)
        self.requirement_grid.setAlignment(Qt.AlignTop)

        self.requirement_label = QLabel(self.requirement_frame)
        self.requirement_label.setPalette(palette)
        self.requirement_label.setFont(font)
        self.requirement_grid.addWidget(self.requirement_label)

        self.line = QFrame(self.requirement_frame)
        self.line.setPalette(line_palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.requirement_grid.addWidget(self.line)

        self.splitter.addWidget(self.requirement_frame)

        ###########################################################

        self.timeLeft_frame = QFrame(self.scrollAreaContents)
        self.timeLeft_frame.setFrameShape(QFrame.StyledPanel)
        self.timeLeft_frame.setFrameShadow(QFrame.Raised)
        self.timeLeft_grid = QVBoxLayout(self.timeLeft_frame)
        self.timeLeft_grid.setContentsMargins(0, -1, 0, -1)
        self.timeLeft_grid.setAlignment(Qt.AlignTop)

        self.timeLeft_label = QLabel(self.timeLeft_frame)
        self.timeLeft_label.setPalette(palette)
        self.timeLeft_label.setFont(font)
        self.timeLeft_grid.addWidget(self.timeLeft_label)

        self.line = QFrame(self.timeLeft_frame)
        self.line.setPalette(line_palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.timeLeft_grid.addWidget(self.line)

        self.splitter.addWidget(self.timeLeft_frame)

        ###########################################################

        self.status_frame = QFrame(self.scrollAreaContents)
        self.status_frame.setFrameShape(QFrame.StyledPanel)
        self.status_frame.setFrameShadow(QFrame.Raised)
        self.status_grid = QVBoxLayout(self.status_frame)
        self.status_grid.setContentsMargins(0, -1, 0, -1)
        self.status_grid.setAlignment(Qt.AlignTop)

        self.status_label = QLabel(self.status_frame)
        self.status_label.setPalette(palette)
        self.status_label.setFont(font)
        self.status_grid.addWidget(self.status_label)

        self.line = QFrame(self.status_frame)
        self.line.setPalette(line_palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.status_grid.addWidget(self.line)

        self.splitter.addWidget(self.status_frame)

        ###########################################################

        self.action_frame = QFrame(self.scrollAreaContents)
        self.action_frame.setFrameShape(QFrame.StyledPanel)
        self.action_frame.setFrameShadow(QFrame.Raised)
        self.action_grid = QVBoxLayout(self.action_frame)
        self.action_grid.setContentsMargins(0, -1, 0, -1)
        self.action_grid.setAlignment(Qt.AlignTop)

        self.action_label = QLabel(self.action_frame)
        self.action_label.setPalette(palette)
        self.action_label.setFont(font)
        self.action_grid.addWidget(self.action_label)

        self.line = QFrame(self.action_frame)
        self.line.setPalette(line_palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.action_grid.addWidget(self.line)

        self.splitter.addWidget(self.action_frame)

        ###########################################################

        for index in range(1, len(self.splitter)):
            if index == 1:
                self.splitter.handle(index).setStyleSheet("background-color: rgb(18, 18, 18)")
                self.splitter.handle(index).setDisabled(True)
            else:
                self.splitter.handle(index).setStyleSheet("background-color: rgba(20, 20, 20, 75%)")

        self.gridLayout_1.addWidget(self.splitter, 0, 0, 1, 1)

        self.gridLayout_2.addWidget(self.main_frame, 4, 0, 1, 3)

        self.active_goals_label = QLabel(self.inner_frame)
        self.active_goals_label.setMinimumSize(QSize(541, 43))
        self.active_goals_label.setMaximumSize(QSize(16777215, 43))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.active_goals_label.setPalette(palette)
        font = QFont()
        font.setFamily("Minecraftia")
        font.setBold(True)
        font.setPointSize(12)
        self.active_goals_label.setFont(font)

        self.completed_goals = QToolButton(self.inner_frame)
        palette = QPalette()
        brush = QBrush(QColor(196, 255, 255))
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.completed_goals.setPalette(palette)
        font = QFont()
        font.setFamily("Minecraftia")
        font.setPointSize(12)
        self.completed_goals.setFont(font)
        self.completed_goals.setIcon(QIcon(path('images', 'pink.png')))
        self.completed_goals.setIconSize(QSize(22, 22))
        self.completed_goals.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.completed_goals.setAutoRaise(True)

        self.config = QToolButton(self.inner_frame)
        self.config.setMaximumSize(QSize(32, 32))
        self.config.setIcon(QIcon(path('images', 'config.png')))
        self.config.setIconSize(QSize(32, 32))
        self.config.setAutoRaise(True)
        self.config.setToolTip("Config")

        self.realtimestats = QLabel(self.outer_frame)
        font = QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(11)
        font.setWeight(75)
        self.realtimestats.setFont(font)

        self.realtimestats2 = QLabel(self.outer_frame)
        self.realtimestats2.setFont(font)

        self.gridLayout_2.addWidget(self.active_goals_label, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.completed_goals, 1, 1, 1, 1)
        self.gridLayout_2.addWidget(self.config, 1, 2, 1, 1)
        self.gridLayout_2.addWidget(self.realtimestats, 5, 0, 1, 3)
        self.gridLayout_2.addWidget(self.realtimestats2, 6, 0, 1, 3)

        self.gridLayout_4.addWidget(self.inner_frame, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.outer_frame, 0, 1, 2, 1)

        self.buttons_frame = QFrame(self.centralwidget)
        self.buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.buttons_frame)

        self.custom_goal = QToolButton(self.buttons_frame)
        self.custom_goal.setMinimumSize(QSize(351, 41))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.custom_goal.setPalette(palette)
        font = QFont()
        font.setFamily("Minecraftia")
        font.setPointSize(12)
        self.custom_goal.setFont(font)
        self.custom_goal.setAutoRaise(True)
        self.gridLayout_5.addWidget(self.custom_goal, 0, 0, 1, 1)

        self.goal_organiser = QToolButton(self.buttons_frame)
        self.goal_organiser.setMinimumSize(QSize(351, 41))
        palette = QPalette()
        brush = QBrush(QColor(255, 170, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.goal_organiser.setPalette(palette)
        self.goal_organiser.setFont(font)
        self.goal_organiser.setAutoRaise(True)
        self.gridLayout_5.addWidget(self.goal_organiser, 1, 0, 1, 1)

        self.coming_soon = QToolButton(self.buttons_frame)
        self.coming_soon.setMinimumSize(QSize(351, 41))
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.coming_soon.setPalette(palette)
        self.coming_soon.setFont(font)
        self.coming_soon.setAutoRaise(True)
        self.gridLayout_5.addWidget(self.coming_soon, 2, 0, 1, 1)

        self.gridLayout_3.addWidget(self.buttons_frame, 1, 0, 1, 1)
        self.win.setCentralWidget(self.centralwidget)

        self.scrollArea.setWidget(self.scrollAreaContents)
        self.gridLayout.addWidget(self.scrollArea, 3, 0, 1, 6)

        QMetaObject.connectSlotsByName(self.win)

class Main(QMainWindow):
    def __init__(self, rpcstate, parent=None):
        super().__init__(parent)

        self.ui = MainUI(self)
        self.ui.setupUi()
        self.all_goals = {}

        self.rpcstate = rpcstate
        self.inside_settings = False

        self.cache = Cache(f'{os.environ["USERPROFILE"]}/AppData/Local/hypixel-goal-tracker', 'data.json')
        quit_ = False

        def func():
            nonlocal quit_
            try:
                module_path = self.cache.folder+"\\pending\\Hypixel Goal Tracker Updater.exe"
                module_path = module_path.replace("\\", "\\\\")
                subprocess.call(f"wmic process where ExecutablePath='{module_path}' delete", shell=True)
            except:
                pass
            try:
                _ = requests.head('https://www.google.com/', timeout=3.5)

                newest_version = requests.get('https://raw.githubusercontent.com/Gloryness/hypixel-goal-tracker/main/version.txt').text.strip()

                if version.parse(__version__) < version.parse(newest_version):
                    update_executable = requests.get('https://raw.githubusercontent.com/Gloryness/hypixel-goal-tracker-backend/main/pending/Hypixel%20Goal%20Tracker%20Updater.exe')

                    if os.path.isfile(directory := self.cache.folder + "\\pending\\Hypixel Goal Tracker Updater.exe"):
                        os.remove(directory)

                    with open(directory, 'wb') as f:
                        f.write(update_executable.content)

                    checking.close()
                    quit_ = True
                    subprocess.call([directory, '-p', path().replace("\\", "/"), '-v', newest_version])
                else:
                    checking.close()
            except:
                checking.close()
                import traceback
                print(traceback.format_exc())

        if is_executable: # Only auto-updating if using the executable.
            thread = threading.Thread(target=func)
            thread.start()

            checking = UpdateCheck()
            checking.exec_()

            if quit_:
                sys.exit()

        self.ui.name_label.setText("Name")
        self.ui.goal_label.setText("Goal")
        self.ui.progress_label.setText("Progress")
        self.ui.requirement_label.setText("Requirement")
        self.ui.timeLeft_label.setText("Time Left")
        self.ui.status_label.setText("Status")
        self.ui.action_label.setText("Action")
        self.ui.active_goals_label.setText("<html><head/><body><p>Active Goals <span style=\"color: white\">[0]</span></p></body></html>")
        self.ui.completed_goals.setText("View all completed goals")
        self.ui.custom_goal.setText("Add a Custom Goal")
        self.ui.goal_organiser.setText("Goal Organiser")
        self.ui.coming_soon.setText("Coming Soon")

        self.ui.custom_goal.clicked.connect(self.setup)
        self.ui.goal_organiser.clicked.connect(self.setup_best_goals)
        self.ui.completed_goals.clicked.connect(self.setup_completed_goals)
        self.ui.config.clicked.connect(self.setup_config)

        cache = self.cache.all()
        if 'uuid' not in cache or 'api-key' not in cache:
            extractor = Extractor(self)
            extractor.exec_()
            cache = self.cache.all()

        if 'uuid' not in cache or 'api-key' not in cache:
            sys.exit()

        self.goals = []
        self.completed_goals = self.cache.get('completed_goals')
        self.goal_organiser = self.cache.get('goal_organiser')

        request_wait = 1.50 if 'request-wait' not in cache else cache.get('request-wait')
        request_step = 0.05 if 'next-request-step' not in cache else cache.get('next-request-step')
        rw = request_wait if not re.search(".+\.\d$", str(request_wait)) else str(request_wait)+'0'
        self.progress_design = True if 'progress-design' not in cache else cache.get('progress-design')
        self.percentage_design = True if 'percentage-design' not in cache else cache.get('percentage-design')

        self.clock_sync = ClockSync(self)
        self.clock_sync.start()

        self.api = API(uuid=cache.get('uuid'), api_key=cache.get('api-key'))
        self.api_sync = APISync(self.api, goals=self.goals, statistics=[self.ui.realtimestats, self.ui.realtimestats2],
                                request_wait=request_wait,
                                request_step=request_step)
        self.api_sync.start_session_sync(limit=True, friends_req=True)
        self.api_sync.thread.join(2)

        self.ui.realtimestats.setText("<html/></head><body><p>"
                                      "<span style=\"color: white\">Statistics: </span>"
                                      f"<span style=\"color: aqua\">Request Wait Time: {rw}s</span>"
                                      "<span style=\"color: white\"> // </span>"
                                      f"<span style=\"color: gold\">Requests/min: {round(60 / request_wait, 2)*len(list(filter(bool, self.api_sync.endpoints.values())))}</span>"
                                      "<span style=\"color: white\"> // </span>"
                                      "<span style=\"color: grey\">API Endpoints:</span> <span style=\"color: red\">/player</span> <span style=\"color: red\">/friends</span>"
                                      "</p></body></html>")

        self.ui.realtimestats2.setText("<html/></head><body><p>"
                                      "<span style=\"color: white\">Next Hypixel API Request: </span>"
                                      "<span style=\"color: cyan\">0.00s</span>"
                                      "</p></body></html>")

        self.manager = ThreadManager(self.all_goals, self)

        self.unpack(self.cache.get('goals'))

        self.manager.cache(self.goals, self.completed_goals, self.goal_organiser)

    def unpack(self, goals):
        for data in goals:
            self.add_goal(None, data, temp=True)

    def setup(self):
        self.s = Setup(self)

    def setup_best_goals(self):
        self.s = BestGoals(self.completed_goals, self.goal_organiser)

    def setup_completed_goals(self):
        self.s = CompletedGoals(self.completed_goals)

    def setup_config(self):
        self.inside_settings = True
        self.s = Config(self)

    def fetch_index(self, index):
        for goal in self.goals:
            if goal['index'] == index:
                return self.goals.index(goal)

    def add_goal(self, setup_window, data, temp=False):
        if not temp:
            infiniteTime = '∞' in setup_window.ui.timeLeft.text()
        else:
            infiniteTime = data['clock'] == '∞'

        if data['status'] == 'EDITING':
            data['status'] = 'INCOMPLETE'

        font = QFont()
        font.setFamily("Nirmala UI")
        font.setBold(True)
        font.setPointSize(9)
        font.setWeight(75)

        def create_group(obj_name):
            group_frame = eval(f"QFrame(self.ui.{obj_name}_frame)", globals(), {"self": self})
            # group_frame.setStyleSheet("background-color: rgba(18, 222, 14, 20%)")
            group_frame.setFixedHeight(27)

            group = QGridLayout(group_frame)
            group.setContentsMargins(1, 1, 1, 1)
            group.setAlignment(Qt.AlignVCenter)
            return group, group_frame
        
        if hasattr(self, f'gamemode_{len(self.goals)}'):
            num = 1
            while hasattr(self, f'gamemode_{num}'):
                num += 1
        else:
            num = len(self.goals)

        data['index'] = num

        group, gamemode_frame = create_group("gamemode")
        exec(f"self.gamemode_{num} = QLabel()")
        gamemode = getattr(self, f'gamemode_{num}')
        gamemode.setPixmap(QPixmap(path('images', 'game-icons', data['gamemode']+'.png')))
        gamemode.setScaledContents(True)
        gamemode.setFixedSize(QSize(16, 16))
        gamemode.setToolTip(data['gamemode'])
        group.addWidget(gamemode)
        self.ui.gamemode_grid.addWidget(gamemode_frame)

        group, name_frame = create_group("name")
        exec(f"self.name_{num} = QLabel()")
        name = getattr(self, f'name_{num}')
        palette = QPalette()
        brush = QBrush(QColor(40, 163, 21))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        name.setPalette(palette)
        name.setFont(font)
        group.addWidget(name)
        self.ui.name_grid.addWidget(name_frame)

        group, goal_frame = create_group("goal")
        exec(f"self.goal_{num} = QLabel()")
        goal = getattr(self, f'goal_{num}')
        palette = QPalette()
        brush = QBrush(QColor(255, 170, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        goal.setPalette(palette)
        goal.setFont(font)
        group.addWidget(goal)
        self.ui.goal_grid.addWidget(goal_frame)

        group, progress_frame = create_group("progress")
        exec(f"self.progress_{num} = QLabel()")
        progress: QLabel = getattr(self, f"progress_{num}")
        palette = QPalette()
        brush = QBrush(QColor(0, 255, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        progress.setPalette(palette)
        progress.setFont(font)
        progress.setTextFormat(Qt.RichText)
        group.addWidget(progress)
        self.ui.progress_grid.addWidget(progress_frame)

        group, requirement_frame = create_group("requirement")
        exec(f"self.requirement_{num} = QLabel()")
        requirement: QLabel = getattr(self, f"requirement_{num}")
        palette = QPalette()
        brush = QBrush(QColor(0, 255, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        requirement.setPalette(palette)
        requirement.setFont(font)
        requirement.setTextFormat(Qt.RichText)
        group.addWidget(requirement)
        self.ui.requirement_grid.addWidget(requirement_frame)

        group, timeLeft_frame = create_group("timeLeft")
        exec(f"self.timeLeft_{num} = QLabel()")
        timeLeft = getattr(self, f"timeLeft_{num}")
        palette = QPalette()
        brush = QBrush(QColor(16, 140, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        timeLeft.setPalette(palette)
        timeLeft.setFont(font)
        group.addWidget(timeLeft)
        self.ui.timeLeft_grid.addWidget(timeLeft_frame)

        group, status_frame = create_group("status")
        exec(f"self.status_{num} = QLabel()")
        status = getattr(self, f'status_{num}')
        palette = QPalette()
        if data['status'] == 'COMPLETE':
            brush = QBrush(QColor(0, 171, 0))
        elif temp and data['goal_amount'] == 'infinite':
            brush = QBrush(QColor(0, 171, 0))
        else:
            brush = QBrush(QColor(255, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        status.setPalette(palette)
        status.setFont(font)
        group.addWidget(status)
        self.ui.status_grid.addWidget(status_frame)

        group, action_frame = create_group("action")
        exec(f"self.complete_goal_{num} = QToolButton()")
        complete_goal = getattr(self, f"complete_goal_{num}")
        complete_goal.setIcon(QIcon(path('images', 'yes.png')))
        complete_goal.setIconSize(QSize(14, 14))
        complete_goal.setAutoRaise(True)
        complete_goal.setAccessibleName(str(num))
        complete_goal.clicked.connect(lambda: self.complete_goal(complete_goal.accessibleName()))
        complete_goal.setDisabled(True if data['status'] != 'COMPLETE' else False)
        group.addWidget(complete_goal, 0, 0, 1, 1)

        exec(f"self.toggle_goal_{num} = QToolButton()")
        toggle_goal = getattr(self, f"toggle_goal_{num}")
        toggle_goal.setIcon(QIcon(path('images', 'pause.png')))
        toggle_goal.setIconSize(QSize(14, 14))
        toggle_goal.setAutoRaise(True)
        toggle_goal.setAccessibleName(str(num))
        toggle_goal.clicked.connect(lambda: self.toggle_goal(toggle_goal.accessibleName()))
        toggle_goal.setDisabled(False if data['status'] != 'COMPLETE' and 'complete_by' not in data else True)
        group.addWidget(toggle_goal, 0, 1, 1, 1)

        exec(f"self.edit_goal_{num} = QToolButton()")
        edit_goal = getattr(self, f"edit_goal_{num}")
        edit_goal.setIcon(QIcon(path('images', 'plus.svg')))
        edit_goal.setIconSize(QSize(12, 12))
        edit_goal.setStyleSheet("padding: 3px")
        edit_goal.setAutoRaise(True)
        edit_goal.setAccessibleName(str(num))
        edit_goal.clicked.connect(lambda: self.edit_setup(edit_goal.accessibleName()))
        edit_goal.setDisabled(False if data['status'] != 'COMPLETE' else True)
        group.addWidget(edit_goal, 0, 2, 1, 1)

        exec(f"self.remove_goal_{num} = QToolButton()")
        remove_goal = getattr(self, f"remove_goal_{num}")
        remove_goal.setIcon(QIcon(path('images', 'no.png')))
        remove_goal.setIconSize(QSize(14, 14))
        remove_goal.setAutoRaise(True)
        remove_goal.setAccessibleName(str(num))
        remove_goal.clicked.connect(lambda: self.remove_goal(remove_goal.accessibleName()))
        group.addWidget(remove_goal, 0, 3, 1, 1)

        self.ui.action_grid.addWidget(action_frame)

        if data['goal_amount'] == 'infinite': # Performing various calculations depending on settings (value, percentage, etc)
            if not temp:
                data['starting_amount'] = data['current_amount']
                data['mid_amount'] = 0
            outOf = processProgress(data, progress_design=self.progress_design)
            percentage = '∞'
            percentage_str = ''
        else:
            calc = 100 / data['goal_amount']

            if data['milestone']:
                if not temp:
                    data['starting_amount'] = data['current_amount']
                outOf = processProgress(data, progress_design=self.progress_design)
                percentage = round(data['current_amount'] * calc, 2)
                if (data['current_amount'] * calc) < 100 and (data['current_amount'] * calc) > 99.99:
                    percentage = 99.99
                percentage_str = f"({percentage})%"
            else:
                if not temp:
                    data['starting_amount'] = data['current_amount']
                    data['mid_amount'] = 0
                outOf = processProgress(data, progress_design=self.progress_design)
                percentage = round(data['mid_amount'] * calc, 2)
                if (data['mid_amount'] * calc) < 100 and (data['mid_amount'] * calc) > 99.99:
                    percentage = 99.99
                percentage_str = f"({percentage})%"

        if infiniteTime:
            data['clock'] = '∞'

        name.setText(data['name'])
        goal.setText(data['goal'])
        if percentage == '∞':
            if outOf.split('/')[0] == '0':
                color = 'color:#ea0000'
            else:
                color = 'color:#00ab00'
        elif percentage > 50 and percentage < 100:
            color = 'color:#f5a300'
        elif percentage < 50:
            color = 'color:#ea0000'
        else:
            color = 'color:#00ab00'

        if 'font-size: 12pt' in outOf and progress.styleSheet() == "margin-bottom: 5px":
            pass
        elif 'font-size: 12pt' in outOf:
            progress.setStyleSheet("margin-bottom: 5px")
        else:
            progress.setStyleSheet("margin-bottom: 0px")

        if self.percentage_design:
            progress.setText(f"<html><head/><body><p><span style=\"{color}\">{outOf} </span><span style=\" color:#2fe813;\">{percentage_str}</span></p></body></html>")
        else:
            progress.setText(f"<html><head/><body><p><span style=\"{color}\">{outOf}</span></p></body></html>")

        if not temp:
            data['requirement'] = setup_window.ui.requirement.currentText()
        else:
            if 'requirement' not in data:
                data['requirement'] = 'minutes'

        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        requirement.setPalette(palette)
        requirement.setText("-")

        if temp:
            if 'complete_by' in data:
                # Updating the time left because this is a goal that was set with the Complete By Date setting

                date = data['complete_by']
                clock = Clock()

                a = datetime.datetime.now()
                b = datetime.datetime(date['year'], date['month'], date['day'], date['hour'], date['minute'], date['second'])
                delta = b - a

                clock.days = delta.days
                clock.hours = 0
                clock.minutes = 0
                clock.seconds = delta.seconds + (1 if delta.microseconds / 10000 > 50 else 0)

                if (clock.days <= 0 and clock.seconds <= 0) or clock.days < 0:
                    data['clock'] = '0m'
                else:
                    data['clock'] = clock.format()

        timeLeft.setText(data['clock'])
        if infiniteTime: # If the infinite duration setting has been enabled, there is no countdown so therefore it counts seconds and converts it to a readable time format.
            timeLeft.setText(f"{data['clock']} ({convert_to_time(data['seconds'])} uptime)")
        status.setText(data['status'])

        complete_goal.setToolTip("Complete Goal")
        toggle_goal.setToolTip("Pause Goal")
        edit_goal.setToolTip("Edit Goal")
        remove_goal.setToolTip("Remove Goal")

        self.all_goals[f'dataset{num}'] = {
            "gamemode": gamemode,
            "name": name,
            "goal": goal,
            "main": self,
            "progress": progress,
            "requirement": requirement,
            "timeLeft": timeLeft,
            "status": status,
            "complete_goal": complete_goal,
            "toggle_goal": toggle_goal,
            "edit_goal": edit_goal,
            "remove_goal": remove_goal
        }

        self.goals.append(data)

        if data['status'] == 'PAUSED':
            data['status'] = 'INCOMPLETE'
            self.toggle_goal(data['index'])

        if not temp:
            goals = self.cache.get('goals')
            goals.append(data.copy())
            self.cache.store({'goals': goals})
            setup_window.close()

        if data['status'] != 'COMPLETE':
            self.manager.load(self.goals[self.fetch_index(data['index'])])
            self.manager.manage(self.goals[self.fetch_index(data['index'])])
            self.manager.sync()

        self.ui.active_goals_label.setText(f"<html><head/><body><p>Active Goals <span style=\"color: white\">[{len(self.goals):,}]</span></p></body></html>")

    def complete_goal(self, index):
        index = int(index)
        data = self.goals[self.fetch_index(index)]
        if data['goal_amount'] == 'infinite':
            goal = f"{data['current_amount']:,} {data['goal']} (+{data['mid_amount']:,})"
        else:
            if data['milestone']:
                goal = f"{data['goal_amount']:,} {data['goal']}"
            else:
                goal = f"{data['current_amount']:,} {data['goal']} (+{data['mid_amount']:,})"

        relevant_data = {
            "name": data['name'],
            "gamemode": data['gamemode'],
            "goal_name": data['goal'],
            "api_goal_name": data['api_goal_name'],
            "started_with": f"{data['starting_amount']:,} {data['goal']}",
            "goal": goal,
            "time_taken": convert_to_time(data['seconds']),
            "paused_time": f"{convert_to_time(round(data['paused_seconds']))}",
            "completed": data['completed'],
            "milestone": "INFINITE" if data['goal_amount'] == 'infinite' else "Yes" if data['milestone'] else "No"
        }
        self.completed_goals.append(relevant_data)
        self.cache.store({'completed_goals': self.completed_goals})

        self.remove_goal(index)

    def toggle_goal(self, index):
        index = int(index)
        if self.goals[self.fetch_index(index)]['status'] == 'PAUSED':
            self.goals[self.fetch_index(index)]['status'] = 'RESUMING'
            edit_goal = getattr(self, f"edit_goal_{index}")
            edit_goal.setDisabled(False)
            toggle_goal = getattr(self, f"toggle_goal_{index}")
            toggle_goal.setIcon(QIcon(path('images', 'pause.png')))
            toggle_goal.setIconSize(QSize(14, 14))
            toggle_goal.setToolTip("Pause Goal")
            status = getattr(self, f'status_{index}')
            status.setText('RESUMING')
            return
        edit_goal = getattr(self, f"edit_goal_{index}")
        edit_goal.setDisabled(True)
        toggle_goal = getattr(self, f"toggle_goal_{index}")
        toggle_goal.setIcon(QIcon(path('images', 'play.png')))
        toggle_goal.setIconSize(QSize(14, 14))
        toggle_goal.setToolTip("Resume Goal")
        self.goals[self.fetch_index(index)]['status'] = 'PAUSED'
        palette = QPalette()
        brush = QBrush(QColor(186, 186, 186))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        status = getattr(self, f'status_{index}')
        status.setPalette(palette)
        status.setText('PAUSED')

    def edit_setup(self, index):
        index = int(index)
        self.goals[self.fetch_index(index)]['status'] = 'EDITING'
        goal = self.goals[self.fetch_index(index)]
        palette = QPalette()
        brush = QBrush(QColor(186, 186, 186))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        name = getattr(self, f'name_{index}')
        goall = getattr(self, f'goal_{index}')
        progress = getattr(self, f"progress_{index}")
        requirement = getattr(self, f"requirement_{index}")
        timeLeft = getattr(self, f"timeLeft_{index}")
        status = getattr(self, f'status_{index}')
        name.setPalette(palette)
        goall.setPalette(palette)
        progress.setText(progress.text().replace("#ea0000", '#BABABA').replace('#2fe813', '#BABABA').replace('#f5a300', '#BABABA').replace('#00ab00', '#BABABA'))
        requirement.setPalette(palette)
        timeLeft.setPalette(palette)
        status.setPalette(palette)
        status.setText('EDITING')
        self.s = Setup(self, auto=goal)

    def edit_goal(self, index, data):
        self.goals[self.fetch_index(index)]['status'] = 'INCOMPLETE'
        data['status'] = 'INCOMPLETE'

        name = getattr(self, f'name_{index}')
        name.setText(data['name'])
        palette = QPalette()
        brush = QBrush(QColor(40, 163, 21))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        name.setPalette(palette)

        goal = getattr(self, f'goal_{index}')
        goal.setText(data['goal'])
        palette = QPalette()
        brush = QBrush(QColor(255, 170, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        goal.setPalette(palette)

        timeLeft = getattr(self, f"timeLeft_{index}")
        palette = QPalette()
        brush = QBrush(QColor(16, 140, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        timeLeft.setPalette(palette)

        status = getattr(self, f'status_{index}')
        status.setText(data['status'])
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        status.setPalette(palette)
        status.setText('INCOMPLETE')

        self.manager.delete(index, temp=True)

        self.goals[self.fetch_index(index)] = data

        self.s.closed = True
        self.s.close()

        self.manager.load(self.goals[self.fetch_index(index)])
        self.manager.manage(self.goals[self.fetch_index(index)])
        self.manager.sync()

    def remove_goal(self, index):
        index = int(index)

        try:
            self.manager.delete(index)
        except:
            pass

        self.goals.pop(self.fetch_index(index))

        gamemode = getattr(self, f'gamemode_{index}')
        name = getattr(self, f'name_{index}')
        goal = getattr(self, f'goal_{index}')
        progress = getattr(self, f"progress_{index}")
        requirement = getattr(self, f"requirement_{index}")
        timeLeft = getattr(self, f"timeLeft_{index}")
        status = getattr(self, f'status_{index}')
        complete_goal = getattr(self, f"complete_goal_{index}")
        toggle_goal = getattr(self, f"toggle_goal_{index}")
        edit_goal = getattr(self, f"edit_goal_{index}")
        remove_goal = getattr(self, f"remove_goal_{index}")

        gamemode.parent().deleteLater(); delattr(self, f"gamemode_{index}")
        name.parent().deleteLater(); delattr(self, f"name_{index}")
        goal.parent().deleteLater(); delattr(self, f"goal_{index}")
        progress.parent().deleteLater(); delattr(self, f"progress_{index}")
        requirement.parent().deleteLater(); delattr(self, f"requirement_{index}")
        timeLeft.parent().deleteLater(); delattr(self, f"timeLeft_{index}")
        status.parent().deleteLater(); delattr(self, f"status_{index}")
        complete_goal.parent().deleteLater(); delattr(self, f"complete_goal_{index}")
        delattr(self, f"toggle_goal_{index}")
        delattr(self, f"edit_goal_{index}")
        delattr(self, f"remove_goal_{index}")

        del self.all_goals[f'dataset{index}']

        self.ui.active_goals_label.setText(f"<html><head/><body><p>Active Goals <span style=\"color: white\">[{len(self.goals):,}]</span></p></body></html>")

    def closeEvent(self, event):
        # goals = list(filter(lambda x: x['status'] != 'COMPLETE', self.goals))
        for goal in self.goals:
            self.manager.delete(goal['index'])
        self.manager.end_cache = True
        self.clock_sync.end_sync = True
        goals = self.cache.get('goals')
        for index in range(len(goals)):
            goals[index]['index'] = index
        self.cache.store({'goals': goals})