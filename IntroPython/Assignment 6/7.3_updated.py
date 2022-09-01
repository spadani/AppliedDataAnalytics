class Account:

    def __init__(self, id=0, balance=100, annualinterestrate=0.0):
        self.id = id
        self.balance = balance
        self.annualinterestrate = annualinterestrate

    def getid(self):
        return self.id

    def setid(self, id):
        self.id = id

    def getbalance(self):
        return self.balance

    def setbalance(self, balance):
        self.balance = balance

    def getannualinterestrate(self):
        return self.annualinterestrate

    def setannualinterestrate(self, annualinterestrate):
        try:
            if annualinterestrate < 0:
                raise NegativeValue("Negative Value")
            self.annualinterestrate = annualinterestrate
        except NegativeValue:
            print("This number is negative")

    def getMonthlyInterestRate(self):
        monthlyInterestRate = (self.getannualinterestrate()/100) / 12
        return monthlyInterestRate

    def getMonthlyInterest(self):
        monthlyinterest = self.getMonthlyInterestRate() * self.getbalance()
        return monthlyinterest

    def withdraw(self, withdrawamount):
        try:
            if withdrawamount < 0:
                raise NegativeValue("Negative Value")
            newwithdrawalbalance = self.getbalance() - withdrawamount
            self.setbalance(newwithdrawalbalance)
        except NegativeValue:
            print("This number is negative")

    def deposit(self, depositamount):
        try:
            if depositamount < 0:
                raise NegativeValue("Negative Value")
            newdepositbalance = self.getbalance() + depositamount
            self.setbalance(newdepositbalance)
        except NegativeValue:
            print("This number is negative")


class NegativeValue(Exception):
    """Raised when the value is negative"""
    pass


def main():
    accounts = []
    for i in range(10):
        accounts.append(i)

    useraccount = eval(input("Please enter an account ID: "))

    while useraccount not in accounts:
        useraccount = eval(input("Please enter a valid account ID: "))

    account = Account(useraccount)

    while True:
            print(" ")
            print("Main Menu")
            print("1: check balance")
            print("2: withdraw")
            print("3: deposit")
            print("4: annual interest")
            choice = eval(input("Enter a choice: "))
            if choice == 1:
                print("The balance is " + str(format(account.getbalance(), '.2f')))

            elif choice == 2:
                amount = eval(input("Please enter withdrawal amount: "))
                account.withdraw(amount)

            elif choice == 3:
                amount = eval(input("Please enter an amount to deposit: "))
                account.deposit(amount)

            elif choice == 4:
                amount = eval(input("Set annual interest rate: "))
                account.setannualinterestrate(amount)

            elif choice == 5:
                break


main()


