from Exceptions.IncorrectValueException import IncorrectValueException
from NonlinearEquations.Equations import EQUATIONS
from SystemsOfNonlinearEquations.SystemsOfEquations import SYSTEMS_OF_EQUATIONS

AMOUNT_OF_METHODS_EQ = 3
AMOUNT_OF_METHODS_SYSTEM = 1


class NonlinearEquationsValidator:
    MIN_EPSILON = 0

    @staticmethod
    def validateEpsilon(epsilon: str):
        try:
            epsilon = float(epsilon)
            if epsilon >= NonlinearEquationsValidator.MIN_EPSILON:
                return epsilon
            else:
                raise IncorrectValueException(f'Точность (эпсилон) должна быть больше или равна 0.')
        except ValueError:
            raise IncorrectValueException(f'Точность (эпсилон) - число с плавающей точкой.')

    @staticmethod
    def validateNumber(number: str):
        try:
            number = float(number)
            return number
        except ValueError:
            raise IncorrectValueException(f'Необходимо ввести число.')

    @staticmethod
    def validateBorders(border_left: float, border_right: float):
        if border_left < border_right:
            return True
        else:
            raise IncorrectValueException(f'Левая граница должна быть строго меньше правой.')

    @staticmethod
    def validateEquationNumber():
        equation_number = int(NonlinearEquationsValidator.validateNumber(input()))
        if 0 < equation_number <= len(EQUATIONS):
            return equation_number
        else:
            raise IncorrectValueException('Неверное введен номер уравнения. Попробуйте еще раз.')

    @staticmethod
    def validateSystemEquationNumber():
        equation_number = int(NonlinearEquationsValidator.validateNumber(input()))
        if 0 < equation_number <= len(SYSTEMS_OF_EQUATIONS):
            return equation_number
        else:
            raise IncorrectValueException('Неверное введен номер системы уравнений. Попробуйте еще раз.')

    @staticmethod
    def validateEquationMethod():
        equation_method = int(NonlinearEquationsValidator.validateNumber(input()))
        if 0 < equation_method <= AMOUNT_OF_METHODS_EQ:
            return equation_method
        else:
            raise IncorrectValueException('Неверное введен номер метода. Попробуйте еще раз.')

    @staticmethod
    def validateSystemEquationMethod():
        equation_method = int(NonlinearEquationsValidator.validateNumber(input()))
        if 0 < equation_method <= AMOUNT_OF_METHODS_SYSTEM:
            return equation_method
        else:
            raise IncorrectValueException('Неверное введен номер метода. Попробуйте еще раз.')