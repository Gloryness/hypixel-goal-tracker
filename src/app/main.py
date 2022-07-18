from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase
import sys
from app import path

if __name__ == '__main__':
    from gui import Main

    app = QApplication(sys.argv)
    app.setStyleSheet('''
                      QToolButton[autoRaise="true"]::hover { background-color: rgba(255, 255, 255, 8%); }
                      QToolButton[autoRaise="true"]::pressed { background-color: rgba(255, 255, 255, 12%); }
                      ''')
    QFontDatabase.addApplicationFont(path("fonts", "Minecraftia-Regular.ttf")) # Loading the custom font
    QFontDatabase.addApplicationFont(path("fonts", "Minecraft-Bold.otf"))
    QFontDatabase.addApplicationFont(path("fonts", "RobotoMono-VariableFont_wght.ttf"))

    win = Main()
    win.show()

    sys.exit(app.exec())