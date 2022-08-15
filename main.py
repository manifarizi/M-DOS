"""Importing modules"""
import sys
import os
import time
import threading
import ChorusFruit as CF
import mafs as FS
import SysCalls as SC
os.chdir(os.path.dirname(__file__))
FS.loadFS()
with CF.Screen() as scr:
    for L in range(CF.LINES + 1):
        for C in range(CF.COLS + 1):
            scr.write(C, L, ' ', '[back_blue]')


def titlebar(_):
    """Makes a bar on top of screen"""
    scr = CF.Screen()
    while True:
        time.sleep(0.5)
        scr.Header(Left='[' + SC.BAR_LEFT_TEXT, Right= time.strftime(r'%H:%M:%S') + ']')
        sys.stdout.flush()
title = threading.Thread(target=titlebar, args=(None,))
title.start()
def System(key):
    """Run a System Command"""
    if key.split('(')[0] in FS.DComands:
        if len(key.split('(')) == 2:
            if key.split('(')[0] == 'cd':
                FS.cd(key.split('(')[1][0:-1])
            elif key.split('(')[0] == 'mkdir':
                FS.mkdir(key.split('(')[1][0:-1])
            elif key.split('(')[0] == 'read':
                FS.read(key.split('(')[1][0:-1])
            elif key.split('(')[0] == 'del':
                FS.delete(key.split('(')[1][0:-1])
            elif key.split('(')[0] == 'rmdir':
                FS.rmdir(key.split('(')[1][0:-1])
            try:
                if key.split('(')[0] == 'mkfile':
                    FS.mkfile(key.split('(')[1].split(', ')[0], key.split(', ')[1][0:-1])
            except IndexError:
                if key.split('(')[0] == 'mkfile':
                    FS.mkfile(key.split('(')[1][0:-1])
        else:
            if key.split('(')[0] == 'ls':
                FS.ls()
            elif key.split('(')[0] == 'save':
                FS.save()
            elif key.split('(')[0] == 'loadFS':
                FS.loadFS()
            elif key.split('(')[0] == 'cd..':
                FS.cdback()
    elif key.split('(')[0] in FS.Programs:
        vlist = {'SC': SC,'FS': FS, 'CF': CF, 'FullInput': key, 'ChorusFruit': CF, 'FileSystem': FS, 'System': System, 'SC': SC}
        if len(key.split('(')) == 1:
            args = ()
            vlist.update({'args': args})
            exec(open('ProgFiles\\' + key.split('(')[0] + '.py', 'r', encoding='utf-8').read(), vlist)
        elif len(key.split('(')) == 2:
            args = []
            for i in range(len(key.replace(', ', '(').split('('))):
                args.append(key.replace(', ', '(').split('(')[i])
            args[len(args) - 1] = args[len(args) - 1][0:-1]
            args = tuple(args)
            vlist.update({'args': args})
            exec(open('ProgFiles\\' + key.split('(')[0] + '.py', 'r', encoding='utf-8').read(), vlist)
    else:
        print('M-DOS: Program Not Found')

while True:
    key = input(f'{CF.AnsiList.back_blue}{FS.WORKING_DIR}>')
    System(key)
    