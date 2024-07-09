import os
import hashlib

# Directory containing theme files
themes_directory = 'themes.d'

# Function to calculate SHA256 hash of a file
def calculate_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

# Function to write manifest file with theme file names and hashes
def write_manifest_file():
    manifest_file = 'themes.d/MANIFEST'
    with open(manifest_file, 'w') as f:
        for filename in sorted(os.listdir(themes_directory)):
            if filename.endswith('.theme'):
                file_path = os.path.join(themes_directory, filename)
                file_hash = calculate_file_hash(file_path)
                f.write(f"{filename}\t{file_hash}\n")
                # Set file permissions to 644 (rw-r--r--)
                os.chmod(file_path, 0o644)

    print(f"Manifest file '{manifest_file}' has been created.")

# Generate manifest file
write_manifest_file()
