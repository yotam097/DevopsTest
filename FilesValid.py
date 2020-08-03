import hashlib
import os

checksum = input("Enter file's checksum: ")

os.chdir("C:\\Users\\yotam.a\\Downloads")

filename = input("Enter the file name: ")
sha256_hash = hashlib.sha256()
with open(filename, "rb") as f:
    for byte_block in iter(lambda: f.read(4096), b""):
        sha256_hash.update(byte_block)
    dest_file_checksum = sha256_hash.hexdigest()
print(dest_file_checksum == checksum)
print("The file's checksum is: ", dest_file_checksum)
