# Name: Dan-Ha Le

# Design Patterns

# I. Abstract Factory

# There are two jungles that both produce bananas, but of different kinds:

# PRODUCE:
# - bananas:
class Banana:
    def harvest(self):
        pass

class GreenBanana(Banana):
    def harvest(self):
        pass

class YellowBanana(Banana):
    def harvest(self):
        pass

# - coconuts:
class Coconut:
    def harvest(self):
        pass

class GreenCoconut(Coconut):
    def harvest(self):
        pass
        
class YellowCoconut(Coconut):
    def harvest(self):
        pass

# JUNGLES/FACTORIES:

class Jungle:
    def get_banana(self):
        pass
    
    def get_coconut(self):
        pass

class JungleA(Jungle):
    def get_banana(self):
        return GreenBanana()

    def get_coconut(self):
        return GreenCoconut()

class JungleB(Jungle):
    def get_banana(self):
        return YellowBanana()
    
    def get_coconut(self):
        return YellowCoconut()
    
# II. Builder Design Pattern

# Build cups of boba:

class Boba:
    def __init__(self, flavour="classic", size="M", toppings=["boba"], ice=100, sugar=100, dinein=True):
        print("Initialized")
        self.flavour = flavour
        self.size = size
        self.toppings = toppings
        self.ice = ice
        self.sugar = sugar
        self.dinein = dinein
    
class BobaBuilder:
    
    def __init__(self, flavour, size, toppings, ice, sugar, dinein):
        self.flavour = flavour
        self.size = size
        self.toppings = toppings
        self.ice = ice
        self.sugar = sugar
        self.dinein = dinein
    
    def flavour(self, flavour):
        self.flavour = flavour
    
    def size(self, size):
        self.size = size
    
    def toppings(self, toppings):
        self.toppings = toppings
    
    def ice(self, ice):
        self.ice = ice
    
    def sugar(self, sugar):
        self.sugar = sugar
    
    def dinein(self, dinein):
        self.dinein = dinein
    
    def build(self):
        return Boba(self.flavour, self.size, self.toppings, self.ice, self.sugar, self.dinein)

class Director:
    
    def build_dan_ha_order(builder):
        builder.flavour("Oolong")
        builder.size("L")
        builder.toppings(["boba", "boba", "boba"])
        builder.ice = 30
        builder.sugar = 50
        builder.dinein = False
        return builder.build()
    
    def build_worst_order(builder):
        builder.flavour("Fruit")
        builder.size("S")
        builder.toppings(["red beans"])
        builder.ice = 120
        builder.sugar = 120
        builder.dinein = True
        return builder.build()
    
# III. Singleton

# A single point of access:

class Company:
    
    CEO = None

    # but this is a public?
    def __init__(self):
        self.data = None
    
    def __Company(self, data):
        self.data = data
    
    def get_CEO(self, data):
        if CEO == None:
            CEO = Company.__Company(self, data)
        return CEO 
    

# IV. Dependency Injection

# Menu Item

# But Python is not type-sensitive, so is there a need to make an interface?

class MenuItem:
    pass

class FriedRice(MenuItem):
    pass

class AvocadoToast(MenuItem):
    pass

class Restaurant:
    def __init__(self, food):
        self.food = food

    def prepare_food(self):
        pass

# V. Delegation

class Researcher:
    def exec(self):
        pass

class UnpaidIntern(Researcher):
    def exec(self):
        print("Unpaid Intern doing research")

class AssistantProfessor(Researcher):
    def exec(self):
        print("Assistant Professor doing research")

class Professor(Researcher):
    helper = None
    
    def __init__(self, helper):
        self.helper = helper
    
    def exec(self):
        self.helper.exec()


# VII. Chain of Responsibility (Chaining Method)

class Handler:
    
    def __init__(self):
        self.next = None
    
    def get_next_handler(self):
        return self.next
    
    def set_next_handler(self, next):
        self.next = next
    
    def handle(self, num, cvv):
        pass
    
    def handle_next(self, num, cvv):
        if self.next is None:
            return True
        return next.handle(num, cvv)
    
class HandleNum(Handler):

    def __init__(self, data):
        self.database = data
        self.next = None
   
    def handle(self, num, cvv):
        if num not in self.database.keys():
            return False
        return self.handle_next(self, num, cvv) 

class HandleCVV(Handler):

    def __init__(self, data):
        self.database = data
        self.next = None
   
    def handle(self, num, cvv):
        if num != self.database.get(num):
            return False
        return self.handle_next(self, num, cvv)

class AuthService:
    def __init__(self, handler):
        self.handler = handler
    
    def authenticate(self, num, cvv):
        if self.handler.handle(num, cvv):
            return True
        return False

def CreditMain():
    database = {}
    handler1 = HandleNum(database).set_next_handler(HandleCVV(database))
    authenticate = AuthService(handler1)
    authenticate.authenticate("number", "security code")


# VIII. Observer Design Pattern

class Cinema:
    def __init__(self, noti):
        self.noti = noti
    
    def new_movie_out(self):
        self.noti.notify()
    
    def get_movie(self):
        return self.noti

class Notification:
    def __init__(self):
        self.listserv = {}
    
    def subscribe(self, event, email):
        if event not in self.listserv:
            self.listserv[event] = [].append(email)
        else:
            if email not in self.listserv[event]:
                self.listserv[event].append(email)
    
    def remove(self, event, email):
        if event in self.listserv.keys():
            self.listserv[event].remove(email)
    
    def notify(self, event):
        emails = self.listserv[event]
        for email in emails:
            email.update(event)

class EventListener:
    def update(self, event):
        pass

class BarbieListener(EventListener):
    def update(self, event):
        # Send mail about Barbie
        pass

class OppenheimerListener(EventListener):
    def update(self, event):
        # Send mail about Oppenheimer
        pass
