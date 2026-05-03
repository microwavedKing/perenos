import os

def get_packages():
    
    os.system("sudo pacman -Qqe > datafiles/list_of_pacman.txt")
    os.system("sudo pacman -Qmq > datafiles/list_of_aur.txt")
    os.system("touch datafiles/list_of_need_package.txt")

    list_of_pacman = list(open("datafiles/list_of_pacman.txt"))
    list_of_aur = list(open("datafiles/list_of_aur.txt"))

    list_of_need_package = open("datafiles/list_of_need_package.txt", "w")
    aurs_dictionary = {}

    for package in list_of_aur:
        aurs_dictionary[package.split()[0]] = 1

    for package in list_of_pacman:
        pkg = package.split()[0]
        if aurs_dictionary.get(pkg) != None:
            continue
        
        list_of_need_package.write(f"{pkg} ")

get_packages()