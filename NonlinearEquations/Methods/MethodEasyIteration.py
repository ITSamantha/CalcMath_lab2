from Exceptions.IncorrectValueException import IncorrectValueException
from NonlinearEquations.NonlinearEquationsSolver import NonlinearEquationsSolver
import numexpr as ne

AMOUNT_OF_COLUMNS_EASY_ITERATIONS = 5
FIRST_NONLINEAR_EQUATION_FI = 'x=sin(x)-5'
SECOND_NONLINEAR_EQUATION_FI = 'x=sqrt(3*x**3/12+19.2/12)'
THIRD_NONLINEAR_EQUATION_FI = 'x=(x+1)**3'
FIRST_NONLINEAR_EQUATION_FI_DERIVATIVE = 'cos(x)'
SECOND_NONLINEAR_EQUATION_FI_DERIVATIVE = '0.29646*x**2/(sqrt(0.15625*x**3+1))'
THIRD_NONLINEAR_EQUATION_FI_DERIVATIVE = '3*(x+1)**2'


class MethodEasyIteration(NonlinearEquationsSolver):
    def methodEasyIteration(self, equatation: str, number_of_equatation: int):
        a = self.getLeftBorder()
        b = self.getRightBorder()
        eps = self.getEpsilon()
        print('\t\t\tМетод простой итерации')
        print(f'1. Левая граница a={a}')
        print(f'2. Правая граница b={b}')
        print(f'3. Точность epsilon={eps}')
        maxIterationNumber = self.calculateMaxIteration(eps)
        iterations = [[0.0 for x in range(AMOUNT_OF_COLUMNS_EASY_ITERATIONS)]
                      for x in range(maxIterationNumber)]
        count_of_iterations = 0
        if self.checkConditionConvergence(a, b, FIRST_NONLINEAR_EQUATION_FI_DERIVATIVE):
            print('Условие сходимости выполняется.')
        else:
            print('Условие сходимости не выполняется.')
        for i in range(maxIterationNumber):
            iterations[i][0] = count_of_iterations
            iterations[i][1] = a
            iterations[i][2] = float(ne.evaluate(FIRST_NONLINEAR_EQUATION_FI.split('=')[1], local_dict={'x': a}))
            iterations[i][3] = float(ne.evaluate(equatation, local_dict={'x': iterations[i][2]}))
            iterations[i][4] = abs(iterations[i][2] - iterations[i][1])
            count_of_iterations += 1
            if iterations[i][4] <= eps:
                break
            a = iterations[i][2]
        self.printTableForMethodEasy(iterations, count_of_iterations)
        print(f'\tНайденный корень уравнения:{iterations[count_of_iterations - 1][2]}\n'
              f'\tЗначение функции в корне:{iterations[count_of_iterations - 1][3]}\n'
              f'\tЧисло итераций: {count_of_iterations}')
        return iterations[count_of_iterations - 1][2]

    def checkConditionConvergence(self, a0, b0, equatation):
        a_derivative = abs(ne.evaluate(equatation, local_dict={'x': a0}))
        b_derivative = abs(ne.evaluate(equatation, local_dict={'x': b0}))
        if a_derivative < 1 and b_derivative < 1:
            return True
        else:
            return False

    def printTableForMethodEasy(self, table, count_of_iterations):
        print('№ итерации| x(k) | x(k+1) | f(x(k+1)) | |x(k+1) - xk| |')
        for i in range(count_of_iterations):
            print(f'  {table[i][0]}  | {table[i][1]} | {table[i][2]} | '
                  f'{table[i][3]} | {table[i][4]} |')
