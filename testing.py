#deleted the testing code this file was only run trial codes
import json as js
import os
import bcrypt as bc
def data_encrypt(text):#hashing the data entered by the user.This is to protect the data.
    bytes=text.encode('utf-8')
    salt=bc.gensalt()# salt-random data
    #hasing the text
    hashed_text=bc.hashpw(bytes,salt)
    return hashed_text.decode('utf-8')
def check_data(text,hashed_text):
    bytes=text.encode('utf-8')
    salt=bc.gensalt()
    hashed_input=bc.hashpw(bytes,salt).decode('utf-8')
    if hashed_input==hashed_text:
        return True
    return False
folder_path=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(folder_path,'customer_data.txt')
test=data_encrypt("Aarya")


#this converts normal dic to a json file 
with open(file_path,'r') as f:
    data=eval(f.read())
    t=js.dumps(data)
with open(file_path,'w') as f:
    f.write(t)

  



with open(file_path,'r') as t:
    data=js.loads(t.read())
empty={} 
count=0   
for i in data:
    if type(data[i])==int:
        empty[i]=data[i]
    else:    
        val=data_encrypt(data[i])
        empty[i]=val
data=js.dumps(empty)
with open(file_path,'w') as f:
    f.write(data)
