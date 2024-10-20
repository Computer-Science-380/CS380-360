import unittest
import caesar

class TestCaesarEncryption(unittest.TestCase):

    def test_caesar_encrypt(self):
        result = caesar.encrypt(caesar,"Hello World!",3)
        self.assertEqual(result,"khoor zruog!")
    def test_caesar_encrypt2(self):
        result = caesar.encrypt(caesar,"1Hello World!",4)
        self.assertEqual(result,"1lipps asvph!")

class TestCaesarDecryption(unittest.TestCase):
    
    def test_caesar_decrypt(self):
        result = caesar.decrypt(caesar,"khOoR zru1og!",3)
        self.assertEqual(result,"hello wor1ld!")
    def test_caesar_decrypt(self):
        result = caesar.decrypt(caesar,"lipps asvph!",4)
        self.assertEqual(result,"hello world!")
        

