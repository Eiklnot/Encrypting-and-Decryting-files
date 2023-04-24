#!//usr/bin/env python3
import os

from cryptography.fernet import Fernet

fileToLock = input("What file do you want to encrypt?\n")

if fileToLock =="Encrypter.py" or fileToLock == "thekey.key" or fileToLock == "Decrypter.py":
	print("You can not encrypt this file")
	exit()
else:
	key = Fernet.generate_key()
	with open("thekey.key", "wb") as thekey:
		thekey.write(key)
	with open(fileToLock, "rb") as thefile:
		contents = thefile.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(fileToLock, "wb") as thefile:
		thefile.write(contents_encrypted)

print("Your file is encrypted")
