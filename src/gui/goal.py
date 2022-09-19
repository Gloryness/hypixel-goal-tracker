from PyQt5.QtCore import QMetaObject, QSize, Qt
from PyQt5.QtGui import QFont, QBrush, QColor, QPalette, QIcon
from PyQt5.QtWidgets import QFormLayout, QGridLayout, QLabel, QDialog

from app import path
from util import constants
from util.subclasses import GoalToolButton

class GoalUI(object):
    def __init__(self, dialog: QDialog):
        self.dialog = dialog

        palette = QPalette()
        brush = QBrush(QColor(255, 170, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.palette = palette

        palette = QPalette()
        brush = QBrush(QColor(85, 255, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.green_palette = palette

        palette = QPalette()
        brush = QBrush(QColor(0, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.cyan_palette = palette

        palette = QPalette()
        brush = QBrush(QColor(239, 239, 119))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.yellow_palette = palette

        palette = QPalette()
        brush = QBrush(QColor(255, 85, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.orange_palette = palette

        palette = QPalette()
        brush = QBrush(QColor(170, 85, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.brown_palette = palette

        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.red_palette = palette

        palette = QPalette()
        brush = QBrush(QColor(0, 85, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.blue_palette = palette

        palette = QPalette()
        brush = QBrush(QColor(170, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.purple_palette = palette

        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.white_palette = palette

        font = QFont()
        font.setFamily("Rockwell Extra Bold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.arrow_font = font

        font = QFont()
        font.setFamily("Minecraftia")
        font.setPointSize(12)
        self.font = font

    def setupUi(self):
        self.dialog.setWindowTitle("Choose Goal")
        self.dialog.resize(640, 200)
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

        self.gridLayout_5 = QGridLayout(self.dialog)

        self.layout_1 = QFormLayout()
        self.layout_2 = QFormLayout()
        self.layout_3 = QFormLayout()
        self.layout_4 = QFormLayout()
        self.layout_5 = QFormLayout()
        self.layout_6 = QFormLayout()
        self.layout_7 = QFormLayout()
        self.layout_8 = QFormLayout()
        self.layout_9 = QFormLayout()

        goals = getattr(constants, self.dialog.win.data['api_gamemode_name'].lower())
        colours = ['green', 'cyan', 'yellow', 'orange', 'brown', 'red', 'blue', 'purple', 'white']

        for num, rows in enumerate(goals):
            for index, goal in enumerate(list(rows.keys())):
                button = GoalToolButton(self, self.dialog)
                button.setPalette(self.palette)
                button.setFont(self.font)
                button.setAutoRaise(True)
                button.setText(goal)
                eval(f'self.layout_{num+1}.setWidget({index}, QFormLayout.FieldRole, button)')

                arrow = QLabel(self.dialog)
                arrow.setMaximumSize(QSize(21, 21))
                arrow.setPalette(eval(f'self.{colours[num]}_palette'))
                arrow.setFont(self.arrow_font)
                arrow.setText(">>")
                eval(f'self.layout_{num+1}.setWidget({index}, QFormLayout.LabelRole, arrow)')
            self.gridLayout_5.addLayout(eval(f'self.layout_{num+1}'), 0 if num <= 4 else 1, num if num <= 4 else num-5, 1, 1)

        QMetaObject.connectSlotsByName(self.dialog)

class Goal(QDialog):
    def __init__(self, win, thread=True, best_goals=False, parent=None):
        super().__init__(parent)
        self.win = win
        self.startThread = thread
        self.best_goals = best_goals
        self.setModal(True)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.ui = GoalUI(self)
        self.ui.setupUi()

        self.clicked_something = False

        self.show()

    def closeEvent(self, event):
        if self.clicked_something:
            if self.startThread:
                self.win.after_goal_()
            else:
                self.win.after_goal()