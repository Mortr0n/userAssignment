from bankAccount import BankAccount


class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account = BankAccount(amount=0, interest=0.02) 
    
    def make_deposit(self, deposit_amount):
        self.account.deposit(deposit_amount)
        return self
    
    def make_withdrawal(self, withdrawal_amount):
        self.account.withdraw(withdrawal_amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()
        return self
    
    def transfer_money(self, other_user, transfer_amount): 
        if(self.account.account_balance>transfer_amount):  #figured it out.  had to use the bank account class 
            self.account.withdraw(transfer_amount)
            other_user.account.deposit(transfer_amount)
        else:
            print(f"{self.name} does not have enough money to complete the transaction.  Sorry")
        return self

chris = User("Chris", "cmsl4y3r@gmail.com")
misty = User("Misty", "marowe0000@gmail.com")
jiraiya = User("Jiraiya", "jmorton@gmail.com")

chris.make_deposit(200).make_deposit(400).make_deposit(7000).make_withdrawal(100).display_user_balance()

misty.make_deposit(400).make_deposit(5000).make_withdrawal(100).make_withdrawal(100).display_user_balance()

jiraiya.make_deposit(99999).make_withdrawal(60).make_withdrawal(90).make_withdrawal(600).display_user_balance()


chris.transfer_money(jiraiya, 100).display_user_balance()

jiraiya.display_user_balance()

chris.transfer_money(misty, 100)


chris.make_deposit(500).display_user_balance()
misty.make_withdrawal(150).display_user_balance()

