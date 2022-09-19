from PyQt5.QtCore import QMetaObject, QSize, Qt
from PyQt5.QtGui import QFont, QIcon, QBrush, QColor, QPalette
from PyQt5.QtWidgets import QSizePolicy, QGridLayout, QLabel, QSpacerItem, QDialog

from app import path
from util.subclasses import GamemodeToolButton

class GamemodeUI:
    def __init__(self, dialog: QDialog):
        self.dialog = dialog

    def setupUi(self):
        self.dialog.setWindowTitle("Choose Gamemode")
        self.dialog.resize(709, 165)
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

        self.gridLayout_2 = QGridLayout(self.dialog)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 2, 1, 1)
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)

        self.game = QLabel(self.dialog)
        palette = QPalette()
        brush = QBrush(QColor(245, 245, 245))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.game.setPalette(palette)
        font = QFont()
        font.setFamily("MV Boli")
        font.setPointSize(12)
        self.game.setFont(font)
        self.gridLayout_2.addWidget(self.game, 1, 1, 1, 1)

        self.gridLayout = QGridLayout()

        self.bedwars = GamemodeToolButton(self, self.dialog)
        self.bedwars.setAccessibleName("BedWars")
        self.bedwars.setObjectName("Bedwars")
        self.bedwars.setIcon(QIcon(path('images', 'game-icons', 'BedWars.png')))
        self.bedwars.setIconSize(QSize(50, 50))
        self.bedwars.setAutoRaise(True)
        self.gridLayout.addWidget(self.bedwars, 0, 0, 1, 1)

        self.skywars = GamemodeToolButton(self, self.dialog)
        self.skywars.setAccessibleName("SkyWars")
        self.skywars.setObjectName("SkyWars")
        self.skywars.setIcon(QIcon(path('images', 'game-icons', 'SkyWars.png')))
        self.skywars.setIconSize(QSize(50, 50))
        self.skywars.setAutoRaise(True)
        self.gridLayout.addWidget(self.skywars, 0, 1, 1, 1)

        self.murdermystery = GamemodeToolButton(self, self.dialog)
        self.murdermystery.setAccessibleName("Murder Mystery")
        self.murdermystery.setObjectName("MurderMystery")
        self.murdermystery.setIcon(QIcon(path('images', 'game-icons', 'Murder Mystery.png')))
        self.murdermystery.setIconSize(QSize(50, 50))
        self.murdermystery.setAutoRaise(True)
        self.gridLayout.addWidget(self.murdermystery, 0, 2, 1, 1)

        self.arcade = GamemodeToolButton(self, self.dialog)
        self.arcade.setAccessibleName("Arcade")
        self.arcade.setObjectName("Arcade")
        self.arcade.setIcon(QIcon(path('images', 'game-icons', 'Arcade.png')))
        self.arcade.setIconSize(QSize(50, 50))
        self.arcade.setAutoRaise(True)
        self.gridLayout.addWidget(self.arcade, 0, 3, 1, 1)

        self.duels = GamemodeToolButton(self, self.dialog)
        self.duels.setAccessibleName("Duels")
        self.duels.setObjectName("Duels")
        self.duels.setIcon(QIcon(path('images', 'game-icons', 'Duels.png')))
        self.duels.setIconSize(QSize(50, 50))
        self.duels.setAutoRaise(True)
        self.gridLayout.addWidget(self.duels, 0, 4, 1, 1)

        self.buildbattle = GamemodeToolButton(self, self.dialog)
        self.buildbattle.setAccessibleName("Build Battle")
        self.buildbattle.setObjectName("BuildBattle")
        self.buildbattle.setIcon(QIcon(path('images', 'game-icons', 'Build Battle.png')))
        self.buildbattle.setIconSize(QSize(50, 50))
        self.buildbattle.setAutoRaise(True)
        self.gridLayout.addWidget(self.buildbattle, 0, 5, 1, 1)

        self.tntgames = GamemodeToolButton(self, self.dialog)
        self.tntgames.setAccessibleName("TNT Games")
        self.tntgames.setObjectName("TNTGames")
        self.tntgames.setIcon(QIcon(path('images', 'game-icons', 'TNT Games.png')))
        self.tntgames.setIconSize(QSize(50, 50))
        self.tntgames.setAutoRaise(True)
        self.gridLayout.addWidget(self.tntgames, 0, 6, 1, 1)

        self.paintball = GamemodeToolButton(self, self.dialog)
        self.paintball.setAccessibleName("Paintball")
        self.paintball.setObjectName("Paintball")
        self.paintball.setIcon(QIcon(path('images', 'game-icons', 'Paintball.png')))
        self.paintball.setIconSize(QSize(50, 50))
        self.paintball.setAutoRaise(True)
        self.gridLayout.addWidget(self.paintball, 0, 7, 1, 1)

        self.quakecraft = GamemodeToolButton(self, self.dialog)
        self.quakecraft.setAccessibleName("Quakecraft")
        self.quakecraft.setObjectName("Quake")
        self.quakecraft.setIcon(QIcon(path('images', 'game-icons', 'Quakecraft.png')))
        self.quakecraft.setIconSize(QSize(50, 50))
        self.quakecraft.setAutoRaise(True)
        self.gridLayout.addWidget(self.quakecraft, 0, 8, 1, 1)

        self.blitz = GamemodeToolButton(self, self.dialog)
        self.blitz.setAccessibleName("Blitz Survival Games")
        self.blitz.setObjectName("HungerGames")
        self.blitz.setIcon(QIcon(path('images', 'game-icons', 'Blitz Survival Games.png')))
        self.blitz.setIconSize(QSize(50, 50))
        self.blitz.setAutoRaise(True)
        self.gridLayout.addWidget(self.blitz, 0, 9, 1, 1)

        self.pit = GamemodeToolButton(self, self.dialog)
        self.pit.setAccessibleName("The Pit")
        self.pit.setObjectName("Pit")
        self.pit.setIcon(QIcon(path('images', 'game-icons', 'The Pit.png')))
        self.pit.setIconSize(QSize(50, 50))
        self.pit.setAutoRaise(True)
        self.gridLayout.addWidget(self.pit, 0, 10, 1, 1)

        self.cvc = GamemodeToolButton(self, self.dialog)
        self.cvc.setAccessibleName("Cops VS Crims")
        self.cvc.setObjectName("MCGO")
        self.cvc.setIcon(QIcon(path('images', 'game-icons', 'Cops VS Crims.png')))
        self.cvc.setIconSize(QSize(50, 50))
        self.cvc.setAutoRaise(True)
        self.gridLayout.addWidget(self.cvc, 1, 0, 1, 1)

        self.arenabrawl = GamemodeToolButton(self, self.dialog)
        self.arenabrawl.setAccessibleName("Arena Brawl")
        self.arenabrawl.setObjectName("Arena")
        self.arenabrawl.setIcon(QIcon(path('images', 'game-icons', 'Arena Brawl.png')))
        self.arenabrawl.setIconSize(QSize(50, 50))
        self.arenabrawl.setAutoRaise(True)
        self.gridLayout.addWidget(self.arenabrawl, 1, 1, 1, 1)

        self.smashheroes = GamemodeToolButton(self, self.dialog)
        self.smashheroes.setAccessibleName("Super Smash Heroes")
        self.smashheroes.setObjectName("SuperSmash")
        self.smashheroes.setIcon(QIcon(path('images', 'game-icons', 'Super Smash Heroes.png')))
        self.smashheroes.setIconSize(QSize(50, 50))
        self.smashheroes.setAutoRaise(True)
        self.gridLayout.addWidget(self.smashheroes, 1, 2, 1, 1)

        self.speeduhc = GamemodeToolButton(self, self.dialog)
        self.speeduhc.setAccessibleName("SpeedUHC")
        self.speeduhc.setObjectName("SpeedUHC")
        self.speeduhc.setIcon(QIcon(path('images', 'game-icons', 'SpeedUHC.png')))
        self.speeduhc.setIconSize(QSize(50, 50))
        self.speeduhc.setAutoRaise(True)
        self.gridLayout.addWidget(self.speeduhc, 1, 3, 1, 1)

        self.megawalls = GamemodeToolButton(self, self.dialog)
        self.megawalls.setAccessibleName("Mega Walls")
        self.megawalls.setObjectName("Walls3")
        self.megawalls.setIcon(QIcon(path('images', 'game-icons', 'Mega Walls.png')))
        self.megawalls.setIconSize(QSize(50, 50))
        self.megawalls.setAutoRaise(True)
        self.gridLayout.addWidget(self.megawalls, 1, 4, 1, 1)

        self.tkr = GamemodeToolButton(self, self.dialog)
        self.tkr.setAccessibleName("Turbo Kart Racers")
        self.tkr.setObjectName("GingerBread")
        self.tkr.setIcon(QIcon(path('images', 'game-icons', 'Turbo Kart Racers.png')))
        self.tkr.setIconSize(QSize(50, 50))
        self.tkr.setAutoRaise(True)
        self.gridLayout.addWidget(self.tkr, 1, 5, 1, 1)

        self.uhc = GamemodeToolButton(self, self.dialog)
        self.uhc.setAccessibleName("UHC")
        self.uhc.setObjectName("UHC")
        self.uhc.setIcon(QIcon(path('images', 'game-icons', 'UHC.png')))
        self.uhc.setIconSize(QSize(50, 50))
        self.uhc.setAutoRaise(True)
        self.gridLayout.addWidget(self.uhc, 1, 6, 1, 1)

        self.vampirez = GamemodeToolButton(self, self.dialog)
        self.vampirez.setAccessibleName("VampireZ")
        self.vampirez.setObjectName("VampireZ")
        self.vampirez.setIcon(QIcon(path('images', 'game-icons', 'VampireZ.png')))
        self.vampirez.setIconSize(QSize(50, 50))
        self.vampirez.setAutoRaise(True)
        self.gridLayout.addWidget(self.vampirez, 1, 7, 1, 1)

        self.walls = GamemodeToolButton(self, self.dialog)
        self.walls.setAccessibleName("Walls")
        self.walls.setObjectName("Walls")
        self.walls.setIcon(QIcon(path('images', 'game-icons', 'Walls.png')))
        self.walls.setIconSize(QSize(50, 50))
        self.walls.setAutoRaise(True)
        self.gridLayout.addWidget(self.walls, 1, 8, 1, 1)

        self.warlords = GamemodeToolButton(self, self.dialog)
        self.warlords.setAccessibleName("Warlords")
        self.warlords.setObjectName("Battleground")
        self.warlords.setIcon(QIcon(path('images', 'game-icons', 'Warlords.png')))
        self.warlords.setIconSize(QSize(50, 50))
        self.warlords.setAutoRaise(True)
        self.gridLayout.addWidget(self.warlords, 1, 9, 1, 1)

        self.woolwars = GamemodeToolButton(self, self.dialog)
        self.woolwars.setAccessibleName("Wool Wars")
        self.woolwars.setObjectName("WoolGames")
        self.woolwars.setIcon(QIcon(path('images', 'game-icons', 'Wool Wars.png')))
        self.woolwars.setIconSize(QSize(50, 50))
        self.woolwars.setAutoRaise(True)
        self.gridLayout.addWidget(self.woolwars, 1, 10, 1, 1)

        self.hypixel = GamemodeToolButton(self, self.dialog)
        self.hypixel.setAccessibleName("Hypixel")
        self.hypixel.setObjectName("Hypixel")
        self.hypixel.setIcon(QIcon(path('images', 'game-icons', 'Hypixel.png')))
        self.hypixel.setIconSize(QSize(50, 50))
        self.hypixel.setAutoRaise(True)
        self.gridLayout.addWidget(self.hypixel, 1, 11, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 3)

        QMetaObject.connectSlotsByName(self.dialog)

class Gamemode(QDialog):
    def __init__(self, win, best_goals=False, parent=None):
        super().__init__(parent)
        self.win = win
        self.best_goals = best_goals
        self.setModal(True)
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        self.ui = GamemodeUI(self)
        self.ui.setupUi()

        self.ui.game.setText("BedWars")

        self.clicked_something = False

        self.show()

    def closeEvent(self, event):
        if self.clicked_something:
            self.win.after_gamemode()