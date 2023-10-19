# class Dog:
#     def walk(self):
#         print("walk")
# class Cat:
#     def walk(self):
#         print("walk")

# in order to avoid repetition use parent class
class Mammal:
    def walk(self):
        print("walk")
class cat(Mammal):
    pass

class dog(Mammal):
    pass
dog1=dog()
dog1.walk()