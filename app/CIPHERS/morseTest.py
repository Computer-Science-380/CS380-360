import unittest 
from morse import Morse

class TestMorseEncryption(unittest.TestCase):

    def test_encrypt_single_letter(self):
        morse = Morse("A")
        self.assertEqual(morse.encrypt(), ".-")

    def test_encrypt_word(self):
        morse = Morse("HELLO")
        self.assertEqual(morse.encrypt(), "....|.|.-..|.-..|---")

    def test_encrypt_sentence(self):
        morse = Morse("HELLO WORLD")
        self.assertEqual(morse.encrypt(), "....|.|.-..|.-..|---  .--|---|.-.|.-..|-..")

    def test_encrypt_with_numbers(self):
        morse = Morse("HELLO 123")
        self.assertEqual(morse.encrypt(), "....|.|.-..|.-..|---  .----|..---|...--")

    def test_encrypt_with_special_characters(self):
        morse = Morse("HELLO?")
        self.assertEqual(morse.encrypt(), "....|.|.-..|.-..|---|..--..")

    def test_encrypt_with_space(self):
        morse = Morse(" ")
        self.assertEqual(morse.encrypt(), "")

# Run the tests
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMorseEncryption))
