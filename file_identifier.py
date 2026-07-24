from signatures import SIGNATURES 
from signatures import SIGNATURES


def identify_file(filename):
    try:
        with open(filename, "rb") as file:
            header = file.read(8)

        for signature in SIGNATURES:
            if header.startswith(signature):
                return SIGNATURES[signature]

        return "Unknown File Type"

    except FileNotFoundError:
        return None
    