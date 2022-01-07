alphabets = 'abcdefghijklmnopqrstuvwxyz '


def locate(x):
    return alphabets.find(x)


def key():
    word = input("Enter the word which is not Encrypted ").lower()
    encrypted = input("Enter the word which is Encrypted ").lower()
    a = word[0]
    b = encrypted[0]
    c = abs(locate(a) - locate(b))
    return c


def key_list():
    word = input("Enter the word which is not Encrypted ").lower()
    encrypted = input("Enter the word which is Encrypted ").lower()
    if len(word) == len(encrypted):
        word += " "
        c = ''
        for i in range(len(word) - 1):
            a = word[i]
            b = encrypted[i]
            c += str(abs(locate(a) - locate(b))) + " "
    return c


def encrypt():
    encrypted = ""
    word = input("enter the word to encrypt ").lower()
    word += ' '
    n = int(input("Enter the key value "))
    a = int(len(word)) - 1
    b = int(len(alphabets)) - 1
    for item in range(a):
        for obj in range(b):
            if word[item] == alphabets[obj]:
                x = obj + n
                if x < 26:
                    y = x
                else:
                    y = x - 26
                encrypted += alphabets[y]
    return encrypted


def decrypt():
    decrypted= ""
    word = input("enter the word to decrypt ").lower()
    word += ' '
    n = int(input("Enter the key value "))
    a = int(len(word)) - 1
    b = int(len(alphabets)) - 1
    for item in range(a):
        for obj in range(b):
            if word[item] == alphabets[obj]:
                x = obj - n
                if x < 0:
                    y = x + 26
                else:
                    y = x
                decrypted += alphabets[y]
    return decrypted


def location(x):
    return str(alphabets.find(x)+1)


def position():
    located = ''
    word = input("Enter the word to get it position ").lower()
    word += ' '
    a = len(word) -1
    for i in range(a):
        located += location(word[i]) + ' '
    return located


def encrypt_list():
    encrypted = ''
    word = input("Enter the word to be encrypted ").lower()
    keys = input("Enter the list of Keys ").split()
    word += ' '
    a = len(word) - 1
    i = 0
    for item in range(a):
        if i > len(keys)-1:
            i = 0
        x = locate(word[item]) + int(keys[i])
        i += 1
        if x < 26:
            y = x
        else:
            y = x - 26
        encrypted += alphabets[y]
    return encrypted


def decrypt_list():
    decrypted = ''
    word = input("Enter the word to be decrypted ").lower()
    keys = input("Enter the list of Keys ").split()
    word += ' '
    a = len(word) - 1
    i = 0
    for item in range(a):
        if i > len(keys) - 1:
            i = 0
        x = locate(word[item]) - int(keys[i])
        if x < 0:
            y = x + 26
        else:
            y = x
        decrypted += alphabets[y]
        i += 1
    return decrypted


i = 1
while i != 0:
    try:
        print("\nOptions can be performed on Cipher")
        print("Enter the option listed below (eg:1)\n  MENU")
        a = int(input("> Encrypt <= 1\n"
                      "> Decrypt <= 2\n"
                      "> Key <= 3\n"
                      "> Key list <= 4\n"
                      "> Position of Word <= 5\n"
                      "> Encrypt with list of Keys <= 6\n"
                      "> Decrypt with list of keys <= 7\n"
                      "> To exit <= 0\n> "))
        
        if a == 1:
            encrypt = encrypt()
            print(f'The encrypted word is {encrypt}')
        elif a == 2:
            decrypted = decrypt()
            print(f'The decrypted word is {decrypted}')
        elif a == 3:
            c = key()
            print(f'the key list is {c}')
        elif a == 4:
            c = key_list()
            print(f'the key list is {c}')
        elif a == 5:
            located = position()
            print(f"location of a word is {located}")
        elif a == 6:
            encrypted = encrypt_list()
            print(f"The encrypted word is {encrypted}")
        elif a == 7:
            decrypt = decrypt_list()
            print(f"The decrypted list is {decrypt}")
        elif a == 0:
            i = 0
        else:
            print("Enter a valid option")
    except ValueError:
        print('Invalid value [abc....] must not be used ')
