Insecure Password Storage Vulnerability
1. Overview
This activity demonstrates a real and common cybersecurity vulnerability: insecure password storage. A vulnerable system was implemented that stores user passwords in plaintext, and then a secure version was created using cryptographic hashing.
This shows:
- What the vulnerability is
- How it can be exploited
- How to fix it properly

2. Vulnerable Version (Plaintext Storage)
The file vulnerable_password_storage.py simulates an insecure registration system.
Vulnerability details:

- Passwords are stored directly in users.txt
- No hashing, no encryption
- Anyone with file access can see every user’s password
- This is a real-world vulnerability found in many data breaches

Example plaintext output:
test123:secret

This demonstrates the vulnerability clearly.

3. Secure Version (Hashed Password Storage)
The file secure_password_storage.py fixes the vulnerability.
Security improvements:

- Password is encoded, then hashed using bcrypt (or hashlib if bcrypt unavailable)
- A random salt is automatically added
- Output is stored in users_secure.txt
- The stored value becomes non-reversible, protecting users even if the file leaks

Example hashed output:
user123:$2b$12$lyVLi4rw0eebAuLRdAfbCu8bTNGn9GARFvrVQKZazSI4njEb3Tt/G

This proves the system is now secure.

4. Files Included
vulnerable_password_storage.py    # insecure version
secure_password_storage.py        # fixed version
users.txt                         # plaintext output (evidence)
users_secure.txt                  # hashed output (evidence)
screenshots/
    insecure_run.png
    plaintext_file.png
    secure_run.png
    hashed_file.png


5. How to Run the Programs
a. Insecure version:

   "python vulnerable_password_storage.py"

   Creates users.txt containing plaintext passwords.
b. Secure version:

   "python secure_password_storage.py"

   Creates users_secure.txt with hashed passwords.

6. What This Demonstrates

This activity shows:

- How insecure password storage exposes users
- Why plaintext passwords are dangerous
- How hashing protects passwords from attackers
- The difference between vulnerable and secure implementations

This is a realistic and widely applicable cybersecurity vulnerability.

This README documents the implementation, evidence, and fix for the vulnerability.
