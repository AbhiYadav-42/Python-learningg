# HASHING is you take some data and run through a hash() which store in a hash (fixed-length output)
# kinda like this 
"""   password123  →  x8A9f0C2... (hash) """

# If the input is same means the hash is same if little bit chnage in the input , hash will be totally different 
#Passswords are never stored diirectly , instead stored in hashes..

import hashlib


h = hashlib.new("SHA256")
correct_pass = "MyPassword123567"
h.update(correct_pass.encode())

# h.update(b"")      # b =  means in a byte form

# print(h.digest())           # this shows in the raw byte form 

password_hash = h.hexdigest()        # this shows in the hexadecimal form and it is recommended
print(password_hash)
print("\n")

User_input = "MyPassword123467"
h = hashlib.new("SHA256")
h.update(User_input.encode())
print(h.hexdigest())




# Hashing is a ""one way"" function
"""  
password → hash   ✅ possible
hash → password   ❌ NOT possible
"""

#   Now u may think encryption but that's not an encryption
# Encryption can be reversed but not HASHING!


# There are various hashing algorthims but most used and kown hashing algorithm is SHA-256 -> 256bits



""" SALTING """
#  You know same input/ password means same hash , so attackers have the 
#  pre-computed table (Rainbow table) for better knowledge try searching it on GOOGLE! 

# To prevent this happenning we use SALTING method 
# it is like pouring little bit extra salt on your FOOD 
# by that i mean , ADDing the extra layer of text before Hashing 

"""Example- """
import hashlib
password = "hello@134"
salt = "X9@#"

final_pass = salt + password
hashed =  hashlib.sha256(final_pass.encode()).hexdigest()
# encode() =  The hashing works on bytes to convert string into bytes that's why encode is used       
print(hashed)

# now this is called hashing with the Salting + one-way + Stable + Secure