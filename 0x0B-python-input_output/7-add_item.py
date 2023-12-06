#!/usr/bin/python3
"""Module 7"""
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    data = load_from_json_file("add_item.json")
except Exception:
    data = []

save_to_json_file(data + sys.argv[1:], "add_item.json")
