import hashlib

filename = input("Enter file name: ")

with open(filename, "rb") as file:
    content = file.read()

hash_value = hashlib.sha256(content).hexdigest()

print("\nSHA256 Hash:")
print(hash_value)
