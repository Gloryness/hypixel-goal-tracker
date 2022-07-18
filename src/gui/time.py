from PyQt5.QtCore import QMetaObject, Qt
from PyQt5.QtGui import QFont, QBrush, QColor, QPalette, QIcon
from PyQt5.QtWidgets import QGridLayout, QLabel, QHBoxLayout, QLayout, QToolButton, QDialog

from app import path

class TimeUI:
    def __init__(self, dialog: QDialog):
        self.dialog = dialog

    def plusOne(self, widget):
        number = int(widget.text())
        if number < 9:
            widget.setText(str(number+1))
        if number == 9:
            widget.setText("0")

    def minusOne(self, widget):
        number = int(widget.text())
        if number > 0:
            widget.setText(str(number-1))
        if number == 0:
            widget.setText("9")
    
    def setupUi(self):
        self.dialog.setWindowTitle("Change Time")
        self.dialog.resize(632, 134)
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

        palette = QPalette()
        brush = QBrush(QColor(244, 157, 70))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)

        self.gridLayout = QGridLayout(self.dialog)

        self.up_arrow_days_layout = QHBoxLayout()
        self.up_arrow_day_1 = QToolButton(self.dialog)
        self.up_arrow_day_1.setPalette(palette)
        font = QFont()
        font.setPointSize(12)
        self.up_arrow_day_1.setFont(font)
        self.up_arrow_day_1.setAutoRaise(True)
        self.up_arrow_day_1.setArrowType(Qt.UpArrow)
        self.up_arrow_day_1.clicked.connect(lambda: self.plusOne(self.days_1))
        self.up_arrow_days_layout.addWidget(self.up_arrow_day_1)

        self.up_arrow_day_2 = QToolButton(self.dialog)
        self.up_arrow_day_2.setPalette(palette)
        self.up_arrow_day_2.setFont(font)
        self.up_arrow_day_2.setAutoRaise(True)
        self.up_arrow_day_2.setArrowType(Qt.UpArrow)
        self.up_arrow_day_2.clicked.connect(lambda: self.plusOne(self.days_2))
        self.up_arrow_days_layout.addWidget(self.up_arrow_day_2)

        self.up_arrow_day_3 = QToolButton(self.dialog)
        self.up_arrow_day_3.setPalette(palette)
        self.up_arrow_day_3.setFont(font)
        self.up_arrow_day_3.setAutoRaise(True)
        self.up_arrow_day_3.setArrowType(Qt.UpArrow)
        self.up_arrow_day_3.clicked.connect(lambda: self.plusOne(self.days_3))
        self.up_arrow_days_layout.addWidget(self.up_arrow_day_3)

        self.gridLayout.addLayout(self.up_arrow_days_layout, 0, 0, 1, 1)

        self.up_arrow_hours_layout = QHBoxLayout()
        self.up_arrow_hours_1 = QToolButton(self.dialog)
        self.up_arrow_hours_1.setPalette(palette)
        self.up_arrow_hours_1.setFont(font)
        self.up_arrow_hours_1.setAutoRaise(True)
        self.up_arrow_hours_1.setArrowType(Qt.UpArrow)
        self.up_arrow_hours_1.clicked.connect(lambda: self.plusOne(self.hours_1))
        self.up_arrow_hours_layout.addWidget(self.up_arrow_hours_1)

        self.up_arrow_hours_2 = QToolButton(self.dialog)
        self.up_arrow_hours_2.setPalette(palette)
        self.up_arrow_hours_2.setFont(font)
        self.up_arrow_hours_2.setAutoRaise(True)
        self.up_arrow_hours_2.setArrowType(Qt.UpArrow)
        self.up_arrow_hours_2.clicked.connect(lambda: self.plusOne(self.hours_2))
        self.up_arrow_hours_layout.addWidget(self.up_arrow_hours_2)

        self.gridLayout.addLayout(self.up_arrow_hours_layout, 0, 2, 1, 1)

        self.up_arrow_mins_layout = QHBoxLayout()
        self.up_arrow_mins_1 = QToolButton(self.dialog)
        self.up_arrow_mins_1.setPalette(palette)
        self.up_arrow_mins_1.setFont(font)
        self.up_arrow_mins_1.setAutoRaise(True)
        self.up_arrow_mins_1.setArrowType(Qt.UpArrow)
        self.up_arrow_mins_1.clicked.connect(lambda: self.plusOne(self.mins_1))
        self.up_arrow_mins_layout.addWidget(self.up_arrow_mins_1)

        self.up_arrow_mins_2 = QToolButton(self.dialog)
        self.up_arrow_mins_2.setPalette(palette)
        self.up_arrow_mins_2.setFont(font)
        self.up_arrow_mins_2.setAutoRaise(True)
        self.up_arrow_mins_2.setArrowType(Qt.UpArrow)
        self.up_arrow_mins_2.clicked.connect(lambda: self.plusOne(self.mins_2))
        self.up_arrow_mins_layout.addWidget(self.up_arrow_mins_2)

        self.gridLayout.addLayout(self.up_arrow_mins_layout, 0, 4, 1, 1)

        self.up_arrow_seconds_layout = QHBoxLayout()
        self.up_arrow_seconds_1 = QToolButton(self.dialog)
        self.up_arrow_seconds_1.setPalette(palette)
        self.up_arrow_seconds_1.setFont(font)
        self.up_arrow_seconds_1.setAutoRaise(True)
        self.up_arrow_seconds_1.setArrowType(Qt.UpArrow)
        self.up_arrow_seconds_1.clicked.connect(lambda: self.plusOne(self.seconds_1))
        self.up_arrow_seconds_layout.addWidget(self.up_arrow_seconds_1)

        self.up_arrow_seconds_2 = QToolButton(self.dialog)
        self.up_arrow_seconds_2.setPalette(palette)
        self.up_arrow_seconds_2.setFont(font)
        self.up_arrow_seconds_2.setAutoRaise(True)
        self.up_arrow_seconds_2.setArrowType(Qt.UpArrow)
        self.up_arrow_seconds_2.clicked.connect(lambda: self.plusOne(self.seconds_2))
        self.up_arrow_seconds_layout.addWidget(self.up_arrow_seconds_2)

        self.gridLayout.addLayout(self.up_arrow_seconds_layout, 0, 6, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetFixedSize)

        palette = QPalette()
        brush = QBrush(QColor(57, 113, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)

        self.days_1 = QLabel(self.dialog)
        self.days_1.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        fontt = QFont()
        fontt.setFamily("Minecraftia")
        fontt.setPointSize(12)
        self.days_1.setFont(font)
        self.horizontalLayout_4.addWidget(self.days_1)

        self.days_2 = QLabel(self.dialog)
        self.days_2.setPalette(palette)
        self.days_2.setFont(font)
        self.horizontalLayout_4.addWidget(self.days_2)

        self.days_3 = QLabel(self.dialog)
        self.days_3.setPalette(palette)
        self.days_3.setFont(font)
        self.horizontalLayout_4.addWidget(self.days_3)
        self.gridLayout.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.days_label = QLabel(self.dialog)
        palettee = QPalette()
        brush = QBrush(QColor(69, 212, 255))
        brush.setStyle(Qt.SolidPattern)
        palettee.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palettee.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.days_label.setPalette(palettee)
        self.days_label.setFont(fontt)
        self.days_label.setIndent(3)
        self.gridLayout.addWidget(self.days_label, 1, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.hours_1 = QLabel(self.dialog)
        self.hours_1.setPalette(palette)
        self.hours_1.setFont(font)
        self.horizontalLayout_3.addWidget(self.hours_1)

        self.hours_2 = QLabel(self.dialog)
        self.hours_2.setPalette(palette)
        self.hours_2.setFont(font)
        self.horizontalLayout_3.addWidget(self.hours_2)

        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)

        self.label_6 = QLabel(self.dialog)
        self.label_6.setPalette(palettee)
        self.label_6.setFont(fontt)
        self.label_6.setIndent(3)
        self.gridLayout.addWidget(self.label_6, 1, 3, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.mins_1 = QLabel(self.dialog)
        self.mins_1.setPalette(palette)
        self.mins_1.setFont(font)
        self.horizontalLayout.addWidget(self.mins_1)

        self.mins_2 = QLabel(self.dialog)
        self.mins_2.setPalette(palette)
        self.mins_2.setFont(font)
        self.horizontalLayout.addWidget(self.mins_2)

        self.gridLayout.addLayout(self.horizontalLayout, 1, 4, 1, 1)
        self.mins_label = QLabel(self.dialog)
        self.mins_label.setPalette(palettee)
        self.mins_label.setFont(fontt)
        self.mins_label.setIndent(3)
        self.gridLayout.addWidget(self.mins_label, 1, 5, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetFixedSize)
        self.seconds_1 = QLabel(self.dialog)
        self.seconds_1.setPalette(palette)
        self.seconds_1.setFont(font)
        self.horizontalLayout_2.addWidget(self.seconds_1)

        self.seconds_2 = QLabel(self.dialog)
        self.seconds_2.setPalette(palette)
        self.seconds_2.setFont(font)
        self.horizontalLayout_2.addWidget(self.seconds_2)

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 6, 1, 1)

        self.seconds_label = QLabel(self.dialog)
        self.seconds_label.setPalette(palettee)
        self.seconds_label.setFont(fontt)
        self.seconds_label.setIndent(3)
        self.gridLayout.addWidget(self.seconds_label, 1, 7, 1, 1)

        self.down_arrow_days_layout = QHBoxLayout()
        self.down_arrow_day_1 = QToolButton(self.dialog)
        palette = QPalette()
        brush = QBrush(QColor(244, 157, 70))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.down_arrow_day_1.setPalette(palette)
        font = QFont()
        font.setPointSize(12)
        self.down_arrow_day_1.setFont(font)
        self.down_arrow_day_1.setAutoRaise(True)
        self.down_arrow_day_1.setArrowType(Qt.DownArrow)
        self.down_arrow_day_1.clicked.connect(lambda: self.minusOne(self.days_1))
        self.down_arrow_days_layout.addWidget(self.down_arrow_day_1)

        self.down_arrow_day_2 = QToolButton(self.dialog)
        self.down_arrow_day_2.setPalette(palette)
        self.down_arrow_day_2.setFont(font)
        self.down_arrow_day_2.setAutoRaise(True)
        self.down_arrow_day_2.setArrowType(Qt.DownArrow)
        self.down_arrow_day_2.clicked.connect(lambda: self.minusOne(self.days_2))
        self.down_arrow_days_layout.addWidget(self.down_arrow_day_2)

        self.down_arrow_day_3 = QToolButton(self.dialog)
        self.down_arrow_day_3.setPalette(palette)
        self.down_arrow_day_3.setFont(font)
        self.down_arrow_day_3.setAutoRaise(True)
        self.down_arrow_day_3.setArrowType(Qt.DownArrow)
        self.down_arrow_day_3.clicked.connect(lambda: self.minusOne(self.days_3))
        self.down_arrow_days_layout.addWidget(self.down_arrow_day_3)

        self.gridLayout.addLayout(self.down_arrow_days_layout, 2, 0, 1, 1)

        self.down_arrow_hours_layout = QHBoxLayout()
        self.down_arrow_hours_1 = QToolButton(self.dialog)
        self.down_arrow_hours_1.setPalette(palette)
        self.down_arrow_hours_1.setFont(font)
        self.down_arrow_hours_1.setAutoRaise(True)
        self.down_arrow_hours_1.setArrowType(Qt.DownArrow)
        self.down_arrow_hours_1.clicked.connect(lambda: self.minusOne(self.hours_1))
        self.down_arrow_hours_layout.addWidget(self.down_arrow_hours_1)

        self.down_arrow_hours_2 = QToolButton(self.dialog)
        self.down_arrow_hours_2.setPalette(palette)
        self.down_arrow_hours_2.setFont(font)
        self.down_arrow_hours_2.setAutoRaise(True)
        self.down_arrow_hours_2.setArrowType(Qt.DownArrow)
        self.down_arrow_hours_2.clicked.connect(lambda: self.minusOne(self.hours_2))
        self.down_arrow_hours_layout.addWidget(self.down_arrow_hours_2)

        self.gridLayout.addLayout(self.down_arrow_hours_layout, 2, 2, 1, 1)

        self.down_arrow_mins_layout = QHBoxLayout()
        self.down_arrow_mins_1 = QToolButton(self.dialog)
        self.down_arrow_mins_1.setPalette(palette)
        self.down_arrow_mins_1.setFont(font)
        self.down_arrow_mins_1.setAutoRaise(True)
        self.down_arrow_mins_1.setArrowType(Qt.DownArrow)
        self.down_arrow_mins_1.clicked.connect(lambda: self.minusOne(self.mins_1))
        self.down_arrow_mins_layout.addWidget(self.down_arrow_mins_1)

        self.down_arrow_mins_2 = QToolButton(self.dialog)
        self.down_arrow_mins_2.setPalette(palette)
        self.down_arrow_mins_2.setFont(font)
        self.down_arrow_mins_2.setAutoRaise(True)
        self.down_arrow_mins_2.setArrowType(Qt.DownArrow)
        self.down_arrow_mins_2.clicked.connect(lambda: self.minusOne(self.mins_2))
        self.down_arrow_mins_layout.addWidget(self.down_arrow_mins_2)

        self.gridLayout.addLayout(self.down_arrow_mins_layout, 2, 4, 1, 1)
        self.down_arrow_seconds_layout = QHBoxLayout()
        self.down_arrow_seconds_1 = QToolButton(self.dialog)
        self.down_arrow_seconds_1.setPalette(palette)
        self.down_arrow_seconds_1.setFont(font)
        self.down_arrow_seconds_1.setAutoRaise(True)
        self.down_arrow_seconds_1.setArrowType(Qt.DownArrow)
        self.down_arrow_seconds_1.clicked.connect(lambda: self.minusOne(self.seconds_1))
        self.down_arrow_seconds_layout.addWidget(self.down_arrow_seconds_1)

        self.down_arrow_seconds_2 = QToolButton(self.dialog)
        self.down_arrow_seconds_2.setPalette(palette)
        self.down_arrow_seconds_2.setFont(font)
        self.down_arrow_seconds_2.setAutoRaise(True)
        self.down_arrow_seconds_2.setArrowType(Qt.DownArrow)
        self.down_arrow_seconds_2.clicked.connect(lambda: self.minusOne(self.seconds_2))
        self.down_arrow_seconds_layout.addWidget(self.down_arrow_seconds_2)
        self.gridLayout.addLayout(self.down_arrow_seconds_layout, 2, 6, 1, 1)

        self.apply = QToolButton(self.dialog)
        self.apply.setShortcut("Return, Ctrl+Q")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.apply.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.apply.setFont(font)
        self.apply.setIcon(QIcon(path('images', 'yes.png')))
        self.apply.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.apply.setAutoRaise(True)
        self.apply.setLayoutDirection(Qt.RightToLeft)
        self.apply.clicked.connect(self.dialog.apply)
        self.gridLayout.addWidget(self.apply, 3, 3, 1, 5)

        QMetaObject.connectSlotsByName(self.dialog)

class Time(QDialog):
    def __init__(self, clock, win, parent=None):
        super().__init__(parent)
        self.clock = clock
        self.win = win
        self.setModal(True)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.ui = TimeUI(self)
        self.ui.setupUi()

        days = list(str(self.clock.days))
        for i in range(3-len(days)):
            days.insert(0, "0")

        hours = list(str(self.clock.hours))
        if len(hours) == 1:
            hours.insert(0, "0")

        mins = list(str(self.clock.minutes))
        if len(mins) == 1:
            mins.insert(0, "0")

        seconds = list(str(self.clock.seconds))
        if len(seconds) == 1:
            seconds.insert(0, "0")
        self.ui.days_1.setText(days[0])
        self.ui.days_2.setText(days[1])
        self.ui.days_3.setText(days[2])
        self.ui.days_label.setText("days")
        self.ui.hours_1.setText(hours[0])
        self.ui.hours_2.setText(hours[1])
        self.ui.label_6.setText("hours")
        self.ui.mins_1.setText(mins[0])
        self.ui.mins_2.setText(mins[1])
        self.ui.mins_label.setText("mins")
        self.ui.seconds_1.setText(seconds[0])
        self.ui.seconds_2.setText(seconds[1])
        self.ui.seconds_label.setText("seconds")

        self.ui.apply.setText("Apply")

        self.show()

    def closeEvent(self, event):
        self.apply()

    def apply(self):
        days = f"{self.ui.days_1.text()}{self.ui.days_2.text()}{self.ui.days_3.text()}"
        hours = f"{self.ui.hours_1.text()}{self.ui.hours_2.text()}"
        minutes = f"{self.ui.mins_1.text()}{self.ui.mins_2.text()}"
        seconds = f"{self.ui.seconds_1.text()}{self.ui.seconds_2.text()}"
        self.win.clock.days = int(days)
        self.win.clock.hours = int(hours)
        self.win.clock.minutes = int(minutes)
        self.win.clock.seconds = int(seconds)

        self.win.data['clock'] = self.win.clock.format()

        self.win.change_time(self.win.clock.format())

        self.close()