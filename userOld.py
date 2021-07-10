class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
    
    def transfer_money(self, other_user, amount):
        if(self.account_balance>amount):
            print(f"Transfering {amount} dollars from {self.name} to {other_user.name}")
            self.account_balance -= amount
            other_user.make_deposit(amount)
        else:
            print(f"{self.name} does not have enough money to complete the transaction.  Sorry")

chris = User("Chris", "cmsl4y3r@gmail.com")
misty = User("Misty", "marowe0000@gmail.com")
jiraiya = User("Jiraiya", "jmorton@gmail.com")

chris.make_deposit(200)
chris.make_deposit(400)
chris.make_deposit(700)
chris.make_withdrawal(10)
chris.display_user_balance()

misty.make_deposit(400)
misty.make_deposit(5000)
misty.make_withdrawal(10)
misty.make_withdrawal(100)
misty.display_user_balance()

jiraiya.make_deposit(99999)
jiraiya.make_withdrawal(60)
jiraiya.make_withdrawal(90)
jiraiya.make_withdrawal(600)
jiraiya.display_user_balance()

chris.transfer_money(jiraiya, 100)
chris.display_user_balance()
jiraiya.display_user_balance()
print(f"{chris.name}, Balance : {chris.account_balance} \n{misty.name}, Balance : {misty.account_balance}")

chris.transfer_money(misty, 100)
print(f"{chris.name}, Balance : {chris.account_balance} \n{misty.name}, Balance : {misty.account_balance}")

chris.make_deposit(500)
misty.make_withdrawal(150)
chris.display_user_balance()
misty.display_user_balance()
