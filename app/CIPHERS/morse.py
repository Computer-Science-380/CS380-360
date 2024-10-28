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
    def __init__(self, message):
        self.message = message

    def encrypt(self):
        if self.message == "" or self.message==" ":
            return self.message
        
        encrypted = ""
        ##for letter in enumerate(self.message):
        for letter in self.message:
            if letter == " ":
                # Replace last character (if it's "|") with a space
                if encrypted.endswith("|"):
                    encrypted = encrypted[:-1] + " "
            else:
                # Check if character is in morseCode, otherwise raise error
                if letter.upper() not in morseCode:
                    raise ValueError(f"Illegal argument: '{letter}' does not exist in Morse code.")
                encrypted += morseCode[letter.upper()] + "|"
        
        # Remove trailing "|" if it exists
        if encrypted.endswith("|"):
            encrypted = encrypted[:-1]
        
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
