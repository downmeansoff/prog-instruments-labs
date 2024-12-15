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
    def __init__(self, flavour="classic", size="M", toppings=["boba"], ice=100, sugar=100, dine_in=True):
        print("Initialized")
        self.flavour = flavour
        self.size = size
        self.toppings = toppings
        self.ice = ice
        self.sugar = sugar
        self.dine_in = dine_in


class BobaBuilder:
    
    def __init__(self, flavour, size, toppings, ice, sugar, dine_in):
        self.flavour = flavour
        self.size = size
        self.toppings = toppings
        self.ice = ice
        self.sugar = sugar
        self.dine_in = dine_in
    
    def set_flavour(self, flavour):
        self.flavour = flavour


    def set_size(self, size):
        self.size = size


    def set_toppings(self, toppings):
        self.toppings = toppings


    def set_ice(self, ice):
        self.ice = ice


    def set_sugar(self, sugar):
        self.sugar = sugar


    def set_dine_in(self, dine_in):
        self.dine_in = dine_in


    def build(self):
        return Boba(self.flavour, self.size, self.toppings, self.ice, self.sugar, self.dine_in)


class Director:
    
    def build_dan_ha_order(self, builder):
        builder.set_flavour("Oolong")
        builder.set_size("L")
        builder.set_toppings(["boba", "boba", "boba"])
        builder.ice = 30
        builder.sugar = 50
        builder.dine_in = False
        return builder.build()
    
    def build_worst_order(self, builder):
        builder.set_flavour("Fruit")
        builder.set_size("S")
        builder.set_toppings(["red beans"])
        builder.ice = 120
        builder.sugar = 120
        builder.dine_in = True
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
        if self.CEO is None:
            self.CEO = Company.__Company(self, data)
        return self.CEO 
    

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
    def __init__(self, helper):
        self.helper = helper
    
    def exec(self):
        self.helper.exec()


# VII. Chain of Responsibility (Chaining Method)

class Handler:
    
    def __init__(self):
        self.next_handler = None
    
    def get_next_handler(self):
        return self.next_handler
    
    def set_next_handler(self, next_handler):
        self.next_handler = next_handler
    
    def handle(self, num, cvv):
        pass
    
    def handle_next(self, num, cvv):
        if self.next_handler is None:
            return True
        return self.next_handler.handle(num, cvv)
    
class HandleNum(Handler):

    def __init__(self, data):
        self.database = data
        self.next_handler = None
   
    def handle(self, num, cvv):
        if num not in self.database.keys():
            return False
        return self.handle_next(num, cvv) 


class HandleCVV(Handler):

    def __init__(self, data):
        self.database = data
        self.next_handler = None
   
    def handle(self, num, cvv):
        if num != self.database.get(num):
            return False
        return self.handle_next(num, cvv)


class AuthService:
    def __init__(self, handler):
        self.handler = handler
    
    def authenticate(self, num, cvv):
        if self.handler.handle(num, cvv):
            return True
        return False


def credit_main():
    database = {}
    handler1 = HandleNum(database)
    handler1.set_next_handler(HandleCVV(database))
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
            self.listserv[event] = []
            self.listserv[event].append(email)
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
