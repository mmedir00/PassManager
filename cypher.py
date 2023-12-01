from cryptography.fernet import Fernet

class cypher():
    def __init__(self):
        self.f = Fernet(self.getKey())

    def getKey(self):
        return open("clave.key","rb").read()

    def encrypt(self, oMessage):
        return self.f.encrypt(oMessage.encode())

    def decrypt(self, cMessage):
        return self.f.decrypt(str(cMessage).encode())

