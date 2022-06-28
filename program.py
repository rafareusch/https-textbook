from audioop import reverse
from ctypes.wintypes import PFLOAT
import os, math
import sys, random;
from decimal import *;
from hashlib import sha256
from numpy import var
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad





# given by exercise
CRIPTO_P = 'B10B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4371'
CRIPTO_G = 'A4D1CBD5C3FD34126765A442EFB99905F8104DD258AC507FD6406CFF14266D31266FEA1E5C41564B777E690F5504F213160217B4B01B886A5E91547F9E2749F4D7FBD7D3B9A92EE1909D0D2263F80A76A6A24C087A091F531DBF0A0169B6A28AD662A4D18E73AFA32D779D5918D08BC8858F4DCEF97C2A24855E6EEB22B3B2E5'

# generated from program
CRIPTO_A = '610B8F96A080E01DDE92DE5EAE5D54EC52C99FBCFB06A3C69A6A9DCA52D23B616073E28675A23D189838EF1E2EE652C013ECB4AEA906112324975C3CD49B83BFACCBDD7D90C4BD7098488E9C219A73724EFFD6FAE5644738FAA31A4FF55BCCC0A151AF5F0DC8B4BD45BF37DF365C1A65E68CFDA76D4DA708DF1FB2BC2E4A4319'

RECEIVED_B = '009B5747A5FAC436175B67CF91BC0977935F5ABB1285F89357AB65110E459BC7FA31CC8B9B77579D455227D61E947A14F11048060AEF6BE0A59CB5EFEE05CC856A6C14E52C6D640008BB431C75FE1651E1C2106AD269B7C31EE19162C90A2AD7EB4464B2379153BDCE0D9B31528F05049EAF8A55EF241B03747A383C56CD3C1487'
RECEIVED_MSG = 'CD100D314D4E5DC6BED4E2B8B6B7EAC43E1DE477E44B9C616DE4F380D63D722D3DEF09C5102C2ED24021546EC3CCE8D27428908D6682BF64211AE9354BBD28C67C7DCAAC419AFFA2D0D2D7824DEE3A151C69545A0B3FCA4EDD2A0C8520836FFC8CA8010BA7C0316B517B8BA5E48C62AF57CF5D73EDE858F09DBA9FEF33B51D7CFB055F3ADE235126F6F7F6F4888C8FBF'

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

    input_B =  int(input("Input B value in hexadecimal:\n").replace(" ",""),16)  # int(RECEIVED_B,16) #

    intV = pow(input_B,a,p)

    print ("V =")
    print (hex(intV))


    

    hash = sha256(bytes.fromhex(str(hex(intV))[2:]))
    hexS = hash.hexdigest()
    print('S= ',hexS)

    hexKey = hexS[0:32]
    print('AES key= ', hexKey)


    input_MSG =  int(input("Input IV+MSG value in hexadecimal:\n").replace(" ",""),16) #int(RECEIVED_MSG,16)

    hexIv = str(hex(input_MSG))[2:34]
    hexMsg = str(hex(input_MSG))[34:]

    print('IV = ', hexIv )
    print('MSG = ', hexMsg )

    print ("\n")

    
    aes = AES.new(bytes.fromhex(hexKey), AES.MODE_CBC, bytes.fromhex(hexIv))
    aes1 = AES.new(bytes.fromhex(hexKey), AES.MODE_CBC, bytes.fromhex(hexIv))
    aes2 = AES.new(bytes.fromhex(hexKey), AES.MODE_CBC, bytes.fromhex(hexIv))

    # DECRYPT PROFESSOR MESSAGE
    recvPlaintextRaw = unpad(aes.decrypt(bytes.fromhex(hexMsg)),16)
    recvPlaintext = recvPlaintextRaw.decode("utf-8")
    print('Received Plaintex: ', recvPlaintext)



    print ("\n")
    sendPlaintextRaw = recvPlaintextRaw[::-1]
    print('Sent Plaintex: ', sendPlaintextRaw.decode("utf-8"))


    #ENCRYPT AND CONVERT TO HEXSTRING
    ciphertext = aes1.encrypt(pad(sendPlaintextRaw,16))
    ciphertext = ciphertext.hex()
    print('Ciphertext Hex String: ',ciphertext)
    print ("\n")
    print ("\n")


    # DECODE THE SENT MESSAGE (VERIFICATION)
    testPlaintext = aes2.decrypt(bytes.fromhex(ciphertext))
    print('RAW DECODE',testPlaintext)
    print('DECODED Plaintex: ', testPlaintext.decode("utf-8"))




