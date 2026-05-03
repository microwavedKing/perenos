import os

def install_packages():
    packages = list(open("datafiles/list_of_need_package.txt"))
    
    os.system(f"sudo pacman -S {packages[0]}")