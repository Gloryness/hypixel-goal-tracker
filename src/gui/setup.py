from PyQt5.QtCore import QMetaObject, pyqtSlot, pyqtSignal, Qt, QDateTime, QDate, QTime
from PyQt5.QtGui import QFont, QIcon, QBrush, QColor, QPalette, QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import QSizePolicy, QFrame, QGridLayout, QLabel, QSpacerItem, QFormLayout, QHBoxLayout, QVBoxLayout, QToolButton, QComboBox, \
    QDialog

import threading
import random
import datetime
import time as time_
import re

from app import path

from gui.gamemode import Gamemode
from gui.goal import Goal
from gui.time import Time
from app.clock import Clock

from util.determine import DManualSetup
from util.process import processManuals, computeHtml
from util.gamemodes.woolwars.wwlevel import getFormattedWoolWarsLevel
from util.gamemodes.bedwars.bwlevel import getFormattedBedWarsLevel
from util.gamemodes.skywars.swlevel import getFormattedSkyWarsLevel
from util.gamemodes.speeduhc.speedlevel import getFormattedSpeedUhcLevel
from util.gamemodes.uhc.uhclevel import getFormattedUhcLevel
from util.gamemodes.pit.pitlevel import getFormattedPitLevel

from util.subclasses import (
    DoneButton,
    MilestoneCheckBox,
    InfiniteGoalCheckBox,
    InfiniteDurationCheckBox,
    NameLineEdit,
    GoalLineEdit
)

class State:
    def __init__(self, state):
        self.state = state

class SetupUI:
    def __init__(self, dialog: QDialog):
        self.dialog = dialog

    def setup(self):
        self.dialog.setWindowTitle("Goal Setup")
        self.dialog.resize(360, 466)
        self.dialog.setWindowIcon(QIcon(path('images', 'logo.png')))

        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(11, 14, 7))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        self.dialog.setPalette(palette)

        self.formLayout = QFormLayout(self.dialog)
        spacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.formLayout.setItem(3, QFormLayout.LabelRole, spacerItem)

        self.horizontalLayout_5 = QGridLayout()

        self.name_label = QLabel(self.dialog)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.name_label.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.name_label.setFont(font)
        self.horizontalLayout_5.addWidget(self.name_label, 0, 0, 1, 1)

        self.name = NameLineEdit(self, self.dialog)
        palette = QPalette()
        brush = QBrush(QColor(0, 170, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(11, 14, 7))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(0, 170, 0, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        self.name.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        self.name.setFont(font)
        self.name.setMaxLength(45)
        self.name.setFrame(False)
        self.horizontalLayout_5.addWidget(self.name, 0, 1, 1, 1)

        self.formLayout.setLayout(1, QFormLayout.SpanningRole, self.horizontalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.goal_setup_label = QLabel(self.dialog)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.goal_setup_label.setPalette(palette)
        font = QFont()
        font.setFamily("Minecraftia")
        font.setPointSize(12)
        self.goal_setup_label.setFont(font)
        self.verticalLayout.addWidget(self.goal_setup_label)

        self.goal_setup_line = QFrame(self.dialog)
        self.goal_setup_line.setFrameShadow(QFrame.Raised)
        self.goal_setup_line.setFrameShape(QFrame.HLine)
        self.verticalLayout.addWidget(self.goal_setup_line)

        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.verticalLayout)

        self.done = DoneButton(self, self.dialog)
        palette = QPalette()
        brush = QBrush(QColor(170, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.done.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.done.setFont(font)
        self.done.setAutoDefault(False)
        self.formLayout.setWidget(9, QFormLayout.SpanningRole, self.done)

        self.gridLayout = QGridLayout()
        self.current_amount = QLabel(self.dialog)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.current_amount.setPalette(palette)
        font = QFont()
        font.setFamily("Minecraft")
        font.setPointSize(16)
        font.setBold(False)
        font.setLetterSpacing(QFont.PercentageSpacing, 95)
        self.current_amount.setFont(font)
        self.current_amount.setTextFormat(Qt.MarkdownText)
        self.gridLayout.addWidget(self.current_amount, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.goal_amount_label = QLabel(self.dialog)
        palette = QPalette()
        brush = QBrush(QColor(255, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.goal_amount_label.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.goal_amount_label.setFont(font)
        self.goal_amount_label.setTextFormat(Qt.PlainText)
        self.horizontalLayout_3.addWidget(self.goal_amount_label)

        self.goal_amount_info = QLabel(self.dialog)
        palette = QPalette()
        brush = QBrush(QColor(255, 161, 28))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.goal_amount_info.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(7)
        self.goal_amount_info.setFont(font)
        self.gridLayout.addWidget(self.goal_amount_info, 6, 0, 1, 1)

        self.goal_amount = GoalLineEdit(self, self.dialog)
        self.goal_amount.setValidator(QIntValidator(bottom=0))
        palette = QPalette()
        brush = QBrush(QColor(255, 170, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(11, 14, 7))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        brush = QBrush(QColor(225, 150, 225, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
        self.goal_amount.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.goal_amount.setFont(font)
        self.goal_amount.setMaxLength(16)
        self.goal_amount.setFrame(False)
        self.horizontalLayout_3.addWidget(self.goal_amount)

        self.milestone = MilestoneCheckBox(self, self.dialog)
        palette = QPalette()
        brush = QBrush(QColor(255, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.milestone.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.milestone.setFont(font)
        self.horizontalLayout_3.addWidget(self.milestone)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.gamemode_label = QLabel(self.dialog)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.gamemode_label.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.gamemode_label.setFont(font)
        self.gamemode_label.setTextFormat(Qt.MarkdownText)
        self.horizontalLayout.addWidget(self.gamemode_label)
        self.gamemode = QToolButton(self.dialog)
        self.gamemode.setIcon(QIcon(path('images', 'plus.svg')))
        self.gamemode.setAutoRaise(True)
        self.horizontalLayout.addWidget(self.gamemode)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.invisible_label = QLabel(self.dialog)
        self.invisible_label.setText("")
        self.gridLayout.addWidget(self.invisible_label, 3, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.goal_label = QLabel(self.dialog)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.goal_label.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.goal_label.setFont(font)
        self.goal_label.setTextFormat(Qt.MarkdownText)
        self.horizontalLayout_2.addWidget(self.goal_label)

        self.goal = QToolButton(self.dialog)
        self.goal.setIcon(QIcon(path('images', 'plus.svg')))
        self.goal.setAutoRaise(True)
        self.horizontalLayout_2.addWidget(self.goal)

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.formLayout.setLayout(2, QFormLayout.SpanningRole, self.gridLayout)
        self.horizontalLayout_4 = QHBoxLayout()

        self.timeLeft = QLabel(self.dialog)
        palette = QPalette()
        brush = QBrush(QColor(45, 255, 42))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.timeLeft.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.timeLeft.setFont(font)
        self.timeLeft.setTextFormat(Qt.MarkdownText)
        self.horizontalLayout_4.addWidget(self.timeLeft)

        self.change = QToolButton(self.dialog)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush = QBrush(QColor(120, 120, 120, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        self.change.setPalette(palette)
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.change.setFont(font)
        self.change.setAutoRaise(True)
        self.horizontalLayout_4.addWidget(self.change)
        self.formLayout.setLayout(8, QFormLayout.SpanningRole, self.horizontalLayout_4)

        QMetaObject.connectSlotsByName(self.dialog)

    def extra(self):
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setWeight(50)

        self.requirement_layout = QHBoxLayout()

        self.requirement_label = QLabel(self.dialog)
        self.requirement_label.setText("<html><head/><body><p><span style=\" color:#aaff00;\">Show live goal requirement in...</span></p></body></html>")

        self.requirement = QComboBox(self.dialog)
        self.requirement.addItems(["months", "weeks", "days", "hours", "minutes", "seconds"])
        self.requirement.setCurrentIndex(3)

        self.requirement_layout.addWidget(self.requirement_label)
        self.requirement_layout.addWidget(self.requirement)

        self.formLayout.setLayout(4, QFormLayout.LabelRole, self.requirement_layout)

        self.requirement_example = QLabel(self.dialog)
        self.requirement_example.setText("<html><head/><body><p><span style=\" color:#aaff00;\">Example:</span><span style=\" font-weight:600; color:#ffffff\">2 Solo Kills/minute </span><span style=\" color:#aaff00;\">required to complete goal</span></p></body></html>")

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.requirement_example)

        palette = QPalette()
        brush = QBrush(QColor(170, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)

        self.infiniteGoalCheck = InfiniteGoalCheckBox(self, self.dialog)
        self.infiniteGoalCheck.setFont(font)
        self.infiniteGoalCheck.setPalette(palette)
        self.infiniteGoalCheck.setText("Enable an infinite goal amount")
        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.infiniteGoalCheck)

        self.infiniteDurationCheck = InfiniteDurationCheckBox(self, self.dialog)
        self.infiniteDurationCheck.setFont(font)
        self.infiniteDurationCheck.setPalette(palette)
        self.infiniteDurationCheck.setText("Enable infinite duration")
        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.infiniteDurationCheck)

class Setup(QDialog):
    closeWin = pyqtSignal()
    set = pyqtSignal(str)
    showw = pyqtSignal()

    def __init__(self, win, auto={}, parent=None):
        super().__init__(parent)
        self.win = win
        self.auto = auto
        self.setModal(True)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.closed = False

        self.setStyleSheet("QLineEdit { background-color: rgba(0, 0, 0, 0); }")

        self.data = {}
        self.value = 0
        self.already_called_api = False

        self.ui = SetupUI(self)
        self.ui.setup()
        self.ui.extra()

        self.api_sync = self.win.api_sync

        self.clock = Clock(0, 0, 0, random.randint(1, 23), random.randint(1, 60), 0)
        self.change_time(self.clock.format())
        self.ui.change.setEnabled(True)

        self.data['clock'] = self.clock.format()
        self.data['status'] = 'INCOMPLETE'
        self.data['seconds'] = 0 # time spent on the goal
        self.data['paused_seconds'] = 0
        self.data['goal'] = ""
        self.data['api_goal_name'] = ""
        self.data['gamemode'] = ""
        self.data['api_gamemode_name'] = ""

        self.ui.name_label.setText("Name:")
        self.ui.name.setPlaceholderText("____")
        self.ui.goal_setup_label.setText(f"Hypixel Goal Setup")
        self.ui.done.setText("Done")
        self.ui.current_amount.setText("<html><head/><body><p><span style=\" color:#2ed0bd;\">: </span><span style=\" font-weight:600; color:#e51be5;\">...</span></p></body></html>")
        self.ui.goal_amount_label.setText("Goal Amount:")
        self.ui.goal_amount.setPlaceholderText("____")
        self.ui.milestone.setText("Milestone")
        self.ui.gamemode_label.setText("<html><head/><body><p>Gamemode:</p></body></html>")
        self.ui.goal_amount_info.setText("<html><head/><body><p><span style=\" font-size:8pt; color:#ff557f;\">For example, if your current wins are 50 and you want to<br/>reach 75, simply enter 25 into this box instead of 75.<br/></span><span style=\" font-size:8pt; color:#ff40e0;\">To change this, simply tick the Milstone checkbox.</span></p></body></html>")
        self.ui.goal_label.setText("<html><head/><body><p>Goal:</p></body></html>")
        self.ui.goal.setText("Browse")
        self.ui.change.setText("CHANGE")

        self.ui.current_amount.hide()

        self.ui.gamemode.clicked.connect(self.setup_gamemode)
        self.ui.goal.clicked.connect(self.setup_goal)
        self.ui.change.clicked.connect(self.setup_time)
        if self.auto == {}:
            self.ui.done.clicked.connect(lambda: self.win.add_goal(self, self.data))
        else:
            if self.auto['api_goal_name'] == "networkExpp":
                self.ui.goal_amount.setValidator(QDoubleValidator(decimals=2))

            def edit_goal():
                self.data['requirement'] = self.ui.requirement.currentText()
                self.win.edit_goal(self.auto['index'], self.data)

            self.ui.done.clicked.connect(edit_goal)

            if 'complete_by' in self.auto:
                self.queues = []

                state = State("active")
                self.queues.append(state)

                complete_by = self.auto['complete_by']
                dateTime = QDateTime(
                    QDate(complete_by['year'], complete_by['month'], complete_by['day']),
                    QTime(complete_by['hour'], complete_by['minute'], complete_by['second'])
                )
                self.completeBy = dateTime
                thread = threading.Timer(0.1, self.auto_update, args=(dateTime, state))
                thread.start()

        self.ui.goal_amount.setDisabled(True)
        self.ui.gamemode.setDisabled(True)
        self.ui.goal.setDisabled(True)
        self.ui.gamemode_label.setDisabled(True)
        self.ui.goal_label.setDisabled(True)
        self.ui.done.setDisabled(True)

        self.closeWin.connect(self.closeWindow)
        self.set.connect(self.setText)
        self.showw.connect(self.showText)

        if self.auto != {}:
            self.data = self.auto.copy()
            self.ui.requirement.setCurrentText(self.data['requirement'])
            self.value = self.data['current_amount']
            self.unpack_data(self.data)

        self.show()

    def add_task(self, data):
        if len(self.queues) > 0:
            self.queues[-1].state = "break"
        state = State("active")
        self.queues.append(state)

        dateTime = QDateTime(
            QDate(data['year'], data['month'], data['day']),
            QTime(data['hour'], data['minute'], data['second'])
        )
        self.completeBy = dateTime
        thread = threading.Thread(target=self.auto_update, args=(dateTime, state))
        thread.start()

    def auto_update(self, dateTime, state):
        while self.isVisible() and state.state != "break":
            date, time = dateTime.date(), dateTime.time()
            a = datetime.datetime.now()
            b = datetime.datetime(date.year(), date.month(), date.day(), time.hour(), time.minute(), time.second())
            delta = b - a

            self.clock.days = delta.days
            self.clock.hours = 0
            self.clock.minutes = 0
            self.clock.seconds = delta.seconds + (1 if delta.microseconds / 10000 > 50 else 0)

            if self.auto:
                if self.clock.days == 0 and self.clock.seconds <= 9:
                    if hasattr(self, 't'):
                        if self.t.isVisible():
                            self.t.closeWin.emit()
                    self.closeWin.emit()
                    state.state = "break"
                    return

            if (self.clock.days <= 0 and self.clock.seconds <= 0) or self.clock.days < 0:
                self.ui.timeLeft.setText(f"<html><head/><body><p><span style=\" font-size:9pt; color:#30df30;\">You have </span><span style=\" font-size:9pt; font-weight:600; color:#FF4242;\">0s</span><span style=\" font-size:9pt; color:#30df30;\"> left to complete this goal.</span></p></body></html>")
                self.ui.done.setEnabled(False)
                state.state = "break"
                return

            self.data['clock'] = self.clock.format()
            self.completeBy = dateTime

            if state.state == "break":
                return

            self.change_time(self.clock.format())

            time_.sleep(1.0)

    def closeEvent(self, event):
        if hasattr(self, 'queues'):
            self.queues[-1].state = "break"

        if not self.closed:
            if self.auto != {}:
                self.win.edit_goal(self.auto['index'], self.data)

    def setup_gamemode(self):
        self.s = Gamemode(self)

    def setup_goal(self):
        self.s = Goal(self)

    def setup_time(self):
        self.t = Time(self.clock, self)

    def unpack_data(self, data):
        self.ui.infiniteDurationCheck.setDisabled(True)
        self.ui.infiniteGoalCheck.setDisabled(True)
        self.ui.name.setText(data['name'])
        self.ui.gamemode_label.setText(f"<html><head/><body><p>Gamemode: <span style=\" font-weight:600; color:#1da8c7;\">{data['gamemode']}</span></p></body></html>")
        self.ui.goal_label.setText(f"<html><head/><body><p>Goal: <span style=\" font-weight:600; color:#1da8c7;\">{data['goal']}</span></p></body></html>")

        goal_value = data['current_amount'] if data['milestone'] else data['starting_amount']

        try:
            gv = f"{goal_value:,}"
        except:
            gv = goal_value

        if self.data['api_goal_name'] == 'Experience':
            gv = computeHtml(getFormattedBedWarsLevel(goal_value))
        elif self.data['api_goal_name'] == 'woolwars_level':
            gv = computeHtml(getFormattedWoolWarsLevel(goal_value))
        elif self.data['api_goal_name'] == 'levelFormatted':
            gv = computeHtml(getFormattedSkyWarsLevel(goal_value, self.data['skywars_star']))
        elif self.data['api_goal_name'] == 'smashLevel':
            gv = computeHtml(f"&b{goal_value}&6✶")
        elif self.data['api_goal_name'] == "speeduhc_level":
            gv = computeHtml(getFormattedSpeedUhcLevel(goal_value))
        elif self.data['api_goal_name'] == "uhc_level":
            gv = computeHtml(getFormattedUhcLevel(goal_value))
        elif self.data['api_goal_name'] == "pit_level":
            gv = computeHtml(getFormattedPitLevel(self.data['pit_prestige'], goal_value))

        self.ui.goal_amount.setDisabled(False)
        self.ui.goal_amount_info.setText("<html><head/><body><p><span style=\" font-size:8pt; color:#ff557f;\">You cannot toggle milstone during editing.</span></p></body></html>")
        self.ui.goal_amount_info.setVisible(True)

        self.ui.current_amount.setText(f"<html><head/><body><p><span style=\" color:#2ed0bd;\">{data['goal']}: </span><span style=\" font-weight:600; color:#e51be5;\">{gv}</span></p></body></html>")
        if data['goal_amount'] == 'infinite':
            self.ui.goal_amount.setText("∞")
            self.ui.goal_amount.setDisabled(True)
            self.ui.goal_amount_info.setText('<html><head/><body><p><span style=" font-size:8pt; font-weight:600; color:#ffffff;">In this instance - you do </span><span style=" font-size:8pt; font-weight:600; color:#00ffff;">not</span><span style=" font-size:8pt; font-weight:600; color:#ffffff;"> have a goal to reach.<br/>You just try the best you can before the time runs out for the goal.</span></p></body></html>')
            self.ui.goal_amount_info.setVisible(True)
        else:
            self.ui.goal_amount.setText(str(data['goal_amount']))
        if data['clock'] == '∞':
            self.ui.change.setDisabled(True)
        self.change_time(data['clock'])
        if data['clock'] != '∞':
            self.clock = Clock().fromFormat(data['clock'])
        else:
            self.clock = '∞'
        self.ui.current_amount.show()
        self.ui.gamemode.setDisabled(True)
        self.ui.goal.setDisabled(True)
        self.ui.gamemode_label.setDisabled(False)
        self.ui.goal_label.setDisabled(False)
        self.ui.done.setDisabled(False)
        self.ui.milestone.setChecked(data['milestone'])
        self.ui.milestone.setDisabled(True)

    def change_time(self, time):
        self.ui.timeLeft.setText(f"<html><head/><body><p><span style=\" font-size:9pt; color:#30df30;\">You have </span><span style=\" font-size:9pt; font-weight:600; color:#3971ff;\">{time}</span><span style=\" font-size:9pt; color:#30df30;\"> left to complete this goal.</span></p></body></html>")

    def after_gamemode(self):
        self.ui.gamemode_label.setText(f"<html><head/><body><p>Gamemode: <span style=\" font-weight:600; color:#1da8c7;\">{self.data['gamemode']}</span></p></body></html>")
        self.ui.goal_label.setText("<html><head/><body><p>Goal:</p></body></html>")
        self.ui.goal_amount.setDisabled(True)
        if not self.ui.infiniteGoalCheck.isEnabled():
            self.ui.goal_amount.clear()
        self.ui.current_amount.hide()
        if 'goal' in self.data:
            del self.data['goal']
            del self.data['api_goal_name']
        self.ui.goal.setDisabled(False)
        self.ui.goal_label.setDisabled(False)
        self.ui.done.setDisabled(True)

    def after_goal_(self):
        thread = threading.Thread(target=self.after_goal)
        thread.start()

    def after_goal(self):
        def api_call():
            if self.already_called_api:
                return False
            elif self.api_sync.syncing and self.api_sync.request_wait <= 10.00:
                if self.data['api_goal_name'] == "records" and self.api_sync.friend_stats == {}:
                    return True
                elif self.data['api_goal_name'] != "records" and self.api_sync.player_stats == {}:
                    return True
                return False
            return True

        if api_call():
            self.api_sync.start_session_sync(limit=True, friends_req=self.data['api_goal_name'] == "records")
            self.api_sync.thread.join()
            self.already_called_api = True

        self.ui.goal_label.setText(f"<html><head/><body><p>Goal: <span style=\" font-weight:600; color:#1da8c7;\">{self.data['goal']}</span></p></body></html>")

        goal_value = '...'

        determine = DManualSetup(self.data['api_gamemode_name'], self.data['api_goal_name'])
        isManual = determine.is_manual_needed()

        try:
            if self.data['api_gamemode_name'] == 'Hypixel':
                if self.data['api_goal_name'] not in ['records', 'networkExpp', 'general_challenger']:
                    goal_value = self.api_sync.player_stats[self.data['api_goal_name']]
            else:
                stats = self.api_sync.player_stats['stats'][self.data['api_gamemode_name']]
        except:
            isManual = 'timeout'

        if not self.ui.infiniteGoalCheck.isChecked() and isManual != 'timeout':
            self.ui.goal_amount.setDisabled(False)

        if isManual == 'timeout':
            goal_value = "Failed to get player stats."
            self.ui.goal_amount.setDisabled(True)
            self.ui.done.setDisabled(True)

        elif not isManual:
            if self.data['api_gamemode_name'] != 'Hypixel':
                try:
                    if self.data['api_gamemode_name'] == 'Pit':
                        if self.data['api_goal_name'] not in stats['profile']:
                            goal_value = stats['pit_stats_ptl'][self.data['api_goal_name']]
                        else:
                            goal_value = round(stats['profile'][self.data['api_goal_name']])
                    elif self.data['api_gamemode_name'] == 'WoolGames':
                        if self.data['api_goal_name'] == 'available_layers':
                            goal_value = stats['progression'][self.data['api_goal_name']]
                        elif self.data['api_goal_name'] == 'coins':
                            goal_value = stats[self.data['api_goal_name']]
                        else:
                            goal_value = stats['wool_wars']['stats'][self.data['api_goal_name']]
                    else:
                        goal_value = stats[self.data['api_goal_name']]
                except:
                    goal_value = 0

        else:
            try:
                goal_value = processManuals(self.data['api_goal_name'], self.data['api_gamemode_name'], self.api_sync)
            except:
                goal_value = 0

        try:
            if self.data['api_goal_name'] != 'levelFormatted' and 'skywars_star' in self.data:
                del self.data['skywars_star']
            if self.data['api_goal_name'] != 'pit_level' and 'pit_prestige' in self.data:
                del self.data['pit_prestige']

            if self.data['api_goal_name'] == 'Experience':
                gv = computeHtml(getFormattedBedWarsLevel(goal_value))
            elif self.data['api_goal_name'] == 'woolwars_level':
                gv = computeHtml(getFormattedWoolWarsLevel(goal_value))
            elif self.data['api_goal_name'] == 'levelFormatted':
                if 'levelFormatted' in stats:
                    self.data['skywars_star'] = stats['levelFormatted']
                else:
                    self.data['skywars_star'] = "⋆"
                self.data['skywars_star'] = re.sub("\d|[a-f]|k|r|l|§", "", self.data['skywars_star'])
                gv = computeHtml(getFormattedSkyWarsLevel(goal_value, self.data['skywars_star']))
            elif self.data['api_goal_name'] == 'smashLevel':
                gv = computeHtml(f"&b{goal_value}&6✶")
            elif self.data['api_goal_name'] == "speeduhc_level":
                gv = computeHtml(getFormattedSpeedUhcLevel(goal_value))
            elif self.data['api_goal_name'] == "uhc_level":
                gv = computeHtml(getFormattedUhcLevel(goal_value))
            elif self.data['api_goal_name'] == "pit_level":
                try:
                    self.data['pit_prestige'] = len(stats['profile']['prestiges'])
                except:
                    self.data['pit_prestige'] = 0
                gv = computeHtml(getFormattedPitLevel(self.data['pit_prestige'], goal_value))

            else:
                gv = f"{goal_value:,}"

            gv = gv.replace("; font-size: 12pt", "")
        except:
            gv = goal_value

        self.set.emit(f"<html><head/><body><p><span style=\" color:#2ed0bd;\">{self.data['goal']}: </span><span style=\"color : #e51be5\">{gv}</span></p></body></html>")
        self.showw.emit()

        self.value = goal_value
        self.data['current_amount'] = self.value

        if self.data['api_goal_name'] == "networkExpp":
            self.ui.goal_amount.setValidator(QDoubleValidator(decimals=2, bottom=0.0))
        else:
            self.ui.goal_amount.setValidator(QIntValidator(bottom=0))

        if self.ui.milestone.isEnabled():
            if self.ui.milestone.isChecked() and (self.ui.goal_amount.text() != "" and int(self.ui.goal_amount.text()) > goal_value):
                self.ui.done.setDisabled(False)
            elif self.ui.milestone.isChecked() and (self.ui.goal_amount.text() == "" or int(self.ui.goal_amount.text()) <= goal_value):
                self.ui.done.setDisabled(True)
            elif not self.ui.milestone.isChecked() and self.ui.goal_amount.text() != "":
                self.ui.done.setDisabled(False)
            else:
                self.ui.done.setDisabled(True)
        else:
            self.ui.done.setDisabled(False)

    @pyqtSlot()
    def closeWindow(self):
        self.close()

    @pyqtSlot(str)
    def setText(self, value):
        self.ui.current_amount.setText(value)

    @pyqtSlot()
    def showText(self):
        self.ui.current_amount.show()