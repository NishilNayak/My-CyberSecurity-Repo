from cryptography.fernet import Fernet
with open('filekey.key','rb') as filekey:
    key = filekey.read()

fernet = Fernet(key)

with open('Myfile.txt','rb') as file:
    original = file.read()

encrypted = fernet.encrypt(original)

with open('Myfile.txt','wb') as encrypted_file:
    encrypted_file.write(encrypted)
