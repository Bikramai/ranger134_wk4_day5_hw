# property: class
# income: rental income, laundry income, storage income, misc
# expenses: mortgage, tax, insurance, utilities( electric, water, sewer, garbage, gas), HOA, lawn, vacnacy, repairs, cap_ex, prop_mngt,mortgage
# cash_flow :income minus total monthly cash flow
# cash_roi: down_payment, closing_costs, repair, misc
# x1 = rental_income
# rental_income = input(“Enter Rental Income “)
# laundry_income = input(“Enter Laundry Income “)
# x2 = laundry_income
# storage_income = input(“Enter Storage Income “)
# x3 = storage_income
# misc_income = input(“Enter Misc Income “)
# x4 = misc_income
# income = (x1 + x2 + x3 + x4)
# x = income
# tax_expenses = input(“Enter Tax Income “)
# y1 = tax_expenses
# insurance_expenses = input(“Enter Insurance Expenses “)
# y2 = insurance_expenses
# utilities_expenses = input(“Enter Utility Expenses “)
# y3 = utilities_expenses
# hoa_expenses = input(“Enter HOA Expenses “)
# y4 = hoa_expenses
# lawn_expenses: input(“Enter Lawn Expenses “)
# y5 = lawn_expenses
# vacancy_expenses = input(“Enter Vacancy Expenses “)
# y6 = vacancy_expenses
# repairs_expenses = input(“Enter Repair Expenses “)
# y7 = repairs_expenses
# cap_ex_expenses = input(“Enter Capital Expenses “)
# y8 = cap_ex_expenses
# prop_mngt_expenses = input(“Enter Property Management Expenses “)
# y9 = prop_mngt_expenses
# mortgage_expenses = input(“Enter Mortgage Expenses “)
# y10 = mortgage_expenses
# expenses = (y1 + y2 + y3 + y4 + y5 + y6 + y7 + y8 + y9 + y10)
# y = expenses
# cash_flow = (x - y)
# a = cash_flow
# # income - expenses: x - y = a
# cash_down = input(“Enter Cash Down “)
# z1 = cash_down
# cash_closing = input(“Enter Cash Closing “)
# z2 = cash_closing
# cash_repair = input(“Enter Cash Repair “)
# z3 = cash_repair
# cash_misc = input(“Enter Cash Misc “)
# z4 = cash_misc
# total_investment = (z1 + z2 + z3 + z4)
# z = total_investment
# total_roi = (a * 12)/z
# b = total_roi
# create a user class and a property class
# the purpuse of the property class is to return the ROI
# the purpuse of the user class is to provide the value of each input

# # OBJECTIVE

#The premise of this assignment/program is to store multiple users who have 
# multiple properties associated with them.
# Within these properties the program needs to calculate what the ROI (return on investment is).
# In order to calculate the ROI we need the following information from the user.
# Property Expenses 
# Property Income 
# Investment (i.e. purchase price, closing costs)
# We use the above characteristics/variables to calculate ROI with this formula, ROI = (Net Profit / Total Investment) x 100



# CODE 

# So lets break down what we know above to code.
# Since we know we need to store multiple users, we might want to have a User class
# Since we know we need to store multipe properties, we might want to have a Property class


# But what would make up these classes? Lets start with User.
# The only characteristic/property we really NEED to store on our User class is the ability for a 
# user to have multiple properties
# So this we could store in our init()


# class User():

#     def __init__(self):
#         self.properties = []


# The above is really all we need but we could add more like a User's name. Are there any methods we 
# need on this user class? 
# Well we know that we need to store multiple properties for this specific user so maybe we put that 
# in our user class.


# class User():

#     def __init__(self, name):
#         self.properties = []
#         self.name = name

#     def add_properties(self):
        #this is where we could instantiate our Property objects and then add them to our list above! 
        # pass


# The above is enough to get started with the User but what about our Propert class? 
# Well we know that we need to calculate ROI for our properties, and we have a couple different values that will help us
# do that: Expenses, Income, Investment. Welp if we need these guys to calculate ROI why don't we store them to our properties?


# class Property():

#     def __init__(self):
#         self.expenses = 0
#         self.income = 0
#         self.investments = 0
#         self.roi = 0

# The above is a good start to what we might need to store on our properties to help us calculate & store our ROI.
# But how to we get there? How do we calculate our ROI. Well a couple methods might help us there or maybe just one method? That is 
# up to you. 


# class Property():

#     def __init__(self):
#         self.expenses = 0
#         self.income = 0
#         self.investments = 0
#         self.roi = 0


#     def calculate_roi(self):
        #this is where we need to gather information from our user in order to calculate our roi. We need to
        #what are expenses, income, investment is. This could either be a total # the user can give us. (i.e. what is the total annual income of your property)
        # Or we can ask them to be more specific(i.e. what type of income is this? rent/laundry/storage, and how much $ do you get from this income?)

        #then we use that information to run our calculation
        #self.roi = your_calculation

        #the above stores the roi on the class because we are using the self keyword. The only thing we need to do now
        #is display that # to the user!

        # pass 


#Well now we have a Property class that we can use to create multiple Property objects on & a User class that we can
#store properties to that User & create multiple different User objects. But how do we use all this code? Well we need a driver class or function.
#This seems like a good place to potentially store all of our users too!




# class ROI():

#     def __init__(self):
#         self.users = []
#         self.current_user = None


#Now we have a list so we can store multiple users and we can also keep track of who the current user is! But we need some
# "driver" code. This might be very similar to what we did with the Theater class. But obviously, ours does not need
# to be that complicated. 



# class ROI():

#     def __init__(self):
#         self.users = []
#         self.current_user = None



#     def run():

        #Here's where can display our options to our users of what they want to do with your program (i.e. add a user, 
        # change a user, add a property, quit etc)
        # itll look something like the below & should look familiar


        # response = input("What do you want to do?")

        # if response == 'add user':
              #well we need to instantiate our User object. And make sure if the init is taking in a paramater we
              #pass in the appropriate argument. We can also add that object to our self.user list & set the current_user
              #to THIS specific user object
            #   pass

        # elif response == 'change user':
              # if you want the user to be able to change who is "logged in" what attribute on the User object might be 
              # helpful in identifying that specific user? Once we traverse through the user list & find that specific user 
              # we can then set the current_user to that object
            #   pass

        # elif response == 'add property':
              #look at that we have a method in the User class for adding a property. How could we access that method on 
              #the current user that is "logged in"? 
            #   pass


        # elif response == 'quit':
             #we know what to do here :) 
            #  pass




class Property:
    def __init__(self):
        self.incomes = {}
        self.expenses = {}
        self.investment = []
       

    def add_income(self, income_key, income_value):
        self.incomes[income_key] = income_value

    def add_expense(self, expense_key, expense_value):
        self.expenses[expense_key] = expense_value

    def calculate_cash_flow(self):
        total_income = sum(self.incomes.values())
        total_expenses = sum(self.expenses_values())
        cash_flow = total_income - total_expenses
        return cash_flow
    
    def add_investment(self, investment_value):
        self.investment.append(investment_value)

    def calculate_roi(self, cash_flow, total_investment):
        roi = float((cash_flow * 12) / total_investment) 
        return roi

    
class User:
    def __init__(self, name):
        self.name = name
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)


def run():
    users = []

    while True:
        response= input("What would like to do? (Add User/Add Property/Calulate ROI): ").lower()

        if response == "quit":
            print("Thank you for visiting Rental House Property!")
            break
        
        elif response == "add user":
            name = input("Enter user name: ")
            user = User(name)
            users.append(user)
            print(f"User {name} added.")

        elif response == "add property":
            property_name = input("Enter property name: ")
            user_index = int(input("Enter the user index to which the property belongs: "))

            if user_index < len(users):
                property_details = Property()
                users[user_index].add_property(property_details)
                print(f"Property {property_name} added to user {users[user_index].name}")
            else:
                print("Invalid user index")

        elif response == "calculate roi":
            user_index = int(input("Enter the user index to calculate ROI: "))
            property_index = int(input("Enter the property index to calculate ROI: "))

            if user_index < len(users) and property_index < len(users[user_index].properties):
                property_object = users[user_index].properties[property_index]

                property_object.add_income("rental", 3000)
                property_object.add_income("laundry", 500)
                property_object.add_expense("repair", 500)
                property_object.add_expense("taxes", 1000)
                property_object.add_expense("insurance", 500)
                property_object.add_investment(100000)

                cash_flow = property_object.calculate_cash_flow()
                total_investment = sum(property_object.investment)
                roi = property_object.calculate_roi(cash_flow, total_investment)

                print(f"ROI for {users[user_index].name}'s property: {roi:.2f}%")
            else:
                print("Invalid user or property index.")

run()