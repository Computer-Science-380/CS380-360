from app.CIPHERS.cipher_SuperClass import Cipher


class NihilistCipher (Cipher) : 
    def __init__(self, keyword) :
        self.keyword = keyword
        self.grid = self.create_grid()
        self.num_mapping = self.create_num_mapping ()
        
    def create_grid (self): 
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" ## DO NOT PUT I J, SINCE THEY ARE COMBINED
        
        used_chars = ""
        
        
        
    