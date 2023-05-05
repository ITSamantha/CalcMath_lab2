import numpy as np
import matplotlib.pyplot as plt

from Exceptions.IncorrectValueException import IncorrectValueException
from NonlinearEquations.Methods.MethodEasyIteration import MethodEasyIteration
from NonlinearEquations.Methods.MethodHalfDivision import MethodHalfDivision
from NonlinearEquations.Methods.MethodSecant import MethodSecant
from NonlinearEquationsValidator import NonlinearEquationsValidator
from Equations import EQUATIONS

AMOUNT_OF_METHODS = 3
METHODS=['Метод половинного деления','Метод секущих', 'Метод простой итерации']


class Terminal:
    def __init__(self):
        self.__isFromFile: bool = False

    def isFile(self, mode) -> bool:
        if mode == 0:
            print("Выберите формат ввода(c клавиатуры - k или из файла - f):")
        else:
            print("Хотите записать результаты в файл?(нет - k или  да - f):")
        is_file = input()
        if is_file.__eq__('k'):
            return False
        elif is_file.__eq__('f'):
            return True
        else:
            return self.isFile(mode)

    def refresh(self):
        self.__isFromFile = False

    def work(self):
        try:
            print('\t\t\tРешение нелинейных уравнений')
            for i in range(len(EQUATIONS)):
                print(f"{i + 1}. {EQUATIONS[i + 1]['FUNCTION']}")
            equation_number = self.enterEquationNumber()
            print('\t\tМетоды решения:')
            for i in range(len(METHODS)):
                print(f'{i + 1}.{METHODS[i]}')
            method_number = self.enterEquationMethod()
            self.__isFromFile = self.isFile(0)
            if self.__isFromFile:
                a, b, epsilon = self.enterFromFile()
            else:
                a, b = self.enterBorders()
                epsilon = self.enterEpsilon()
            x = np.arange((a - 5), (b + 5), 0.01)
            if equation_number == 1:
                plt.plot(x, (x - np.sin(x) + np.cos(10 * x) + 5))
            elif equation_number == 2:
                plt.plot(x, (3 * x ** 3 - 12 * x ** 2 + 19.2))
            else:
                plt.plot(x, (x ** 5 + (x + 1) ** 4 - x))
            plt.xlabel(r'$x$')
            plt.ylabel(r'$f(x)$')
            plt.title(EQUATIONS[equation_number]['FUNCTION'])
            plt.grid(True)
            if method_number == 1:
                solver = MethodHalfDivision(epsilon, left_border=a, right_border=b)
                answer_x, fun_value, count_of_iter = solver.methodHalfDivision(equation_number)
            elif method_number == 2:
                solver = MethodSecant(epsilon, left_border=a, right_border=b)
                answer_x, fun_value, count_of_iter = solver.methodSecant(equation_number)
            else:
                solver = MethodEasyIteration(epsilon, left_border=a, right_border=b)
                answer_x, fun_value, count_of_iter = solver.methodEasyIteration(equation_number)
            answer_str = f'\tНайденный корень уравнения:{answer_x}\n' \
                         f'\tЗначение функции в корне:{fun_value}\n' \
                         f'\tЧисло итераций: {count_of_iter}'
            print(answer_str)
            self.__isFromFile = self.isFile(1)
            if self.__isFromFile:
                f = open(input('Введите путь к файлу, в который будет записан результат:'), 'w', encoding='utf-8')
                f.write(answer_str, )
                f.close()
            plt.scatter(answer_x, 0, color='red', s=40, marker='o')
        except IncorrectValueException as e:
            print(e.message)
            return
        finally:
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
            return a, b
        except IncorrectValueException as e:
            print(e.message)
            return self.enterBorders()

    def enterFromFile(self):
        try:
            f = open(input('Введите путь к файлу:'), 'r')
            parameters = f.read().split(';')
            if len(parameters) != 3:
                raise IncorrectValueException('Количество аргументов должно быть строго 3: граница a, граница b (a>b) '
                                              'и точность вычислений (через ;).')
            a = NonlinearEquationsValidator.validateNumber(parameters[0])
            b = NonlinearEquationsValidator.validateNumber(parameters[1])
            eps = NonlinearEquationsValidator.validateEpsilon(parameters[2])
            return a, b, eps
        except IncorrectValueException as e:
            print(e.message)
            return self.enterFromFile()
        except FileNotFoundError as e:
            print(e.strerror)
            return self.enterFromFile()

    def enterEpsilon(self):
        try:
            print('Введите точность epsilon:')
            eps = NonlinearEquationsValidator.validateEpsilon(input())
            if eps < 0.000001:
                print('Можете пойти сделать кофе, это будет долго...')
            return eps
        except IncorrectValueException as e:
            print(e.message)
            return self.enterEpsilon()
