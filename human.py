import random

def random_sex():
    random_number = random.randint(0,1)
    if(random_number==0):
        return "man"
    else:
        return "woman"

class human:
    def __init__(self):
        self.age = 1
        self.sex = random_sex()

penny = []

for loop in range(20):
    obj = human()
    penny.append(obj)

print(obj)