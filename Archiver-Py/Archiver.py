import os

def find_dirs():
    config = list(open("Archiver.conf"))
    print(config)
    return [[dir.split("\n") for dir in config[5].split()], config[13].split("\n")]

def last_name(path):
    path = path.split("/")
    last = "ROOT"

    for i in range(len(path) - 1, -1, -1):
        if path[i] != "":
            last = path[i]
            break

    return last

def archive_directory(path, iterat):
    global saving_dir
    os.system(f"sudo 7z a -t7z {saving_dir}{last_name(path)}-zipsfile{iterat}.7z {path}")
    print(f"File {path} created")

finds = find_dirs()
dirs, saving_dir = finds[0], finds[1][0]
print(dirs)
iterat = 0
for dir in dirs:
    print(dir[0])
    archive_directory(dir[0], iterat)
    iterat += 1