from NonlinearEquationsValidator import NonlinearEquationsValidator


# Класс для хранения данных для вычислений
class NonlinearEquationsSolver:

    def __init__(self, epsilon, left_border=None, right_border=None, x0=None):
        self.__right_border = right_border if right_border is None else NonlinearEquationsValidator.validateNumber(
            right_border)
        self.__left_border = left_border if left_border is None else NonlinearEquationsValidator.validateNumber(
            left_border)
        if self.__right_border is not None and self.__left_border is not None:
            NonlinearEquationsValidator.validateBorders(left_border, right_border)
        self.__x0 = x0 if x0 is None else NonlinearEquationsValidator.validateNumber(x0)
        self.__epsilon = NonlinearEquationsValidator.validateEpsilon(epsilon)

    def getEpsilon(self):
        return self.__epsilon

    def getX0(self):
        return self.__x0

    def getLeftBorder(self):
        return self.__left_border

    def getRightBorder(self):
        return self.__right_border

    def calculateMaxIteration(self, eps):
        return int(100 / eps) if eps < 1 else int(100 * eps)


