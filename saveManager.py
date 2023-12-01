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
        user = ""
        found = False
        counter = 0
        while not found and counter < len(self.getInfo()):
            if self.getInfo()[counter][0] == page:
                user = self.getInfo()[counter][1]
                found = True
            counter += 1
        return user
            
    def getPass(self, page):
        password = ""
        found = False
        counter = 0
        while not found and counter < len(self.getInfo()):
            if self.getInfo()[counter][0] == page:
                password = self.getInfo()[counter][1]
                found = True
            counter += 1
        return password