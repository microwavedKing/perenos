import os

def find_dir():
    config = list(open("Unpacker.conf"))
    print(config)
    return config[8].split("\n")[0]

path = find_dir()
print(path)
os.system(f"ls {path} > {path}files.txt")
os.system(f"mkdir {path}unpacks/")
files = list(open(f"{path}files.txt"))

for file in files:
    file = file.split("\n")[0]
    print(f"7z x -t7z {path}{file} {path}unpacks/")
    os.system(f"7z x -t7z {path}{file} -o{path}unpacks/")