from NonlinearEquationsValidator import NonlinearEquationsValidator


# Класс для хранения данных для вычислений
class NonlinearSystemEquationsSolver:

    def __init__(self, epsilon, start: []):
        self.__start = start
        self.__epsilon = epsilon

    def getEpsilon(self):
        return self.__epsilon

    def getStart(self):
        return self.__start

    def calculateMaxIteration(self, eps):
        return int(100 / eps) if eps < 1 else int(100 * eps)
