#My Encryption and Decryption Tool

#This is a simple encryption and decryption tool that can be used to encrypt and decrypt text using different types of ciphers.
print("Welcome to My Encryption and Decryption Tool!")


def d1():
    print("What would you like to do?")
    print("    1. Use a Cipher")# caesar ci[her, keyword and railfence only atm
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
        elif decision12 == "2":
            print("Keyword Cipher")
        elif decision12 == "3":
            print("Railfence Cipher")
        elif decision12 == "4":
            print("Vigenere Cipher")
        elif decision12 == "5":
            print("Playfair Cipher")
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


decision2 = d2(decision1)

def cc():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabetlist = []
    for i in range(0, len(alphabet)):
        alphabetlist = alphabetlist + [alphabet[i]]
    shift = input("What is the shift number?")
    if shift.isnumeric() == True:
        shift = int(shift)%26
        fpart = alphabetlist[0:shift]
        lpart = alphabetlist[shift:len(alphabetlist)]
        ciphertextkey = lpart + fpart
        if encrypt == True:
            print("The ciphertext key is:")
            print(ciphertextkey)
        elif decrypt == True:
            print("The plaintext key is:")
            print(ciphertextkey)
    
cc()