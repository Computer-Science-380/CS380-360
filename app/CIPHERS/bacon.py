from .cipher_SuperClass import Cipher

baconCipher = {
    "A": "aaaaa",
    "B": "aaaab",
    "C": "aaaba",
    "D": "aaabb",
    "E": "aabaa",
    "F": "aabab",
    "G": "aabba",
    "H": "aabbb",
    "I": "abaaa",
    "J": "abaaa",
    "K": "abaab",
    "L": "ababa",
    "M": "ababb",
    "N": "abbaa",
    "O": "abbab",
    "P": "abbba",
    "Q": "abbbb",
    "R": "baaaa",
    "S": "baaab",
    "T": "baaba",
    "U": "baabb",
    "V": "babaa",
    "W": "babab",
    "X": "babba",
    "Y": "babbb",
    "Z": "bbaaa",
}


class BaconCipher(Cipher):
    def __init__(self, message):
        self.message = message

    # Encode a message using the Bacon Cipher
    def encrypt(self):
        encoded_message = "".join(
            f"{baconCipher[char]} " for char in self.message.upper() if char.isalpha()
        )
        return encoded_message.strip()

    # Decode a Bacon Cipher message
    def decode(self, encoded_message):
        decoded_message = ''
        bacon_sequences = encoded_message.split()
        for sequence in bacon_sequences:
            for key, value in self.bacon_cipher.items():
                if sequence == value:
                    decoded_message += key
        return decoded_message
    
    #Scramble the Bacon Cipher
    

