 def withdraw(self, amount):

        if amount <= self.bal:

            self.bal = self.bal - amount

            print("Withdrawn amount: " + str(amount) + "\nNew Balance: " + str(self.bal))

            return self.bal

        else:

            print("Insufficient funds")

            return self.bal
