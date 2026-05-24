class ATM:

    def __init__(self):
        self.counts = [0, 0, 0, 0, 0]

    def deposit(self, banknotesCount):
        for i in range(5):
            self.counts[i] += banknotesCount[i]

    def withdraw(self, amount):
        denoms = [20, 50, 100, 200, 500]
        use = [0, 0, 0, 0, 0]
        remaining = amount
        for i in range(4, -1, -1):
            take = min(self.counts[i], remaining // denoms[i])
            use[i] = take
            remaining -= take * denoms[i]
        if remaining != 0:
            return [-1]
        for i in range(5):
            self.counts[i] -= use[i]
        return use

# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)