from PyQt5.QtCore import QMetaObject, QSize, QRect, QStringListModel, Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon, QBrush, QColor, QPalette
from PyQt5.QtWidgets import QSizePolicy, QFrame, QWidget, QScrollArea, QGridLayout, QLabel, QSpacerItem, QDialog
import threading

from app import path
from util.subclasses import CompletedGoalsLabel

class CompletedGoalsUI:
    def __init__(self, dialog: QDialog):
        self.win = dialog

    def setupUi(self):
        self.win.setWindowTitle("Completed Goals")
        self.win.setWindowIcon(QIcon(path('images', 'yes.png')))
        self.win.resize(1050, 290)

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

        self.gridLayout = QGridLayout()

        self.completed_goals_label = QLabel(self.win)
        self.completed_goals_label.setMinimumSize(QSize(822, 0))
        palette = QPalette()
        brush = QBrush(QColor(196, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush = QBrush(QColor(196, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush = QBrush(QColor(120, 120, 120))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        self.completed_goals_label.setPalette(palette)
        font = QFont()
        font.setFamily("Minecraftia")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.completed_goals_label.setFont(font)

        self.gridLayout.addWidget(self.completed_goals_label, 1, 0, 1, 1)
        self.symbol = QLabel(self.win)
        self.symbol.setMaximumSize(QSize(22, 22))
        self.symbol.setPixmap(QPixmap(path('images', 'yes.png')))
        self.symbol.setScaledContents(True)

        self.gridLayout.addWidget(self.symbol, 1, 1, 1, 1)
        self.line = QFrame(self.win)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush)
        brush = QBrush(QColor(255, 255, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush)
        brush = QBrush(QColor(255, 255, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush)
        self.line.setPalette(palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)
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

        ############################################## Name

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

        ############################################## Gamemode

        self.gamemode_frame = QFrame(self.scrollAreaWidgetContents)
        self.gamemode_frame.setFrameShape(QFrame.StyledPanel)
        self.gamemode_frame.setFrameShadow(QFrame.Raised)
        self.gamemode_grid = QGridLayout(self.gamemode_frame)
        self.gamemode_grid.setContentsMargins(0, -1, 0, -1)
        spacerItem6 = QSpacerItem(20, 78, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gamemode_grid.addItem(spacerItem6, 9999, 0, 1, 1)

        self.gamemode_label = QLabel(self.gamemode_frame)
        self.gamemode_label.setPalette(palette)
        self.gamemode_label.setFont(font)
        self.gamemode_grid.addWidget(self.gamemode_label, 0, 0, 1, 1)

        self.line = QFrame(self.gamemode_frame)
        self.line.setPalette(line_palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.gamemode_grid.addWidget(self.line, 1, 0, 1, 1)

        spacerItem = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gamemode_grid.addItem(spacerItem, 2, 0, 1, 1)

        self.gridLayout_4.addWidget(self.gamemode_frame, 0, 1, 1, 1)

        ############################################## Completed

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

        self.gridLayout_4.addWidget(self.completed_frame, 0, 2, 1, 1)

        ############################################## Started With

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

        self.gridLayout_4.addWidget(self.started_with_frame, 0, 3, 1, 1)

        ############################################## Goal

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

        self.gridLayout_4.addWidget(self.goal_frame, 0, 4, 1, 1)

        ############################################## Time Taken

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

        self.gridLayout_4.addWidget(self.time_taken_frame, 0, 5, 1, 1)

        ############################################## Paused Time

        self.paused_time_frame = QFrame(self.scrollAreaWidgetContents)
        self.paused_time_frame.setFrameShape(QFrame.StyledPanel)
        self.paused_time_frame.setFrameShadow(QFrame.Raised)
        self.paused_time_grid = QGridLayout(self.paused_time_frame)
        self.paused_time_grid.setContentsMargins(0, -1, 0, -1)
        spacerItem4 = QSpacerItem(20, 78, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.paused_time_grid.addItem(spacerItem4, 9999, 0, 1, 1)

        self.paused_time_label = QLabel(self.paused_time_frame)
        self.paused_time_label.setPalette(palette)
        self.paused_time_label.setFont(font)
        self.paused_time_grid.addWidget(self.paused_time_label, 0, 0, 1, 1)

        self.line = QFrame(self.paused_time_frame)
        self.line.setPalette(line_palette)
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.paused_time_grid.addWidget(self.line, 1, 0, 1, 1)

        spacerItem = QSpacerItem(0, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.paused_time_grid.addItem(spacerItem, 2, 0, 1, 1)

        self.gridLayout_4.addWidget(self.paused_time_frame, 0, 6, 1, 1)

        ############################################## Milestone

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

        self.gridLayout_4.addWidget(self.milestone_frame, 0, 7, 1, 1)

        ##############################################

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.main_frame.addWidget(self.scrollArea, 2, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)

        QMetaObject.connectSlotsByName(self.win)

class CompletedGoals(QDialog):
    def __init__(self, completed_goals, parent=None):
        super().__init__(parent)

        self.setModal(True)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.ui = CompletedGoalsUI(self)
        self.ui.setupUi()

        self.ui.name_label.setText("Name")
        self.ui.gamemode_label.setText("Gamemode ➔ Goal")
        self.ui.completed_label.setText("Completed")
        self.ui.goal_label.setText("Goal/Result")
        self.ui.started_with_label.setText("Started With")
        self.ui.time_taken_label.setText("Time Taken")
        self.ui.paused_time_label.setText("Paused Time")
        self.ui.milestone_label.setText("Milestone?")

        self.completed_goals = completed_goals

        self.ui.completed_goals_label.setText(f"{len(self.completed_goals)} Completed Goal{'s' if len(self.completed_goals) != 1 else ''}")

        self.locals = {}
        self.name_widths = []
        self.gamemode_widths = []
        self.goal_widths = []
        self.started_with_widths = []
        self.time_taken_widths = []
        self.paused_time_widths = []
        self.completed_widths = []

        self.unpack(self.completed_goals)

        self.show()

    def unpack(self, completed_goals):
        for index, goal in enumerate(completed_goals, start=2):
            self.add_row(goal, index)
        event = threading.Event()
        event.wait(0.4)
        try:
            self.ui.name_label.setMinimumSize(QSize(sum(self.name_widths) / len(self.name_widths), 13))
            self.ui.gamemode_label.setMinimumSize(QSize(sum(self.gamemode_widths) / len(self.gamemode_widths), 13))
            self.ui.goal_label.setMinimumSize(QSize(sum(self.goal_widths) / len(self.goal_widths), 13))
            self.ui.started_with_label.setMinimumSize(QSize(sum(self.started_with_widths) / len(self.started_with_widths), 13))
            self.ui.time_taken_label.setMinimumSize(QSize(sum(self.time_taken_widths) / len(self.time_taken_widths), 13))
            self.ui.paused_time_label.setMinimumSize(QSize(sum(self.paused_time_widths) / len(self.paused_time_widths), 13))
            self.ui.completed_label.setMinimumSize(QSize(sum(self.completed_widths) / len(self.completed_widths), 13))
        except:
            pass

    def add_row(self, data, index):
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setBold(True)
        font.setWeight(75)

        name = CompletedGoalsLabel(self.completed_goals, self.locals, index, self.ui.name_frame)
        name.setFont(font)
        palette = QPalette()
        brush = QBrush(QColor(85, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        name.setPalette(palette)
        name.setText(data['name'])
        self.ui.name_grid.addWidget(name, index, 0, 1, 1)

        gamemode = CompletedGoalsLabel(self.completed_goals, self.locals, index, self.ui.gamemode_frame)
        gamemode.setFont(font)
        palette = QPalette()
        brush = QBrush(QColor(255, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        gamemode.setPalette(palette)
        gamemode.setText(data['gamemode'] + ' ➔ ' + data['goal_name'])
        self.ui.gamemode_grid.addWidget(gamemode, index, 0, 1, 1)

        goal = CompletedGoalsLabel(self.completed_goals, self.locals, index, self.ui.goal_frame)
        goal.setFont(font)
        palette = QPalette()
        brush = QBrush(QColor(255, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        goal.setPalette(palette)
        goal.setText(data['goal'])
        self.ui.goal_grid.addWidget(goal, index, 0, 1, 1)

        started_with = CompletedGoalsLabel(self.completed_goals, self.locals, index, self.ui.goal_frame)
        started_with.setFont(font)
        palette = QPalette()
        brush = QBrush(QColor(208, 139, 208))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        started_with.setPalette(palette)
        started_with.setText(data['started_with'])
        self.ui.started_with_grid.addWidget(started_with, index, 0, 1, 1)

        time_taken = CompletedGoalsLabel(self.completed_goals, self.locals, index, self.ui.time_taken_frame)
        time_taken.setFont(font)
        palette = QPalette()
        brush = QBrush(QColor(255, 170, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        time_taken.setPalette(palette)
        time_taken.setText(data['time_taken'])
        self.ui.time_taken_grid.addWidget(time_taken, index, 0, 1, 1)

        paused_time = CompletedGoalsLabel(self.completed_goals, self.locals, index, self.ui.paused_time_frame)
        paused_time.setFont(font)
        palette = QPalette()
        brush = QBrush(QColor(255, 170, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        paused_time.setPalette(palette)
        paused_time.setText(data['paused_time'])
        self.ui.paused_time_grid.addWidget(paused_time, index, 0, 1, 1)

        completed = CompletedGoalsLabel(self.completed_goals, self.locals, index, self.ui.completed_frame)
        completed.setFont(font)
        palette = QPalette()
        brush = QBrush(QColor(0, 255, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        completed.setPalette(palette)
        completed.setText(data['completed'])
        self.ui.completed_grid.addWidget(completed, index, 0, 1, 1)

        milestone = CompletedGoalsLabel(self.completed_goals, self.locals, index, self.ui.milestone_frame)
        milestone.setFont(font)
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        milestone.setPalette(palette)
        milestone.setText(data['milestone'])
        self.ui.milestone_grid.addWidget(milestone, index, 0, 1, 1)

        local_variables = locals().copy()
        self.locals[str(index)] = local_variables
        thread = threading.Timer(0.1, lambda: self.sort(local_variables))
        thread.start()

    def sort(self, data):
        self.name_widths.append(data['name'].width() + 20)
        self.gamemode_widths.append(data['gamemode'].width() + 20)
        self.goal_widths.append(data['goal'].width() + 20)
        self.started_with_widths.append(data['started_with'].width() + 20)
        self.time_taken_widths.append(data['time_taken'].width() + 20)
        self.paused_time_widths.append(data['paused_time'].width() + 20)
        self.completed_widths.append(data['completed'].width() + 20)