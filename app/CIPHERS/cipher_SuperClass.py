<<<<<<< HEAD
from abc import ABC, abstractmethod, abstractmethod
=======
from abc import ABC, abstractmethod
>>>>>>> 2886a555bcebdbd28ba7b77794de2cced0c09694

## THIS IS AN ABSTRACT CLASS
## MEANING THAT THIS METHOD WILL BE USED IN EVERY CIPHER SINCE WE KNOW THAT 
## WE WILL HAVE TO ENCRYPT AT LEAST A MESSAGE.

class Cipher (ABC) : 
    @abstractmethod
<<<<<<< HEAD
    def encrypt(self, key): 
=======
    def encrypt(self, string) : 
>>>>>>> 2886a555bcebdbd28ba7b77794de2cced0c09694
        pass
    
    