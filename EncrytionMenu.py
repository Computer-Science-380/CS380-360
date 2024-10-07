from caesar_encrypter import CaesarEncrypter

class EncryptionMenu:
    def __init__(self):
        self.encrypter = CaesarEncrypter(shift=3)  
        
    def run(self):
        while True:
            print("Encryption Menu:")
            print("1. Encrypt a message")
            print("2. Decrypt a message")
            print("3. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.encrypt_message()
            elif choice == "2":
                self.decrypt_message()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def encrypt_message(self):
        message = input("Enter a message to encrypt: ")
        encrypted_message = self.encrypter.encrypt(self.convert_string_to_int_list(message))
        print("Encrypted message:", self.convert_int_list_to_string(encrypted_message))

    def decrypt_message(self):
        message = input("Enter a message to decrypt: ")
        decrypted_message = self.encrypter.decrypt(self.convert_string_to_int_list(message))
        print("Decrypted message:", self.convert_int_list_to_string(decrypted_message))

    def convert_string_to_int_list(self, string: str) -> list[int]:
        return [ord(c) - 97 for c in string.lower()]

    def convert_int_list_to_string(self, int_list: list[int]) -> str:
        return "".join([chr(c + 97) for c in int_list])

if __name__ == "__main__":
    menu = EncryptionMenu()
    menu.run()