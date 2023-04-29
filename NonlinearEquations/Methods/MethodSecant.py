from NonlinearEquations.NonlinearEquationsSolver import NonlinearEquationsSolver
from NonlinearEquations.Equations import EQUATIONS
from NonlinearEquations.Equations import *

AMOUNT_OF_COLUMNS_SECANT = 6


class MethodSecant(NonlinearEquationsSolver):
    # Метод секущих
    def methodSecant(self, number_of_equatation: int):
        a = self.getLeftBorder()
        b = self.getRightBorder()
        eps = self.getEpsilon()
        print('\t\t\tМетод секущих')
        if checkConvergenceCondition(a, b, number_of_equatation):
            print('Достаточное условие сходимости выполянется. Вычисляем начальные приближения x0 и x1.')
            if self.calculateStart(a, number_of_equatation) > 0:
                b = a - a * 0.25
            elif self.calculateStart(b, number_of_equatation) > 0:
                a = b
                b = a + a * 0.25
        else:
            print(
                'Достаточное условие сходимости не выполнилось. На интервале или нет корней, или существует несколько.')
            return
        print(f'1. Значение x0 ={a}')
        print(f'2. Значение x1 ={b}')
        print(f'3. Точность epsilon={eps}')
        maxIterationNumber = self.calculateMaxIteration(eps)
        iterations = [[0.0 for x in range(AMOUNT_OF_COLUMNS_SECANT)]
                      for x in range(maxIterationNumber)]
        count_of_iterations = 0
        for i in range(maxIterationNumber):
            iterations[i][0] = count_of_iterations
            iterations[i][1] = a
            iterations[i][2] = b
            iterations[i][3] = b - (b - a) / (calculateFunctionValue(b, number_of_equatation) -
                                              calculateFunctionValue(a, number_of_equatation)) * calculateFunctionValue(
                b, number_of_equatation)
            iterations[i][4] = calculateFunctionValue(iterations[i][3], number_of_equatation)
            iterations[i][5] = abs(iterations[i][3] - iterations[i][2])
            count_of_iterations += 1
            if iterations[i][5] <= eps:
                break
            a, b = iterations[i][2], iterations[i][3]
        self.printTableForMethodSecant(iterations, count_of_iterations)
        return iterations[count_of_iterations - 1][3], iterations[count_of_iterations - 1][4], count_of_iterations

    def calculateStart(self, x, number_of_equation):
        return calculateFunctionValue(x, number_of_equation) \
            * calculateDerivativeSecondValue(x, number_of_equation)

    def printTableForMethodSecant(self, table, count_of_iterations):
        print('№ итерации| x(i-1) | xi | x(i+1) | f(x(i+1)) | |x(i+1) - xi| |')
        for i in range(count_of_iterations):
            print(f'  {table[i][0]}  | {table[i][1]} | {table[i][2]} | '
                  f'{table[i][3]} | {table[i][4]} | {table[i][5]} |')
