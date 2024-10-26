import unittest
from morseDecrypt import MorseDecrypt 

class TestMorseDecryption(unittest.TestCase):

    def test_decrypt_basic_sentence(self):
        encrypted = "....|.|.-..|.-..|--- .--|---|.-.|.-..|-.."
        expected_output = "HELLO WORLD"
        self.assertEqual(MorseDecrypt(encrypted).decrypter(), expected_output)

    def test_decrypt_single_word(self):
        encrypted = "....|.|.-..|.-..|---"
        expected_output = "HELLO"
        self.assertEqual(MorseDecrypt(encrypted).decrypter(), expected_output)

    def test_decrypt_with_invalid_character(self):
        encrypted = "....|.|.-..|.-..|--- .--|---|.-.|-..|..--"
        expected_output = "Character not found"
        self.assertEqual(MorseDecrypt(encrypted).decrypter(), expected_output)

    def test_decrypt_space_between_words(self):
        encrypted = "....|.|.-..|.-..|---  .--|---|.-.|.-..|-.."
        expected_output = "HELLO WORLD"
        self.assertEqual(MorseDecrypt(encrypted).decrypter(), expected_output)

    def test_decrypt_empty_input(self):
        encrypted = ""
        expected_output = ""
        self.assertEqual(MorseDecrypt(encrypted).decrypter(), expected_output)

    def test_decrypt_trailing_symbol(self):
        encrypted = "....|.|.-..|.-..|--- .--|---|.-.|.-..|-..|"
        expected_output = "HELLO WORLD"
        self.assertEqual(MorseDecrypt(encrypted).decrypter(), expected_output)

    def test_decrypt_continuous_characters_without_spaces(self):
        encrypted = "....|.|.-..|.-..|---"
        expected_output = "HELLO"
        self.assertEqual(MorseDecrypt(encrypted).decrypter(), expected_output)

    def test_decrypt_only_spaces(self):
        encrypted = "   "
        expected_output = ""
        self.assertEqual(MorseDecrypt(encrypted).decrypter(), expected_output)


if __name__ == '__main__':
    unittest.main()
