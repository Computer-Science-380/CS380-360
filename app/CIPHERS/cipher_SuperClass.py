from abc import ABC, abstractmethod, abstractmethod

## THIS IS AN ABSTRACT CLASS
## MEANING THAT THIS METHOD WILL BE USED IN EVERY CIPHER SINCE WE KNOW THAT 
## WE WILL HAVE TO ENCRYPT AT LEAST A MESSAGE.

class Cipher (ABC) : 
    @abstractmethod
    def encrypt(self, key): 
        pass
    
    