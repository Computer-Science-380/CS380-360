import unittest
from app.CIPHERS.bacon import BaconCipher

class TestBaconCipher(unittest.TestCase):
    
    def setup(self):
        self.bacon_cipher = BaconCipher()
        
    def test_encode_simple_message(self):
        message = "HELLO"
        expected = "aabaa aabab abaaa abaaa ababb"
        self.assertEqual(self.bacon_cipher.encode(message), expected)
        
    def test_decode_simple_message(self):
        encoded_message = "aabaa aabab abaaa abaaa ababb"
        expected = "HELLO"
        self.assertEqual(self.bacon_cipher.decode(encoded_message), expected)
        
    def test_encode_lowercase_message(self):
        message = "hello"
        expected = "aabaa aabab abaaa abaaa ababb"
        self.assertEqual(self.bacon_cipher.encode(message), expected)

    def test_decode_uppercase_message(self):
        encoded_message = "AABAA AABAB ABAAA ABAAA ABABB"
        expected = "HELLO"
        self.assertEqual(self.bacon_cipher.decode(encoded_message), expected)
        
    def test_encode_message_no_alphabet(self):
        message = "HELLO, WORLD!"
        expected = "aabbb aabaa ababa ababa abbab babab abbab baaaa ababa aaabb"
        self.assertEqual(self.bacon_cipher.encode(message), expected)
        
if __name__ == "__main__":
    unittest.main()