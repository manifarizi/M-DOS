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
for i in os.listdir('ProgFiles'):
    Apps.append(i[0:-3])
WORKING_DIR = '#'
def is_file(file_name):
    """Return True if the input is a dict"""
    if isinstance(file_name, dict):
        return True
    else:
        return False
    save()

def filename(name):
    """Return name of a file"""
    if not name is None:
        if is_file(name):
            return name['File_Name']
        else:
            return name
    else:
        print('nul')
    save()

def is_dir(file_name):
    """Returns True if input is not Dict"""
    if isinstance(file_name, dict):
        return False
    else:
        return True
    save()
def exist_dir(name):
    """Returns True if input is not dict"""
    if name in dir_sys[WORKING_DIR]:
        return True
    else:
        return False
    save()

def ls():
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

def mkdir(name):
    """makes a directory"""
    if not exist_dir(name):
        dir_sys.update(dict(zip([WORKING_DIR + '/' + name], [['nul']])))
        dir_sys[WORKING_DIR].append(name)

    else:
        print('mkdir: File Or Dir with Same name Exist')
        save()

def read(name):
    """reads a files"""
    try:
        print(file_sys[WORKING_DIR + '/' + name])
    except KeyError:
        print('read: File Not Found!')
    save()

def cd(name):
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

def cdback():
    """change directory to one dicectory before"""
    global WORKING_DIR
    if WORKING_DIR != '#':
        WORKING_DIR = '/'.join(WORKING_DIR.split('/')[0:-1])
    save()

def mkfile(name, data=''):
    """makes a folder"""
    if not exist_dir(name):
        if not WORKING_DIR + '/' + name in [i for i in file_sys]:
            dir_sys[WORKING_DIR].append({'File_Name': name})
        file_sys.update({WORKING_DIR + '/' + name: data})
    else:
        print('mkfile: File Or dir with Same name Exist')
    save()

def delete(name):
    """deletes a file"""
    try:
        dir_sys[WORKING_DIR].remove({'File_Name': name})
        del file_sys[WORKING_DIR + '/' + name]
    except ValueError:
        print('delete: File Not Found!')
    finally:
        print('deleted!')
    save()


def rmdir(name):
    """removes a diretory"""
    if exist_dir(name):
        del dir_sys[WORKING_DIR + '/' + name]
        dir_sys[WORKING_DIR].remove(name)
        print('deleted!')
    else:
        print('rmdir: Dir Not Found!')
    save()

def save():
    appReset()
    """Saves the files and dirs"""
    global file_sys
    global dir_sys
    with open("Save.mafs", "wb") as a_file:
        pickle.dump((file_sys, dir_sys), a_file)

def loadFS():
    """Loads the old Saves"""
    global file_sys
    global dir_sys
    with open("Save.mafs", "rb") as a_file:
        file_sys, dir_sys = pickle.load(a_file)
        appReset()

def list_dir():
    """list dir"""
    LIST_DIR_VAR = []
    for item in dir_sys[WORKING_DIR]:
        if not item == 'nul':
            LIST_DIR_VAR.append(filename(item))
    return LIST_DIR_VAR
def appReset():
    """Resets Apps Dir"""
    dir_sys['#/home/Apps'] = []
    for item in Apps:
        dir_sys['#/home/Apps'].append({'File_Name': item})

    if 'Apps' not in dir_sys['#/home']:
        dir_sys['#/home'].append('Apps')
