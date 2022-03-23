class Category:
    def __init__(self, name):
        self.ledger = list()
        self.categoryName = name

    def deposit(self, amount, desc=""):
        self.ledger.append({"amount": amount, "description" : desc})

    def get_balance(self):
        return sum([i["amount"] for i in self.ledger])
    


    def check_funds(self, amount):
        return amount <= self.get_balance()
    
    def withdraw(self, amount, desc=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description" : desc})
            return True
        return False


    def transfer(self, amount : int, otherCategory):
        if self.withdraw(amount, f"Transfer to {otherCategory.categoryName}"):
            otherCategory.deposit(amount, f"Transfer from {self.categoryName}")
            return True
        return False


    def formatRecord(self, record):
        return '{:<23}{:>7.2f}\n'.format(record["description"],  round(record["amount"],2))
    def getTitle(self):
        asterix = ((30-len(self.categoryName))//2)*"*"

        return asterix + self.categoryName + asterix

    def getRepr(self):
        a = []
        a.append(self.getTitle())
        a.extend(list(map(self.formatRecord, self.ledger)))
        a.append("Total: {:.2f}".format(self.get_balance()))
        return "\n".join(a)

    def __str__(self):
        return self.getRepr();
    def __repr__(self):
        return self.getRepr()
        
        
    def getSpent(self):
        return sum([i["amount"] for i in self.ledger if i["amount"] <0])


a = Category("Food")
c = Category("clothing")

a.deposit(1000, "initial deposit")
a.deposit(-10.15, "groceries")
a.deposit(-15.89, "restaurant and more foo")
a.transfer(50, c)
print(a)

def create_spend_chart(a): 
    # unclear how to calculate the percentage between the categories or only in the category ??
    pass