class User:
    def __init__(self, name):
        self.name = name
        self.properties = []

    def add_property(self, property_obj):
        self.properties.append(property_obj)


class Property:
    def __init__(self):
        self.expenses = 0
        self.income = 0
        self.investment = 0
        self.roi = 0

    def calculate_roi(self):
        if self.investment != 0:
            self.roi = (self.income - self.expenses) / self.investment * 100


class ROI:
    def __init__(self):
        self.users = []
        self.current_user = None

    def run(self):
        while True:
            response = input(
                "What do you want to do? (add user / change user / add property / quit): ")

            if response == 'add user':
                name = input("Enter user's name: ")
                user = User(name)
                self.users.append(user)
                self.current_user = user
                print(f"User {name} added.")

            elif response == 'change user':
                name = input("Enter user's name: ")
                for user in self.users:
                    if user.name == name:
                        self.current_user = user
                        print(f"Changed to user: {name}")
                        break
                else:
                    print("User not found.")

            elif response == 'add property':
                if not self.current_user:
                    print("No user selected. Please select or add a user first.")
                    continue

                property_obj = Property()
                property_obj.expenses = float(
                    input("Enter expenses for the property: "))
                property_obj.income = float(
                    input("Enter income for the property: "))
                property_obj.investment = float(
                    input("Enter investment for the property: "))
                property_obj.calculate_roi()
                self.current_user.add_property(property_obj)
                print("Property added.")

            elif response == 'quit':
                print("Thank you for visiting Rental House Property.")
                break

            else:
                print("Invalid option. Please choose again.")


roi = ROI()
roi.run()

