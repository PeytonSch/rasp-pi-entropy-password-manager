#this file will handle reading and writing to and from files.

from Crypto.Cipher import AES



def encrypt(message):
    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message)

    print(nonce,ciphertext,tag)

    return [nonce,ciphertext,tag]


def decrypt(nonce,ciphertext,tag):

    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        print("The message is authentic:", plaintext)
    except ValueError:
        print("Key incorrect or message corrupted")



n,ct,tag = encrypt(b"This is my plaintext")

#write encrypted info to file
f = open("savefile.txt","a")
user = "User1"
f.write(user + "\n" + str(n) + "\n" + str(ct) + "\n" + str(tag) + "\n")
'''
f.write("\n BREAK \n ")
f.write(str(n))
f.write("\n BREAK \n ")
f.write(str(ct))
f.write("\n BREAK \n ")
f.write(str(tag))
'''
f.close()

f = open("savefile.txt", "r")
lines = f.readlines()
read_list = []
for line in lines:
    read_list.append(line)
print(read_list)
#read from file and send to decrypt function
n = read_list[0]
ct = read_list[1]
tag = read_list[2]

n[len(n)-1]

#decrypt(n,ct,tag)
