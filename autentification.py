from saveManager import *
from cypher import *

class authentification:
    path = ""
    def __init__(self):
        self.path = "etc/autentificator"

    def check(self, password):
        unde = saveManager(self.path).read()
        cyph = cypher()
        decyph = str(cyph.decrypt(unde))
        if decyph[2:-1] in [password]:
            return True
        else:
            return False
    
    def change(self, password):
        cyph = cypher()
        encyph = cyph.encrypt(password)
        saveManager(self.path).write(encyph)
        return True