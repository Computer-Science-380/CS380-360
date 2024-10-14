from app.CIPHERS.cipher_SuperClass import Cipher


class NihilistCipher(Cipher):
    def __init__(self, keyword):
        self.keyword = keyword
        self.grid = self.create_grid()
        self.num_mapping = self.create_num_mapping()

    def create_grid(self):
        alphabet = (
            "ABCDEFGHIKLMNOPQRSTUVWXYZ"  ## DO NOT PUT I J, SINCE THEY ARE COMBINED
        )

        used_chars = ""

        for char in self.keyword:
            if char not in used_chars and char in alphabet:
                used_chars += char

        for char in alphabet:
            if char not in used_chars:
                used_chars += char
                
        grid = [list(used_chars[i:i + 5]) for i in range(0, 25, 5)]
        return grid
    
    
    


