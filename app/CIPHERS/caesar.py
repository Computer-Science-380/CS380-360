from cipher_SuperClass import Cipher

class caesar(Cipher):
    
    def encrypt(self, plainTxt, key: int):
        codeTxt = ""

        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for plainChar in plainTxt:
            #print(codeChar)

            isLetter = False
            for i, item in enumerate(alphabet):
                if plainChar == alphabet[i]:
                    codeTxt += alphabet[i+key]
                    isLetter = True

            if isLetter == False:
                codeTxt += plainChar

        return (codeTxt)
    

    def decrypt(self, codeTxt, key):
        plainTxt = ""

        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for codeChar in codeTxt:
            #print(codeChar)

            isLetter = False
            for i, item in enumerate(alphabet):
                if codeChar == alphabet[i]:
                    plainTxt += alphabet[i-key]
                    isLetter = True

            if isLetter == False:
                plainTxt += codeChar

        return (plainTxt)
    

    def bruteDecrypt(self, userInput):
        plainTxt = userInput.lower()
        wordBank = open("")
        print(wordBank.read())

        return userInput



#Manual Test Caesar Cipher  
"""
print()
print()
print(caesar.encrypt(caesar,"Hello World!", 3))
print(caesar.decrypt(caesar, "Khoor Zruog!", 3))
"""
caesar.bruteDecrypt(caesar,"")