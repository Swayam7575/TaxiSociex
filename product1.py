 
import string
 
 
# A list containing all characters
all_letters= string.ascii_letters
  
     
"""
create a dictionary to store the substitution
for the given alphabet in the plain text
based on the key
"""
  
     
dict1 = {}
key = int(input("Enter key value: "))
  
for i in range(len(all_letters)):
    dict1[all_letters[i]] = all_letters[(i*key)%len(all_letters)]
  
  
plain_txt= input("Enter plaintext: ")
print(plain_txt)
cipher_txt=[]
  
# loop to generate ciphertext
  
for char in plain_txt:
    if char in all_letters:
        temp = dict1[char]
        cipher_txt.append(temp)
    else:
        temp =char
        cipher_txt.append(temp)
         
cipher_txt= "".join(cipher_txt)
print("Cipher Text is: ",cipher_txt)


