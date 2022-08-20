"""Importing modules"""
import os
import pickle
os.chdir(os.path.dirname(__file__))
dir_sys = {'#': ['home', {'File_Name': 'text.txt'}],
    '#/home': ['Dir1', 'Apps'],
    '#/home/Apps': ['nul'],
    '#/home/Dir2': ['nul']}
file_sys = {'#/text.txt': 'This is a text file'}
DComands = ['cd', 'read', 'ls', 'mkdir', 'mkfile', 'loadFS', 'save', 'del', 'rmdir', 'cd..']
DComandsl1 = ['cd', 'read', 'mkdir', 'mkfile', 'del', 'rmdir']
Apps = []
MEXEApps = []
for i in os.listdir('ProgFiles'):
    if i[-3:len(i)] == '.py':
        Apps.append(i[0:-3])
    elif i[-5:len(i)] == '.mexc':
        MEXEApps.append(i[0:-5])
WORKING_DIR = '#'
def is_file(file_name: str) -> bool:
    """Return True if the input is a dict"""
    if isinstance(file_name, dict):
        return True
    else:
        return False
    save()

def filename(name: str) -> str:
    """Return name of a file"""
    if not name is None:
        if is_file(name):
            return name['File_Name']
        else:
            return name
    else:
        print('nul')
    save()

def is_dir(file_name: str) -> bool:
    """Returns True if input is not Dict"""
    if isinstance(file_name, dict):
        return False
    else:
        return True
    save()
def exist_dir(name: str) -> bool:
    """Returns True if input is not dict"""
    if name in dir_sys[WORKING_DIR]:
        return True
    else:
        return False
    save()

def ls() -> None:
    """list dir"""
    appReset()
    for item in dir_sys[WORKING_DIR]:
        if not item == 'nul':
            if not is_file(i):
                try:
                    print(item + ' <Dir>')
                except TypeError:
                    print(filename(item))
    save()

def mkdir(name: str) -> None:
    """makes a directory"""
    if not exist_dir(name):
        dir_sys.update(dict(zip([WORKING_DIR + '/' + name], [['nul']])))
        dir_sys[WORKING_DIR].append(name)

    else:
        print('mkdir: File Or Dir with Same name Exist')
        save()

def read(name: str) -> None:
    """reads a files"""
    try:
        print(file_sys[WORKING_DIR + '/' + name])
    except KeyError:
        print('read: File Not Found!')
    save()
def readReturn(name: str) -> str:
    try:
        return file_sys[WORKING_DIR + '/' + name]
    except KeyError:
        print('read: File Not Found!')
def cd(name: str) -> None:
    """change directory"""
    global WORKING_DIR
    for i in name.split('/'):
        if is_dir(i):
            if exist_dir(i):
                WORKING_DIR = WORKING_DIR + '/' + i
            else:
                print("cd: Can't Find Dir With this name")
        else:
            print("cd: Can't Find Dir With this name")
    save()

def cdback() -> None:
    """change directory to one dicectory before"""
    global WORKING_DIR
    if WORKING_DIR != '#':
        WORKING_DIR = '/'.join(WORKING_DIR.split('/')[0:-1])
    save()

def mkfile(name: str, data: str='') -> None:
    """makes a file"""
    if not exist_dir(name):
        if not WORKING_DIR + '/' + name in [i for i in file_sys]:
            dir_sys[WORKING_DIR].append({'File_Name': name})
        file_sys.update({WORKING_DIR + '/' + name: data})
    else:
        print('mkfile: File Or dir with Same name Exist')
    save()

def delete(name: str) -> None:
    """deletes a file"""
    try:
        dir_sys[WORKING_DIR].remove({'File_Name': name})
        del file_sys[WORKING_DIR + '/' + name]
    except ValueError:
        print('delete: File Not Found!')
    save()

def rmdir(name: str) -> None:
    """removes a diretory"""
    if exist_dir(name):
        del dir_sys[WORKING_DIR + '/' + name]
        dir_sys[WORKING_DIR].remove(name)
    else:
        print('rmdir: Dir Not Found!')
    save()

def save() -> None:
    """Saves the files and dirs"""
    appReset()
    global file_sys
    global dir_sys
    with open("Save.mafs", "wb") as a_file:
        pickle.dump((file_sys, dir_sys), a_file)

def loadFS() -> None:
    """Loads the old Saves"""
    global file_sys
    global dir_sys
    with open("Save.mafs", "rb") as a_file:
        file_sys, dir_sys = pickle.load(a_file)
        appReset()

def list_dir() -> None:
    """list dir"""
    LIST_DIR_VAR = []
    for item in dir_sys[WORKING_DIR]:
        if not item == 'nul':
            LIST_DIR_VAR.append(filename(item))
    return LIST_DIR_VAR
def appReset() -> None:
    """Resets Apps Dir"""
    dir_sys['#/home/Apps'] = []
    for item in Apps:
        dir_sys['#/home/Apps'].append({'File_Name': item})

    if 'Apps' not in dir_sys['#/home']:
        dir_sys['#/home'].append('Apps')
