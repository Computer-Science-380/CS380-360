class CaesarEncrypter:
    def __init__(self, shift: int):
        self.shift = shift

    def encrypt(self, data: list[int]) -> list[int]:
        return [(x + self.shift) % 26 for x in data]

    def decrypt(self, data: list[int]) -> list[int]:
        return [(x - self.shift) % 26 for x in data]