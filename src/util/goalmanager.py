from PyQt5.QtGui import QPalette, QBrush, QColor
from PyQt5.QtCore import Qt

from app.clock import Clock
from app.cache import Cache
from util.determine import DManualSetup
from util.process import processManuals, processProgress, computeHtml

from app import convert_to_time
from datetime import datetime
import time
import os

class GoalManager:
    def __init__(self, datasets):
        self.datasets = datasets

        self.finished = False
        self.deleted = False

    def begin_process(self, data):
        dataset = self.datasets[f'dataset{data["index"]}']
        timeLeft = dataset['timeLeft']
        status = dataset['status']
        toggle_goal = dataset['toggle_goal']
        edit_goal = dataset['edit_goal']
        complete_goal = dataset['complete_goal']
        isInfinite = data['goal_amount'] == 'infinite'
        infiniteTime = data['clock'] == '∞'

        while True:
            if data['status'] == 'EDITING' or data['status'] == 'PAUSED':
                while True:
                    if data['status'] in ['COMPLETE', 'INCOMPLETE', 'CONNECTION ERROR', 'RESUMING', 'N/A']:
                        break

                    if self.deleted:
                        cache = Cache(f'{os.environ["USERPROFILE"]}/AppData/Local/hypixel-goal-tracker', 'data.json')
                        if data['status'] == 'EDITING':
                            data['status'] = 'INCOMPLETE'
                        cache.store({'goals': dataset['main'].goals})
                        return

                    palette = QPalette()
                    brush = QBrush(QColor(186, 186, 186))
                    brush.setStyle(Qt.SolidPattern)
                    palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
                    palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
                    status.setPalette(palette)
                    status.setText(data['status'])
                    time.sleep(1.0)
                    if data['status'] == 'PAUSED':
                        data['paused_seconds'] += 1

            if self.finished or self.deleted:
                return

            if not infiniteTime:
                second = Clock().fromFormat(data['clock']).inSeconds()
                second -= 1

                if second <= -1:
                    break

                clock = Clock().fromSeconds(second).format()
                timeLeft.setText(clock)
                data['clock'] = clock
            else:
                timeLeft.setText(f'∞ ({convert_to_time(data["seconds"])} uptime)')

            time.sleep(1)
            data['seconds'] += 1

        self.finished = True
        if isInfinite:
            now = datetime.now()
            data['completed'] = now.strftime("%d/%m/%Y %H:%M:%S")
            data['status'] = 'COMPLETE'
            status.setText("COMPLETE")
            palette = QPalette()
            brush = QBrush(QColor(0, 171, 0))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
            palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
            status.setPalette(palette)
            complete_goal.setDisabled(False)
        else:
            status.setText("FAILED")
            palette = QPalette()
            brush = QBrush(QColor(170, 0, 0))
            brush.setStyle(Qt.SolidPattern)
            palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
            palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
            status.setPalette(palette)
            data['status'] = 'FAILED'
        toggle_goal.setDisabled(True)
        edit_goal.setDisabled(True)

    def manage_process(self, data, main):
        dataset = self.datasets[f'dataset{data["index"]}']
        progress = dataset['progress']
        timeLeft = dataset['timeLeft']
        status = dataset['status']
        complete_goal = dataset['complete_goal']
        edit_goal = dataset['edit_goal']
        toggle_goal = dataset['toggle_goal']
        isInfinite = data['goal_amount'] == 'infinite'
        api = main.api_sync
        exception = 0

        while True:
            if data['status'] == 'EDITING' or data['status'] == 'PAUSED':
                complete_goal.setDisabled(True)
                while True:
                    if self.deleted:
                        return
                    if data['status'] in ['COMPLETE', 'INCOMPLETE', 'CONNECTION ERROR', 'RESUMING', 'N/A']:
                        break
                    time.sleep(0.2)
            if self.finished or self.deleted:
                return

            determine = DManualSetup(data['api_gamemode_name'], data['api_goal_name'])
            isManual = determine.is_manual_needed()

            try:
                if data['api_gamemode_name'] == 'Hypixel':
                    if data['api_goal_name'] not in ['records', 'networkExpp']:
                        current_amount = api.player_stats[data['api_goal_name']]
                else:
                    stats = api.player_stats['stats'][data['api_gamemode_name']]
            except:
                if exception < 1:
                    exception += 1
                    time.sleep(1.0)
                    continue
                isManual = 'timeout'

            if isManual == 'timeout':
                complete_goal.setDisabled(True)
                if data['status'] != 'PAUSED' and data['status'] != 'EDITING':
                    data['status'] = 'INCOMPLETE'
                    status.setText("CONNECTION ERROR")
                    palette = QPalette()
                    brush = QBrush(QColor(159, 159, 159))
                    brush.setStyle(Qt.SolidPattern)
                    palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
                    palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
                    status.setPalette(palette)

            elif isManual != 'timeout':
                if not isManual:
                    try:
                        if data['api_gamemode_name'] == 'Pit':
                            if data['api_goal_name'] not in stats['profile']:
                                current_amount = stats['pit_stats_ptl'][data['api_goal_name']]
                            else:
                                current_amount = stats['profile'][data['api_goal_name']]
                        elif data['api_gamemode_name'] == 'WoolGames':
                            if data['api_goal_name'] == 'available_layers':
                                current_amount = stats['progression'][data['api_goal_name']]
                            elif data['api_goal_name'] == 'coins':
                                current_amount = stats[data['api_goal_name']]
                            else:
                                current_amount = stats['wool_wars']['stats'][data['api_goal_name']]
                        else:
                            current_amount = stats[data['api_goal_name']]
                    except:
                        try: current_amount
                        except: current_amount = data['current_amount'] if 'current_amount' in data else 0
                else:
                    try:
                        current_amount = processManuals(data['api_goal_name'], data['api_gamemode_name'], api)
                    except:
                        current_amount = data['current_amount'] if 'current_amount' in data else 0

                if isInfinite:
                    data['mid_amount'] = current_amount - data['starting_amount']
                    if data['mid_amount'] < 0:
                        data['starting_amount'] = current_amount
                    data['current_amount'] = current_amount
                    outOf = processProgress(data, progress_design=main.progress_design)
                    percentage = '∞'
                    percentage_str = ''
                else:
                    calc = 100 / data['goal_amount']

                    if data['milestone']:
                        data['current_amount'] = current_amount
                        outOf = processProgress(data, progress_design=main.progress_design)
                        percentage = round(current_amount * calc, 2)
                        if (current_amount * calc) < 100 and (current_amount * calc) > 99.99:
                            percentage = 99.99
                        if percentage >= 100:
                            percentage = 100.0
                        percentage_str = f"({percentage})%"
                    else:
                        data['mid_amount'] = current_amount - data['starting_amount']
                        if data['mid_amount'] < 0:
                            data['starting_amount'] = current_amount
                        data['current_amount'] = current_amount
                        outOf = processProgress(data, progress_design=main.progress_design)
                        percentage = round(data['mid_amount'] * calc, 2)
                        if (data['mid_amount'] * calc) < 100 and (data['mid_amount'] * calc) > 99.99:
                            percentage = 99.99
                        if percentage >= 100:
                            percentage = 100.0
                        percentage_str = f"({percentage})%"

                try:
                    if data['status'] != 'EDITING':
                        if percentage == '∞':
                            if outOf.split('/')[0] == '0':
                                color = 'color:#ea0000'
                            else:
                                color = 'color:#00ab00'
                        elif percentage > 50 and percentage < 100:
                            color = 'color:#f5a300'
                        elif percentage < 50:
                            color = 'color:#ea0000'
                        else:
                            color = 'color:#00ab00'
                        if 'font-size: 12pt' in outOf and progress.styleSheet() == "margin-bottom: 5px":
                            pass
                        elif 'font-size: 12pt' in outOf:
                            progress.setStyleSheet("margin-bottom: 5px")
                        else:
                            progress.setStyleSheet("margin-bottom: 0px")

                        if main.percentage_design:
                            progress.setText(f"<html><head/><body><p><span style=\"{color}\">{outOf} </span><span style=\" color:#2fe813;\">{percentage_str}</span></p></body></html>")
                        else:
                            progress.setText(f"<html><head/><body><p><span style=\"{color}\">{outOf}</span></p></body></html>")
                except:
                    return
                if isInfinite:
                    if data['status'] != 'PAUSED' and data['status'] != 'EDITING' and data['status'] != 'FAILED' and data['status'] != 'COMPLETE':
                        data['status'] = 'N/A'
                        status.setText("N/A")
                        palette = QPalette()
                        brush = QBrush(QColor(0, 171, 0))
                        brush.setStyle(Qt.SolidPattern)
                        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
                        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
                        status.setPalette(palette)
                    if data['status'] != 'FAILED' and data['status'] != 'COMPLETE':
                        toggle_goal.setDisabled(False)
                        complete_goal.setDisabled(True)
                else:
                    if (data['milestone'] and (current_amount >= data['goal_amount'])) or \
                            (not data['milestone'] and (data['mid_amount'] >= data['goal_amount'])):
                        now = datetime.now()
                        self.finished = True
                        data['status'] = 'COMPLETE'
                        status.setText("COMPLETE")
                        data['completed'] = now.strftime("%d/%m/%Y %H:%M:%S")
                        complete_goal.setDisabled(False)
                        toggle_goal.setDisabled(True)
                        edit_goal.setDisabled(True)
                        palette = QPalette()
                        brush = QBrush(QColor(0, 171, 0))
                        brush.setStyle(Qt.SolidPattern)
                        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
                        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
                        status.setPalette(palette)
                    else:
                        if data['status'] != 'PAUSED' and data['status'] != 'EDITING' and data['status'] != 'FAILED':
                            data['status'] = 'INCOMPLETE'
                            status.setText("INCOMPLETE")
                            palette = QPalette()
                            brush = QBrush(QColor(255, 0, 0))
                            brush.setStyle(Qt.SolidPattern)
                            palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
                            palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
                            status.setPalette(palette)
                        if data['status'] != 'FAILED' and data['status'] != 'COMPLETE':
                            toggle_goal.setDisabled(False)
                            complete_goal.setDisabled(True)
            time.sleep(1.2)