filedata = FS.readReturn(args[1])
FS.mkfile(args[2], filedata)
FS.delete(args[1])