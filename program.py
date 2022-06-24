from ctypes.wintypes import PFLOAT
import os, math
import sys, random;
from decimal import *;
from hashlib import sha256
from numpy import var





def coprime(a, b):
    return gcd(a, b) == 1

def find_expoent(euler_function):
    # Generates a random expoent and test if it's coprime of the euler function, if it is, returns it.
    while(1):
        random_e = random.randint(0, euler_function-1)
        if (coprime(random_e,euler_function)):
            return random_e



def gcd(a, b):
    # got from https://github.com/jchen2186/rsa-implementation/blob/master/rsa.py
    """
    Performs the Euclidean algorithm and returns the gcd of a and b
    """
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

def xgcd(a, b):
    # got from https://github.com/jchen2186/rsa-implementation/blob/master/rsa.py
    """
    Performs the extended Euclidean algorithm
    Returns the gcd, coefficient of a, and coefficient of b
    """
    x, old_x = 0, 1
    y, old_y = 1, 0

    while (b != 0):
        quotient = a // b
        a, b = b, a - quotient * b
        old_x, x = x, old_x - quotient * x
        old_y, y = y, old_y - quotient * y

    return a, old_x, old_y



# given by exercise
CRIPTO_P = 'B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371'
CRIPTO_G = 'A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28AD662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5'

# generated from program
CRIPTO_A = '610B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4319'

RECEIVED_B = '009B5747A5FAC436175B67CF91BC0977935F5ABB1285F89357AB65110E459BC7FA31CC8B9B77579D455227D61E947A14F11048060AEF6BE0A59CB5EFEE05CC856A6C14E52C6D640008BB431C75FE1651E1C2106AD269B7C31EE19162C90A2AD7EB4464B2379153BDCE0D9B31528F05049EAF8A55EF241B03747A383C56CD3C1487'


if __name__ == "__main__":

    sys.setrecursionlimit(1500)
    n_length = 1024

    p  = int(CRIPTO_P,16)
    g  = int(CRIPTO_G,16)
    a  = int(CRIPTO_A,16)
    received_B  = int(RECEIVED_B,16)
    
    bigA = pow(g,a,p)
        

    print("p = ")
    print(p) 
    print("g = ")
    print(g) 

    print("bigA = ")
    print(hex(bigA)) 


    ######## PROGRAM START


    input_B = int(input("Input B value in hexadecimal:\n").replace(" ",""),16)

    V = pow(input_B,a,p)

    print ("\n\nV =")
    print (hex(V))

    print ("\n")
    

    hash = sha256(bytes.fromhex(str(hex(V))[2:]))
    S = hash.hexdigest()
    print('S= ', S)



    programEnd = False
    while(programEnd == False):
        cmd = -1
        try:
            cmd = int(input("\n\nChoose an option\n 0 - Leave\n 1- Cipher message \n 2- Decipher message \n 3- Generate new keys\n"))
        except:
            print("Invalid command")

        if (cmd == 0):
            programEnd = True

        elif (cmd == 1): # CRYPT ADICIONAR LIMITE MENSAGEM

            publicN = int(input("\n\nInsert n ( 0 to use private key )\n"))
            if (publicN == 0): 
                publicN = cripto_n
                publicE = cripto_e
            else:
                publicE = int(input("\n\nInsert e (0 to use private key)\n"))
            
            inputText = str(input("\n\nInsert text to be ciphered\n"))
        
            # Convert INPUT to ASCII int
            codedMessage = ord(inputText[0])
            for i in range(1,len(inputText)):
                codedMessage = codedMessage * 100
                codedMessage += ord(inputText[i])
            print("ascii: ",int(codedMessage))    
            
            # Process M
            print ("M =  ")
            print(pow(int(codedMessage),publicE,publicN))


        elif (cmd == 2): # DECRYPT
            publicN = int(input("\n\nInsert n ( 0 to use private key )\n"))
            if (publicN == 0): 
                publicN = cripto_n
                publicD = cripto_d
            else:
                publicD = int(input("\n\nInsert d ( 0 to use private key )\n"))
             
            cipheredM = int(input("\n\nInsert ciphered message\n"))
            
            decodedMessage = pow(int(cipheredM),publicD,publicN)
            print(" \n Decoded message: ")
            strDecodedMessage = str(decodedMessage)
            i = 0
            while ( i+1 < len(strDecodedMessage)):
                print(str(chr(int(strDecodedMessage[i])*10 + int(strDecodedMessage[i+1]))), end = '')
                i += 2
            strDecodedMessage = ""
                

        elif (cmd == 3): # NEW KEYS
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            cripto_p = number.getPrime(n_length, os.urandom)
            print("p = ")
            print(cripto_p) 
            cripto_q = number.getPrime(n_length, os.urandom)
            print("d = ")
            print(cripto_q) 

            cripto_n = cripto_p * cripto_q
            print ("n = ")
            print(cripto_n)

            cripto_euler = (cripto_p - 1)*(cripto_q - 1)

            cripto_e = find_expoent(cripto_euler)
            print ("e =" )
            print(cripto_e)


            xgcd_return,a,b = xgcd(cripto_e,cripto_euler) 
            if (a < 0):
                cripto_d = a + cripto_euler
            else:
                cripto_d = a
            print ("d =" )
            print(cripto_d)
        else:
            print("Incorrect message\n")
    """ 
    Encryption: <number> * e mod n = <cryptogram>

    Decryption: <cryptogram> * d mon n = <number>
    """ 