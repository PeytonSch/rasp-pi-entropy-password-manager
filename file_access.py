#this file will handle reading and writing to and from files.

from Crypto.Cipher import AES
import numpy as np

class manager:
    def manager():
        print("mananger intialized")

    def getOptions(password):
        print("Please select a menu option by entering its number: ")
        print("1: Save Password")
        print("2: Exit without saving password to manager")

        while True:
            user_selection = input("Selection: ")
            if user_selection == "1":
                addNewPasswordToManager(password)
                print("Password successfully saved to file")
                return
            elif user_selection == "2":
                return
            else:
                print("Selection",user_selection, "is not an option")


    def addNewPasswordToManager(password):
        print("Please enter the service that this password should be connected to.")
        service = input("Service:")

        encrypt_this_string = password
        encrypt_this_string = encrypt_this_string.encode(encoding='UTF-8')

        user = service
        user = user.encode(encoding='UTF-8')


        tempFileLines = []
        while len(tempFileLines) != 4:
            temp = open("tempFile.txt",'wb')
            n,ct,tag = encrypt(encrypt_this_string)
            temp.write(user)
            temp.write('\n'.encode(encoding='UTF-8'))
            temp.write(n)
            temp.write('\n'.encode(encoding='UTF-8'))
            temp.write(ct)
            temp.write('\n'.encode(encoding='UTF-8'))
            temp.write(tag)
            temp.write('\n'.encode(encoding='UTF-8'))
            temp.close()
            temp = open("tempFile.txt",'rb')
            tempFileLines = temp.readlines()
            temp.close()




        #write encrypted info to file
        f = open("savefile.txt","ab")
        print(type(n))
        f.write(user)
        f.write('\n'.encode(encoding='UTF-8'))
        f.write(n)
        f.write('\n'.encode(encoding='UTF-8'))
        f.write(ct)
        f.write('\n'.encode(encoding='UTF-8'))
        f.write(tag)
        f.write('\n'.encode(encoding='UTF-8'))


        f.close()

        return

    def recoverPassword():

        print("You have passwords saved for the following services:")

        for i in range(0,len(read_list),4):
            current = read_list[i].decode(encoding='UTF-8')
            print(current)

        print("Please type the name of the service you would like to recover your password for:")

        searchingFor = input("Service:")

        #find the right user
        for i in range(0,len(read_list),4):
            current = read_list[i].decode(encoding='UTF-8')
            current = current[:-1]
            if(current == searchingFor):
                n = read_list[i+1]
                ct = read_list[i+2]
                tag = read_list[i+3]
                break


        n = n[:-1]
        ct = ct[:-1]
        tag = tag[:-1]

        decrypt(n,ct,tag)

        return



    def encrypt(message):
        key = "Sixteen byte key"
        key = key.encode(encoding='UTF-8')
        cipher = AES.new(key, AES.MODE_EAX)
        nonce = cipher.nonce
        ciphertext, tag = cipher.encrypt_and_digest(message)

        #print(nonce,ciphertext,tag)

        return [nonce,ciphertext,tag]


    def decrypt(nonce,ciphertext,tag):


        key = "Sixteen byte key"
        key = key.encode(encoding='UTF-8')

        cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
        plaintext = cipher.decrypt(ciphertext)

        try:
            cipher.verify(tag)
            plaintext = plaintext.decode(encoding='UTF-8')
            print("The ciphertext is authentic, your password is:", plaintext)
            return
        except ValueError:
            print("Key incorrect or message corrupted")
            return


def readButtonLines():
    lines = np.loadtxt("buttonStatus.txt")
    print(type(lines))
    return lines
def readAudioLines():
    lines = np.loadtxt("soundDetectorStatus.txt")
    print(type(lines))
    return lines

def writeNewData(buttonData,audioData):
    np.savetxt("buttonStatus.txt",buttonData,fmt='%i')
    np.savetxt("soundDetectorStatus.txt",audioData,fmt='%i')
    return




'''
f = open("savefile.txt", "rb")
lines = f.readlines()
read_list = []

for line in lines:
    read_list.append(line)


#find the right user
searchingFor="User2"
for i in range(0,len(read_list),4):
    current = read_list[i].decode(encoding='UTF-8')
    current = current[:-1]
    if(current == searchingFor):
        n = read_list[i+1]
        ct = read_list[i+2]
        tag = read_list[i+3]
        break



#read from file and send to decrypt function



n = n[:-1]
ct = ct[:-1]
tag = tag[:-1]


decrypt(n,ct,tag)


test = np.array([1,0,0,1,1,0,1,0,1])

writeNewData(test,test)
'''
