class bacon_encrypter:
    def __init__(self):
        self.bacon_cipher = {
            'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa',
            'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaaa',
            'K': 'abaab', 'L': 'ababa', 'M': 'ababb', 'N': 'abbaa', 'O': 'abbab',
            'P': 'abbba', 'Q': 'abbbb', 'R': 'baaaa', 'S': 'baaab', 'T': 'baaba',
            'U': 'baabb', 'V': 'babaa', 'W': 'babab', 'X': 'babba', 'Y': 'babbb', 'Z': 'bbaaa'
        }
        self.reverse_bacon_cipher = {v: k for k, v in self.bacon_cipher.items()}    

    def encode(self, message):
        message = message.upper()
        encoded_message = ""

        for char in message:
            if char.isalpha():
                encoded_message += self.bacon_cipher[char] + " "
            else:
                encoded_message += char
        return encoded_message.strip()
        
    def decode(self, message):
        encoded_message = message.replace(" ", "")
        decoded_message = ""

        for i in range(0, len(encoded_message), 5):
            part = encoded_message[i:i+5]
            decoded_message += self.reverse_bacon_cipher[part]
        return decoded_message

cipher = bacon_encrypter()
plain_text = "HOUSE"
encoded_text = cipher.encode(plain_text)
decoded_text = cipher.decode(encoded_text)

print(f"Plain text: {plain_text}")
print(f"Encoded text: {encoded_text}")
print(f"Decoded text: {decoded_text}")