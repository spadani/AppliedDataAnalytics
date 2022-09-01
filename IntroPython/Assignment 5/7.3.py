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


def main():
    account1122 = Account(1122, 20000, 4.5)
    account1122.withdraw(2500)
    account1122.deposit(3000)
    print("Id:", account1122.getid(), "Balance:", account1122.getbalance(), "Monthly Interest Rate:",
          account1122.getMonthlyInterestRate(), "Monthly Interest:", account1122.getMonthlyInterest())


main()

