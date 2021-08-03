import math
class Complex():
    def __init__(self, real, imaginary):
        self.re = real
        self.im = imaginary
    def __str__(self):
        if self.re==0 and self.im==0:
            return "0"
        if self.re==0 and self.im>0:
            return "i ".format(self.im)
        if self.re==0 and self.im<0:
            return "-i{}".format(-self.im)
        if self.im<0:
            return "{}-i{}".format(self.re, -self.im)
        if self.im>0:
            return "{}+i{}".format(self.re, self.im)
        return str(self.re)
    def length(self):
        return math.sqrt(self.re*self.re+self.im*self.im)
    def arg(self):
        if self.re == 0 and self.im == 0:
            raise ValueError
        if self.re > 0:
            return math.atan(self.im/self.re)
        if self.re < 0 and self.im >= 0:
            return math.atan(self.im/self.re) + math.pi
        if self.re < 0 and self.im < 0:
            return math.atan(self.im/self.re) - math.pi
        if self.re == 0 and self.im > 0:
            return math.pi/2
        if self.re == 0 and self.im < 0:
            return -math.pi/2
    def conjugate(self):
        return Complex(self.re,-self.im)
    def __add__(self,other):
        return Complex(self.re+other.re, self.im+other.im)
    def __sub__(self,other):
        return Complex(self.re-other.re, self.im-other.im)
    def __mul__(self,other):
        return Complex(self.re*other.re-self.im*other.im, self.re*other.im+self.im*other.re)
    def __truediv__(self,other):
        frac = other.re**2+other.im**2
        return Complex((self.re*other.re+self.im*other.im)/frac, (self.im*other.re-self.re*other.im)/frac)
    def __eq__(self,other):
        if isinstance(other, Complex):
            return self.re==other.re and self.im==other.im
        if isinstance(other, float) or isinstance(other,int):
            return self.re==other and self.im == 0
        return NotImplemented
    def __ne__(self,other):
        if isinstance(other, Complex):
            return self.re!=other.re and self.im!=other.im
        if isinstance(other, float) or isinstance(other,int):
            return self.re!=other and self.im != 0
        return NotImplemented

if __name__ == "__main__":
    a = Complex(2,3)
    b = Complex(3,-5)
    print(a==b, a!=b)
    print(a==Complex(2,3), a!=Complex(2,3))
    a+=b
    print(a)
    print(a+b,a-b,a*b,a/b)
    a /= b
    print(a)




