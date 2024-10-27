class BaconCipher:
    def __init__(self):
        self.bacon_cipher = {
            'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
            'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaaa',
            'K': 'abaab', 'L': 'ababa', 'M': 'ababb', 'N': 'abbaa', 'O': 'abbab',
            'P': 'abbba', 'Q': 'abbbb', 'R': 'baaaa', 'S': 'baaab', 'T': 'baaba',
            'U': 'baabb', 'V': 'babaa', 'W': 'babab', 'X': 'babba', 'Y': 'babbb', 'Z': 'bbaaa'
        }
    
    # Encode a message using the Bacon Cipher
    def encode(self, message):
        encoded_message = ''.join(
            f'{self.bacon_cipher[char]} '
            for char in message.upper()
            if char.isalpha()
        )
        return encoded_message.strip()


# # Menu for Bacon Cipher message 
# def main():
#     bacon_cipher = BaconCipher()
    
#     while True:
#         print("Choose an option:")
#         print("1. Encode a message")
#         print("2. Quit")
        
#         choice = input("Enter your choice: ")
        
#         if choice == "1":
#             message = input("Enter the message to encode: ")
#             encoded_message = bacon_cipher.encode(message)  # Change from encoded to encode
#             print(f"Encoded message: {encoded_message}")
        
#         elif choice == "2":
#             print("Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please try again.")
                
# if __name__ == "__main__":
#     main()
