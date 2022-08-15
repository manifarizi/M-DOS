"""Importing modules"""
import os
import pickle
os.chdir(os.path.dirname(__file__))
dir_sys = {'#': ['home', {'File_Name': 'text.txt'}],
'#/home': ['Dir1', 'Dir2'],
'#/home/Dir1': ['nul'],
'#/home/Dir2': ['nul']}
file_sys = {'#/text.txt': 'This is a text file'}
DComands = ['cd', 'read', 'ls', 'mkdir', 'mkfile', 'loadFS', 'save', 'del', 'rmdir', 'cd..']
DComandsl1 = ['cd', 'read', 'mkdir', 'mkfile', 'del', 'rmdir']
Programs = []
for i in os.listdir('ProgFiles'):
    Programs.append(i[0:-3])
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
    """reads a fileS"""
    for item in file_sys:
        if item == WORKING_DIR + '/' + name:
            print(file_sys[WORKING_DIR + '/' + name])
    save()

def cd(name):
    """change directory"""
    global WORKING_DIR
    if is_dir(name):
        if exist_dir(name):
            WORKING_DIR = WORKING_DIR + '/' + name
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
        print('deleted!')
        dir_sys[WORKING_DIR].remove({'File_Name': name})
        del file_sys[WORKING_DIR + '/' + name]
    except ValueError:
        print('Delete: File Not Found!')
    save()


def rmdir(name):
    """removes a diretory"""
    if exist_dir(name):
        print('deleted!')
        del dir_sys[WORKING_DIR + '/' + name]
        dir_sys[WORKING_DIR].remove(name)
    else:
        print('rmdir: Dir Not Found!')
    save()

def save():
    """saves the files and dirs"""
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
