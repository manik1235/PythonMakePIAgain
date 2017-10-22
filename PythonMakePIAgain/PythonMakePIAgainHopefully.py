
""" Print digits of PI; code adapted from the second, shorter solution
at http://www.codecodex.com/wiki/Calculate_digits_of_pi#Python
"""

from time import perf_counter

def pi_digits_Python(digits):
    scale = 10000
    maxarr = int((digits / 4) * 14)
    arrinit = 2000
    carry = 0
    arr = [arrinit] * (maxarr + 1)
    output = ""

    for i in range(maxarr, 1, -14):
        total = 0
        for j in range(i, 0, -1):
            total = (total * j) + (scale * arr[j])
            arr[j] = total % ((j * 2) - 1)
            total = total / ((j * 2) - 1)
            ## """ print("%s",j,' ','')



        output += "%04d" % (carry + (total / scale))
        carry = total % scale

    return output;

def test_py():
    digits = 1000;

    start = perf_counter()
    print("Starting at {0}", str(int(start * 10000)))
    output = pi_digits_Python(digits);
    elapsed = perf_counter() - start;

    print("PIneapple penguins to " + str(digits) + " digits in " + str(int(elapsed * 10000)/10000) + " seconds:")

    ## replace inserts the decimal point
    print(output.replace("3", "3.", 1))


def decrypt(encryptedmsg):
    ### K  ->  M, O -> Q, E -> G
    ### 11 -> 13, 15 -> 17, 5 -> 7

    for choice in range(-25,25):
        print('Choice: ',choice)
        unencryptedmsg = ''
        for letter in encryptedmsg:
            unencryptedmsg = unencryptedmsg + chr((ord(letter) + choice))
        print(unencryptedmsg)

def decryptagain(encryptedmsg):
    
  # newmsg = encryptedmsg.replace("m","k")

  # newmsg = encryptedmsg.replace("q","o")

  # newmsg = encryptedmsg.replace("g", "e")

    newmsg = encryptedmsg.replace("k","m")

    newmsg = encryptedmsg.replace("o", "q")

    newmsg = encryptedmsg.replace("e", "g")    
    
    
    print ("Encrypted Msg: ", encryptedmsg)
    print ("Decrypt'd Msg: ", newmsg)

def decrypttitle(encryptedmsg):
    from string import maketrans

    outtab = "koe"
    intab= "mqg"
    transtab = maketrans(intab,outtab)
    
    print (out.translate(out)) 

    #encryptedmsg2 = "test"
    #encryptedmsg2.translate()


if __name__ == "__main__":
    ## test_py();
    decryptstr = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
    otherstring = "everybody thinks twice before solving this."
    decryptagain(decryptstr)
    # decrypt(decryptstr)