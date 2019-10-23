class account:

    def __init__(self):
        self.balance = 0
        self.transaction_list=[]
    
    def deposit(self, request):
        self.balance += request
        self.transaction_list.append(f"You deposited ${request}")
        return self.balance
    
    def withdrawl(self, request):
        if request >= self.balance:
            print("Insufficient funds! Unfortunately you do not have funds to complete the transaction!")
            return self.balance
        else:
            self.balance -= request
            self.transaction_list.append(f"You withdrew ${request}")
            return self.balance

    def check_balance(self):
        self.balance
        return self.balance

    def print_tranactions(self):
        return(self.transaction_list)
 
def main():

    bank_account = account()
    while True:

        action = input("Hello, how can I help you today? What would you like to do?.........(d=deposit, w=withdraw, c=check balance, h=history)").lower()    

        if action == "d":
            request = int(input("How much would you like to deposit?......"))
            print(f"The total in your account is ${bank_account.deposit(request)}!")

        if action == "w":
            request = int(input("How much would you like to withdrawl?........."))
    
            if bank_account.withdrawl(request) != "insufficient funds!":
                
                print(f'${bank_account.check_balance()}')

        if action == "c":
            print(f"The total is your account is ${bank_account.check_balance()}!")

        if action == "h":
            print(bank_account.print_tranactions())

main ()
