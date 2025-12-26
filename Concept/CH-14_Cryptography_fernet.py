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
