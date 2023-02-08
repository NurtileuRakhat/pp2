class String:
    def getString(self):
        self.str = input()
    def printString(self):   
        print(self.str.upper())

p = String()
p.getString()
p.printString()
