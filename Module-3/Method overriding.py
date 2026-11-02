class parent:
    def role(self):
        print("I am the Boss!...")
    def test(self):
        print("I am testing")

class child(parent):
    def role(self):
        print("I am the child of the Boss!...")

obj1 =child()
obj1.role()
obj1.test()
print("---------------------------------------------------")
parent_obj = parent()
parent_obj.role()