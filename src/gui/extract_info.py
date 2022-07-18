from PyQt5.QtCore import QMetaObject, QSize, Qt
from PyQt5.QtGui import QFont, QIcon, QBrush, QColor, QPalette
from PyQt5.QtWidgets import QGridLayout, QLabel, QDialog, QToolButton, QLineEdit, QSizePolicy

import os
import requests

from app import path
from app.cache import Cache
from util.subclasses import (
    UsernameCheckBox,
    APIKeyCheckBox
)

class ExtractorUI:
    def __init__(self, dialog: QDialog):
        self.win = dialog

    def setupUi(self):
        self.win.setWindowTitle("Information Required")
        self.win.setWindowIcon(QIcon(path('images', 'logo.png')))
        self.win.resize(622, 170)
        self.win.setMinimumSize(QSize(622, 170))
        self.win.setMaximumSize(QSize(622, 170))

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
        self.gridLayout = QGridLayout(self.win)
        self.welcome_message_1 = QLabel(self.win)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.welcome_message_1.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_message_1.setFont(font)
        self.welcome_message_1.setTextFormat(Qt.MarkdownText)
        self.gridLayout.addWidget(self.welcome_message_1, 0, 0, 1, 2)
        self.apikey_label = QLabel(self.win)
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.apikey_label.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.apikey_label.setFont(font)
        self.apikey_label.setTextFormat(Qt.PlainText)
        self.gridLayout.addWidget(self.apikey_label, 3, 0, 1, 1)

        self.apikey = QLineEdit(self.win)
        self.apikey.setClearButtonEnabled(True)
        self.gridLayout.addWidget(self.apikey, 3, 1, 1, 1)

        self.username_label = QLabel(self.win)
        palette = QPalette()
        brush = QBrush(QColor(255, 0, 0))
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
        self.gridLayout.addWidget(self.username_label, 2, 0, 1, 1)

        self.username = QLineEdit(self.win)
        self.username.setFrame(True)
        self.username.setClearButtonEnabled(True)
        self.gridLayout.addWidget(self.username, 2, 1, 1, 1)

        self.welcome_message_2 = QLabel(self.win)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.welcome_message_2.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.welcome_message_2.setFont(font)
        self.welcome_message_2.setTextFormat(Qt.MarkdownText)
        self.gridLayout.addWidget(self.welcome_message_2, 1, 0, 1, 3)

        self.made_by = QLabel(self.win)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.made_by.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.made_by.setFont(font)
        self.made_by.setTextFormat(Qt.MarkdownText)
        self.gridLayout.addWidget(self.made_by, 5, 0, 1, 1)

        self.done = QToolButton(self.win)
        self.done.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.done.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setBold(True)
        font.setWeight(75)
        self.done.setFont(font)
        self.done.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.done.setIcon(QIcon(path('images', 'yes.png')))
        self.done.setIconSize(QSize(18, 18))
        self.done.setAutoRaise(True)
        self.gridLayout.addWidget(self.done, 4, 1, 1, 2)

        self.cancel = QToolButton(self.win)
        self.cancel.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.cancel.setPalette(palette)
        font = QFont()
        font.setFamily("Nirmala UI")
        font.setBold(True)
        font.setWeight(75)
        self.cancel.setFont(font)
        self.cancel.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.cancel.setIcon(QIcon(path('images', 'no.png')))
        self.cancel.setIconSize(QSize(20, 20))
        self.cancel.setAutoRaise(True)
        self.gridLayout.addWidget(self.cancel, 5, 1, 1, 2)

        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)

        self.userCheck = UsernameCheckBox(self, self.win)
        self.userCheck.setText("OK")
        self.userCheck.setPalette(palette)
        self.gridLayout.addWidget(self.userCheck, 2, 2, 1, 1)

        self.apiCheck = APIKeyCheckBox(self, self.win)
        self.apiCheck.setText("OK")
        self.apiCheck.setPalette(palette)
        self.gridLayout.addWidget(self.apiCheck, 3, 2, 1, 1)

        QMetaObject.connectSlotsByName(self.win)

class Extractor(QDialog):
    def __init__(self, window, parent=None):
        super().__init__(parent)
        self.main = window

        self.setModal(True)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint, 0)

        self.ui = ExtractorUI(self)
        self.ui.setupUi()

        self.ui.welcome_message_1.setText("<html><head/><body><p><span style=\" font-weight:400; color:#ffffff;\">Hey! Welcome to the </span><span style=\" color:#ca8700;\">Hypixel Goal Tracker!</span></p></body></html>")
        self.ui.apikey_label.setText("API Key")
        self.ui.apikey.setPlaceholderText("API key goes here")
        self.ui.username_label.setText("Username")
        self.ui.username.setPlaceholderText("Username goes here")
        self.ui.welcome_message_2.setText("<html><head/><body><p><span style=\" font-weight:400; color:#ffffff;\">In order for this to successfully work, your </span><span style=\" color:#ca8700;\">username</span><span style=\" font-weight:400; color:#ffffff;\"> and a valid </span><a href=\"https://api.hypixel.net\" style=\" text-decoration: underline; color:#2fcfda;\" target=\"_blank\">API key</a><span style=\" font-weight:400; color:#ffffff;\"> is required.</span></p></body></html>")
        self.ui.made_by.setText("<html><head/><body><p><span style=\" font-weight:400; color:#ffffff;\">Made by </span><a href=\"https://github.com/Gloryness\" target=\"_blank\"><span style=\" text-decoration: underline; color:#02d5ff;\">Gloryness</span></a></p></body></html>")
        self.ui.made_by.setOpenExternalLinks(True)
        self.ui.welcome_message_2.setOpenExternalLinks(True)
        self.ui.done.setText("Done")
        self.ui.cancel.setText("Cancel")
        self.ui.done.setEnabled(False)

        self.ui.done.clicked.connect(self.finished)
        self.ui.cancel.clicked.connect(self.cancel)

        self.show()

    def finished(self):
        cache = Cache(f'{os.environ["USERPROFILE"]}/AppData/Local/hypixel-goal-tracker', 'data.json')

        username = self.ui.username.text().strip()
        api_key = self.ui.apikey.text().strip()

        data = requests.get(f'https://playerdb.co/api/player/minecraft/{username}').json()['data']
        uuid = data['player']['raw_id']
        data = requests.get(f'https://playerdb.co/api/player/minecraft/{uuid}').json()['data']
        ign = data['player']['username']

        cache.store({'username': ign, 'uuid': uuid, 'api-key': api_key})

        self.close()

    def cancel(self):
        self.close()