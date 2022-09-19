from PyQt5.QtCore import QMetaObject, QDate, QTime, QDateTime, Qt, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QFont, QBrush, QColor, QPalette, QIcon
from PyQt5.QtWidgets import QGridLayout, QLabel, QHBoxLayout, QGroupBox, QToolButton, QSpinBox, QDateTimeEdit, QDialog

import threading
import datetime

from app import path

class State:
    def __init__(self, state):
        self.state = state

class GroupBox(QGroupBox):
    def __init__(self, win, parent=None):
        super().__init__(parent=parent)
        self.win = win

    def mousePressEvent(self, a0):
        QGroupBox.mousePressEvent(self, a0)
        x, y = a0.x(), a0.y()
        frame = self.title()

        if x in [23, 22, 21]:
            return

        if x >= 8 and x <= (66 if frame == "Manual" else 50) and y >= 0 and y <= 12: # Checkbox
            if frame == "Manual":
                if not self.isChecked():
                    self.win.date_frame.setChecked(False)
                else:
                    self.win.date_frame.setChecked(True)
            else:
                if not self.isChecked():
                    self.win.manual_frame.setChecked(False)
                else:
                    self.win.manual_frame.setChecked(True)

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

        self.gridLayout = QGridLayout(self.dialog)

        self.manual_frame = GroupBox(self, self.dialog)

        white_palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        white_palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        white_palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        white_palette.setBrush(QPalette.Active, QPalette.Text, brush)
        white_palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255, 128))
        brush.setStyle(Qt.SolidPattern)
        white_palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        white_palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(120, 120, 120))
        brush.setStyle(Qt.SolidPattern)
        white_palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        white_palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.SolidPattern)
        white_palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)

        self.manual_frame.setPalette(white_palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setBold(True)
        font.setWeight(75)
        self.manual_frame.setFont(font)
        self.manual_frame.setCheckable(True)

        self.manual_grid = QGridLayout(self.manual_frame)

        self.manualLayoutD = QHBoxLayout()
        self.manualLabelD = QLabel(self.manual_frame)
        self.manualLabelD.setFont(font)
        self.manualLabelD.setPalette(white_palette)
        self.manualLayoutD.addWidget(self.manualLabelD)
        self.manualSpinD = QSpinBox(self.manual_frame)

        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(120, 120, 120))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)

        self.manualSpinD.setPalette(palette)
        self.manualSpinD.setMaximum(9999)
        self.manualLayoutD.addWidget(self.manualSpinD)
        self.manualLayoutD.setStretch(1, 1)
        self.manual_grid.addLayout(self.manualLayoutD, 0, 0, 2, 1)

        self.manualLayoutH = QHBoxLayout()
        self.manualLabelH = QLabel(self.manual_frame)
        self.manualLabelH.setFont(font)
        self.manualLabelH.setPalette(white_palette)
        self.manualLayoutH.addWidget(self.manualLabelH)
        self.manualSpinH = QSpinBox(self.manual_frame)
        self.manualSpinH.setPalette(palette)
        self.manualSpinH.setMaximum(24)
        self.manualLayoutH.addWidget(self.manualSpinH)
        self.manualLayoutH.setStretch(1, 1)
        self.manual_grid.addLayout(self.manualLayoutH, 0, 1, 2, 1)

        self.manualLayoutM = QHBoxLayout()
        self.manualLabelM = QLabel(self.manual_frame)
        self.manualLabelM.setFont(font)
        self.manualLabelM.setPalette(white_palette)
        self.manualLayoutM.addWidget(self.manualLabelM)
        self.manualSpinM = QSpinBox(self.manual_frame)
        self.manualSpinM.setPalette(palette)
        self.manualSpinM.setMaximum(1440)
        self.manualLayoutM.addWidget(self.manualSpinM)
        self.manualLayoutM.setStretch(1, 1)
        self.manual_grid.addLayout(self.manualLayoutM, 0, 2, 2, 1)

        self.manualLayoutS = QHBoxLayout()
        self.manualLabelS = QLabel(self.manual_frame)
        self.manualLabelS.setFont(font)
        self.manualLabelS.setPalette(white_palette)
        self.manualLayoutS.addWidget(self.manualLabelS)
        self.manualSpinS = QSpinBox(self.manual_frame)
        self.manualSpinS.setPalette(palette)
        self.manualSpinS.setMaximum(86400)
        self.manualLayoutS.addWidget(self.manualSpinS)
        self.manualLayoutS.setStretch(1, 1)
        self.manual_grid.addLayout(self.manualLayoutS, 0, 3, 2, 1)

        self.gridLayout.addWidget(self.manual_frame, 0, 0, 1, 2)

        self.date_frame = GroupBox(self, self.dialog)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(255, 255, 255, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        brush = QBrush(QColor(120, 120, 120))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        brush = QBrush(QColor(0, 0, 0, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
        self.date_frame.setPalette(palette)

        self.date_frame.setFont(font)
        self.date_frame.setFlat(False)
        self.date_frame.setCheckable(True)
        self.date_frame.setChecked(False)
        self.date_grid = QGridLayout(self.date_frame)

        self.dateLayout = QHBoxLayout()

        self.completed_by_label = QLabel(self.date_frame)
        self.completed_by_label.setPalette(white_palette)
        self.dateLayout.addWidget(self.completed_by_label)

        self.date = QDateTimeEdit(self.date_frame)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        brush = QBrush(QColor(120, 120, 120))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)

        now = datetime.datetime.now()

        now_ = now + datetime.timedelta(days=1)
        now_ = now_.replace(hour=0, minute=0, second=0)

        self.date.setPalette(palette)
        self.date.setDate(QDate(2022, 10, 16))
        self.date.setTime(QTime(0, 0, 0))
        self.date.setMinimumDate(QDate(now.year, now.month, now.day))
        self.date.setMinimumDateTime(QDateTime(QDate(now.year, now.month, now.day), QTime(now.hour, now.minute, now.second)))
        self.date.setDateTime(QDateTime(QDate(now_.year, now_.month, now_.day), QTime(now_.hour, now_.minute, now_.second)))
        self.date.setCalendarPopup(True)
        self.dateLayout.addWidget(self.date)
        self.dateLayout.setStretch(1, 1)
        self.date_grid.addLayout(self.dateLayout, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.date_frame, 1, 0, 1, 2)

        self.apply = QToolButton(self.dialog)
        self.apply.setShortcut("Return, Ctrl+Q")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.apply.setPalette(palette)

        self.apply.setFont(font)
        self.apply.setIcon(QIcon(path('images', 'yes.png')))
        self.apply.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.apply.setAutoRaise(True)
        self.apply.setLayoutDirection(Qt.RightToLeft)
        self.apply.clicked.connect(self.dialog.apply)
        self.gridLayout.addWidget(self.apply, 2, 1, 1, 1)

        QMetaObject.connectSlotsByName(self.dialog)

class Time(QDialog):
    closeWin = pyqtSignal()

    def __init__(self, clock, win, parent=None):
        super().__init__(parent)
        self.clock = clock
        self.win = win
        self.setModal(True)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.ui = TimeUI(self)
        self.ui.setupUi()

        if not hasattr(self.win, 'completeBy'):
            self.ui.manualSpinD.setValue(self.clock.days)
            self.ui.manualSpinH.setValue(self.clock.hours)
            self.ui.manualSpinM.setValue(self.clock.minutes)
            self.ui.manualSpinS.setValue(self.clock.seconds)
        else:
            self.ui.date_frame.setChecked(True)
            self.ui.manual_frame.setChecked(False)
            # if self.win.auto:
            #     now = self.win.auto['complete_by']
            #     self.ui.date.setMinimumDate(QDate(now['year'], now['month'], now['day']))
            #     self.ui.date.setMinimumDateTime(QDateTime(QDate(now['year'], now['month'], now['day']), QTime(now['hour'], now['minute'], now['second'])))
            self.ui.date.setDateTime(self.win.completeBy)

        self.ui.apply.setText("Apply")
        self.ui.manual_frame.setTitle("Manual")
        self.ui.manualLabelD.setText("Days:")
        self.ui.manualSpinD.setSuffix("d")
        self.ui.manualLabelH.setText("Hours:")
        self.ui.manualSpinH.setSuffix("h")
        self.ui.manualLabelM.setText("Minutes:")
        self.ui.manualSpinM.setSuffix("m")
        self.ui.manualLabelS.setText("Seconds:")
        self.ui.manualSpinS.setSuffix("s")
        self.ui.date_frame.setTitle("Date")
        self.ui.completed_by_label.setText("Complete By:")
        self.ui.date.setDisplayFormat("dd/MM/yyyy HH:mm:ss")

        self.closeWin.connect(self.closeWindow)

        self.show()

    def apply(self):
        if self.ui.manual_frame.isChecked():
            if hasattr(self.win, 'queues'):
                self.win.queues[-1].state = "break"
                del self.win.queues
                del self.win.data['complete_by']

            days = self.ui.manualSpinD.value()
            hours = self.ui.manualSpinH.value()
            minutes = self.ui.manualSpinM.value()
            seconds = self.ui.manualSpinS.value()

            self.win.clock.days = int(days)
            self.win.clock.hours = int(hours)
            self.win.clock.minutes = int(minutes)
            self.win.clock.seconds = int(seconds)

            self.win.data['clock'] = self.win.clock.format()

            self.win.change_time(self.win.clock.format())
        else:
            if not hasattr(self.win, 'queues'):
                self.win.queues = []
            else:
                self.win.queues[-1].state = "break"

            state = State("active")
            self.win.queues.append(state)

            date, time = self.ui.date.date(), self.ui.date.time()
            a = datetime.datetime.now()
            b = datetime.datetime(date.year(), date.month(), date.day(), time.hour(), time.minute(), time.second())
            delta = b - a

            self.win.clock.days = delta.days
            self.win.clock.hours = 0
            self.win.clock.minutes = 0
            self.win.clock.seconds = delta.seconds + (1 if delta.microseconds / 10000 > 50 else 0)

            self.win.data['clock'] = self.win.clock.format()
            self.win.data['complete_by'] = {
                "year": date.year(),
                "month": date.month(),
                "day": date.day(),
                "hour": time.hour(),
                "minute": time.minute(),
                "second": time.second()
            }

            self.win.completeBy = self.ui.date.dateTime()
            self.win.change_time(self.win.clock.format())

            thread = threading.Thread(target=self.win.auto_update, args=(self.ui.date.dateTime(), state))
            thread.start()

        self.close()

        self.win.ui.done.setEnabled(True)
        self.win.ui.name.keyPressEvent("")
        self.win.ui.goal_amount.keyPressEvent("")

    @pyqtSlot()
    def closeWindow(self):
        self.close()