import sys
import os

# main.py

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.CIPHERS.nihilist import NihilistCipher

cipher = NihilistCipher('maquiav')
print(cipher.encrypt('mano'))
