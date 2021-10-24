def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    # print when object is called
    def show(self):
        print(self.num, "/", self.den)

    #Overiding the print statment, thus allowing it to be used in the main program
    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum, newden)

        return Fraction(newnum//common,newden//common)

if __name__ == '__main__':
    f1 = Fraction(1,4)
    f2 = Fraction(1,2)
    result = f1 + f2
    print (result)