BAR_LEFT_TEXT = ''
class Top_Bar(object):
    global BAR_LEFT_TEXT
    '''The Bar at the Top'''
    def __init__(self) -> None:
        pass
    def set(self, data: str) -> None:
        global BAR_LEFT_TEXT
        '''Set Text of Top-Left of TopBar'''
        BAR_LEFT_TEXT = data
    def remove(self):
        global BAR_LEFT_TEXT
        '''Removes Text of Top-Left of TopBar'''
        BAR_LEFT_TEXT = ''
