class BankAccount:
    def __init__(self, name, initialBalance):
        self._balance = initialBalance or 0
        self.name = name
        
    def getBalance(self):
        return self._balance
    
    def deposit(self, newAmount):
        if newAmount > 0:
            self._balance += newAmount
            print('Amount added successfully')
        else:
            print('Please add a valid amount')

    def withdraw(self, withdrawAmount):
        if withdrawAmount <= 0:
            print("Invalid withdraw amount")
            return

        newBalance = self._balance - withdrawAmount
        if newBalance >= 0:
            self._balance = newBalance
            print('Amount withdrawn successfully')
        else:
            print('Insufficient balance')


class SavingAccount(BankAccount):
    def __init__(self, name, initialBalance):
        super().__init__(name, initialBalance)
        self.minimumBalance = 2000

    def withdraw(self, withdrawAmount):
        newBalance = self._balance - withdrawAmount
        if newBalance < self.minimumBalance:
            print("Can't proceed, minimum balance required")
        else:
            self._balance = newBalance
            print("Withdraw successful")


class CurrentAccount(BankAccount):
    def __init__(self, name, initialBalance):
        super().__init__(name, initialBalance)
        self.overdraftLimit = -2000

    def withdraw(self, withdrawAmount):
        newBalance = self._balance - withdrawAmount
        if newBalance < self.overdraftLimit:
            print("Can't proceed, overdraft limit exceeded")
        else:
            self._balance = newBalance
            print("Withdraw successful")


accountInstance = None  # ✅ IMPORTANT

while True:
    print("\n1. Create account\n2. Deposit\n3. Withdraw\n4. Show balance\n5. Exit\n")
    option = input("Please choose option number: ")
    print('mainnn', __name__)
    match option:
        case '1':
            name = input("Please enter name: ")
            initialAmount = int(input("Please enter initial amount: "))
            accType = input("Please enter account type (saving/current): ").lower()

            if accType == 'saving':
                accountInstance = SavingAccount(name, initialAmount)
            elif accType == 'current':
                accountInstance = CurrentAccount(name, initialAmount)
            else:
                print("Invalid account type")
                continue

            print('Account Created')

        case '2':
            if not accountInstance:
                print("Please create an account first")
                continue
            newAmount = int(input("Please enter amount to add: "))
            accountInstance.deposit(newAmount)

        case '3':
            if not accountInstance:
                print("Please create an account first")
                continue
            newAmount = int(input("Please enter amount to withdraw: "))
            accountInstance.withdraw(newAmount)

        case '4':
            if not accountInstance:
                print("Please create an account first")
                continue
            print("Current Balance:", accountInstance.getBalance())

        case '5':
            break
