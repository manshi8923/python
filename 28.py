class Person:
    def __init__(self,name):
        self.name=name
    def talk(self):
        print("talk")
        print(f"Hey nice to talk to you {self.name}")
p=Person("manshi")
print(p.name)
p.talk()