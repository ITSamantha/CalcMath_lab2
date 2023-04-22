from NonlinearEquations.NonlinearEquationsSolver import NonlinearEquationsSolver
from Exceptions.IncorrectValueException import IncorrectValueException
import numexpr as ne

AMOUNT_OF_COLUMNS_SECANT = 6


class MethodSecant(NonlinearEquationsSolver):
    # Метод секущих
    def methodSecant(self, equatation: str):
        a = self.getLeftBorder()
        b = self.getRightBorder()
        eps = self.getEpsilon()
        print('\t\t\tМетод секущих')
        print(f'1. Начальное приближение x0={a}')
        print(f'2. Приближение x1={b}')
        print(f'3. Точность epsilon={eps}')
        maxIterationNumber = self.calculateMaxIteration(eps)
        iterations = [[0.0 for x in range(AMOUNT_OF_COLUMNS_SECANT)]
                      for x in range(maxIterationNumber)]
        count_of_iterations = 0
        for i in range(maxIterationNumber):
            iterations[i][0] = count_of_iterations
            iterations[i][1] = a
            iterations[i][2] = b
            iterations[i][3] = b - (b - a) / \
                               (float(ne.evaluate(equatation, local_dict={'x': b})) - float(
                                   ne.evaluate(equatation, local_dict={'x': a}))) * float(
                ne.evaluate(equatation, local_dict={'x': b}))
            iterations[i][4] = float(ne.evaluate(equatation, local_dict={'x': iterations[i][3]}))
            iterations[i][5] = abs(iterations[i][3] - iterations[i][2])
            count_of_iterations += 1
            if iterations[i][5] <= eps:
                break
            a, b = iterations[i][2], iterations[i][3]
        self.printTableForMethodSecant(iterations, count_of_iterations)
        print(f'\tНайденный корень уравнения:{iterations[count_of_iterations - 1][3]}\n'
              f'\tЗначение функции в корне:{iterations[count_of_iterations - 1][4]}\n'
              f'\tЧисло итераций: {count_of_iterations}')
        return iterations[count_of_iterations - 1][3]

    def printTableForMethodSecant(self, table, count_of_iterations):
        print('№ итерации| x(i-1) | xi | x(i+1) | f(x(i+1)) | |x(i+1) - xi| |')
        for i in range(count_of_iterations):
            print(f'  {table[i][0]}  | {table[i][1]} | {table[i][2]} | '
                  f'{table[i][3]} | {table[i][4]} | {table[i][5]} |')
