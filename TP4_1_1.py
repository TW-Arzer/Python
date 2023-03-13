import math


class Fraction:

    def __init__(self, num=0, denom=1):
        self.__num = int(num)
        self.__denom = int(denom)
        self.simplify()

    def __str__(self):
        return f"{self.__num}/{self.__denom}"

    def value(self):
        return float(self.__num) / float(self.__denom)

    def get_num(self):
        return self.__num

    def set_num(self, value):
        self.__num = value
        self.simplify()

    def get_denom(self):
        return self.__denom

    def set_denom(self, value):
        try:
            value = int(value)
            if value == 0:
                raise ZeroDivisionError("Le dénominateur ne peut pas être égal à zèro.")
            self.__denom = value
        except ValueError:
            print("La valeur doit être convertible en entier.")
        self.simplify()

    def simplify(self):
        gcd = math.gcd(self.__num, self.__denom)
        self.__num //= gcd
        self.__denom //= gcd

        if self.__denom < 0:
            self.__num *= -1
            self.__denom *= -1
        return self.__num, self.__denom

    def __add__(self, other):
        if isinstance(other, (int, float)):
            new_num = self.__num + (self.__denom * other)
            result = Fraction(new_num, self.__denom)
        else:
            new_num = self.__num * other.__denom + self.__denom * other.__num
            new_denom = self.__denom * other.__denom
            result = Fraction(new_num, new_denom)
        result.simplify()
        return result

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            new_num = self.__num - (self.__denom * other)
            result = Fraction(new_num, self.__denom)
        else:
            new_num = self.__num * other.__denom - self.__denom * other.__num
            new_denom = self.__denom * other.__denom
            result = Fraction(new_num, new_denom)
        result.simplify()
        return result

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_num = self.__num * other
            result = Fraction(new_num, self.__denom)
        else:
            new_num = self.__num * other.__num
            new_denom = self.__num * other.__denom
            result = Fraction(new_num, new_denom)
        result.simplify()
        return result

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            new_denom = self.__denom * other
            result = Fraction(self.__num, new_denom)
        else:
            new_num = self.__num * other.__denom
            new_denom = self.__denom * other.__num
            result = Fraction(new_num, new_denom)
        result.simplify()
        return result

    def __pow__(self, other):
        if isinstance(other, (int, float)):
            new_num = self.__num ** other
            new_denom = self.__denom ** other
            result = Fraction(new_num, new_denom)
            return result
        else:
            power = Fraction(other.__num, other.__denom).value()
            new_num = self.__num ** power
            new_denom = self.__denom ** power
            return f"{new_num}/{new_denom}"

    def __eq__(self, other):
        if isinstance(other, (float, int)):
            if Fraction(self.__num, self.__denom).value() == other:
                return True
            else:
                return False
        else:
            if Fraction(self.__num, self.__denom).value() == Fraction(other.__num, other.__denom).value():
                return True
            elif Fraction(self.__num, self.__denom).value() != Fraction(other.__num, other.__denom).value():
                return False

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            if Fraction(self.__num, self.__denom).value() < other:
                return True
            else:
                return False
        else:
            if Fraction(self.__num, self.__denom).value() < Fraction(other.__num, other.__denom).value():
                return True
            elif Fraction(self.__num, self.__denom).value() >= Fraction(other.__num, other.__denom).value():
                return False

    def __le__(self, other):
        if isinstance(other, (int, float)):
            if Fraction(self.__num, self.__denom).value() <= other:
                return True
            else:
                return False
        else:
            if Fraction(self.__num, self.__denom).value() <= Fraction(other.__num, other.__denom).value():
                return True
            elif Fraction(self.__num, self.__denom).value() > Fraction(other.__num, other.__denom).value():
                return False

    def __ne__(self, other):
        if isinstance(other, (int, float)):
            if Fraction(self.__num, self.__denom).value() != other:
                return True
            else:
                return False
        else:
            if Fraction(self.__num, self.__denom).value() != Fraction(other.__num, other.__denom).value():
                return True
            elif Fraction(self.__num, self.__denom).value() == Fraction(other.__num, other.__denom).value():
                return False

    def __ge__(self, other):
        if isinstance(other, (int, float)):
            if Fraction(self.__num, self.__denom).value() >= other:
                return True
            else:
                return False
        else:
            if Fraction(self.__num, self.__denom).value() >= Fraction(other.__num, other.__denom).value():
                return True
            elif Fraction(self.__num, self.__denom).value() < Fraction(other.__num, other.__denom).value():
                return False

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            if Fraction(self.__num, self.__denom).value() > other:
                return True
            else:
                return False
        else:
            if Fraction(self.__num, self.__denom).value() > Fraction(other.__num, other.__denom).value():
                return True
            elif Fraction(self.__num, self.__denom).value() <= Fraction(other.__num, other.__denom).value():
                return False


if __name__ == "__main__":
    f1 = Fraction(4, 6)
    f2 = Fraction(8, 12)

    print(Fraction(4, 3) + 4)
    print(Fraction(4, 3) + Fraction(5, 6))
    print(Fraction(4, 3) * Fraction(9, 8))
    print(Fraction(4, 3) * 5)


