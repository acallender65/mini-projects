#My Encryption and Decryption Tool

#This is a simple encryption and decryption tool that can be used to encrypt and decrypt text using different types of ciphers.
print("Welcome to My Encryption and Decryption Tool!")


def d1():
    print("What would you like to do?")
    print("    1. Use a Cipher")# caesar cipher, keyword and railfence only atm
    print("    2. Use Public Key Cryptography") #not added yet
    print("    3. Use the Euclidean Algorithm")
    decision1 = input("Please type 1, 2 or 3:")
    if decision1 == "1":
        print("Types of Ciphers:")
        print("    Monoalphabetic Ciphers:")
        print("         Caesar Cipher")
        print("         Keyword Cipher")
        print("    Permutation Ciphers:")
        print("         Railfence Cipher")
        print("    Polyalphabetic Ciphers:")
        print("         Vigenere Cipher")
        print("         Playfair Cipher")
    elif decision1 == "2":
        print("Public Key Cryptography:")
        print("    Diffie Hellman Key Exchange")
        print("    Elgamal Cipher")
    elif decision1 == "3":
        print("    Euclidean Algorithm")
    else:
        print("Please pick a valid option")
        decision1= d1()
    return decision1
    

decision1 = d1()

def d3():
    print("Would you like to encrypt or decrypt?")
    decision3 = input("Please type encrypt or decrypt:")
    if decision3.lower() == "encrypt":
        print("You have chosen to encrypt")
        encrypt = True
        decrypt = False
    elif decision3.lower() == "decrypt":
        print("You have chosen to decrypt")
        decrypt = True
        encrypt = False
    else:
        print("Please pick a valid option")
        decision3 = d3()
    return encrypt, decrypt


def cc(encrypt, decrypt):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetlist = []
    ciphertext = ""
    plaintext = ""
    ciphertextkey = []
    for i in range(0, len(alphabet)):
        alphabetlist = alphabetlist + [alphabet[i]]
    shift = input("What is the shift number?")
    if shift.isnumeric() == True:
        shift = int(shift)%26
        fpart = alphabetlist[0:shift]
        lpart = alphabetlist[shift:len(alphabetlist)]
        ciphertextkey = lpart + fpart
        if encrypt is True:
            plaintext = input("What is the plaintext?")
            for j in range(0, len(plaintext)):
                if plaintext[j].lower() in alphabetlist:
                    index = alphabetlist.index(plaintext[j].lower())
                    ciphertext = ciphertext + ciphertextkey[index]
                else:
                    ciphertext = ciphertext + plaintext[j]
            print("The ciphertext is: " + ciphertext)         
        elif decrypt is True:
            ciphertext = input("What is the ciphertext?")
            for j in range(0, len(ciphertext)):
                if ciphertext[j].lower() in ciphertextkey:
                    index = ciphertextkey.index(ciphertext[j].lower())
                    plaintext = plaintext + alphabetlist[index]
                else:
                    plaintext = plaintext + ciphertext[j]
            print("The plaintext is: " + plaintext)
    else:
        print("Please pick a valid option")
        cc(encrypt, decrypt)        

def kc(encrypt, decrypt):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetlist = []
    newalphalist = []
    ciphertext = ""
    plaintext = ""
    ciphertextkey = []
    for i in range(0, len(alphabet)):
        alphabetlist = alphabetlist + [alphabet[i]]
    kw = input("What is the keyword?")
    if kw.isalpha() is True:
        newalphalist = alphabetlist
        for j in range(0, len(kw)):
            index = newalphalist.index(kw[j].lower())
            ciphertextkey = ciphertextkey + [newalphalist[index]]
            newalphalist = newalphalist[0:index] + newalphalist[index+1:len(newalphalist)]
        ciphertextkey = ciphertextkey + newalphalist    
        if encrypt is True:
            plaintext = input("What is the plaintext?")
            for j in range(0, len(plaintext)):
                if plaintext[j].lower() in alphabetlist:
                    index = alphabetlist.index(plaintext[j].lower())
                    ciphertext = ciphertext + ciphertextkey[index]
                else:
                    ciphertext = ciphertext + plaintext[j]
            print("The ciphertext is: " + ciphertext)         
        elif decrypt is True:
            ciphertext = input("What is the ciphertext?")
            for j in range(0, len(ciphertext)):
                if ciphertext[j].lower() in ciphertextkey:
                    index = ciphertextkey.index(ciphertext[j].lower())
                    plaintext = plaintext + alphabetlist[index]
                else:
                    plaintext = plaintext + ciphertext[j]
            print("The plaintext is: " + plaintext)
    else:
        print("Please pick a valid option")
        kc(encrypt, decrypt)  


def rc(encrypt, decrypt):
    ciphertext = []
    plaintext = ""
    rows = input("What is the row number?")
    if rows.isnumeric() == True:
        if encrypt is True:
            plaintext = input("What is the plaintext?")
            length = len(plaintext)
            value = int(rows)*2 -2
            for i in range(0, int(rows)):
                for j in range(i, len(plaintext), value):
                    ciphertext = ciphertext + [plaintext[j]]
                    if i < (int(rows) - 1) and i > 0:
                        value2 = value - 2*i
                        ciphertext = ciphertext + [plaintext[value2+j]]
                        print(ciphertext, value2, plaintext[value2]) 
            print("The ciphertext is: " + "".join(ciphertext))         
        elif decrypt is True: #tiaehssrifneialc (test with row 3) hluerdelohrlwoaow (test with row 5)   
            plaintext = []
            encryptedtext = input("What is the ciphertext?") 
            for o in range(0, len(encryptedtext)):
                ciphertext = ciphertext + [encryptedtext[o]]
            print(ciphertext)    
            length = len(ciphertext)
            value = int(rows)*2 -2
            quotient = length//value
            remainder = length%value
            if remainder == 0:
                frow = ciphertext[0:quotient]
                if remainder < int(rows):
                    lrow = ciphertext[len(ciphertext)-quotient:len(ciphertext)] 
                    midrow = ciphertext[quotient:len(ciphertext)-quotient] 
                else:
                    lrow = ciphertext[len(ciphertext)-quotient-1:len(ciphertext)]  
                    midrow = ciphertext[quotient:len(ciphertext)-quotient-1]     
            elif remainder > 0:
                frow = ciphertext[0:quotient+1]
                if remainder < int(rows):
                    lrow = ciphertext[len(ciphertext)-quotient:len(ciphertext)]  
                    midrow = ciphertext[quotient+1:len(ciphertext)-quotient]
                else:
                    lrow = ciphertext[len(ciphertext)-quotient-1:len(ciphertext)] 
                    midrow = ciphertext[quotient+1:len(ciphertext)-quotient-1] 
            mid = []
            tempmidrow = midrow            
            for k in range(2, int(rows)):
                if remainder < k:
                    mid = mid + [tempmidrow[0:(quotient*2)]]
                    tempmidrow = tempmidrow[(quotient*2):len(tempmidrow)]
                elif remainder >= k and remainder < ((2*int(rows)) - k):
                    mid = mid + [tempmidrow[0:(2*quotient)]]
                    tempmidrow = tempmidrow[(2*quotient):len(tempmidrow)]
                elif remainder >= ((2*int(rows)) - k):
                    mid = mid + [tempmidrow[0:(2*quotient)]]
                    tempmidrow = tempmidrow[(2*quotient):len(tempmidrow)] 
            maxi = max(len(frow), len(lrow))     
            for l in range(0, maxi):
                try:
                    plaintext = plaintext + [frow[l]] 
                except:
                        plaintext = plaintext + [""]     
                for m in range(0, len(mid)):
                    try:
                        plaintext = plaintext + [mid[m][(2*l)]]
                    except:
                        plaintext = plaintext + [""] 
                try:        
                    plaintext = plaintext + [lrow[l]]   
                except:
                        plaintext = plaintext + [""]   
                for n in range(0, len(mid)):
                    try: 
                        plaintext = plaintext + [mid[len(mid)-1-n][(2*l)+1]]
                    except:
                        plaintext = plaintext + [""]
            print("The plaintext is: ", "".join(plaintext)) 
    else:
        print("Please pick a valid option")
        rc(encrypt, decrypt)   

def modfunc (big, small, xip, xic, yip, yic):
    remainder = big%small
    quotient = big//small
    holderx = xic
    holdery = yic
    xic = xip - (quotient*xic)
    yic = yip - (quotient*yic)
    xip = holderx
    yip = holdery
    print(remainder, "=", big, "x", "+", small, "y", "where x is", xic, "and y is", yic)
    big = small
    small = remainder
    return big, small, xip, xic, yip, yic



def euclidalgo():
    x = input("What is the first number?")
    y = input("What is the second number?")
    if x.isnumeric() is True and y.isnumeric() is True:
        x = int(x)
        y = int(y)
        if x > y:
            big = 0
            small = 0
            big, small, xip, xic, yip, yic = modfunc(x, y, 1, 0, 0, 1)
            while small != 0:
                big, small, xip, xic, yip, yic = modfunc(big, small, xip, xic, yip, yic)
            print("The GCD is: ", big)
        elif y > x:
            big = 0
            small = 0
            big, small, xip, xic, yip, yic = modfunc(y, x, 1, 0, 0, 1)
            while small != 0:
                big, small, xip, xic, yip, yic = modfunc(big, small, xip, xic, yip, yic)
            print("The GCD is: ", big)
        elif x == y:
            print("The GCD is: " + x)
        else:
            print("Please pick a valid option")
            euclidalgo()
    else:
        print("Please pick a valid option")
        euclidalgo()                     

def d2(decision1):
    if decision1 == "1":
        print("What cipher would you like to use?")
        print("    1. Caesar Cipher")
        print("    2. Keyword Cipher")
        print("    3. Railfence Cipher")
        print("    4. Vigenere Cipher") #add this
        print("    5. Playfair Cipher") #add this
        decision12 = input("Please type 1, 2, 3, 4 or 5:")
        if decision12 == "1":
            print("Caesar Cipher")
            encrypt, decrypt = d3()
            cc(encrypt, decrypt)
        elif decision12 == "2":
            print("Keyword Cipher")
            encrypt, decrypt = d3()
            kc(encrypt, decrypt)
        elif decision12 == "3":
            print("Railfence Cipher")
            encrypt, decrypt = d3()
            rc(encrypt, decrypt)
        elif decision12 == "4":
            print("Vigenere Cipher")
            encrypt, decrypt = d3()
            vc(encrypt, decrypt)
        elif decision12 == "5":
            print("Playfair Cipher")
            encrypt, decrypt = d3()
            pc(encrypt, decrypt)
        else:
            print("Please pick a valid option")
            decision12 = d2()
        return decision12
    elif decision1 == "2":
        print("What would you like to use?")
        print("    a. Diffie Hellman Key Exchange") #add this
        print("    b. Elgamal Cipher") #add this
        decision22  = input("Please type a or b:")
        if decision22.lower() == "a":
            print("Diffie Hellman Key Exchange")
        elif decision22.lower() == "b":
            print("Elgamal Cipher")
        else:
            print("Please pick a valid option")
            decision12 = d2()
        return decision22
    elif decision1 == "3":
        print("The Euclidean Algorithm")
        euclidalgo()


decision2 = d2(decision1)
