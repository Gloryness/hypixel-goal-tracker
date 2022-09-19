from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase
from pypresence import Presence
import sys
import threading
import asyncio
import time
from app import path, __version__

def rich_presence(rpcstate):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    rpc = Presence("1020806141887922197")
    rpc.connect()
    start = time.time()

    while win.isVisible():
        if len(rpcstate.state) > 128:
            rpcstate.state = f"{rpcstate.state[:125]}..."
        rpc.update(state=rpcstate.state, details=rpcstate.details, large_image="hypixel", large_text=rpcstate.large_text, start=start)
        time.sleep(1.0)

class RPCState:
    state = ""
    details = "Tracking Hypixel Stats"
    large_text = ""

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

    rpcstate = RPCState()

    win = Main(rpcstate)
    win.show()

    rpcstate.state = f"Active Goals: {len(win.goals):,} | Completed Goals: {len(win.completed_goals):,}"
    rpcstate.large_text = f"v{__version__}"

    thread = threading.Thread(target=rich_presence, args=(rpcstate,))
    thread.start()

    sys.exit(app.exec())