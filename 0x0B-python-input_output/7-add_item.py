#!/usr/bin/python3

"""
Python script thatadds all arguments to a
Python lists, and then saves them to a file
Next time the script is called, it appends to the
existing file
"""
import sys
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"
if not os.path.isfile(filename):
    save_to_json_file([], filename)

my_list = load_from_json_file(filename)

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

save_to_json_file(my_list, "add_item.json")
