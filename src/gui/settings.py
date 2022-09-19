from PyQt5.QtCore import QMetaObject, QSize, Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon, QBrush, QColor, QPalette
from PyQt5.QtWidgets import QSizePolicy, QGridLayout, QLabel, QSpacerItem, QDialog, QToolButton, QMessageBox, QHBoxLayout, QLineEdit, \
    QDoubleSpinBox, QGroupBox, QCheckBox

from app import path, __version__
from app.cache import Cache
from util.api import Test
from util.process import computeHtml

import requests
import os
import re

class PercentageDesignCheckBox(QCheckBox):
    def __init__(self, win, parent):
        super().__init__(parent)
        self.win = win

    def nextCheckState(self):
        QCheckBox.nextCheckState(self)

        if self.isChecked():
            self.win.simplistic_example.setText(f"» Simplistic: {computeHtml('&6530 / 1000 &a(53.0%)')}")
            self.win.unsimplistic_example.setText(f"» Oversimplified: {computeHtml('&3[530✫] &6/ &c[&61&e0&a0&b0&d✫&5] &a(53.0%)')}")
        else:
            self.win.simplistic_example.setText(f"» Simplistic: {computeHtml('&6530 / 1000')}")
            self.win.unsimplistic_example.setText(f"» Oversimplified: {computeHtml('&3[530✫] &6/ &c[&61&e0&a0&b0&d✫&5]')}")

class ProgressDesignCheckBox(QCheckBox):
    def __init__(self, win, parent):
        super().__init__(parent)
        self.win = win

    def nextCheckState(self):
        QCheckBox.nextCheckState(self)

        font = self.win.simplistic_example.font()
        font2 = self.win.unsimplistic_example.font()
        if self.isChecked():
            font.setWeight(600)
            font2.setWeight(60)

            self.win.simplistic_example.setFont(font)
            self.win.unsimplistic_example.setFont(font2)
        else:
            font.setWeight(60)
            font2.setWeight(600)

            self.win.simplistic_example.setFont(font)
            self.win.unsimplistic_example.setFont(font2)


class ConfigUI:
    def __init__(self, dialog: QDialog):
        self.win = dialog
        
    def setupUi(self):
        self.win.setWindowTitle("Settings")
        self.win.setWindowIcon(QIcon(path('images', 'config.png')))
        self.win.resize(810, 208)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        brush = QBrush(QColor(20, 23, 15))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        self.win.setPalette(palette)

        self.gridLayout_2 = QGridLayout(self.win)
        self.horizontalLayout = QHBoxLayout()

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)

        self.title_icon = QLabel(self.win)
        self.title_icon.setMinimumSize(QSize(41, 41))
        self.title_icon.setMaximumSize(QSize(41, 41))
        self.title_icon.setPixmap(QPixmap(path("images", "config.png")))
        self.title_icon.setScaledContents(True)
        self.horizontalLayout.addWidget(self.title_icon)

        self.title = QLabel(self.win)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.title.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setTextFormat(Qt.PlainText)
        self.horizontalLayout.addWidget(self.title)

        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        spacerItem3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 3, 1, 1, 1)

        self.version = QLabel(self.win)
        font.setPointSize(13)
        font.setWeight(400)
        self.version.setFont(font)
        self.version.setPalette(palette)
        self.version.setAlignment(Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.version, 1, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.cancel_button = QToolButton(self.win)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancel_button.sizePolicy().hasHeightForWidth())
        self.cancel_button.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush = QBrush(QColor(255, 255, 255, 128))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
        self.cancel_button.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setBold(True)
        font.setWeight(75)
        self.cancel_button.setFont(font)
        icon = QIcon()
        icon.addPixmap(QPixmap(path("images", "no.png")), QIcon.Normal, QIcon.Off)
        self.cancel_button.setIcon(icon)
        self.cancel_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.cancel_button.setAutoRaise(True)
        self.horizontalLayout_3.addWidget(self.cancel_button)

        self.apply_button = QToolButton(self.win)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apply_button.sizePolicy().hasHeightForWidth())
        self.apply_button.setSizePolicy(sizePolicy)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.apply_button.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setBold(True)
        font.setWeight(75)
        self.apply_button.setFont(font)
        icon = QIcon()
        icon.addPixmap(QPixmap(path("images", "yes.png")), QIcon.Normal, QIcon.Off)
        self.apply_button.setIcon(icon)
        self.apply_button.setIconSize(QSize(20, 20))
        self.apply_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.apply_button.setAutoRaise(True)
        self.horizontalLayout_3.addWidget(self.apply_button)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 4, 2, 1, 1)

        self.frame = QGroupBox(self.win)
        self.frame.setTitle("General")
        self.frame.setFont(font)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.frame.setPalette(palette)

        self.gridLayout = QGridLayout(self.frame)

        self.username_label = QLabel(self.frame)
        palette = QPalette()
        brush = QBrush(QColor(0, 170, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.username_label.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.username_label.setFont(font)
        self.username_label.setTextFormat(Qt.PlainText)
        self.gridLayout.addWidget(self.username_label, 0, 0, 1, 1)

        self.username = QLineEdit(self.frame)
        self.username.setFrame(True)
        self.username.setClearButtonEnabled(True)
        self.gridLayout.addWidget(self.username, 0, 1, 1, 1)

        self.api_key_label = QLabel(self.frame)
        palette = QPalette()
        brush = QBrush(QColor(0, 170, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.api_key_label.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.api_key_label.setFont(font)
        self.api_key_label.setTextFormat(Qt.PlainText)
        self.gridLayout.addWidget(self.api_key_label, 1, 0, 1, 1)

        self.api_key = QLineEdit(self.frame)
        self.api_key.setFrame(True)
        self.api_key.setClearButtonEnabled(True)
        self.gridLayout.addWidget(self.api_key, 1, 1, 1, 1)

        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(60)

        self.horizontalLayout_3 = QHBoxLayout()
        self.time_label = QLabel(self.frame)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.time_label.setPalette(palette)
        self.time_label.setFont(font)
        self.time_label.setTextFormat(Qt.PlainText)
        self.horizontalLayout_3.addWidget(self.time_label)

        self.time_spinbox = QDoubleSpinBox(self.frame)
        self.time_spinbox.setMinimum(1.50)
        self.time_spinbox.setMaximum(120.0)
        self.time_spinbox.setSingleStep(0.01)
        self.time_spinbox.setMinimumWidth(70)
        self.time_spinbox.setMaximumWidth(70)
        self.time_spinbox.setSuffix("s")
        self.horizontalLayout_3.addWidget(self.time_spinbox)

        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)

        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.time_label_2 = QLabel(self.frame)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.time_label_2.setPalette(palette)
        self.time_label_2.setFont(font)
        self.time_label_2.setTextFormat(Qt.PlainText)
        self.horizontalLayout_4.addWidget(self.time_label_2)

        self.time_spinbox_2 = QDoubleSpinBox(self.frame)
        self.time_spinbox_2.setMinimum(0.05)
        self.time_spinbox_2.setMaximum(1.00)
        self.time_spinbox_2.setSingleStep(0.05)
        self.time_spinbox_2.setMinimumWidth(70)
        self.time_spinbox_2.setMaximumWidth(70)
        self.time_spinbox_2.setSuffix("s")
        self.horizontalLayout_4.addWidget(self.time_spinbox_2)

        spacerItem1 = QSpacerItem(20, 40, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)

        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 2)

        font = QFont()
        font.setFamily("Nirmala UI")
        font.setBold(True)
        font.setWeight(75)

        self.design_frame = QGroupBox(self.win)
        self.design_frame.setTitle("Design")
        self.design_frame.setFont(font)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.design_frame.setPalette(palette)

        self.design_grid = QGridLayout(self.design_frame)

        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(60)

        self.percentage_design = PercentageDesignCheckBox(self, self.design_frame)
        self.percentage_design.setFont(font)
        self.percentage_design.setStyleSheet("color: white")
        self.design_grid.addWidget(self.percentage_design, 0, 0, 1, 1)

        self.progress_design = ProgressDesignCheckBox(self, self.design_frame)
        self.progress_design.setFont(font)
        self.progress_design.setStyleSheet("color: white")
        self.design_grid.addWidget(self.progress_design, 1, 0, 1, 1)

        font.setWeight(600)

        self.simplistic_example = QLabel()
        self.simplistic_example.setFont(font)
        self.simplistic_example.setStyleSheet("color: white")

        self.unsimplistic_example = QLabel()
        self.unsimplistic_example.setFont(font)
        self.unsimplistic_example.setStyleSheet("color: white")

        self.design_grid.addWidget(self.simplistic_example, 2, 0, 1, 1)
        self.design_grid.addWidget(self.unsimplistic_example, 3, 0, 1, 1)

        self.gridLayout_2.addWidget(self.frame, 2, 0, 1, 3)
        self.gridLayout_2.addWidget(self.design_frame, 3, 0, 1, 3)

        QMetaObject.connectSlotsByName(self.win)

class Config(QDialog):
    def __init__(self, window, parent=None):
        super().__init__(parent)

        self.main = window

        self.setModal(True)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint, 0)

        self.setStyleSheet('QLineEdit { background-color: rgba(0, 0, 0, 0); border-bottom: 1px solid red; border-radius: 2px; color: white; font-size: 12px; font-weight: 600; padding: 1px }')

        self.ui = ConfigUI(self)
        self.ui.setupUi()

        self.test = Test()

        self.ui.version.setText(f"v{__version__}")
        self.ui.title.setText("Configuration")
        self.ui.cancel_button.setText("Cancel")
        self.ui.apply_button.setText("Apply")
        self.ui.username_label.setText("Username: ")
        self.ui.username.setPlaceholderText("Username goes here")
        self.ui.api_key_label.setText("API Key: ")
        self.ui.api_key.setPlaceholderText("API Key goes here")
        self.ui.time_label.setText("Amount of time to wait between each request to the Hypixel API: ")
        self.ui.time_label_2.setText("How long inbetween each refresh of \"Next Hypixel API Request\": ")
        self.ui.percentage_design.setText("Show progress percentage until goal completion")
        self.ui.progress_design.setText("Keep progress design simplistic (if unchecked, effects only modes that contain a levelling system e.g bedwars)")

        self.ui.apply_button.clicked.connect(self.apply)
        self.ui.cancel_button.clicked.connect(self.close)

        self.auto_fill()

        self.show()

    def auto_fill(self):
        cache = Cache(f'{os.environ["USERPROFILE"]}/AppData/Local/hypixel-goal-tracker', 'data.json').all()

        self.original_username = "" if "username" not in cache else cache['username']
        self.original_api_key = "" if "api-key" not in cache else cache['api-key']
        self.original_location = "" if "play-file" not in cache else cache['play-file']
        self.original_time = 1.50 if "request-wait" not in cache else cache['request-wait']
        self.original_step = 0.05 if "next-request-step" not in cache else cache['next-request-step']
        self.progress_design = True if "progress-design" not in cache else cache['progress-design']
        self.percentage_design = True if "percentage-design" not in cache else cache['percentage-design']

        self.ui.username.setText(self.original_username)
        self.ui.api_key.setText(self.original_api_key)
        self.ui.time_spinbox.setValue(self.original_time)
        self.ui.time_spinbox_2.setValue(self.original_step)
        self.ui.progress_design.setChecked(self.progress_design)
        self.ui.percentage_design.setChecked(self.percentage_design)

        font = self.ui.simplistic_example.font()
        font2 = self.ui.unsimplistic_example.font()
        if self.ui.progress_design.isChecked():
            font.setWeight(600)
            font2.setWeight(60)

            self.ui.simplistic_example.setFont(font)
            self.ui.unsimplistic_example.setFont(font2)
        else:
            font.setWeight(60)
            font2.setWeight(600)

            self.ui.simplistic_example.setFont(font)
            self.ui.unsimplistic_example.setFont(font2)

        if self.ui.percentage_design.isChecked():
            self.ui.simplistic_example.setText(f"» Simplistic: {computeHtml('&6530 / 1000 &a(53.0%)')}")
            self.ui.unsimplistic_example.setText(f"» Oversimplified: {computeHtml('&3[530✫] &6/ &c[&61&e0&a0&b0&d✫&5] &a(53.0%)')}")
        else:
            self.ui.simplistic_example.setText(f"» Simplistic: {computeHtml('&6530 / 1000')}")
            self.ui.unsimplistic_example.setText(f"» Oversimplified: {computeHtml('&3[530✫] &6/ &c[&61&e0&a0&b0&d✫&5]')}")

    def apply(self):
        cache = Cache(f'{os.environ["USERPROFILE"]}/AppData/Local/hypixel-goal-tracker', 'data.json')

        username = self.ui.username.text().strip()
        api_key = self.ui.api_key.text().strip()
        time = round(self.ui.time_spinbox.value(), 2)
        step = round(self.ui.time_spinbox_2.value(), 2)
        progress_design = self.ui.progress_design.isChecked()
        percentage_design = self.ui.percentage_design.isChecked()

        if username.lower() != self.original_username.lower():
            if not self.test.test_user(username):
                msg = QMessageBox()
                msg.setWindowTitle("An error occured")
                msg.setText("You must enter a valid Minecraft username that has to of joined Hypixel.")
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)

                msg.exec_()
                return

            data = requests.get(f'https://playerdb.co/api/player/minecraft/{username}').json()['data']
            uuid = data['player']['raw_id']
            data = requests.get(f'https://playerdb.co/api/player/minecraft/{uuid}').json()['data']
            ign = data['player']['username']

            cache.store({"username": ign, "uuid": uuid})
            self.main.api.uuid = uuid
            self.main.api_sync.start_session_sync(limit=True)

        if api_key != self.original_api_key:
            if not self.test.test_key(api_key):
                msg = QMessageBox()
                msg.setWindowTitle("An error occured")
                msg.setText("You must enter a valid API key.")
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setDefaultButton(QMessageBox.Ok)

                msg.exec_()
                return

            cache.store({"api-key": api_key})
            self.main.api.api_key = api_key

        if time != self.original_time:
            cache.store({"request-wait": time})
            self.main.api_sync.request_wait = time

            request_wait = time if not re.search(".+\.\d$", str(time)) else str(time) + '0'

            self.main.ui.realtimestats.setText("<html/></head><body><p>"
                                    "<span style=\"color: white\">Statistics: </span>"
                                    f"<span style=\"color: aqua\">Request Wait Time: {request_wait}s</span>"
                                    "<span style=\"color: white\"> // </span>"
                                    f"<span style=\"color: gold\">Requests/min: {round(60 / time, 2)*len(list(filter(bool, self.main.api_sync.endpoints.values())))}</span>"
                                    "<span style=\"color: white\"> // </span>"
                                    f"<span style=\"color: grey\">API Endpoints:</span> <span style=\"color: {'green' if self.main.api_sync.endpoints['player'] else 'red'}\">/player</span> <span style=\"color: {'green' if self.main.api_sync.endpoints['friends'] else 'red'}\">/friends</span>"
                                    "</p></body></html>")

        if step != self.original_step:
            cache.store({"next-request-step": step})
            self.main.api_sync.request_step = step

        if progress_design != self.progress_design:
            cache.store({"progress-design": progress_design})
            self.main.progress_design = progress_design

        if percentage_design != self.percentage_design:
            cache.store({"percentage-design": percentage_design})
            self.main.percentage_design = percentage_design

        self.close()

    def closeEvent(self, event):
        self.main.inside_settings = False