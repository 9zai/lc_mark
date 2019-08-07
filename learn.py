#http://c.biancheng.net/view/2295.html
import types
class Person:
    pass

def walk(self):
    print("some one is walking")

a = Person()
Person.walk = walk
a.walk()