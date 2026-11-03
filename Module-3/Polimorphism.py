# Polymorphism
class Role:
    def act(self):
        pass

class Cook(Role):
    def act(self):
        print("Cooking Delicious Food...")

class Doctor(Role):
    def act(self):
        print("Treating Patients.............")

def daily_roles(role):
    role.act()

daily_roles(Cook())
daily_roles(Doctor())