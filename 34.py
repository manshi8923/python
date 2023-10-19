class Person:
    #constructor
    def __init__(self,name):
        self.name=name
    
    def talk(self):
        # print("talk"+self.name)
        print(f"talk {self.name}")

    
john=Person("manshi")
# print(john.name)
manshi=Person("maalik")
john.talk()
manshi.talk()