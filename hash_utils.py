import hashlib 
def calculate_hash(filename):
    try:
        with open(filename, "rb") as file:
            sha256 = hashlib.sha256()

            data = file.read()

            sha256.update(data)

            return sha256.hexdigest()

    except FileNotFoundError:
        return None
