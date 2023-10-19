#basic types in python - numbers , string , booleans
#complex types in python - list , tuple and dictionary
#classes
class Point:
    # sytax of constructor
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self):
        print("move")
    def draw(self):
        print("draw")

# point1=Point()
# point1.move()
# point1.draw()

point2=Point(10,20)
print(point2.x)
print(point2.y)