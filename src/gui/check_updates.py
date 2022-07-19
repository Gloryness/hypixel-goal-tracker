from PyQt5.QtCore import QMetaObject, QSize, Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon, QBrush, QColor, QPalette
from PyQt5.QtWidgets import QSizePolicy, QProgressBar, QGridLayout, QLabel, QDialog

from app import path

class UpdateCheckUI:
    def __init__(self, dialog: QDialog):
        self.win = dialog

    def setupUi(self):
        self.win.setWindowTitle("Hypixel Goal Tracker")
        self.win.setWindowIcon(QIcon(path('images', 'logo.png')))
        self.win.setFixedSize(310, 58)

        self.gridLayout = QGridLayout(self.win)

        self.label = QLabel(self.win)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.progressBar = QProgressBar(self.win)
        self.progressBar.setMaximum(0)
        self.progressBar.setValue(-1)
        self.progressBar.setTextVisible(False)

        self.gridLayout.addWidget(self.progressBar, 1, 0, 1, 1)

        QMetaObject.connectSlotsByName(self.win)

class UpdateCheck(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setModal(True)
        self.setWindowFlags(Qt.WindowCloseButtonHint)
        self.setWindowFlag(Qt.WindowCloseButtonHint, 0)

        self.ui = UpdateCheckUI(self)
        self.ui.setupUi()

        self.ui.label.setText("Checking for updates...")

        self.show()