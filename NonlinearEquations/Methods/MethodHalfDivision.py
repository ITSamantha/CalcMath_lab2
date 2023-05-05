from Exceptions.IncorrectValueException import IncorrectValueException
from NonlinearEquations.NonlinearEquationsSolver import NonlinearEquationsSolver
from NonlinearEquations.Equations import *
import numexpr as ne

AMOUNT_OF_COLUMNS_HALF_DIVISION = 8


class MethodHalfDivision(NonlinearEquationsSolver):
    # Метод половинного деления
    def methodHalfDivision(self, number_of_equation):
        a = self.getLeftBorder()
        b = self.getRightBorder()
        eps = self.getEpsilon()
        print('\t\t\tМетод половинного деления')
        print(f'1. Левая граница a={a}')
        print(f'2. Правая граница b={b}')
        print(f'3. Точность epsilon={eps}')
        maxIterationNumber = self.calculateMaxIteration(eps)
        iterations = [[0.0 for x in range(AMOUNT_OF_COLUMNS_HALF_DIVISION)]
                      for x in range(maxIterationNumber)]
        count_of_iterations = 0
        for i in range(maxIterationNumber):
            x = (a + b) / 2
            iterations[i][0] = i + 1
            iterations[i][1], iterations[i][2] = a, b
            iterations[i][3] = x
            iterations[i][4] = calculateFunctionValue(a, number_of_equation)
            iterations[i][5] = calculateFunctionValue(b, number_of_equation)
            iterations[i][6] = calculateFunctionValue(x, number_of_equation)
            iterations[i][7] = abs(a - b)
            if iterations[i][4] * iterations[i][6] > 0 and iterations[i][5] * iterations[i][6] > 0:
                raise IncorrectValueException('Невозможно найти корень на данном интервале. Его нет или их несколько.')
            if iterations[i][4] * iterations[i][6] > 0:
                a = x
            else:
                b = x
            count_of_iterations += 1
            if iterations[i][7] <= eps:
                break
        self.printTableForMethodHalfDivision(iterations, count_of_iterations)
        return iterations[count_of_iterations - 1][3], iterations[count_of_iterations - 1][6], count_of_iterations

    def printTableForMethodHalfDivision(self, table, count_of_iterations):
        print('№ итерации| a | b | x | f(a) | f(b) | f(x) | |a-b| |')
        for i in range(count_of_iterations):
            print(f'  {table[i][0]}  | {table[i][1]} | {table[i][2]} | '
                  f'{table[i][3]} | {table[i][4]} | {table[i][5]} | {table[i][6]} | {table[i][7]} |')
