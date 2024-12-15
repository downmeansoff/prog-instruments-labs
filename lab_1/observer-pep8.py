# Name: Dan-Ha Le

# Design Patterns

# I. Abstract Factory

# There are two jungles that both produce bananas, but of different kinds:

# Produce:
# - Bananas:

class Banana:
    """Class representing a banana."""
    
    def harvest(self):
        """Harvests the banana."""
        pass


class GreenBanana(Banana):
    """Class representing a green banana."""
    
    def harvest(self):
        """Harvests the green banana."""
        pass


class YellowBanana(Banana):
    """Class representing a yellow banana."""
    
    def harvest(self):
        """Harvests the yellow banana."""
        pass


# - Coconuts:

class Coconut:
    """Class representing a coconut."""
    
    def harvest(self):
        """Harvests the coconut."""
        pass


class GreenCoconut(Coconut):
    """Class representing a green coconut."""
    
    def harvest(self):
        """Harvests the green coconut."""
        pass


class YellowCoconut(Coconut):
    """Class representing a yellow coconut."""
    
    def harvest(self):
        """Harvests the yellow coconut."""
        pass


# Jungle/Factories:

class Jungle:
    """Abstract class for jungles."""
    
    def get_banana(self):
        """Returns a banana."""
        pass


    def get_coconut(self):
        """Returns a coconut."""
        pass


class JungleA(Jungle):
    """Class representing Jungle A."""
    
    def get_banana(self):
        """Returns a green banana."""
        return GreenBanana()


    def get_coconut(self):
        """Returns a green coconut."""
        return GreenCoconut()


class JungleB(Jungle):
    """Class representing Jungle B."""
    
    def get_banana(self):
        """Returns a yellow banana."""
        return YellowBanana()
    
    def get_coconut(self):
        """Returns a yellow coconut."""
        return YellowCoconut()


# II. Builder Design Pattern

# Build cups of boba:

class Boba:
    """Class representing a boba drink."""
    
    def __init__(
            self,
            flavour="classic",
            size="M",
            toppings=["boba"],
            ice=100, sugar=100,
            dine_in=True):
        """
        Initializes the boba drink.

        :param flavour: The flavour of the drink.
        :param size: The size of the drink.
        :param toppings: The toppings of the drink.
        :param ice: The amount of ice.
        :param sugar: The level of sugar.
        :param dine_in: Flag for dine-in option.
        """
        print("Initialized")
        self.flavour = flavour
        self.size = size
        self.toppings = toppings
        self.ice = ice
        self.sugar = sugar
        self.dine_in = dine_in


class BobaBuilder:
    """Builder class for boba drinks."""
    
    def __init__(self, flavour, size, toppings, ice, sugar, dine_in):
        """
        Initializes the boba builder.

        :param flavour: The flavour of the drink.
        :param size: The size of the drink.
        :param toppings: The toppings of the drink.
        :param ice: The amount of ice.
        :param sugar: The level of sugar.
        :param dine_in: Flag for dine-in option.
        """
        self.flavour = flavour
        self.size = size
        self.toppings = toppings
        self.ice = ice
        self.sugar = sugar
        self.dine_in = dine_in
    
    def set_flavour(self, flavour):
        """Sets the flavour of the drink."""
        self.flavour = flavour


    def set_size(self, size):
        """Sets the size of the drink."""
        self.size = size


    def set_toppings(self, toppings):
        """Sets the toppings of the drink."""
        self.toppings = toppings


    def set_ice(self, ice):
        """Sets the amount of ice."""
        self.ice = ice


    def set_sugar(self, sugar):
        """Sets the level of sugar."""
        self.sugar = sugar


    def set_dine_in(self, dine_in):
        """Sets the dine-in flag."""
        self.dine_in = dine_in


    def build(self):
        """Creates and returns the boba drink."""
        return Boba(
            flavour=self.flavour,
            size=self.size,
            toppings=self.toppings,
            ice=self.ice,
            sugar=self.sugar,
            dine_in=self.dine_in)


class Director:
    """Director class for building boba orders."""
    
    def build_dan_ha_order(self, builder):
        """Builds the boba order for Dan-Ha."""
        builder.set_flavour("Oolong")
        builder.set_size("L")
        builder.set_toppings(["boba", "boba", "boba"])
        builder.ice = 30
        builder.sugar = 50
        builder.dine_in = False
        return builder.build()
    
    def build_worst_order(self, builder):
        """Builds the worst boba order."""
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
    """Class representing a company."""
    
    def __init__(self):
        """Initializes the company."""
        self.ceo = None
        self.data = None
    
    def __company(self, data):
        """Private method to initialize company data."""
        self.data = data
    
    def get_ceo(self, data):
        """Returns the CEO of the company."""
        if self.ceo is None:
            self.ceo = Company.__company(self, data)
        return self.ceo 
    

# IV. Dependency Injection

class MenuItem:
    """Abstract class for menu items."""
    pass


class FriedRice(MenuItem):
    """Class representing fried rice."""
    pass


class AvocadoToast(MenuItem):
    """Class representing avocado toast."""
    pass


class Restaurant:
    """Class representing a restaurant."""
    
    def __init__(self, food):
        """
        Initializes the restaurant.

        :param food: The dishes offered in the restaurant.
        """
        self.food = food

    def prepare_food(self):
        """Prepares the food."""
        pass


# V. Delegation

class Researcher:
    """Abstract class for researchers."""
    
    def exec(self):
        """Executes research."""
        pass


class UnpaidIntern(Researcher):
    """Class representing an unpaid intern."""
    
    def exec(self):
        """Executes research for the unpaid intern."""
        print("Unpaid Intern doing research")


class AssistantProfessor(Researcher):
    """Class representing an assistant professor."""
    
    def exec(self):
        """Executes research for the assistant professor."""
        print("Assistant Professor doing research")


class Professor(Researcher):
    """Class representing a professor."""
    
    def __init__(self, helper):
        """
        Initializes the professor.

        :param helper: The professor's helper.
        """
        self.helper = helper
    
    def exec(self):
        """Executes research using the helper."""
        self.helper.exec()


# VII. Chain of Responsibility (Chaining Method)

class Handler:
    """Abstract class for handlers."""
    
    def __init__(self):
        """Initializes the handler."""
        self.next_handler = None
    
    def get_next_handler(self):
        """Returns the next handler."""
        return self.next_handler
    
    def set_next_handler(self, next_handler):
        """Sets the next handler."""
        self.next_handler = next_handler
    
    def handle(self, num, cvv):
        """Handles the request."""
        pass
    
    def handle_next(self, num, cvv):
        """Handles the next request."""
        if self.next_handler is None:
            return True
        return self.next_handler.handle(num, cvv)
    
class HandleNum(Handler):
    """Handler for card numbers."""

    def __init__(self, data):
        """
        Initializes the card number handler.

        :param data: The database of card numbers.
        """
        self.database = data
        self.next_handler = None
   
    def handle(self, num, cvv):
        """Handles the card number."""
        if num not in self.database.keys():
            return False
        return self.handle_next(num, cvv) 


class HandleCVV(Handler):
    """Handler for CVV codes."""

    def __init__(self, data):
        """
        Initializes the CVV handler.

        :param data: The database of CVV codes.
        """
        self.database = data
        self.next_handler = None
   
    def handle(self, num, cvv):
        """Handles the CVV code."""
        if cvv != self.database.get(num):
            return False
        return self.handle_next(num, cvv)


class AuthService:
    """Authentication service."""
    
    def __init__(self, handler):
        """
        Initializes the authentication service.

        :param handler: The authentication handler.
        """
        self.handler = handler
    
    def authenticate(self, num, cvv):
        """Authenticates the user by card number and CVV code."""
        if self.handler.handle(num, cvv):
            return True
        return False


def credit_main():
    """Main function for processing credit cards."""
    database = {}
    handler1 = HandleNum(database)
    handler1.set_next_handler(HandleCVV(database))
    authenticate = AuthService(handler1)
    authenticate.authenticate("number", "security code")


# VIII. Observer Design Pattern

class Cinema:
    """Class representing a cinema."""
    
    def __init__(self, noti):
        """
        Initializes the cinema.

        :param noti: The notification object.
        """
        self.noti = noti
    
    def new_movie_out(self):
        """Notifies about a new movie."""
        self.noti.notify()
    
    def get_movie(self):
        """Returns the notification object."""
        return self.noti


class Notification:
    """Class for managing notifications."""
    
    def __init__(self):
        """Initializes notifications."""
        self.listserv = {}
    
    def subscribe(self, event, email):
        """Subscribes to an event."""
        if event not in self.listserv:
            self.listserv[event] = []
            self.listserv[event].append(email)
        else:
            if email not in self.listserv[event]:
                self.listserv[event].append(email)
    
    def remove(self, event, email):
        """Removes subscription to an event."""
        if event in self.listserv.keys():
            self.listserv[event].remove(email)
    
    def notify(self, event):
        """Notifies subscribers about an event."""
        emails = self.listserv[event]
        for email in emails:
            email.update(event)


class EventListener:
    """Abstract class for event listeners."""
    
    def update(self, event):
        """Updates the listener when an event occurs."""
        pass


class BarbieListener(EventListener):
    """Listener for Barbie events."""
    
    def update(self, event):
        """Updates the listener about the Barbie event."""
        pass


class OppenheimerListener(EventListener):
    """Listener for Oppenheimer events."""
    
    def update(self, event):
        """Updates the listener about the Oppenheimer event."""
        pass
