from .nihilist import NihilistCipher


class CipherManager:
    def __init__(self, cipher_type, keyword):
        # Depending on the cipher type, instantiate the relevant cipher
        if cipher_type == "nihilist":
            self.cipher = NihilistCipher(keyword)
        # You can add more cipher types in the future

    def encrypt_message(self, message):
        # Use the encrypt method from the chosen cipher
        return self.cipher.encrypt(message)
