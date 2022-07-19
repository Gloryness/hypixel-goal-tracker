from PyQt5.QtWidgets import QToolButton, QCheckBox, QLineEdit, QMessageBox, QLabel, QMenu, QAction
from PyQt5.QtGui import QColor, QBrush, QPalette, QFont, QIcon
from PyQt5.QtCore import Qt

import re
from app import path
from util.api import Test
from util import constants
from util.process import computeHtml

class NameLineEdit(QLineEdit):
    def __init__(self, win, parent):
        super().__init__(parent)
        self.win = win

    def keyPressEvent(self, event):
        if event != "":
            QLineEdit.keyPressEvent(self, event)
        if len(self.text().strip()) >= 1:
            self.win.dialog.data['name'] = self.text().strip()
            if len(self.win.goal_amount.text().strip()) >= 1 and len(self.win.goal_label.text()) > 46 and (self.win.milestone.isChecked() and not self.win.goal_amount_info.isVisible()):
                self.win.done.setEnabled(True)
            if self.win.infiniteGoalCheck.isChecked() and self.win.current_amount.isVisible():
                self.win.done.setEnabled(True)
            if self.win.gamemode_label.isEnabled() and len(self.win.goal_label.text().strip()) >= 47:
                self.win.current_amount.setVisible(True)
            self.win.gamemode.setDisabled(False)
            self.win.gamemode_label.setDisabled(False)
            if len(self.win.gamemode_label.text().strip()) >= 51:
                self.win.goal.setDisabled(False)
                self.win.goal_label.setDisabled(False)
            if self.win.dialog.auto != {}:
                self.win.goal.setDisabled(True)
                self.win.gamemode.setDisabled(True)

        else:
            self.win.dialog.data['name'] = ""
            self.win.done.setEnabled(False)
            if len(self.win.goal_amount.text().strip()) >= 1 and len(self.win.goal_label.text()) > 46:
                return
            self.win.gamemode.setDisabled(True)
            self.win.goal.setDisabled(True)
            self.win.gamemode_label.setDisabled(True)
            self.win.goal_label.setDisabled(True)

class GoalLineEdit(QLineEdit):
    def __init__(self, win, parent):
        super().__init__(parent)
        self.win = win

    def keyPressEvent(self, event):
        if event != "":
            QLineEdit.keyPressEvent(self, event)
        if self.win.dialog.data['api_goal_name'] == "networkExpp":
            cls = float
        else:
            cls = int
        if (re.match('\d+', self.text()) or re.match('\d+\.\d+', self.text())) and hasattr(self.win.dialog, 'value') and self.win.milestone.isChecked():
            if self.win.current_amount.text().__contains__("Failed to get player stats."):
                self.clear()
                return

            if cls(self.text()) <= self.win.dialog.value:
                self.win.goal_amount_info.setText("<html><head/><body><p><span style=\" font-size:8pt; color:#d90000;\">Must be higher than your current amount.</span></p></body></html>")
                self.win.goal_amount_info.show()
                self.win.done.setEnabled(False)
            else:
                self.win.dialog.data['goal_amount'] = cls(self.text())
                self.win.done.setEnabled(True)
                self.win.goal_amount_info.setText("<html><head/><body><p><span style=\" font-size:8pt; color:#ff557f;\">For example, if your current wins are 50 and you want to<br/>reach 75, simply enter 25 into this box instead of 75.<br/></span><span style=\" font-size:8pt; color:#ff40e0;\">To change this, simply tick the Milstone checkbox.</span></p></body></html>")
                if self.win.milestone.isChecked():
                    self.win.goal_amount_info.hide()
                else:
                    self.win.goal_amount_info.show()

            if self.win.dialog.data['api_goal_name'] == "smashLevel" and cls(self.text()) > 1920:
                self.win.goal_amount_info.setText(f"<html><head/><body><p><span style=\" font-size:10pt; color:#d90000;\">The maximum Smash Level is {computeHtml('&b1920&6✶').replace('; font-size: 12pt', '')}.</span></p></body></html>")
                self.win.goal_amount_info.show()
                self.win.done.setEnabled(False)
            elif self.win.dialog.data['api_goal_name'] == "smashLevel" and cls(self.text()) <= 1920 and cls(self.text()) > self.win.dialog.value:
                self.win.done.setEnabled(True)

            if self.win.dialog.data['api_goal_name'] == "speeduhc_level" and cls(self.text()) > 10:
                self.win.goal_amount_info.setText(f"<html><head/><body><p><span style=\" font-size:10pt; color:#d90000;\">The maximum SpeedUHC Level is {computeHtml('&d10❋').replace('; font-size: 12pt', '')}.</span></p></body></html>")
                self.win.goal_amount_info.show()
                self.win.done.setEnabled(False)
            elif self.win.dialog.data['api_goal_name'] == "speeduhc_level" and cls(self.text()) <= 10 and cls(self.text()) > self.win.dialog.value:
                self.win.done.setEnabled(True)

            if self.win.dialog.data['api_goal_name'] == "uhc_level" and cls(self.text()) > 15:
                self.win.goal_amount_info.setText(f"<html><head/><body><p><span style=\" font-size:10pt; color:#d90000;\">The maximum UHC Level is {computeHtml('&615✫').replace('; font-size: 12pt', '')}.</span></p></body></html>")
                self.win.goal_amount_info.show()
                self.win.done.setEnabled(False)
            elif self.win.dialog.data['api_goal_name'] == "uhc_level" and cls(self.text()) <= 15 and cls(self.text()) > self.win.dialog.value:
                self.win.done.setEnabled(True)

            if self.win.dialog.data['api_goal_name'] == "pit_level" and cls(self.text()) > 120:
                self.win.goal_amount_info.setText(f"<html><head/><body><p><span style=\" font-size:10pt; color:#d90000;\">The maximum Pit Level is {computeHtml('&7[&b120&7]').replace('; font-size: 12pt', '')}.</span></p></body></html>")
                self.win.goal_amount_info.show()
                self.win.done.setEnabled(False)
            elif self.win.dialog.data['api_goal_name'] == "pit_level" and cls(self.text()) <= 120 and cls(self.text()) > self.win.dialog.value:
                self.win.done.setEnabled(True)

        elif re.match('\d+', self.text()) and not self.win.milestone.isChecked():
            self.win.dialog.data['mid_amount'] = 0
            if cls(self.text()) != 0:
                self.win.dialog.data['goal_amount'] = cls(self.text())
                self.win.done.setEnabled(True)
            else:
                self.win.done.setEnabled(False)

            self.win.goal_amount_info.setText("<html><head/><body><p><span style=\" font-size:8pt; color:#ff557f;\">For example, if your current wins are 50 and you want to<br/>reach 75, simply enter 25 into this box instead of 75.<br/></span><span style=\" font-size:8pt; color:#ff40e0;\">To change this, simply tick the Milstone checkbox.</span></p></body></html>")

            if self.win.dialog.data['api_goal_name'] == "smashLevel" and self.win.dialog.data['current_amount']+cls(self.text()) > 1920:
                self.win.goal_amount_info.setText(f"<html><head/><body><p><span style=\" font-size:10pt; color:#d90000;\">The maximum Smash Level is {computeHtml('&b1920&6✶').replace('; font-size: 12pt', '')}.</span></p></body></html>")
                self.win.goal_amount_info.show()
                self.win.done.setEnabled(False)
            elif self.win.dialog.data['api_goal_name'] == "smashLevel" and self.win.dialog.data['current_amount']+cls(self.text()) <= 1920 and cls(self.text()) != 0:
                self.win.done.setEnabled(True)

            if self.win.dialog.data['api_goal_name'] == "speeduhc_level" and self.win.dialog.data['current_amount']+cls(self.text()) > 10:
                self.win.goal_amount_info.setText(f"<html><head/><body><p><span style=\" font-size:10pt; color:#d90000;\">The maximum SpeedUHC Level is {computeHtml('&d10❋').replace('; font-size: 12pt', '')}.</span></p></body></html>")
                self.win.goal_amount_info.show()
                self.win.done.setEnabled(False)
            elif self.win.dialog.data['api_goal_name'] == "speeduhc_level" and self.win.dialog.data['current_amount']+cls(self.text()) <= 10 and cls(self.text()) != 0:
                self.win.done.setEnabled(True)

            if self.win.dialog.data['api_goal_name'] == "uhc_level" and self.win.dialog.data['current_amount']+cls(self.text()) > 15:
                self.win.goal_amount_info.setText(f"<html><head/><body><p><span style=\" font-size:10pt; color:#d90000;\">The maximum UHC Level is {computeHtml('&615✫').replace('; font-size: 12pt', '')}.</span></p></body></html>")
                self.win.goal_amount_info.show()
                self.win.done.setEnabled(False)
            elif self.win.dialog.data['api_goal_name'] == "uhc_level" and self.win.dialog.data['current_amount']+cls(self.text()) <= 15 and cls(self.text()) != 0:
                self.win.done.setEnabled(True)

            if self.win.dialog.data['api_goal_name'] == "pit_level" and self.win.dialog.data['current_amount']+cls(self.text()) > 120:
                self.win.goal_amount_info.setText(f"<html><head/><body><p><span style=\" font-size:10pt; color:#d90000;\">The maximum Pit Level is {computeHtml('&7[&b120&7]').replace('; font-size: 12pt', '')}.</span></p></body></html>")
                self.win.goal_amount_info.show()
                self.win.done.setEnabled(False)
            elif self.win.dialog.data['api_goal_name'] == "pit_level" and self.win.dialog.data['current_amount']+cls(self.text()) <= 120 and cls(self.text()) != 0:
                self.win.done.setEnabled(True)

        if self.win.name.text() == "":
            self.win.done.setEnabled(False)

class GamemodeToolButton(QToolButton):
    def __init__(self, win, parent):
        super().__init__(parent)
        self.win = win

    def enterEvent(self, a0):
        if self.win.dialog.not_close:
            self.win.game.setText(self.accessibleName())
        else:
            res = len(list(filter(lambda k: k['gamemode'] == self.accessibleName(), self.win.dialog.win.completed_goals)))
            self.win.game.setText(f"<html><head/><body><p>"
                                  f"<span>{self.accessibleName()}</span> "
                                  f"<span style=\"color: {'green' if res >= 1 else 'red'}\">[{res:,} Completed Goal{'' if res == 1 else 's'}]</span>"
                                  f"</p></body></html>")

    def mousePressEvent(self, a0):
        QToolButton.mousePressEvent(self, a0)
        self.win.dialog.clicked_something = True
        self.win.dialog.win.data['gamemode'] = self.accessibleName()
        self.win.dialog.win.data['api_gamemode_name'] = self.objectName()
        if not self.win.dialog.not_close:
            self.win.dialog.win.goal_organiser['gamemode'] = self.accessibleName()
            self.win.dialog.win.goal_organiser['api_gamemode_name'] = self.objectName()
        self.win.dialog.close()

class GoalToolButton(QToolButton):
    def __init__(self, win, parent):
        super().__init__(parent)
        self.win = win

    def mousePressEvent(self, event):
        QToolButton.mousePressEvent(self, event)
        self.win.dialog.clicked_something = True
        for row in getattr(constants, self.win.dialog.win.data['api_gamemode_name'].lower()):
            if self.text() in row:
                self.win.dialog.win.data['api_goal_name'] = row[self.text()]
                self.win.dialog.win.data['goal'] = self.text()
                if not self.win.dialog.not_close:
                    self.win.dialog.win.goal_organiser['api_goal_name'] = row[self.text()]
                    self.win.dialog.win.goal_organiser['goal'] = self.text()
                break
        self.win.dialog.close()

class GamemodeAction(QAction):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.win = parent
        self.triggered.connect(self.clicked)

    def clicked(self):
        self.win.data['gamemode'] = self.text()
        self.win.data['api_gamemode_name'] = self.win.names[self.text()]
        self.win.goal_organiser['gamemode'] = self.text()
        self.win.goal_organiser['api_gamemode_name'] = self.win.names[self.text()]
        self.win.after_gamemode()

class GoalAction(QAction):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.win = parent
        self.triggered.connect(self.clicked)

    def clicked(self):
        self.win.data['goal'] = self.text()
        for row in getattr(constants, self.win.data['api_gamemode_name'].lower()):
            if self.text() in row:
                self.win.data['api_goal_name'] = row[self.text()]
                self.win.goal_organiser['api_goal_name'] = row[self.text()]
                break
        self.win.after_goal()

class MilestoneCheckBox(QCheckBox):
    def __init__(self, win, parent):
        super().__init__(parent)
        self.win = win

        self.setChecked(self.win.dialog.win.cache.get('milestone'))
        self.win.goal_amount_info.setHidden(self.win.dialog.win.cache.get('milestone'))
        self.win.dialog.data['milestone'] = self.win.dialog.win.cache.get('milestone')

    def nextCheckState(self):
        QCheckBox.nextCheckState(self)
        if self.isChecked():
            if 'mid_amount' in self.win.dialog.data:
                del self.win.dialog.data['mid_amount']
            self.win.goal_amount_info.hide()
            if 'current_amount' in self.win.dialog.data and self.win.goal_amount.text() != "":
                if int(self.win.goal_amount.text()) <= self.win.dialog.data['current_amount']:
                    self.win.goal_amount_info.setText("<html><head/><body><p><span style=\" font-size:8pt; color:#d90000;\">Must be higher than your current amount.</span></p></body></html>")
                    self.win.goal_amount_info.show()
                    self.win.done.setEnabled(False)
            else:
                self.win.done.setEnabled(False)
        else:
            self.win.dialog.data['mid_amount'] = 0
            self.win.goal_amount_info.setText("<html><head/><body><p><span style=\" font-size:8pt; color:#ff557f;\">For example, if your current wins are 50 and you want to<br/>reach 75, simply enter 25 into this box instead of 75.<br/></span><span style=\" font-size:8pt; color:#ff40e0;\">To change this, simply tick the Milstone checkbox.</span></p></body></html>")
            if self.win.goal_amount.text() != "":
                self.win.done.setEnabled(True)
            self.win.goal_amount_info.show()
        self.win.dialog.data['milestone'] = self.isChecked()
        self.win.dialog.win.cache.store({'milestone': self.isChecked()})

class MilestoneOption(QCheckBox):
    def __init__(self, parent):
        super().__init__(parent)
        self.win = parent

    def nextCheckState(self):
        QCheckBox.nextCheckState(self)
        for index in self.win.indexes:
            data = self.win.locals[str(index)]
            self.win.goal_organiser['milestone'] = self.checkState()
            if self.checkState() == 0:
                result = True if data['milestone'].text() in ['No', 'INFINITE'] else False
            elif self.checkState() == 1:
                result = True
            elif self.checkState() == 2:
                result = True if data['milestone'].text() in ['Yes', 'INFINITE'] else False
            data['name'].setVisible(result)
            data['goal'].setVisible(result)
            data['started_with'].setVisible(result)
            data['time_taken'].setVisible(result)
            data['completed'].setVisible(result)
            data['milestone'].setVisible(result)

class SortByAction(QAction):
    def __init__(self, parent):
        super().__init__(parent)
        self.win = parent
        self.triggered.connect(self.clicked)

    def clicked(self):
        self.win.ui.sort_by_option.setText(self.text())
        self.win.goal_organiser['sort_by'] = self.text()
        self.win.unpack(self.win.completed_goals, sorted_key=self.text().lower().replace(" ", "_") if self.text() != "Ended With" else "goal")

class UsernameCheckBox(QCheckBox):
    def __init__(self, win, parent):
        super().__init__(parent)
        self.win = win
        self.test = Test()

    def nextCheckState(self):
        QCheckBox.nextCheckState(self)
        if len(self.win.username.text()) >= 1 and self.test.test_user(self.win.username.text().strip()):
            palette = QPalette()
            brush = QBrush(QColor(0, 171, 0))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
            palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
            palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
            font = QFont()
            font.setFamily("Nirmala UI")
            font.setBold(True)
            self.win.username_label.setPalette(palette)
            self.win.username.setPalette(palette)
            self.win.username.setFont(font)
            self.win.username.setDisabled(True)
            self.setDisabled(True)
            if self.isChecked() and self.win.apiCheck.isChecked():
                self.win.done.setEnabled(True)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("An error occured")
            msg.setText("You must enter a valid Minecraft username that has to of joined Hypixel.")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)

            msg.exec_()
            self.setChecked(False)

class APIKeyCheckBox(QCheckBox):
    def __init__(self, win, parent):
        super().__init__(parent)
        self.win = win
        self.test = Test()

    def nextCheckState(self):
        QCheckBox.nextCheckState(self)
        if len(self.win.apikey.text()) >= 1 and self.test.test_key(self.win.apikey.text().strip()):
            palette = QPalette()
            brush = QBrush(QColor(0, 171, 0))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
            palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
            palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
            font = QFont()
            font.setFamily("Nirmala UI")
            font.setBold(True)
            self.win.apikey_label.setPalette(palette)
            self.win.apikey.setPalette(palette)
            self.win.apikey.setFont(font)
            self.win.apikey.setDisabled(True)
            self.setDisabled(True)
            if self.isChecked() and self.win.userCheck.isChecked():
                self.win.done.setEnabled(True)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("An error occured")
            msg.setText("You must enter a valid API key.")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setDefaultButton(QMessageBox.Ok)

            msg.exec_()
            self.setChecked(False)

class CompletedGoalsLabel(QLabel):
    def __init__(self, completed_goals, local, index, parent=None):
        super().__init__(parent)

        self.completed_goals = completed_goals
        self.locals = local
        self.index = index

    def enterEvent(self, event):
        data = self.locals[str(self.index)]

        self.name_palette = data['name'].palette()
        self.gamemode_palette = data['gamemode'].palette()
        self.goal_palette = data['goal'].palette()
        self.started_with_palette = data['started_with'].palette()
        self.time_taken_palette = data['time_taken'].palette()
        self.paused_time_palette = data['paused_time'].palette()
        self.completed_palette = data['completed'].palette()
        self.milestone_palette = data['milestone'].palette()

        palette = QPalette()
        brush = QBrush(QColor(255, 229, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)

        data['name'].setPalette(palette)
        data['gamemode'].setPalette(palette)
        data['goal'].setPalette(palette)
        data['started_with'].setPalette(palette)
        data['time_taken'].setPalette(palette)
        data['paused_time'].setPalette(palette)
        data['completed'].setPalette(palette)
        data['milestone'].setPalette(palette)

    def leaveEvent(self, event):
        data = self.locals[str(self.index)]

        data['name'].setPalette(self.name_palette)
        data['gamemode'].setPalette(self.gamemode_palette)
        data['goal'].setPalette(self.goal_palette)
        data['started_with'].setPalette(self.started_with_palette)
        data['time_taken'].setPalette(self.time_taken_palette)
        data['paused_time'].setPalette(self.paused_time_palette)
        data['completed'].setPalette(self.completed_palette)
        data['milestone'].setPalette(self.milestone_palette)

    def contextMenuEvent(self, event):
        menu = QMenu()

        delete = menu.addAction('Delete')
        delete.setIcon(QIcon(path('images', 'no.png')))

        action = menu.exec_(self.mapToGlobal(event.pos()))

        if action == delete:
            msg = QMessageBox()
            msg.setWindowIcon(QIcon(path('images', 'no.png')))
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Are you SURE?")
            msg.setText("Are you sure you want to remove this complete goal from the database?")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.buttonClicked.connect(self.delete)

            msg.exec_()

    def delete(self, output):
        if output.text() == 'OK':
            data = self.locals[str(self.index)]

            preview = {
                "name": data['name'].text(),
                "goal": data['goal'].text(),
                "completed": data['completed'].text()
            }

            data['name'].deleteLater(); del data['name']
            data['gamemode'].deleteLater(); del data['gamemode']
            data['goal'].deleteLater(); del data['goal']
            data['started_with'].deleteLater(); del data['started_with']
            data['time_taken'].deleteLater(); del data['time_taken']
            data['paused_time'].deleteLater(); del data['paused_time']
            data['completed'].deleteLater(); del data['completed']
            data['milestone'].deleteLater(); del data['milestone']

            self.completed_goals.pop(list(map(lambda k: {"name": k['name'], "goal": k['goal'], "completed": k['completed']}, self.completed_goals)).index(preview))
        else:
            pass

class BestGoalsLabel(QLabel):
    def __init__(self, completed_goals, local, index, parent=None):
        super().__init__(parent)

        self.completed_goals = completed_goals
        self.locals = local
        self.index = index

    def enterEvent(self, event):
        data = self.locals[str(self.index)]

        palette = QPalette()
        brush = QBrush(QColor(85, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.name_palette = palette

        palette = QPalette()
        brush = QBrush(QColor(255, 170, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.goal_palette = palette

        palette = QPalette()
        brush = QBrush(QColor(208, 139, 208))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.started_with_palette = palette

        palette = QPalette()
        brush = QBrush(QColor(255, 170, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.time_taken_palette = palette

        palette = QPalette()
        brush = QBrush(QColor(0, 255, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.completed_palette = palette

        palette = QPalette()
        brush = QBrush(QColor(255, 0, 127))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        self.milestone_palette = palette

        palette = QPalette()
        brush = QBrush(QColor(255, 229, 30))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)

        data['name'].setPalette(palette)
        data['goal'].setPalette(palette)
        data['started_with'].setPalette(palette)
        data['time_taken'].setPalette(palette)
        data['completed'].setPalette(palette)
        data['milestone'].setPalette(palette)

    def leaveEvent(self, event):
        data = self.locals[str(self.index)]

        data['name'].setPalette(self.name_palette)
        data['goal'].setPalette(self.goal_palette)
        data['started_with'].setPalette(self.started_with_palette)
        data['time_taken'].setPalette(self.time_taken_palette)
        data['completed'].setPalette(self.completed_palette)
        data['milestone'].setPalette(self.milestone_palette)

    def contextMenuEvent(self, event):
        menu = QMenu()

        delete = menu.addAction('Delete')
        delete.setIcon(QIcon(path('images', 'no.png')))

        action = menu.exec_(self.mapToGlobal(event.pos()))

        if action == delete:
            msg = QMessageBox()
            msg.setWindowIcon(QIcon(path('images', 'no.png')))
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Are you SURE?")
            msg.setText("Are you sure you want to remove this complete goal from the database?")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.setDefaultButton(QMessageBox.Ok)
            msg.buttonClicked.connect(self.delete)

            msg.exec_()

    def delete(self, output):
        if output.text() == 'OK':
            data = self.locals[str(self.index)]

            data['name'].deleteLater(); del data['name']
            data['goal'].deleteLater(); del data['goal']
            data['started_with'].deleteLater(); del data['started_with']
            data['time_taken'].deleteLater(); del data['time_taken']
            data['completed'].deleteLater(); del data['completed']
            data['milestone'].deleteLater(); del data['milestone']

            self.completed_goals.pop(self.index)
        else:
            pass

class InfiniteGoalCheckBox(QCheckBox):
    def __init__(self, win, parent):
        super().__init__(parent)
        self.win = win
        self.previous_milestone_text = ''
        self.previous_milestone_visibility = True
        self.previous_goal_amount = ''
        self.previous_goal_amount_enabled = True
        self.previous_done_enabled = True
        self.previous_goal_amount_data = ''

    def nextCheckState(self):
        QCheckBox.nextCheckState(self)
        self.win.infiniteDurationCheck.setDisabled(self.isChecked())
        if self.isChecked():
            self.win.milestone.setDisabled(True)
            self.previous_milestone_text = self.win.goal_amount_info.text()
            self.previous_milestone_visibility = self.win.goal_amount_info.isVisible()
            self.previous_goal_amount = self.win.goal_amount.text()
            self.previous_goal_amount_visibility = self.win.goal_amount.isEnabled()
            self.previous_done_enabled = self.win.done.isEnabled()
            self.previous_goal_amount_data = self.win.dialog.data['goal_amount'] if 'goal_amount' in self.win.dialog.data else ''
            self.win.goal_amount_info.setText('<html><head/><body><p><span style=" font-size:8pt; font-weight:600; color:#ffffff;">In this instance - you do </span><span style=" font-size:8pt; font-weight:600; color:#00ffff;">not</span><span style=" font-size:8pt; font-weight:600; color:#ffffff;"> have a goal to reach.<br/>You just try the best you can before the time runs out for the goal.</span></p></body></html>')
            self.win.goal_amount_info.setVisible(True)
            self.win.goal_amount.setEnabled(False)
            self.win.goal_amount.setText('∞')
            self.win.dialog.data['goal_amount'] = 'infinite'

            if self.win.current_amount.isVisible() and len(self.win.name.text()) >= 1:
                self.win.done.setEnabled(True)
        else:
            self.win.milestone.setDisabled(False)
            self.win.goal_amount_info.setText(self.previous_milestone_text)
            self.win.goal_amount_info.setVisible(self.previous_milestone_visibility)
            self.win.goal_amount.setEnabled(self.previous_goal_amount_enabled)
            self.win.goal_amount.setText(self.previous_goal_amount)
            self.win.done.setEnabled(self.previous_done_enabled)
            self.win.dialog.data['goal_amount'] = self.previous_goal_amount_data
            self.win.name.keyPressEvent("")
            self.win.goal_amount.keyPressEvent("")

class InfiniteDurationCheckBox(QCheckBox):
    def __init__(self, win, parent):
        super().__init__(parent)
        self.win = win

    def nextCheckState(self):
        QCheckBox.nextCheckState(self)
        self.win.infiniteGoalCheck.setDisabled(self.isChecked())
        if self.isChecked():
            self.win.dialog.change_time('∞')
            self.win.change.setDisabled(True)
        else:
            self.win.dialog.change_time(self.win.dialog.data['clock'])
            self.win.change.setDisabled(False)