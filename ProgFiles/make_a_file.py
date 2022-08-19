@use IO::FS
Func IO::main():
    FS.mkfile("A_file")
if __name__ == "__MDOS__":
    main()