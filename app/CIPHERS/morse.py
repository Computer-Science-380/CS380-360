from .cipher_SuperClass import Cipher

morseCode = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


class Morse(Cipher):
    def __init__(self,message):
        self.message=message

    def encrypt(self):
        encrypted=""
        for letter in self.message:
            if(letter!=" "):
                encrypted+=morseCode[letter.upper()]+"|"
            else:
                encrypted+=" "
        encrypted=encrypted[:-1]
        return encrypted
    
    
    

    


##while True:
##    print("Hi, this is a program for morse code")
##    message=input("Please enter the message you want to translate ")
##
##    print(f"The encrypted message is:\n{Morse(message).encrypt()}")
##
##    answer=input("Do you want to play again? (Y/N)")
##    if(answer.lower()=="n"):
##        break
##
##