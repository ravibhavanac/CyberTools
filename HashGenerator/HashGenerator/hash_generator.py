import hashlib

text = input("Enter text: ")

print("\nMD5:")
print(hashlib.md5(text.encode()).hexdigest())

print("\nSHA1:")
print(hashlib.sha1(text.encode()).hexdigest())

print("\nSHA256:")
print(hashlib.sha256(text.encode()).hexdigest())

print("\nSHA512:")
print(hashlib.sha512(text.encode()).hexdigest())
