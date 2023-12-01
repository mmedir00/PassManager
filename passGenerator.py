import random

class passGenerator:
    abc = "abcdefghijklmnopqrstuvwxyz" # 26
    ABC = abc.upper() # 26 
    num = "1234567890" # 10
    esp = "!@#$%^&*()_+" # 12

    def __init__(self):
        pass

    def generate(num):
        password = ""
        for i in range(num):
            a = random.randint(0, 3)
            if a == 0:
                password += random.choice(passGenerator.abc)
            if a == 1:
                password += random.choice(passGenerator.ABC)
            if a == 2:
                password += random.choice(passGenerator.num)
            if a == 3:
                password += random.choice(passGenerator.esp)
        return password