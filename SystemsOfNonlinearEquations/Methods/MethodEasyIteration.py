from Exceptions.IncorrectValueException import IncorrectValueException
from SystemsOfNonlinearEquations.NonlinearSystemEquationsSolver import NonlinearSystemEquationsSolver
import numpy as np
from SystemsOfNonlinearEquations.SystemsOfEquations import *

AMOUNT_OF_COLUMNS_EASY_ITERATIONS = 5


class MethodEasyIteration(NonlinearSystemEquationsSolver):

    def methodEasyIteration(self, number_of_system):
        starts = self.getStart()
        eps = self.getEpsilon()
        print('\t\t\tМетод простой итерации для систем нелинейных уравнений')
        for i in range(len(starts)):
            print(f'Начальное приближение x{i + 1} = {starts[i]}')
        print(f'3. Точность epsilon={eps}')
        maxIterationNumber = self.calculateMaxIteration(eps)
        iterations = [[0.0 for x in range(AMOUNT_OF_COLUMNS_EASY_ITERATIONS)]
                      for x in range(maxIterationNumber)]
        count_of_iterations = 0
        if not self.checkConditionConvergence(starts, number_of_system):
            return
        for i in range(maxIterationNumber):
            iterations[i][0] = count_of_iterations
            iterations[i][1] = calculateEquivalent(number_of_system, 1, starts[0], starts[1])
            iterations[i][2] = calculateEquivalent(number_of_system, 0, starts[0], starts[1])
            iterations[i][3] = abs(iterations[i][1] - starts[0])
            iterations[i][4] = abs(iterations[i][2] - starts[1])
            count_of_iterations += 1
            if max(iterations[i][3], iterations[i][4]) <= eps:
                break
            starts = iterations[i][1], iterations[i][2]
        else:
            raise IncorrectValueException('На данном промежутке либо несколько корней, либо нет корней.')
        self.printTableForMethodEasy(iterations, count_of_iterations)
        return iterations[count_of_iterations - 1][1], iterations[count_of_iterations - 1][2], count_of_iterations

    def checkConditionConvergence(self, starts, number_of_system):
        yak_1 = calculateYacobian(number_of_system, 0, 0, starts[0], starts[1])
        yak_2 = calculateYacobian(number_of_system, 0, 1, starts[0], starts[1])
        yak_3 = calculateYacobian(number_of_system, 1, 0, starts[0], starts[1])
        yak_4 = calculateYacobian(number_of_system, 1, 1, starts[0], starts[1])
        J = np.array([[yak_1, yak_2],
                      [yak_3, yak_4]])

        # Вычисляем собственные значения матрицы Якоби
        eigvals = np.linalg.eigvals(J)

        # Вычисляем спектральный радиус матрицы
        rho = np.max(np.abs(eigvals))

        # Проверяем условие сходимости.
        if rho < 1:
            print(f"Метод сойдется, так как спектральный радиус матрицы якобиана равен {rho}<1.")
            return True
        else:
            print(f"Метод не сойдется, так как спектральный радиус матрицы якобиана равен {rho}>1.")
            return False

    def printTableForMethodEasy(iterations, table, count_of_iterations):
        print('№ итерации| x1 | x2 | |x1(i)-x1(i-1)| | |x2(i)-x2(i-1)| |')
        for i in range(count_of_iterations):
            print(f'  {table[i][0]}  | {table[i][1]} | {table[i][2]} | '
                  f'{table[i][3]} | {table[i][4]} |')
