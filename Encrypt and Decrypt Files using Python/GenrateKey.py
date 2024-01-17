from cryptography.fernet import Fernet
key = Fernet.generate_key()
 
# 'wb' opens files for writing in binary format which is not human readable 
with open('filekey.key','wb')as filekey:
    filekey.write(key)
    
