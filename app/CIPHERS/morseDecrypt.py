#Here is the decryption method
from cipher_SuperClass import Cipher
from morse import morseCode

class MorseDecrypt(Cipher):
    def __init__(self,encrypted):
        self.encrypted=encrypted
    def encrypt(self):
        pass
    def keyFinder(self,value):
        for key,keyValue in morseCode.items():
            if keyValue==value:
                return key  
        return None     
    def decrypter(self):
        message=self.encrypted
        decrypted=""
        size=len(message)
        word=""

        i=0
        while i<size:
            symbol=message[i]

            #Beginning of if statement
            if symbol == "|":
                key = self.keyFinder(word)
                if key is None:
                    return "Character not found"
                decrypted += key
                word = ""
            elif symbol == " ":
                if word:
                   key = self.keyFinder(word)
                   if key is None:
                     return "Character not found"
                decrypted += key
                word = ""
                decrypted += " "
            else:
                word += symbol 
            i += 1
            #end of if statement

        if word:
            key = self.keyFinder(word)
            if key is None:
                return "Character not found"
            decrypted += key

        return decrypted

"""while True:
    print("Hi, this is a program for morse code decryption")
    encrpyted=input("Please enter the encrypted message you want to translate ")

    print(f"The decrypted message is:\n{MorseDecrypt(encrpyted).decrypter()}")

    answer=input("Do you want to play again? (Y/N)")
    if(answer.lower()=="n"):
        break"""
            

          
        