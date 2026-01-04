""" Cryptography """
# it is practice used  for securing the information while transmitting to other computer or stroing on computer 
# it just deals with the encryption of the plain text into the cipher text and decryption of cipher text to plain text 

#  We gonna use the Fernet ,
# Fernet is a module, guarantees that data encrypted using it cannot be further manipulated or read without the key. 


from cryptography.fernet import Fernet

# Gernrate the key
key = Fernet.generate_key()


#  giving varibale to value of key 
k = Fernet(key)

# converting plain text to cipher-text
conversion = k.encrypt(b'Hello World!')

# display the cipher text
print(conversion,"\n")


# Decrypting cipher text
Decrypt_conversion = k.decrypt(conversion)

# display the decrypted text
print(Decrypt_conversion)






""" Using Passwords with Fernet """

import os
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend

password = b'84260'

# Adding salting with randomness of OS 
salt = os.urandom(16)
print(salt)

# Key derivation function -  cryptographic hash function 
# Password Based Key Derivation Function 2 hash-based message authentication 
kdf = PBKDF2HMAC(
  algorithm=hashes.SHA256() ,
  length=32,
  salt=salt,
  iterations=100000,
  backend=default_backend()
)

# Derive key 
key = kdf.derive(password)


# verify the key - need to make another kdf (i am not gonna do.) 
# kdf.verify(password,key)

#Make key-fernet compatible
Fernet_key = urlsafe_b64encode(key)

#create a fernet object
f = Fernet(Fernet_key)

#Encrypt 
add_password = f.encrypt(b'abhii@134')
print(add_password)

#Decrypt
de = f.decrypt(add_password).decode('utf-8')
print(de)