import os


FILE_EXTENSIONS = {
    "PNG Image": ".png",
    "JPEG Image": ".jpg",
    "PDF Document": ".pdf",
    "ZIP Archive": ".zip",
    "Windows Executable": ".exe"
}


def get_file_size(filename):
    try:
        size = os.path.getsize(filename)
        size = size / 1024
        return f"{size:.2f} KB"

    except FileNotFoundError:
        return "File not found"



def get_extension(filename):
    extension = os.path.splitext(filename)[1]
    return extension



def check_extension(file_type, extension):
    if file_type in FILE_EXTENSIONS:
        if FILE_EXTENSIONS[file_type] == extension.lower():
            return True
        else:
            return False

    return True