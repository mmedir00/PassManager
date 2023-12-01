class saveManager:
    path = ""
    def __init__(self, path):
        self.path = path

    def append(self, data):
        with open(self.path, 'a') as file:
            file.write(data)

    def read(self):
        with open(self.path, 'r') as file:
            return file.read()

    def readLine(self, line):
        with open(self.path, 'r') as file:
            return file.readlines()[line]
    
    def getInfo(self):
        info = []
        for i in range(len(self.read().split("\n")) - 1):
            try:
               info.append(self.readLine(i).split("/"))
            except:
                pass
        return info
    
    def clear(self):
        with open(self.path, 'w') as file:
            file.write("")
    
    def getUser(self, page):
        for i in self.getInfo():
            if i[0] == page:
                return i[1]
            
    def getPass(self, page):
        for i in self.getInfo():
            if i[0] == page:
                return i[2]