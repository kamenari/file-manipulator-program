import sys

if len(sys.argv) < 2:
    print("コマンドを指定してください。")
    sys.exit(1)

command = sys.argv[1]

if command == "reverse" or command == "copy":
    if len(sys.argv) != 4:
        print("inputpath と outputpath を指定してください。")
        sys.exit(1)
    inputpath = sys.argv[2]
    outputpath = sys.argv[3]
    contents = ""
    with open(inputpath) as f:
        contents = f.read()
    if command == "reverse":
        contents = contents[::-1]
    with open(outputpath, "w") as f:
        f.write(contents)
    print("操作が完了しました。")

elif command == "duplicate-contents":
    if len(sys.argv) != 4:
        print("inputpath と n を指定してください。")
        sys.exit(1)
    inputpath = sys.argv[2]
    n = sys.argv[3]
    if not n.isdigit() or int(n) < 1:
        print("n は1以上の整数で指定してください。")
        sys.exit(1)
    n = int(n)
    contents = ""
    with open(inputpath) as f:
        contents = f.read()
    with open(inputpath, "w") as f:
        f.write(contents * n)
    print("操作が完了しました。")

elif command == "replace-string":
    if len(sys.argv) != 5:
        print("inputpath, needle, newstring を指定してください。")
        sys.exit(1)
    inputpath = sys.argv[2]
    needle = sys.argv[3]
    newstring = sys.argv[4]
    contents = ""
    with open(inputpath) as f:
        contents = f.read()
    contents = contents.replace(needle, newstring)
    with open(inputpath, "w") as f:
        f.write(contents)
    print("操作が完了しました。")

else:
    print("不明なコマンドです。")
    sys.exit(1)
