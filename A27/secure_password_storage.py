import bcrypt

print("=== User Registration (Secure Version) ===")

username = input("Enter username: ")
password = input("Enter password: ")

# Convert password to bytes
password_bytes = password.encode('utf-8')

# Hash the password using bcrypt (with automatic salt)
hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())

# Store username + hashed password
with open("/Users/navy651/Documents/users_secure.txt", "a") as f:
    f.write(f"{username}:{hashed.decode()}\n")

print("User registered successfully (SECURE).")
print("Password stored as a cryptographic hash in users_secure.txt")