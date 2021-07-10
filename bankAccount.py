class BankAccount:
    def __init__(self, amount="0", interest="1"):
        self.account_balance = amount
        self.interest_rate = interest*.01
        
        
    def check_interest(self):  #making sure my math was correct remove later
        print(f"Interest is {self.interest_rate}")
        return self
        
    def deposit(self, amount):
        self.account_balance += amount
        print(f"Adding ${amount} new balance is ${self.account_balance}")  #for verifying code operability.  remove later
        return self
    
    def withdraw(self, amount):
        nsf_fee = 5  # keeping easy to manipulate for later changes to insufficient funds amount
        if(self.account_balance>amount):
            self.account_balance -= amount
            print(f"withdrawing ${amount} new balance is ${self.account_balance}")  #for verifying code operability.  remove later
        else:
            amount_needed = (self.account_balance - amount) *-1
            print(f"You would need ${amount_needed} more dollars to make that withdrawal.")
            self.account_balance-=nsf_fee
            print(f"Due to insufficient funds you are being charged a {nsf_fee} and your new balance is {self.account_balance}")
        return self
    
    def display_account_info(self):
        print(f"Balance: {self.account_balance}")
        return self
    
    def account_balance(self):
        return self.account_balance
        
    def yield_interest(self):
        if(self.account_balance>0):
            self.account_balance+=(self.interest_rate*self.account_balance) # probably can be done cleaner
            client_account_view = round(self.account_balance, 2)  # making it pretty for printing,but leaving their money alone
            print(f"You've got interest! \nYou're new balance is\n{client_account_view}")
        return self

new_account = BankAccount(20, 1)
my_other_account = BankAccount(4500, 5)
#next two lines are my tests during coding
new_account.withdraw(30)
new_account.check_interest().deposit(2500) .deposit(2500).withdraw(500).display_account_info().yield_interest()
# next 2 lines are what the assignment asked for
new_account.deposit(200).deposit(900).deposit(100).withdraw(45).yield_interest().display_account_info()
my_other_account.deposit(1000).deposit(750).withdraw(100).withdraw(200).withdraw(800).yield_interest().display_account_info()

