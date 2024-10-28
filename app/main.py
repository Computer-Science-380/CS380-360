import sys
import os
from typing import Self

# main.py

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.ciphers.nihilist import NihilistCipher
from app.ciphers.morse import Morse
from app.ciphers.bacon import BaconCipher
cipher = NihilistCipher("maquiav")
print(cipher.encrypt("mano"))


test = Morse("marco").encrypt()
print(test)

testbacon = BaconCipher("test").encrypt()
print(testbacon)
