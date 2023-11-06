import app
import math

class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def substract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not app.util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')

        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")

        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")
    
    
    def raizCuadrada(x):
        if x < 0:
            return "No se puede calcular la raíz cuadrada de un número negativo."
        else:
        return math.sqrt(x)

    def logBase10(x):
        if x <= 0:
            return "El número debe ser mayor que 0 para calcular su logaritmo en base 10."
        else:
        return math.log10(x)

    def seno(x):
        return math.sin(x)

    def tangente(x):
        return math.tan(x)

    def coseno(x):
        return math.cos(x)


if __name__ == "__main__":  # pragma: no cover
    calc = Calculator()
    result = calc.add(2, 2)
    print(result)
