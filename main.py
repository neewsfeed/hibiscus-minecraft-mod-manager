import time
import os
import pathlib
import shutil
import urllib.request
import csv

''' Colors '''
MAIN2 = '\033[38;5;85m'
GREEN = '\033[38;5;169m'
GRAY = '\033[38;5;183m'
MAIN = '\033[38;5;219m'
MAIN3 = '\033[38;5;218m'
RED = '\033[38;5;207m'
FAIL = '\033[1;91m'
ORANGE = '\033[0;38;5;177m'
LRED = '\033[0;38;5;205m'
BOLD = '\033[1m'
PURPLE = '\033[0;38;5;141m'
BLUE = '\033[0;38;5;147m'
UNDERLINE = '\033[4m'
UNSTABLE = '\033[5m'
END = '\033[0m'


''' MSG Prefixes '''
INFO = f'{MAIN}Info{END}'
WARN = f'{ORANGE}Warning{END}'
IMPORTANT = f'{ORANGE}Important{END}'
FAILED = f'{RED}Fail{END}'
ERR = f'{LRED}Error{END}'
DEBUG = f'{ORANGE}Debug{END}'
GRN_BUL = f'[{GREEN}*{END}]'

def haxor_print(text, leading_spaces = 0):

    text_chars = list(text)
    current, mutated = '', ''

    for i in range(len(text)):
        
        original = text_chars[i]
        current += original
        mutated += f'\033[1;38;5;210m{text_chars[i].upper()}\033[0m'
        print(f'\r{" " * leading_spaces}{mutated}', end = '')
        time.sleep(0.05)
        print(f'\r{" " * leading_spaces}{current}', end = '')
        mutated = current

    print(f'\r{" " * leading_spaces}{text}')


haxor_print(f"{INFO} ✿ Hibiscus 1.0")
haxor_print(f"{INFO} ✿ Made with love by @newsfeed")
print("\n", end='')
haxor_print(f"{INFO} ✿ Loading %appdata%/.minecraft/mods")
appdata_dir = os.environ['APPDATA']
try:
    mods_path = pathlib.WindowsPath(f"{appdata_dir}\\.minecraft\\mods")
    mods_list = []
    for currentFile in mods_path.iterdir():
        mods_list.append(currentFile)
except Exception as e:
    haxor_print(f"{FAILED} ✿ Something failed :c. {e}. Exiting.")
    exit()

haxor_print(f"{INFO} ✿ Succesfuly loaded mod files")
print("\n", end='')
for i in range(len(mods_list)):
        print(f"{INFO} ✿ Mod Name: [{i}] {str(mods_list[i]).split("\\")[-1]}")

print(f"\n{GRN_BUL}{MAIN3} ✿ Options:{END}")
print(f"{GRN_BUL} ✿ [1] Install a mod (locally downloaded)")
print(f"{GRN_BUL} ✿ [2] Delete a mod")
print(f"{GRN_BUL} ✿ [3] Download mod from online repo (github repo)")
option = input(f"{GRN_BUL} ✿ > Select an option: ")
if option == str(1):
    path_to_mod_to_copy = input(f"{GRN_BUL} ✿ > What is the path of the mod you want to install?: ")
    try:
        shutil.copy(path_to_mod_to_copy, f"{appdata_dir}\\.minecraft\\mods")
    except Exception as e:
        print(f"{GRN_BUL} ✿ > Failed installing {path_to_mod_to_copy.split("\\")[-1]} {e}")
        exit()
    print(f"{GRN_BUL} ✿ > Succesfuly installed {path_to_mod_to_copy.split("\\")[-1]}")

if option == str(2):
    mod_to_delete = input(f"{GRN_BUL} ✿ > Select the ID of the mod to delete: ")

    y_or_no = input(f"{GRN_BUL} ✿ > Are you sure you want to delete {str(mods_list[int(mod_to_delete)]).split("\\")[-1]}? y/n: ")
    if y_or_no.lower() == "y":
        print(f"{GRN_BUL} ✿ > Deleting {str(mods_list[int(mod_to_delete)]).split("\\")[-1]}")
        try:
            os.remove(mods_list[int(mod_to_delete)])
        except Exception as e:
            print(f"{GRN_BUL} ✿ > Failed deleting {str(mods_list[int(mod_to_delete)]).split("\\")[-1]} {e}")
            exit()
        print(f"{GRN_BUL} ✿ > Succesfuly deleted {str(mods_list[int(mod_to_delete)]).split("\\")[-1]}")
    else:
        print(f"{GRN_BUL} ✿ > Operation canceled")
        exit()

if option == str(3):
    mod_dict = {}
    print(f"{GRN_BUL} ✿ > Pick a online mod id from the following mod index: {MAIN}{BOLD}{UNDERLINE}https://github.com/neewsfeed/hibiscus-mod-repository/blob/main/index.csv{END}")
    mod_id = input(f"{GRN_BUL} ✿ > Mod ID: ")
    print(f"{GRN_BUL} ✿ > Downloading latest mod index...")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/neewsfeed/hibiscus-mod-repository/main/index.csv", "mod_index.csv")
    with open("mod_index.csv", mode='r', newline='') as mod_index:
        csvreader = csv.DictReader(mod_index)
        for row in csvreader:
            mod_id = int(row['mod_id'])  # Convert mod_id to integer
            mod_name = row['mod_name']
            mod_dict[mod_id] = mod_name
    os.remove('mod_index.csv')
    print(f"{GRN_BUL} ✿ > Starting download for: {mod_dict[mod_id]}")
    urllib.request.urlretrieve(f"https://raw.githubusercontent.com/neewsfeed/hibiscus-mod-repository/main/{mod_dict[mod_id]}", mod_dict[mod_id])
    print(f"{GRN_BUL} ✿ > Finished the download process. Starting the install process ")
    try:
        shutil.copy(mod_dict[mod_id], f"{appdata_dir}\\.minecraft\\mods")
    except Exception as e:
        print(f"{GRN_BUL} ✿ > Failed installing {mod_dict[mod_id]} {e}")
        exit()
    print(f"{GRN_BUL} ✿ > Succesfuly installed {mod_dict[mod_id]}")
    os.remove(mod_dict[mod_id])