"""Importing modules"""
from time import sleep
import ChorusFruit as CF
scr = CF.Screen()
BAR_LEFT_TEXT = ''
class Top_Bar(object):
    '''The Bar at the Top'''
    global BAR_LEFT_TEXT
    def __init__(self) -> None:
        pass
    def set(self, data: str) -> None:
        '''Set Text of Top-Left of TopBar'''
        global BAR_LEFT_TEXT
        BAR_LEFT_TEXT = data
    def remove(self):
        '''Removes Text of Top-Left of TopBar'''
        global BAR_LEFT_TEXT
        BAR_LEFT_TEXT = ''
class MSGBox(object):
    '''Makes a message box'''
    def __init__(self) -> None:
        pass
    def Warn(self, text: str):
        '''Makes a Warning message box'''
        print("  ▄")
        print(" ▞!▚ " + text.replace('\n', '').replace('\r', ''))
        print(" ▔▔▔")
    def Error(self, text: str):
        '''Makes a Error message box'''
        print(" ▄▄▄")
        print(" ▌X▐ " + text.replace('\n', '').replace('\r', ''))
        print(" ▀▀▀")
    def Info(self, text: str):
        '''Makes a Error message box'''
        print(" ▄▄▄")
        print(" ▌i▐ " + text.replace('\n', '').replace('\r', ''))
        print(" ▀▀▀")
