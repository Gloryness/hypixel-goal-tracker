from PyQt5.QtCore import QMetaObject, QSize, QRect, Qt
from PyQt5.QtGui import QFont, QIcon, QBrush, QColor, QPalette
from PyQt5.QtWidgets import QSizePolicy, QFrame, QWidget, QScrollArea, QGridLayout, QLabel, QToolButton, QSpacerItem, QDialog, QMenu

from itertools import cycle
import random

from app import path
from util import constants

from gui.gamemode import Gamemode
from gui.goal import Goal

from util.subclasses import (
    BestGoalsLabel,
    MilestoneOption,
    SortByAction,
    GamemodeAction,
    GoalAction
)

class BestGoalsUI(object):
    def __init__(self, dialog: QDialog):
        self.win = dialog

    def setupUi(self):
        self.win.setWindowTitle("Best Saved Goals")
        self.win.setWindowIcon(QIcon(path('images', 'yes.png')))
        self.win.resize(900, 300)

        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(11, 14, 7))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        self.win.setPalette(palette)

        self.gridLayout_2 = QGridLayout(self.win)
        self.gridLayout_2.setVerticalSpacing(10)

        self.gridLayout = QGridLayout()

        self.goal_option = QToolButton(self.win)

        palette = QPalette()
        brush = QBrush(QColor(85, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.goal_option.setPalette(palette)

        font = QFont()
        font.setFamily("Minecraftia")
        font.setPointSize(12)
        self.goal_option.setFont(font)
        self.goal_option.setIconSize(QSize(20, 20))
        self.goal_option.setPopupMode(QToolButton.MenuButtonPopup)
        self.goal_option.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.goal_option.setAutoRaise(True)
        self.gridLayout.addWidget(self.goal_option, 0, 4, 1, 1)

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)

        self.arrow = QLabel(self.win)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.arrow.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.arrow.setFont(font)
        self.arrow.setWordWrap(False)
        self.gridLayout.addWidget(self.arrow, 0, 3, 1, 1)

        self.gamemode_option = QToolButton(self.win)
        palette = QPalette()
        brush = QBrush(QColor(85, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.gamemode_option.setPalette(palette)
        font = QFont()
        font.setFamily("Minecraftia")
        font.setPointSize(12)
        font.setBold(True)
        self.gamemode_option.setFont(font)
        self.gamemode_option.setIcon(QIcon(path('images', 'logo.png')))
        self.gamemode_option.setIconSize(QSize(20, 20))
        self.gamemode_option.setPopupMode(QToolButton.MenuButtonPopup)
        self.gamemode_option.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.gamemode_option.setAutoRaise(True)
        self.gridLayout.addWidget(self.gamemode_option, 0, 2, 1, 1)

        self.sort_by_label = QLabel(self.win)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(120, 120, 120))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        self.sort_by_label.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.sort_by_label.setFont(font)
        self.sort_by_label.setWordWrap(False)
        self.gridLayout.addWidget(self.sort_by_label, 0, 7, 1, 1)

        self.sort_by_option = QToolButton(self.win)
        palette = QPalette()
        brush = QBrush(QColor(85, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.sort_by_option.setPalette(palette)
        self.sort_by_option.setPopupMode(QToolButton.MenuButtonPopup)
        self.sort_by_option.setAutoRaise(True)
        self.gridLayout.addWidget(self.sort_by_option, 0, 8, 1, 1)

        self.line = QFrame(self.win)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        self.line.setPalette(palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.gridLayout.addWidget(self.line, 1, 0, 1, 9)

        self.milestone_option = MilestoneOption(self.win)
        palette = QPalette()
        brush = QBrush(QColor(85, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.milestone_option.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        self.milestone_option.setFont(font)
        self.milestone_option.setTristate(True)
        self.milestone_option.setCheckState(1)
        self.gridLayout.addWidget(self.milestone_option, 0, 6, 1, 1)

        self.best_saved_goals_label = QLabel(self.win)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.best_saved_goals_label.setPalette(palette)
        font = QFont()
        font.setFamily("Minecraftia")
        font.setPointSize(12)
        font.setBold(False)
        self.best_saved_goals_label.setFont(font)
        self.best_saved_goals_label.setTextFormat(Qt.PlainText)
        self.gridLayout.addWidget(self.best_saved_goals_label, 0, 0, 1, 2)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.frame = QFrame(self.win)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(110, 0))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(26, 26, 26))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        self.frame.setPalette(palette)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.main_frame = QGridLayout(self.frame)

        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setFrameShape(QFrame.StyledPanel)
        self.scrollArea.setFrameShadow(QFrame.Raised)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 860, 180))
        self.scrollAreaWidgetContents.setAutoFillBackground(True)

        palette = QPalette()
        brush = QBrush(QColor(11, 14, 7))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(18, 18, 18))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        self.scrollAreaWidgetContents.setPalette(palette)

        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)

        line_palette = QPalette()
        brush = QBrush(QColor(170, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        line_palette.setBrush(QPalette.Active, QPalette.Light, brush)
        line_palette.setBrush(QPalette.Inactive, QPalette.Light, brush)

        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)

        self.gridLayout_4 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(0)

        self.goal_frame = QFrame(self.scrollAreaWidgetContents)
        self.goal_frame.setFrameShape(QFrame.StyledPanel)
        self.goal_frame.setFrameShadow(QFrame.Raised)
        self.goal_grid = QGridLayout(self.goal_frame)
        self.goal_grid.setContentsMargins(0, -1, 0, -1)
        spacerItem1 = QSpacerItem(20, 78, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.goal_grid.addItem(spacerItem1, 9999, 0, 1, 1)

        self.goal_label = QLabel(self.goal_frame)
        self.goal_label.setPalette(palette)
        self.goal_label.setFont(font)
        self.goal_grid.addWidget(self.goal_label, 0, 0, 1, 1)

        self.line = QFrame(self.goal_frame)
        self.line.setPalette(line_palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.goal_grid.addWidget(self.line, 1, 0, 1, 1)

        spacerItem = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.goal_grid.addItem(spacerItem, 2, 0, 1, 1)

        self.gridLayout_4.addWidget(self.goal_frame, 0, 2, 2, 1)

        self.milestone_frame = QFrame(self.scrollAreaWidgetContents)
        self.milestone_frame.setFrameShape(QFrame.StyledPanel)
        self.milestone_frame.setFrameShadow(QFrame.Raised)
        self.milestone_grid = QGridLayout(self.milestone_frame)
        self.milestone_grid.setContentsMargins(0, -1, 0, -1)
        spacerItem2 = QSpacerItem(20, 78, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.milestone_grid.addItem(spacerItem2, 9999, 0, 1, 1)

        self.milestone_label = QLabel(self.milestone_frame)
        self.milestone_label.setPalette(palette)
        self.milestone_label.setFont(font)
        self.milestone_grid.addWidget(self.milestone_label, 0, 0, 1, 1)

        self.line = QFrame(self.milestone_frame)
        self.line.setPalette(line_palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.milestone_grid.addWidget(self.line, 1, 0, 1, 1)

        spacerItem = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.milestone_grid.addItem(spacerItem, 2, 0, 1, 1)

        self.gridLayout_4.addWidget(self.milestone_frame, 0, 5, 2, 1)

        self.completed_frame = QFrame(self.scrollAreaWidgetContents)
        self.completed_frame.setFrameShape(QFrame.StyledPanel)
        self.completed_frame.setFrameShadow(QFrame.Raised)
        self.completed_grid = QGridLayout(self.completed_frame)
        self.completed_grid.setContentsMargins(0, -1, 0, -1)
        spacerItem3 = QSpacerItem(20, 78, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.completed_grid.addItem(spacerItem3, 9999, 0, 1, 1)

        self.completed_label = QLabel(self.completed_frame)
        self.completed_label.setPalette(palette)
        self.completed_label.setFont(font)
        self.completed_grid.addWidget(self.completed_label, 0, 0, 1, 1)

        self.line = QFrame(self.completed_frame)
        self.line.setPalette(line_palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.completed_grid.addWidget(self.line, 1, 0, 1, 1)

        spacerItem = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.completed_grid.addItem(spacerItem, 2, 0, 1, 1)

        self.gridLayout_4.addWidget(self.completed_frame, 0, 4, 2, 1)

        self.time_taken_frame = QFrame(self.scrollAreaWidgetContents)
        self.time_taken_frame.setFrameShape(QFrame.StyledPanel)
        self.time_taken_frame.setFrameShadow(QFrame.Raised)
        self.time_taken_grid = QGridLayout(self.time_taken_frame)
        self.time_taken_grid.setContentsMargins(0, -1, 0, -1)
        spacerItem4 = QSpacerItem(20, 78, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.time_taken_grid.addItem(spacerItem4, 9999, 0, 1, 1)

        self.time_taken_label = QLabel(self.time_taken_frame)
        self.time_taken_label.setPalette(palette)
        self.time_taken_label.setFont(font)
        self.time_taken_grid.addWidget(self.time_taken_label, 0, 0, 1, 1)

        self.line = QFrame(self.time_taken_frame)
        self.line.setPalette(line_palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.time_taken_grid.addWidget(self.line, 1, 0, 1, 1)

        spacerItem = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.time_taken_grid.addItem(spacerItem, 2, 0, 1, 1)

        self.gridLayout_4.addWidget(self.time_taken_frame, 0, 3, 2, 1)

        self.started_with_frame = QFrame(self.scrollAreaWidgetContents)
        self.started_with_frame.setFrameShape(QFrame.StyledPanel)
        self.started_with_frame.setFrameShadow(QFrame.Raised)
        self.started_with_grid = QGridLayout(self.started_with_frame)
        self.started_with_grid.setContentsMargins(0, -1, 0, -1)
        spacerItem5 = QSpacerItem(20, 78, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.started_with_grid.addItem(spacerItem5, 9999, 0, 1, 1)

        self.started_with_label = QLabel(self.started_with_frame)
        self.started_with_label.setPalette(palette)
        self.started_with_label.setFont(font)
        self.started_with_grid.addWidget(self.started_with_label, 0, 0, 1, 1)

        self.line = QFrame(self.started_with_frame)
        self.line.setPalette(line_palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.started_with_grid.addWidget(self.line, 1, 0, 1, 1)

        spacerItem = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.started_with_grid.addItem(spacerItem, 2, 0, 1, 1)

        self.gridLayout_4.addWidget(self.started_with_frame, 0, 1, 2, 1)

        self.name_frame = QFrame(self.scrollAreaWidgetContents)
        self.name_frame.setFrameShape(QFrame.StyledPanel)
        self.name_frame.setFrameShadow(QFrame.Raised)
        self.name_grid = QGridLayout(self.name_frame)
        self.name_grid.setContentsMargins(0, -1, 0, -1)
        spacerItem6 = QSpacerItem(20, 78, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.name_grid.addItem(spacerItem6, 9999, 0, 1, 1)

        self.name_label = QLabel(self.name_frame)
        self.name_label.setPalette(palette)
        self.name_label.setFont(font)
        self.name_grid.addWidget(self.name_label, 0, 0, 1, 1)

        self.line = QFrame(self.name_frame)
        self.line.setPalette(line_palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.name_grid.addWidget(self.line, 1, 0, 1, 1)

        spacerItem = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.name_grid.addItem(spacerItem, 2, 0, 1, 1)

        self.gridLayout_4.addWidget(self.name_frame, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.main_frame.addWidget(self.scrollArea, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        QMetaObject.connectSlotsByName(self.win)

class BestGoals(QDialog):
    def __init__(self, completed_goals, goal_organiser, parent=None):
        super().__init__(parent)

        self.setModal(True)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.ui = BestGoalsUI(self)
        self.ui.setupUi()

        self.stars = cycle(['blue.png', 'pink.png'])
        self.second_stars = cycle(['blue.png', 'pink.png'])
        self.completed_goals = completed_goals
        self.goal_organiser = goal_organiser

        self.data = {
            'api_gamemode_name': self.goal_organiser['api_gamemode_name'],
            'gamemode': self.goal_organiser['gamemode'],
            'api_goal_name': self.goal_organiser['api_goal_name'],
            'goal': self.goal_organiser['goal']
        }

        self.names = {
            "SpeedUHC": "SpeedUHC",
            "SkyWars": "SkyWars",
            "Duels": "Duels",
            "Turbo Kart Racers": "GingerBread",
            "BedWars": "Bedwars",
            "UHC": "UHC",
            "VampireZ": "VampireZ",
            "The Pit": "Pit",
            "TNT Games": "TNTGames",
            "Walls": "Walls",
            "Murder Mystery": "MurderMystery",
            "Build Battle": "BuildBattle",
            "Mega Walls": "Walls3",
            "Super Smash Heroes": "SuperSmash",
            "Warlords": "Battleground",
            "Quakecraft": "Quake",
            "Arena Brawl": "Arena",
            "Arcade": "Arcade",
            "Paintball": "Paintball",
            "Blitz Survival Games": "HungerGames",
            "Cops VS Crims": "MCGO",
            "Hypixel": "Hypixel",
            'Wool Wars': 'WoolGames'
        }

        self.locals = {}
        self.indexes = []

        self.ui.best_saved_goals_label.setText("Best Saved Goals:   ")
        self.ui.gamemode_option.setText(self.data['gamemode'])
        self.ui.arrow.setText("➔")
        self.ui.goal_option.setText(self.data['goal'])
        self.ui.milestone_option.setText("Milestone")
        self.ui.sort_by_label.setText("Sort by:")
        self.ui.sort_by_option.setText("Name")

        self.ui.name_label.setText("Name")
        self.ui.started_with_label.setText("Started With")
        self.ui.goal_label.setText("Ended With")
        self.ui.time_taken_label.setText("Time Taken")
        self.ui.completed_label.setText("Completed")
        self.ui.milestone_label.setText("Milestone?")

        self.ui.gamemode_option.clicked.connect(self.setup_gamemode_option)
        self.ui.goal_option.clicked.connect(self.setup_goal_option)

        self.gamemodeMenu = QMenu()
        action = GamemodeAction(self)
        action.setIcon(QIcon(path('images', 'logo.png')))
        action.setText("Hypixel")
        self.gamemodeMenu.addAction(action)
        self.unpack_gamemode_menu()

        self.ui.gamemode_option.setMenu(self.gamemodeMenu)

        self.goalMenu = QMenu()
        self.unpack_goal_menu()

        self.ui.goal_option.setMenu(self.goalMenu)

        self.sortByMenu = QMenu()
        self.unpack_sorting_menu()

        self.ui.sort_by_option.setMenu(self.sortByMenu)

        self.after_gamemode()
        self.after_goal()

        self.ui.milestone_option.setCheckState(self.goal_organiser['milestone'])
        self.ui.sort_by_option.setText(self.goal_organiser['sort_by'])

        self.unpack(self.completed_goals, sorted_key=self.goal_organiser['sort_by'].lower().replace(" ", "_") if self.goal_organiser['sort_by'] != "Ended With" else "goal")

        self.show()

    def unpack(self, completed_goals, sorted_key='name'):
        for index in self.indexes:
            data = self.locals[str(index)]
            data['name'].deleteLater(); del data['name']
            data['goal'].deleteLater(); del data['goal']
            data['started_with'].deleteLater(); del data['started_with']
            data['time_taken'].deleteLater(); del data['time_taken']
            data['completed'].deleteLater(); del data['completed']
            data['milestone'].deleteLater(); del data['milestone']
            del self.locals[str(index)]

        self.ui.name_label.setText("Name")
        self.ui.goal_label.setText("Ended With")
        self.ui.started_with_label.setText("Started With")
        self.ui.time_taken_label.setText("Time Taken")
        self.ui.completed_label.setText("Completed")
        self.ui.milestone_label.setText("Milestone?")
        eval(f'self.ui.{sorted_key}_label.setText("<html><head/><body><p>'
             f'<span>{eval("self.ui."+sorted_key+"_label"+".text()")} </span>'
             f'<span style=\\"color: red\\">#</span>'
             f'</p></body></html>")')

        completed_goals = list(sorted(list(filter(lambda k: k['gamemode'] == self.data['gamemode'] and k['api_goal_name'] == self.data['api_goal_name'], completed_goals)), key=lambda item: item[sorted_key]))

        self.indexes = []
        for index, goal in enumerate(completed_goals):
            self.add_row(goal, index+3)
            self.indexes.append(index+3)

    def add_row(self, data, index):
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setBold(True)
        font.setWeight(75)

        name = BestGoalsLabel(self.completed_goals, self.locals, index, self.ui.name_frame)
        name.setFont(font)
        palette = QPalette()
        brush = QBrush(QColor(85, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        name.setPalette(palette)
        name.setText(data['name'])
        self.ui.name_grid.addWidget(name, index, 0, 1, 1)

        goal = BestGoalsLabel(self.completed_goals, self.locals, index, self.ui.goal_frame)
        goal.setFont(font)
        palette = QPalette()
        brush = QBrush(QColor(255, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        goal.setPalette(palette)
        goal.setText(data['goal'])
        self.ui.goal_grid.addWidget(goal, index, 0, 1, 1)

        started_with = BestGoalsLabel(self.completed_goals, self.locals, index, self.ui.goal_frame)
        started_with.setFont(font)
        palette = QPalette()
        brush = QBrush(QColor(208, 139, 208))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        started_with.setPalette(palette)
        started_with.setText(data['started_with'])
        self.ui.started_with_grid.addWidget(started_with, index, 0, 1, 1)

        time_taken = BestGoalsLabel(self.completed_goals, self.locals, index, self.ui.time_taken_frame)
        time_taken.setFont(font)
        palette = QPalette()
        brush = QBrush(QColor(255, 170, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        time_taken.setPalette(palette)
        time_taken.setText(data['time_taken'])
        self.ui.time_taken_grid.addWidget(time_taken, index, 0, 1, 1)

        completed = BestGoalsLabel(self.completed_goals, self.locals, index, self.ui.completed_frame)
        completed.setFont(font)
        palette = QPalette()
        brush = QBrush(QColor(0, 255, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        completed.setPalette(palette)
        completed.setText(data['completed'])
        self.ui.completed_grid.addWidget(completed, index, 0, 1, 1)

        milestone = BestGoalsLabel(self.completed_goals, self.locals, index, self.ui.milestone_frame)
        milestone.setFont(font)
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        milestone.setPalette(palette)
        milestone.setText(data['milestone'])
        self.ui.milestone_grid.addWidget(milestone, index, 0, 1, 1)

        if (option := self.ui.milestone_option.checkState()) != 1:
            if option == 0:
                result = True if data['milestone'] in ['No', 'INFINITE'] else False
            elif option == 2:
                result = True if data['milestone'] in ['Yes', 'INFINITE'] else False
            name.setVisible(result)
            goal.setVisible(result)
            started_with.setVisible(result)
            time_taken.setVisible(result)
            completed.setVisible(result)
            milestone.setVisible(result)

        local_variables = locals().copy()
        self.locals[str(index)] = local_variables

    def setup_gamemode_option(self):
        self.s = Gamemode(self, not_close=False)

    def setup_goal_option(self):
        self.s = Goal(self, thread=False, not_close=False)

    def unpack_sorting_menu(self):
        sorting = ['Name', 'Started With', 'Ended With', 'Time Taken', 'Completed', 'Milestone']

        for value in sorting:
            action = SortByAction(self)
            action.setText(value)
            action.setIcon(QIcon(path('images', next(self.second_stars))))
            self.sortByMenu.addAction(action)

    def unpack_gamemode_menu(self):
        gamemodes = []
        for goal in self.completed_goals:
            if goal['gamemode'] not in gamemodes:
                gamemodes.append(goal['gamemode'])

        gamemodes = list(sorted(gamemodes))

        for gamemode in gamemodes:
            if gamemode != 'Hypixel':
                action = GamemodeAction(self)
                action.setIcon(QIcon(path('images', 'game-icons', f'{gamemode}.png')))
                action.setText(gamemode)
                self.gamemodeMenu.addAction(action)

    def unpack_goal_menu(self):
        if self.ui.gamemode_option.text() == 'Hypixel':
            name = 'hypixel'
        else:
            name = self.names[self.ui.gamemode_option.text()]
        goalss = list(map(lambda x: list(x.values()), getattr(constants, name.lower())))

        allowed_goals = []
        for goal in goalss:
            allowed_goals.extend(goal)

        goals = []
        for goal in self.completed_goals:
            if goal['api_goal_name'] in allowed_goals and goal['api_goal_name'] not in goals and goal['gamemode'] == self.data['gamemode']:
                goals.append(goal['api_goal_name'])

        itemss = list(map(lambda x: list(x.items()), getattr(constants, name.lower())))
        items = []
        for item in itemss:
            items.extend(item)

        for goal in goals:
            action = GoalAction(self)
            action.setIcon(QIcon(path('images', next(self.stars))))
            for item in items:
                if item[1] == goal:
                    action.setText(item[0])
            self.goalMenu.addAction(action)

        return goals

    def after_gamemode(self):
        self.goalMenu.clear()
        prev = self.ui.gamemode_option.text() # Since it auto-selects a random goal each time a gamemode is chosen, if the same one is chosen then it will not re-select.
        self.ui.gamemode_option.setText(self.data['gamemode'])
        if self.data['gamemode'] == 'Hypixel':
            self.ui.gamemode_option.setText("Hypixel")
            self.ui.gamemode_option.setIcon(QIcon(path('images', 'logo.png')))
        else:
            self.ui.gamemode_option.setIcon(QIcon(path('images', 'game-icons', f'{self.data["gamemode"]}.png')))

        if prev != self.data['gamemode']:
            goals = self.unpack_goal_menu()
            if len(goals) == 0:
                goals = getattr(constants, self.names[self.data['gamemode']].lower())
                goal = goals[random.randint(0, len(goals)-1)]
            else:
                goals__ = getattr(constants, self.names[self.data['gamemode']].lower())
                goals_ = {}
                for goal_ in goals__:
                    goals_.update(goal_)
                goal = dict(filter(lambda x: x[1] in goals, goals_.items()))
            self.ui.goal_option.setText(list(goal.keys())[random.randint(0, len(list(goal.keys()))-1)])
            self.data['goal'] = self.ui.goal_option.text()
            self.data['api_goal_name'] = goal[self.data['goal']]
            self.goal_organiser['goal'] = self.ui.goal_option.text()
            self.goal_organiser['api_goal_name'] = goal[self.data['goal']]

        self.unpack(self.completed_goals, sorted_key=self.ui.sort_by_option.text().lower().replace(" ", "_"))

    def after_goal(self):
        self.ui.goal_option.setText(self.data['goal'])

        self.unpack(self.completed_goals, sorted_key=self.ui.sort_by_option.text().lower().replace(" ", "_"))