import os
from util.process import convert_to_time

__title__ = 'app'
__author__ = 'Gloryness'
__license__ = 'MIT License'
__version__ = '0.0.2-alpha-03'
__module__ = os.getcwd()

if not __module__.endswith("app"):
    __module__ = __module__+'\\'
    is_executable = True
else:
    __module__ = __module__.replace("/", "\\").replace("src\\app", "")
    is_executable = False

path = lambda *p: __module__+'\\'.join(p)