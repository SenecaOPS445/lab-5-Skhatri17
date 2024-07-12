#!/usr/bin/env python3
# Author ID: SKHATRI17

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    try:
        f = open(file_name, 'r')
        content = f.read()
        f.close()
        return content
    except FileNotFoundError:
        return f"Error: File '{file_name}' not found."

def read_file_list(file_name):
    # Takes a file_name as string for a file name,
    # return its entire contents as a list of lines without new-line characters
    try:
        f = open(file_name, 'r')
        lines = f.readlines()
        f.close()
        return [line.strip('\n') for line in lines]
    except FileNotFoundError:
        return []

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
