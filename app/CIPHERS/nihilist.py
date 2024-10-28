from .cipher_SuperClass import Cipher


class NihilistCipher(Cipher):
    def __init__(self, keyword):
        self.keyword = self.prepare_keyword(keyword)  # Ensure keyword is valid
        self.grid = self.create_grid()
        self.num_mapping = self.create_num_mapping()

    def prepare_keyword(self, keyword):
        # Remove non-alphabet characters and replace J with I
        prepared_keyword = keyword.upper().replace("J", "I")
        prepared_keyword = "".join(
            filter(lambda x: x in "ABCDEFGHIKLMNOPQRSTUVWXYZ", prepared_keyword)
        )

        if not prepared_keyword:
            raise ValueError(
                "Keyword must contain valid letters from A-Z (excluding J)."
            )

        return prepared_keyword

    def create_grid(self):
        alphabet = (
            "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # Polybius alphabet (J is combined with I)
        )
        used_chars = ""

        # Add characters from the keyword first
        for char in self.keyword:
            if char not in used_chars and char in alphabet:
                used_chars += char

        # Add remaining alphabet characters to fill the grid
        for char in alphabet:
            if char not in used_chars:
                used_chars += char

        grid = [list(used_chars[i : i + 5]) for i in range(0, 25, 5)]
        return grid

    def create_num_mapping(self):
        # Create a dictionary that maps each letter to its grid position
        num_mapping = {}
        for i, row in enumerate(self.grid):
            for j, char in enumerate(row):
                num_mapping[char] = (
                    f"{i + 1}{j + 1}"  # Position as a two-digit string (row, column)
                )
        return num_mapping

    def encrypt(self, message):
        # Prepare the message (remove non-alphabet characters, handle J as I)
        message = message.upper().replace("J", "I")
        message = "".join(filter(str.isalpha, message))

        ## print(f"Prepared message: {message}")  # Debugging output

        # Step 1: Get numerical equivalents of the message using Polybius square
        message_nums = [self.num_mapping[char] for char in message]
        ##print(f"Message numbers: {message_nums}")  # Debugging output

        # Step 2: Generate numerical equivalents for the keyword (repeated)
        keyword_nums = [self.num_mapping[char] for char in self.keyword]
        keyword_nums = (keyword_nums * (len(message_nums) // len(keyword_nums) + 1))[
            : len(message_nums)
        ]
        ##print(f"Keyword numbers: {keyword_nums}")  # Debugging output

        # Step 3: Add the keyword values to the message values (nihilist encryption)
        encrypted_nums = [
            str(int(message_nums[i]) + int(keyword_nums[i]))
            for i in range(len(message_nums))
        ]

        ##print(f"Encrypted numbers: {encrypted_nums}")  # Debugging output

        # Return encrypted message as a string of numbers
        return " ".join(encrypted_nums)
