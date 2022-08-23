# Write a function that determines if any given string 450 has all unique characters 197 (i.e. no character in the string is duplicated). If the string has all unique characters, print “all unique”. If the string does not have all unique characters, print “duplicates found.”

def duplicate_character(a_string):
    a_string = a_string.lower()
    new_string = a_string.replace(" ", "")
    each_char_list = list(new_string)
    each_char_set = set(each_char_list)
    if len(each_char_list) != len(each_char_set):
        print("duplicates found.")
    else:
        print("all unique")

duplicate_character("Hello my name is Kat")
duplicate_character("Yo I Kat")