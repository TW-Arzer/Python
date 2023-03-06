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

    def add(self, other):
        new_num = self.__num * other.__denom + self.__denom * other.__num
        new_denom = self.__denom * self.__num
        result = Fraction(new_num, new_denom)
        result.simplify()
        return result

    def multi(self, other):
        new_num = self.__num * other.__num
        new_denom = self.__num * other.__denom
        result = Fraction(new_num, new_denom)
        result.simplify()
        return result

    def equal(self, other):
        if Fraction(self.__num, self.__denom).value() == Fraction(other.__num, other.__denom).value():
            return True
        else:
            return False


if __name__ == "__main__":
    f1 = Fraction(4, 6)
    f2 = Fraction(8, 12)
