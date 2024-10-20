from cipher_SuperClass import Cipher

class caesar(Cipher):
    
    def encrypt(self, userInput, key: int):
        codeTxt: str = ""
        plainTxt = [char for char in userInput.lower()]
        
        #print(plainTxt)

        #Loop through elements of plainTxt
        pIndex = 0
        for element in plainTxt[0:len(plainTxt):1]:
            
            #Loop through alphabet to get letter index int
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            aIndex = 0

            for letter in alphabet[0:len(alphabet):1]:
                if element == letter:
                    #change char in plainTxt
                    codeTxt += alphabet[aIndex+key]
                    break
                    

                aIndex += 1
                if aIndex > len(alphabet):
                    aIndex = 0
                    codeTxt += plainTxt[pIndex]

            #print(plainTxt[pIndex])
            #print(codeTxt)

        pIndex += 1
        if pIndex > len(plainTxt):
            pIndex = 0

        return codeTxt



#Manual Test Caesar Cipher  
print()
print()
print(caesar.encrypt(caesar,"Hello World!", 3))