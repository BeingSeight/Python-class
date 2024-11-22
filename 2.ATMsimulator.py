# ATM Simulator project
# Create a simple console based ATM Simulator system. It contains various functions which include Withdrawing amount,
# Depositing amount and changing the pin.
# Here, at first the user has to enter an existing username, when the username matches the system proceed toward the
# next procedure i.e asking pin number. When a user passes all these sign-in procedures,
# he/she can use all those features.

class ATM:
    def __init__(self,cardnumber,pin,balance):
        self.cardnumber = cardnumber
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        print(f"Your balance is {self.balance}")
        print("==============================")
        

    def withdrawl(self,amount):
        if amount > self.balance:
            print("Insufficient funds")
            print("==============================")
        else:
            self.balance -= amount  # Update the balance after withdrawal
            print("You have withdrawn amount "+str(amount)+" Your remaining balance is "+str(self.balance))
            print("==============================")

    def deposit(self,amount):
        self.balance += amount  # Update the balance after deposit
        print("You have deposited amount "+str(amount)+" Your remaining balance is "+str(self.balance))
        print("==============================")

    def change_pin(self,new_pin):
        self.pin = new_pin
        print("Your pin has been changed")
        print("==============================")


print("""░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒▒▒▒▒░░▒▒▒▒████████████████████████████████████▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒░░▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒░░▒▒▒▒██▒▒██████▒▒██████▒▒██████████▒▒▒▒██▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒
░░░░░░░░░░░░██▒▒██▒▒██▒▒▒▒██▒▒▒▒██▒▒██▒▒██▒▒▒▒██░░░░░░░░░░░░░░░░
░░▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
░░▒▒▒▒▒▒▒▒▒▒████████████████████████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
░░▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
░░░░░░░░░░░░██▒▒████████████████████▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░
▒▒▒▒▒▒░░▒▒▒▒██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒░░▒▒▒▒██▒▒██  ▒▒▒▒▒▒▒▒▒▒▒▒  ██████████████▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒░░▒▒▒▒██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████████████▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒
░░░░░░░░░░░░██▒▒██ Welcome To ATM ██▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░
░░▒▒▒▒▒▒▒▒▒▒██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
░░▒▒▒▒▒▒▒▒▒▒██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒  ██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
░░▒▒▒▒▒▒▒▒▒▒██▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
░░░░░░░░░░░░██▒▒████████████████████▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░
▒▒▒▒▒▒░░▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒░░▒▒▒▒████████████████████████████████████▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒
▒▒▒▒▒▒░░▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒
░░░░░░░░░░░░██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██░░░░░░░░░░░░░░░░
░░▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
░░▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
""")


cardnumber = int(input("Enter your card number: "))
pin = int(input("Enter your pin: "))
name = input("Enter your name: ")
user = ATM(cardnumber,pin,50000)
if cardnumber == 868806 and pin == 8888:
    print("Login Successful")
    print("==============================")
    print("Welcome "+name)
    print("==============================")
    while True:
        print("1. Check Balance")
        print("2. Withdrawl")
        print("3. Deposit")
        print("4. Change Pin")
        print("5. Exit")
        print("==============================")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            user.check_balance()
        elif choice == 2:
            amount = int(input("Enter the amount you want to withdraw: "))
            user.withdrawl(amount)
        elif choice == 3:
            amount = int(input("Enter the amount you want to deposit: "))
            user.deposit(amount)
        elif choice == 4:
            new_pin = input("Enter your new pin: ")
            user.change_pin(new_pin)
        elif choice == 5:
            print("Thank you for using our service")
else:
    print("Invalid card number or pin")


