@use IO::FS
Func IO::main():
    filedata = FS.readReturn(args[1])
    FS.mkfile(args[2], filedata)
    FS.delete(args[1])
if __name__ == "__MDOS__":
    main()