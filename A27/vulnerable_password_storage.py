# vulnerable_password_storage.py

print("=== User Registration (Insecure Version) ===")

username = input("Enter username: ")
password = input("Enter password: ")

# VULNERABILITY:
# Storing passwords in plaintext in a file
with open("/Users/navy651/Documents/users.txt", "a") as f:
    f.write(f"{username}:{password}\n")

print("User registered successfully (INSECURE).")
print("Password stored in plaintext inside users.txt")