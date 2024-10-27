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
        self.assertEqual(morse.encrypt(), "....|.|.-..|.-..|--- .--|---|.-.|.-..|-..")

    def test_encrypt_with_numbers(self):
        morse = Morse("HELLO 123")
        self.assertEqual(morse.encrypt(), "....|.|.-..|.-..|--- .----|..---|...--")

    def test_encrypt_with_special_characters(self):
        morse = Morse("HELLO?")
        self.assertEqual(morse.encrypt(), "....|.|.-..|.-..|---|..--..")

    def test_encrypt_with_space(self):
        morse = Morse(" ")
        self.assertEqual(morse.encrypt(), " ")

    def test_encrypt_empty(self):
        morse = Morse("")
        self.assertEqual(morse.encrypt(), "")

    def test_encrypt_unsupported_character(self):
        morse = Morse("sdf!sd")
        with self.assertRaises(ValueError) as context:
            morse.encrypt()
        self.assertEqual(str(context.exception), "Illegal argument: '!' does not exist in Morse code.")

# Run the tests
if __name__ == "__main__":
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestMorseEncryption))
