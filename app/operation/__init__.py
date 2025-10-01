class Operation:

    @staticmethod
    def addition(a: float, b: float) -> float:

        return a + b 

    @staticmethod
    def subtraction(a: float, b: float) -> float:

        return a - b  

    @staticmethod
    def multiplication(a: float, b: float) -> float:

        return a * b  

    @staticmethod
    def division(a: float, b: float) -> float:

        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b  

    @staticmethod
    def power(base: float, exponent: float) -> float:

        return base ** exponent
    
    @staticmethod
    def modulus(a: float, b: float) -> float:

        return a % b
    
    @staticmethod
    def floor(a: float, b: float) -> float:

        return a // b