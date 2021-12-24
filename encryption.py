from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time


class Encryptor:
    def __init__(self, key):
        self.key = key

    def pad(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    def encrypt(self, message, key, key_size=256):
        message = self.pad(message)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(message)

    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            plaintext = fo.read()
        enc = self.encrypt(plaintext, self.key)
        with open(file_name + ".enc", 'wb') as fo:
            fo.write(enc)
        os.remove(file_name)

    def decrypt(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as fo:
            ciphertext = fo.read()
        dec = self.decrypt(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)


key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
clear = lambda: os.system('cls')

if os.path.isfile('data.txt.enc'):
    while True:
        password = str(input("\n Enter password: "))
        enc.decrypt_file("data.txt.enc")
        p = ''
        with open("data.txt", "r") as f:
            p = f.readlines()
        if p[0] == password:
            enc.encrypt_file("data.txt")
            break

    while True:
        clear()
        choice = int(
            input("\n > Press '1' to encrypt file.\n > Press '2' to decrypt file.\n > Press '0' to exit.\n\n >>> "))
        clear()
        if choice == 1:
            print()
            enc.encrypt_file(str(input(" Enter name of file to encrypt: ")))
            print("\n\n File encrypted! Going back...")
            time.sleep(3)
        elif choice == 2:
            print()
            enc.decrypt_file(str(input(" Enter name of file to decrypt: ")))
            print("\n\n File decrypted! Going back...")
            time.sleep(3)
        elif choice == 0:
            exit()
        else:
            print()
            print("\n Please select a valid option!")
            time.sleep(3)

else:
    while True:
        clear()
        password = str(input(
            "\n It seems you are using this for first time...Setting up stuff.\n Enter a permanent password that will be used for decryption: "))
        repassword = str(input("\n Confirm password: "))
        clear()
        if password == repassword:
            break
        else:
            print(" Passwords Mismatched! Rerouting in 5 seconds...")
            time.sleep(5)
    f = open("data.txt", "w+")
    f.write(password)
    f.close()
    enc.encrypt_file("data.txt")
    os.system('python encryption.py')
