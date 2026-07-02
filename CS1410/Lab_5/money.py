"""
Complete Lab 5 and update the following information:

Author: Kollin DeWitt
Date: 7/2/2026
"""
class Money:
    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents
        self.normalize()

    def normalize(self):
        if self.cents >= 100:
            self.dollars += self.cents // 100
            self.cents = self.cents % 100

    def __str__(self):
        return f"${self.dollars}.{self.cents:02d}"
    
    def __add__(self, other):
        return Money(self.dollars + other.dollars, self.cents + other.cents)
    
    def __mul__(self, other):
        return Money(self.dollars * other, self.cents * other)
    
    def __rmul__(self, other):
        return Money(self.dollars * other, self.cents * other)
    
    def __eq__(self, other):
        return self.dollars == other.dollars and self.cents == other.cents

def main():
    m1 = Money(3, 50)
    m2 = Money(2, 75)

    print("m1:", m1)
    print("m2:", m2)

    m3 = m1 + m2
    print("m3:", m3)

    m4 = m1 * 2
    m5 = 3 * m2
    print("m4:", m4)
    print("m5:", m5)

    print(m1 == Money(2, 150))
    print(m1 == Money(3, 49))

if __name__ == "__main__":
    main()