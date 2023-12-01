from cryptography.fernet import Fernet

class cypher():
    def __init__(self):
        self.f = Fernet(self.getKey())

    def getKey(self):
        key = open("etc/key.key","rb").read()
        return key

    def encrypt(self, oMessage):
        result = self.f.encrypt(oMessage.encode())
        return result

    def decrypt(self, cMessage):
        encoded = cMessage.encode()
        result = self.f.decrypt(encoded)
        return result

