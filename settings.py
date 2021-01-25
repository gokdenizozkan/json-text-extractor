mode = "w" 
# r = read/export, w = write/import         e.g. mode = "r"            r is for extracting text values into a txt file. w is for importing translated text files back into json file.

#add every object/dictionary item below other than the ARRAY that includes texts to be translated
other_dict_items = {
    "FileVersion": 1,
}

source_path = "en.json" # The JSON file
target_path_txt = "tr.txt"  # The TXT file for EXPORT purposes
target_path_json = "tr.json" # The JSON file for IMPORT purposes

if mode == "w":
    IsImport = True

array_name = "Entries" #name of the Array that holds the dictionaries of text values in the source file
text_name = "Value" #name of the Key of the inner-dictionary that holds the text values
newLine_symbol = "#" #Please insert a symbol that cannot be found in the source file when you CTRL+F, e.g. #
if IsImport:
    key_name = "Key"  #name of the Key of the inner-dictionary that holds value of where the text is located