class User:
    def __init__(self, name: str, phone: str, email: str, username: str, role: str):
        self.name = name
        self.phone = phone
        self.email = email
        self._password = None
        self.username = username
        self.role = role
        self.products = {}

    def set_password(self, password):
        if len(password) < 10 or not any(char.isupper() for char in password) or not any(char.islower() for char in password):
            raise ValueError("The password must have at least 8 characters, including one uppercase and one lowercase letter.")
        else:
            self._password = password

    def get_password(self):
        return self._password

    def vinculation(self, vinculation):
        self.vinculation = vinculation

    def add_product(self, product_name, product_price):
        self.products[product_name] = product_price

    def get_products(self):
        return self.products


class Provider(User):
    def __init__(self, name: str, phone: str, email: str, username: str, role: str, associated_brand: str):
        super().__init__(name, phone, email, username, role)
        self.associated_brand = associated_brand


class Personal(User):
    def __init__(self, name: str, phone: str, email: str, username: str, role: str, personal_position: str):
        super().__init__(name, phone, email, username, role)
        self.personal_position = personal_position


class System(User):
    def __init__(self, name: str, phone: str, email: str, username: str, role: str, vinculation: str):
        super().__init__(name, phone, email, username, role)
        self.vinculation = vinculation

    def vinculation(self, vinculation):
        if self.vinculation.lower() == "client":
            return f"Client vinculated. Welcome to the system {self.name}!\n Enjoy your searching buy."
        elif self.vinculation.lower() == "provider":
            return f"Provider vinculated. Welcome to the system {self.name}!\n You will be redirected to our provider base."
        elif self.vinculation.lower() == "personal":
            return f"Personal vinculated. Welcome to the system {self.name}!\n You will be redirected to the personal base."


class Product:
    def __init__(self, name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand=None):
        self.name = name
        self.quantity = quantity
        self.set_provider(provider, provider_id)
        self.set_description(description)
        self.set_price(price_personal, price_wholesale)
        self.brand = brand

    def __str__(self):
        return f"{self.name}: {self.quantity} units"

    def set_provider(self, provider, provider_id):
        if isinstance(provider, str) and isinstance(provider_id, int):
            self.provider = provider
            self.provider_id = provider_id
        else:
            raise TypeError("Provider must be a string and provider ID must be an integer.")

    def get_provider(self):
        return self.provider

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_price(self, personal, wholesale):
        if isinstance(personal, (int, float)) and isinstance(wholesale, (int, float)):
            self.price_personal = personal
            self.price_wholesale = wholesale
        else:
            raise TypeError("Prices must be integers or decimals.")

    def get_price_wholesale(self):
        return self.price_wholesale

    def get_price_personal(self):
        return self.price_personal


class Agenda(Product):
    def __init__(self, name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand):
        super().__init__(name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand)
        self.agenda = None  # Placeholder for agenda specific attribute


class Colors(Product):
    def __init__(self, name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand, color):
        super().__init__(name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand)
        self.color = color


class Micropoint(Product):
    def __init__(self, name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand, point_type, color):
        super().__init__(name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand)
        self.point_type = point_type
        self.color = color


class Corrector(Product):
    def __init__(self, name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand):
        super().__init__(name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand)


class Eraser(Product):
    def __init__(self, name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand):
        super().__init__(name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand)


class SewingMachine(Product):
    def __init__(self, name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand):
        super().__init__(name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand)


class Notebook(Product):
    def __init__(self, name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand, format, sheets):
        super().__init__(name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand)
        self.format = format
        self.sheets = sheets


class Pen(Product):
    def __init__(self, name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand, color):
        super().__init__(name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand)
        self.color = color


class GeometrySet(Product):
    def __init__(self, name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand):
        super().__init__(name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand)


class Pencil(Product):
    def __init__(self, name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand):
        super().__init__(name, quantity, provider, provider_id, description, price_personal, price_wholesale, brand)


class ProductSystem:
    def __init__(self):
        self.products = []
        self.users = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        for product in self.products:
            print(product)

    def search_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None


class UserRegistration:
    def __init__(self, system):
        self.system = system

    def register_user(self, name, phone, email, password, username, role):
        user = User(name, phone, email, username, role)
        self.system.users.append(user)
        print(f"\nUser {name} registered as {role}.")

    def show_users(self):
        for user in self.system.users:
            print(user.name, user.email, user.role)


def login(system):
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    # TODO: Implement login logic here. It would be great if we add the shopping cart logic here.


def register(system):
    print("Welcome to the Warehouse System.")

    user_registration = UserRegistration(system)

    while True:
        print("\nPlease choose an option:")
        print("1. Register new user")
        print("2. Login")
        print("3. Exit")
        print("4. Show users")  # This is for testing if the users are registered

        option = input("Enter your choice: ")

        if option == "1":
            name = input("Enter your name: ")
            phone = input("Enter your phone number: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            username = input("Enter your username: ")
            role = input("Enter your role (client, provider, personal): ")

            user_registration.register_user(name, phone, email, password, username, role)
            # TODO: Implement ProductSystem logic here. The user has been registered, now we can add products to the system.

        elif option == "2":
            login(system)

        elif option == "3":
            print("Exiting program. Goodbye!")
            break

        elif option == "4":
            user_registration.show_users()

        else:
            print("Invalid option. Please enter a valid choice.")

system = ProductSystem()
register(system)