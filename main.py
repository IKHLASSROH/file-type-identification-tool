import os

from hash_utils import calculate_hash
from file_identifier import identify_file
from file_metadata import get_file_size, get_extension, check_extension
from folder_scanner import scan_folder



def analyze_file(filename):

    file_type = identify_file(filename)

    if file_type is None:
        print(" File not found!")
        return


    file_size = get_file_size(filename)

    extension = get_extension(filename)

    extension_status = check_extension(file_type, extension)

    file_hash = calculate_hash(filename)


    print("\n========== FILE ANALYSIS ==========")
    print("File :", filename)
    print("File Type :", file_type)
    print("SHA256 :", file_hash)
    print("Size :", file_size)
    print("Extension :", extension)


    if extension_status:
        print("Status : Extension OK")
    else:
        print("⚠ Warning : Extension mismatch!")


    print("===================================")



path = input("Enter file/folder path: ")


if os.path.isdir(path):

    files = scan_folder(path)

    for file in files:
        analyze_file(file)


else:

    analyze_file(path)