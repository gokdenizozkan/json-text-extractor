#json-text-extractor (JTEx)
#written by Gökdeniz Özkan, github:gokdenizozkan
#Under GNU GPLv3 License

#
# imports
#

import json
from time import sleep

#
# defs
#

## functional
# to open files
def toRead():
    global source_path
    global source_file
    global source_data
    source_file = open(source_path, 'r', encoding="UTF-8")
    source_data = source_file.read()

def toWrite():
    global target_path_txt
    global target_file
    global target_data
    target_file = open(target_path_txt, 'r', encoding="UTF-8")
    target_data = target_file.readlines()

# to parse files
def toParseSource():
    global source_data
    global source_objects
    source_objects = json.loads(source_data)

def toParseTarget():
    global target_data
    global target_objects
    target_objects = json.loads(target_data)

# to close files
def toClose():
    global IsImport
    global source_file
    if IsImport:
        global target_file

        target_file.close()
    source_file.close()

## variable conversions
"""
JSON - Python
Object = Dictionary
Array = List

arrayTo_ListDict: It access to the OBJECT that contains ARRAYS of OBJECTS and converts them to a LIST that contains DICTIONARIES
TL;DR:
Object{     List[Object{}]      }  => Dict{     List[Dict{}]     }
it works only for "text values", not the other keys.


"""
def Array_To_ListDict():
    global source_objects
    global array_name
    global source_dicts_in_list
    source_dicts_in_list = source_objects[array_name]

def ListDict_Modifier_and_Export():
    global source_modified_list
    global text_name
    global newLine_symbol
    global target_path_txt
    global source_dicts_in_list

    with open(target_path_txt, 'w', encoding="UTF-8") as target_file:
        for i in range(len(source_dicts_in_list)):
            source_modified_list = source_dicts_in_list[i].get(text_name).replace("\n", newLine_symbol)           
            target_file.write("%s\n" %source_modified_list)
            
def Unmodifier_and_List_To_ListDict():
    global target_data
    global source_dicts_in_list
    global target_dicts_in_list
    global key_name
    global text_name
    global newLine_symbol
    
    for i in range(len(target_data)):
        if target_data[i] == "#\n":
            target_data[i] = {key_name: source_dicts_in_list[i].get(key_name), text_name: "\n"}
            target_dicts_in_list = target_data[:]
            continue
        target_data[i] = {key_name: source_dicts_in_list[i].get(key_name), text_name: target_data[i].replace(newLine_symbol, "\n").rstrip("\n")}
        target_dicts_in_list = target_data[:]

def Universal_Dict_Creator():
    global other_dict_items
    global source_objects
    global target_dicts_in_list
    global target_path_json

    source_objects = other_dict_items
    source_objects[array_name] = target_dicts_in_list

    with open(target_path_json, 'w', encoding="UTF-8") as target_file:
        json.dump(source_objects, target_file, ensure_ascii=False, indent=2)

#
# declarations
#

#
IsImport = False
IsSettings = False

#inputs
x = input("Do you have a settings file that is up-to-date?\ny/n\n\nTo use 'Write' function, you need to configure your settings.txt file.")
if x == "y":
    IsSettings = True
    exec(open("settings.py").read())
else:
    source_path = input("Source file's path (.json):\n")
    target_path_txt = input("Target file's path (.txt):\n")
    target_path_json = input("Target file's path (.json):\nThis is needed for 'Import' feature.\n")
    mode = input("What do you want to do?\nr/w (export/import)")
    if mode == "w":
        IsImport = True

    array_name = input("What is the name of the Array that holds the text values in the source file?\n")
    text_name = input("What is the name of the Key of the inner-dictionary that holds the text values?\n")
    newLine_symbol = input("Please insert a symbol that cannot be found in the source file when you CTRL+F, e.g. #\n")
    if IsImport:
        key_name = input("What is the name of the Key of the inner-dictionary that holds value of where the text is located?\n")
#
# code
#

# Opening the files
toRead()
if IsImport:
    toWrite()

print("Opening the files...\nIt is necessary to work on files.")

#Parsing the files
toParseSource()

print("Parsing the files...\nIt is necessary to import objects from JSON to Python.")

#Converting the variable types
toClose()
Array_To_ListDict()

print("Converting the variable types...\nIt is necessary to access, change, or manipulate the data.")

#Universal dict creator
#Modify the text and Export OR Unmodify the text and continue
try:
    if IsImport:
        Unmodifier_and_List_To_ListDict()
        Universal_Dict_Creator()
        print("Unmodifying the text, creating dictionaries in it, and creating a universal dictionary...\nThis is the part where we'll see the beans's benefits.")
    else:
        ListDict_Modifier_and_Export()
        print("Modifying and exporting the file.\nWe're almost done.")
finally:
    print("The process is finished.\nYou may find your exported or imported data on your target path or source path.")
    exit