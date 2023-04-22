import numpy as np
import matplotlib.pyplot as plt

from Exceptions.IncorrectValueException import IncorrectValueException
from NonlinearEquations.Methods.MethodEasyIteration import MethodEasyIteration
from NonlinearEquations.Methods.MethodHalfDivision import MethodHalfDivision
from NonlinearEquations.Methods.MethodSecant import MethodSecant
from NonlinearEquations.NonlinearEquationsValidator import NonlinearEquationsValidator
from NonlinearEquationsSolver import NonlinearEquationsSolver

FIRST_NONLINEAR_EQUATION = 'x-sin(x)+5=0'
SECOND_NONLINEAR_EQUATION = '3*x**3-12*x**2+19.2=0'
THIRD_NONLINEAR_EQUATION = '(x+1)**3-x=0'

AMOUNT_OF_METHODS = 3


class Terminal:

    def work(self):
        try:
            print('\t\t\tРешение нелинейных уравнений')
            print(f'1. {FIRST_NONLINEAR_EQUATION}')
            print(f'2. {SECOND_NONLINEAR_EQUATION}')
            print(f'3. {THIRD_NONLINEAR_EQUATION}')
            equation_number = self.enterEquationNumber()
            equation = FIRST_NONLINEAR_EQUATION.split('=')[0] \
                if equation_number == 1 else (SECOND_NONLINEAR_EQUATION.split('=')[0]
                                              if equation_number == 2 else THIRD_NONLINEAR_EQUATION.split('=')[0])
            print('\t\tМетоды решения:')
            print('1.Метод половинного деления\n2.Метод секущих\n3.Метод простой итерации')
            method_number = self.enterEquationMethod()
            a, b = self.enterBorders()
            epsilon = self.enterEpsilon()
            if method_number == 1:
                solver = MethodHalfDivision(epsilon, left_border=a, right_border=b)
                answer_x = solver.methodHalfDivision(equation)
            elif method_number == 2:
                solver = MethodSecant(epsilon, left_border=a, right_border=b)
                answer_x = solver.methodSecant(equation)
            else:
                solver = MethodEasyIteration(epsilon, left_border=a, right_border=b)
                answer_x = solver.methodEasyIteration(equation, equation_number)
        except IncorrectValueException as e:
            print(e.message)
            return

        x = np.arange(-10, 10.01, 0.01)
        plt.plot(x, 3 * x ** 3 - 12 * x ** 2 + 19.2)
        plt.xlabel(r'$x$')
        plt.ylabel(r'$f(x)$')
        plt.title('f(x)')
        plt.grid(True)
        plt.scatter(answer_x, 0, color='red', s=40, marker='o')
        plt.show()


def enterEquationNumber(self):
    try:
        print('Введите номер уравнения:')
        return NonlinearEquationsValidator.validateEquationNumber()
    except IncorrectValueException as e:
        print(e.message)
        return self.enterEquationNumber()


def enterEquationMethod(self):
    try:
        print('Введите номер метода:')
        return NonlinearEquationsValidator.validateEquationMethod()
    except IncorrectValueException as e:
        print(e.message)
        return self.enterEquationMethod()


def enterBorders(self):
    try:
        print('Введите границы интервала a и b:')
        print('a = ', end='')
        a = NonlinearEquationsValidator.validateNumber(input())
        print('b = ', end='')
        b = NonlinearEquationsValidator.validateNumber(input())
        NonlinearEquationsValidator.validateBorders(a, b)
        return a, b
    except IncorrectValueException as e:
        print(e.message)
        return self.enterBorders()


def enterEpsilon(self):
    try:
        print('Введите точность epsilon:')
        eps = NonlinearEquationsValidator.validateEpsilon(input())
        return eps
    except IncorrectValueException as e:
        print(e.message)
        return self.enterEpsilon()
