'''Importing modules'''
import time
import ChorusFruit as CF
scr = CF.Screen()
BAR_LEFT_TEXT = '['
BAR_CENTER_TEXT = ''
BAR_RIGHT_TEXT = '%Hour:%Minute:%Second' + ']'
def var(inputs):
    output = inputs
    vardict = {'%Hour': time.strftime('%H'), '%Minute': time.strftime('%M'), '%Second': time.strftime('%S')}
    for i in vardict:
        output = output.replace(i, vardict[i])
    return output
class Top_Bar(object):
    '''The Bar at the Top'''
    global BAR_LEFT_TEXT
    global BAR_RIGHT_TEXT
    global BAR_CENTER_TEXT
    def __init__(self) -> None:
        pass
    def set(self, LEFT: str, CENTER: str, RIGHT: str) -> None:
        '''Set Text of Top-Left of TopBar'''
        global BAR_LEFT_TEXT
        global BAR_RIGHT_TEXT
        global BAR_CENTER_TEXT
        BAR_LEFT_TEXT = LEFT
        BAR_CENTER_TEXT = CENTER
        BAR_RIGHT_TEXT = RIGHT

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
