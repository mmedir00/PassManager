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
        result = self.f.decrypt(str(cMessage).encode())
        return result

