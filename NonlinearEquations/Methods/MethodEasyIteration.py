import numpy as np
from numpy import inf, nan
import pandas as pd
from Exceptions.IncorrectValueException import IncorrectValueException
from NonlinearEquations.NonlinearEquationsSolver import NonlinearEquationsSolver
from NonlinearEquations.Equations import *
import numexpr as ne

AMOUNT_OF_COLUMNS_EASY_ITERATIONS = 5


class MethodEasyIteration(NonlinearEquationsSolver):
    def methodEasyIteration(self, number_of_equation: int):
        a = self.getLeftBorder()
        b = self.getRightBorder()
        eps = self.getEpsilon()
        lamb = calculateLambda(a, b, number_of_equation)
        EQUATIONS[number_of_equation]['FI'] = EQUATIONS[number_of_equation]['FI'].replace('la', f'{lamb}')
        EQUATIONS[number_of_equation]['DERIVATIVE_FI'] = EQUATIONS[number_of_equation]['DERIVATIVE_FI'].replace('la',
                                                                                                                f'{lamb}')
        print('\t\t\tМетод простой итерации')
        print(f'1. Левая граница a={a}')
        print(f'2. Правая граница b={b}')
        print(f'3. Точность epsilon={eps}')
        maxIterationNumber = self.calculateMaxIteration(eps)
        iterations = [[0.0 for x in range(AMOUNT_OF_COLUMNS_EASY_ITERATIONS)]
                      for x in range(maxIterationNumber)]
        count_of_iterations = 0
        if self.checkConditionConvergence(a, b, number_of_equation):
            print('Условие сходимости выполняется.')
        else:
            print('Условие сходимости не выполняется.')
        for i in range(maxIterationNumber):
            iterations[i][0] = count_of_iterations
            iterations[i][1] = a
            iterations[i][2] = calculateFiValue(iterations[i][1], number_of_equation)
            iterations[i][3] = calculateFunctionValue(iterations[i][2], number_of_equation)
            if np.isinf(iterations[i][2]) or np.isnan(iterations[i][3]) or np.isinf(iterations[i][3]) or np.isnan(iterations[i][3]):
                raise IncorrectValueException('На данном промежутке либо несколько корней, либо нет корней.')
            iterations[i][4] = abs(iterations[i][2] - iterations[i][1])
            count_of_iterations += 1
            if iterations[i][4] <= eps:
                break
            a = iterations[i][2]
        else:
            raise IncorrectValueException('На данном промежутке либо несколько корней, либо нет корней.')
        self.printTableForMethodEasy(iterations, count_of_iterations)
        return iterations[count_of_iterations - 1][2], iterations[count_of_iterations - 1][3], count_of_iterations

    def checkConditionConvergence(self, a0, b0, number_of_equation):
        a_derivative = abs(calculateFunctionValue(a0, number_of_equation))
        b_derivative = abs(calculateFunctionValue(b0, number_of_equation))
        if a_derivative < 1 and b_derivative < 1:
            return True
        else:
            return False

    def printTableForMethodEasy(self, table, count_of_iterations):
        print('№ итерации| x(k) | x(k+1) | f(x(k+1)) | |x(k+1) - xk| |')
        for i in range(count_of_iterations):
            print(f'  {table[i][0]}  | {table[i][1]} | {table[i][2]} | '
                  f'{table[i][3]} | {table[i][4]} |')
