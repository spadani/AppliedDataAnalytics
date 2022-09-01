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
        self.annualinterestrate = annualinterestrate

    def getMonthlyInterestRate(self):
        monthlyInterestRate = (self.getannualinterestrate()/100) / 12
        return monthlyInterestRate

    def getMonthlyInterest(self):
        monthlyinterest = self.getMonthlyInterestRate() * self.getbalance()
        return monthlyinterest

    def withdraw(self, withdrawamount):
        newwithdrawalbalance = self.getbalance() - withdrawamount
        self.setbalance(newwithdrawalbalance)

    def deposit(self, depositamount):
        newdepositbalance = self.getbalance() + depositamount
        self.setbalance(newdepositbalance)

    def printoptions(self):
        print(" ")
        print("Main Menu")
        print("1: check balance")
        print("2: withdraw")
        print("3: deposit")
        print("4: exit")


def main():
    accounts = []
    for i in range(10):
        accounts.append(i)

    useraccount = eval(input("Please enter an account ID: "))

    while useraccount not in accounts:
        useraccount = eval(input("Please enter a valid account ID: "))

    account = Account(useraccount)
    print("Main Menu")
    print("1: check balance")
    print("2: withdraw")
    print("3: deposit")
    print("4: exit")
    while True:
        choice = eval(input("Enter a choice: "))
        if choice == 1:
            print("The balance is " + str(format(account.getbalance(), '.2f')))
            account.printoptions()

        elif choice == 2:
            amount = eval(input("Please enter withdrawal amount: "))
            account.withdraw(amount)
            account.printoptions()

        elif choice == 3:
            amount = eval(input("Please enter an amount to deposit: "))
            account.deposit(amount)
            account.printoptions()

        elif choice == 4:
            break


main()


