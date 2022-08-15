# maniFileSystem
A in-memory file-system
# commands:
### ls:
you can list files of a directory with ls command, you can use it like this:
```
ls()
```
or
```
ls
```
### cd:
it's change directory you can use it like this:
```
cd(dirName)
```
### mkdir:
You can make a directory like this:
```
mkdir(dirName)
```
### mkfile:
You can make a file like this:
```
mkfile(fileName, fileData)
```
### read:
You Can Read Files with Read command like:
```
read(fileName)
```
### del:
del is short for "delete" you can use it for deleting "files" like this:
```
delete(fileName)
```
### rmdir:
you can use rmdir for deleting "dirs" like this:
```
rmdir(dirName)
```
# Custom Programs
Programs Are just Python Files You can Create a Python File And Run it
but You can use Custom Modules like FileSystem
### File system
with FileSystem You can do Things Like 

Deleting Files, Making Files, Changing Files, Deleting Dirs, Making Dirs
if you see a Warning in VSCode ___Ignore the Warnings!___ Because We Changed The ```globals()```

For Deleting a File You can:

FS.del(fileName)
For Deleting a Dir You can:
```python
FS.rmdir(fileName)
```
For Deleting a Dir You can:

```python
FS.rmdir(fileName)
```

For Making a File You can:

```python
FS.mkfile(fileName, FileData)
# or
FS.mkfile(fileName)
# to make a blank file
```
For Reading a File You can:

```python
FS.read(fileName)
```
For Making a Variable of All Files You can:

```python
MyList = FS.listDir()
```
### FullInput
A Variable That Contains Code That Runed
### args
arguments that executed like:
```
ProgramName(args[0], args[1]) and to infinite
```
### System
Runs a Command in Shell