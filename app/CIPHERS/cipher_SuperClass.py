from abc import ABC, abstractmehtod


class Cipher (ABC) : 
    @abstractmehtod
    def encrypt(self, plaintext: str) -> str : 
        pass