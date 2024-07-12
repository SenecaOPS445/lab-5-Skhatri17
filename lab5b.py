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
def append_file_string(file_name, string_of_lines):
    try:
        f = open(file_name, 'a')  # Append mode
        f.write(string_of_lines)
        f.close()
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
def write_file_list(file_name, list_of_lines):
    try:
        f = open(file_name, 'w')  # Write mode (overwrite)
        for line in list_of_lines:
            f.write(line + '\n')
        f.close()
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
def copy_file_add_line_numbers(file_name_read, file_name_write):
    try:
        f_read = open(file_name_read, 'r')
        f_write = open(file_name_write, 'w')

        line_number = 1
        for line in f_read:
            f_write.write(f"{line_number}:{line}")
            line_number += 1

        f_read.close()
        f_write.close()

    except FileNotFoundError:
        print(f"Error: One of the files '{file_name_read}' or '{file_name_write}' not found.")

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)
    print(read_file_string(file1))

    write_file_list(file2, list1)
    print(read_file_string(file2))

    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
    