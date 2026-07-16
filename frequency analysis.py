
##caeser cipher##

#option select#
def selectoption():
    print("""
what do you want to do today?
~---------------~
(1) encrypt text
(2) decrypt text
(3) crack encrypted text via frequency analysis
~---------------~
""")
    opt = input()
    if opt == "1":
        encryptopt()
    elif opt == "2":
        decryptopt()
    elif opt == "3":
        frequencyanalysis()

#encrypt functions#
def encryptopt():
    plaintext, key = getPlaintextandKey()
    encrypted = encrypt(plaintext, key)
    print(encrypted)

def getPlaintextandKey():
    plaintext = input("enter text to be encrypted: ").lower()
    key = int(input("enter key to be used: "))%26
    return plaintext, key

def encrypt(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""
    for i in range(len(plaintext)):
        letter = plaintext[i]
        if letter in alphabet:
            index = alphabet.index(letter)
            newindex = (index+key)%26
            encrypted += alphabet[newindex]
        else:
            encrypted += letter
    return encrypted


#decrypt functions#
def decryptopt():
    encryptedtext = input("enter the encrypted text: ")
    key = int(input("enter key to be used in decryption: "))%26
    plaintext = decrypt(encryptedtext,key)
    print(plaintext)

def decrypt(encrytext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decrypted = ""
    for i in range(len(encrytext)):
        letter = encrytext[i]
        if letter in alphabet:
            index = alphabet.index(letter)
            newindex = (index-key)%26
            decrypted += alphabet[newindex]
        else:
            decrypted += letter
    return decrypted


#frequency analyser:
def frequencyanalysis():
   
   #position of letter in alphabet but orderd by highest avrage frequency
    posofletter = {'e': 4,
                't': 19,
                'a': 0,
                'o': 14,
                'i': 8,
                'n': 13,
                's': 18,
                'r': 17,
                'h': 7,
                'd': 3,
                'l': 11,
                'u': 20,
                'c': 2,
                'm': 12,
                'f': 5,
                'y': 24,
                'w': 22,
                'g': 6,
                'p': 15,
                'b': 1,
                'v': 21,
                'k': 10,
                'x': 23,
                'q': 16,
                'j': 9,
                'z':25
                }


   #get the frequency of the letters in the encrypted text
    encryptedtext = input("enter the encrypted text: ")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    frequency = {}
    for letter in alphabet:
        frequency[letter] = 0
    for i in range(len(encryptedtext)):
        letter = encryptedtext[i]
        if letter in alphabet:
            frequency[letter] += 1
   
   #print frequency of letters in the encrypted text
    print("\nletter : frequency")
    for letter in alphabet:
        print(f"{letter}: {frequency[letter]}")

    #sort and get a list of the letters in the encrypted text by frequency
    freq = dict(sorted(frequency.items(),key = lambda x:x[1], reverse=True))
    orderedbyfreq = list(freq.keys())
    print("\nOrdered by frequency: ")
    print(orderedbyfreq)

    #get the key and decrypt the ciphertext
    keys = getkey(orderedbyfreq, posofletter)

    #decrypt the top 5 possible and print results
    for i in range(5):
        key = keys[i]
        print(f"\nKey: {i+1}, \nDecrypted: \n{decrypt(encryptedtext, key)} ")
    correctkey = int(input("which key seems accurate? (1-5): "))
    print(f"\nCRACKED TEXT: \n{decrypt(encryptedtext, keys[correctkey-1])} \nwith the key: {keys[correctkey-1]}")

def getkey(encryletters, posofletters):
    keys = []
    for i in range(5):
        key = 26-((posofletters[encryletters[i]]-list(posofletters.values())[i]))%26
        keys.append(key)
    return keys
    
        
## main ##
selectoption()



# test script below
#       V V V 
# wkhfdhvdufbskhulvdzrqghuixohadpsohriprqrdoskdehwlfvxevwlwxwlrqzkhuhhdfkohwwhulvshulrglfdoobvkliwhgebdilahgqxpehurisrvlwlrqvwkhruljlqdowhawlvfrpsohwhobwudqviruphgexwwkhxqghuoblqjvwdwlvwlfdoilqjhusulqwriwkhudzodqjxdjhlvqhyhueurphqebwkhsurfhvvlqidfwdqborqjhuwdujhwphvvdjhzloovwloopdlqwdlqwkhhadfwvdphshdnvdqgydoohbvdvqrupdohqjolvksurylglqjvxiilflhqwfoxhvirudqdqdobvwwrtxlfnobghgxfhwkhklgghqnhbvlqfhwkhohwwhuhuhpdlqvrxuprvwfrpprqfkdudfwhulwlvdozdbvwkhehvwvwduwlqjsrlqwirudqbfudfnlqjvfulswrufdofxodwlrq
