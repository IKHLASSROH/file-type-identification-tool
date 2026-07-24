import os


def scan_folder(folder_path):
    files = []

    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            files.append(full_path)

    return files