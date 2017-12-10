
from PlayfairCipher.Cipher import *


option = str((input("What do you want to do, encrypt(E), decrypt(D) or exit(X): ").strip()).upper())
while option != 'X':
    cipher = str(input("Enter the cipher: ").strip())  # playfair example
    mycipher = Cipher(cipher)
    print(mycipher)
    if option == 'E':
        txt = str(input("Enter the message ro encrypt: ").strip()) # "Hide the gold in the tree stump"
        encrypted = mycipher.encrypt(txt)
        print("Encrypted: " + encrypted)
        if encrypted == "BMODZBXDNABEKUDMUIXMMOUVIF":
            print("Passed the test")
        else:
            print("Failed the test")
    elif option == 'D':
        txt = str(input("Enter the code to decrypt: ").strip()) # "BMODZBXDNABEKUDMUIXMMOUVIF"
        decrypted = mycipher.decrypt(txt)
        print("Decrypted: " + decrypted)
        if decrypted == "HIDETHEGOLDINTHETREESTUMP":
            print("Passed the test")
        else:
            print("Failed the test")
    option = str((input("What do you want to do, encrypt(E), decrypt(D) or exit(X): ").strip()).upper())


