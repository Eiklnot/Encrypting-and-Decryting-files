#!//usr/bin/env python3
import os
from cryptography.fernet import Fernet

FileToUnlock = input("What file do you want to decrypt?\n")

if FileToUnlock == "Encrypter.py" or FileToUnlock == "thekey.key" or  FileToUnlock == "Decrypter.py":
        print("This file does not need to be decrypted")
        exit()
else:
	with open("thekey.key", "rb") as key:
		secretkey = key.read()
	password = "gotcha"
	user_phrase = input("Enter the password to decrypt the file\n")
	if user_phrase == password:
		with open(FileToUnlock, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(FileToUnlock, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("Congrats, your file is decrypted")
	else:
		print("Wrong password")
