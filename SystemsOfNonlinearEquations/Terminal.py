import math
from typing import List

import numpy as np
import matplotlib.pyplot as plt

from SystemsOfNonlinearEquations.Methods.MethodEasyIteration import MethodEasyIteration
from NonlinearEquationsValidator import NonlinearEquationsValidator
from Exceptions.IncorrectValueException import IncorrectValueException
from SystemsOfEquations import *

AMOUNT_OF_METHODS = 3
AMOUNT_OF_UNKNOWN = 2
INTERVAL_FOR_GRAPHIC_X = 10
INTERVAL_FOR_GRAPHIC_Y = 10
METHODS = ['Метод простой итерации']


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
            print('\t\t\tРешение ситем нелинейных уравнений')
            for i in range(len(SYSTEMS_OF_EQUATIONS)):
                print(f"{i + 1}.")
                for eq in SYSTEMS_OF_EQUATIONS[i + 1]['SYSTEM']:
                    print(f"{eq}")
            equation_number = self.enterSystemEquationNumber()
            print('\t\tМетоды решения:')
            for i in range(len(METHODS)):
                print(f'{i + 1}.{METHODS[i]}')
            method_number = self.enterSystemEquationMethod()
            self.__isFromFile = self.isFile(0)
            if self.__isFromFile:
                starts, epsilon = self.enterFromFile()
            else:
                starts = self.enterStarts()
                epsilon = self.enterEpsilon()
            x = np.arange(starts[0] - INTERVAL_FOR_GRAPHIC_X, (starts[0] + INTERVAL_FOR_GRAPHIC_X), 0.1)
            y = np.arange(starts[1] - INTERVAL_FOR_GRAPHIC_Y, (starts[1] + INTERVAL_FOR_GRAPHIC_Y), 0.1)
            X, Y = np.meshgrid(x, y)
            if equation_number == 1:
                plt.plot(x, np.sin(x - 0.6) - 1.6)
                plt.plot((np.cos(y) + 0.9) / 3, y)
            elif equation_number == 2:
                plt.plot(x, (x - 3) ** 2 - 2 * x + 1)
                plt.plot((y ** 3 + 27), y)
            elif equation_number == 3:
                plt.plot(x, 0.70 - 0.20 * x ** 2 - 0.10 * x * y)
                plt.plot(0.30 - 0.10 * x ** 2 - 0.20 * y ** 2, y)
            elif equation_number == 4:
                plt.plot(x, x * y + x * y ** 2 - 6)
                plt.plot(-x * (y) ** 3 + 9, y)
            plt.xlabel(r'$x$')
            plt.ylabel(r'$f$')
            plt.title('\n'.join(SYSTEMS_OF_EQUATIONS[equation_number]['EQUIVALENT']))
            plt.grid(True)
            if method_number == 1:
                solver = MethodEasyIteration(epsilon, starts)
                answer_x, answer_y, count_of_iter = solver.methodEasyIteration(equation_number)
            answer_str = f'\tНайденный корень x1:{answer_x}\n' \
                         f'\tНайденный корень x2:{answer_y}\n' \
                         f'\tЧисло итераций: {count_of_iter}'
            print(answer_str)
            self.__isFromFile = self.isFile(1)
            if self.__isFromFile:
                f = open(input('Введите путь к файлу, в который будет записан результат:'), 'w', encoding='utf-8')
                f.write(answer_str, )
                f.close()
            plt.scatter(answer_x, answer_y, color='blue', s=40, marker='o')
        except IncorrectValueException as e:
            print(e.message)
            return
        finally:
            plt.show()

    def enterSystemEquationNumber(self):
        try:
            print('Введите номер ситемы уравнений:')
            return NonlinearEquationsValidator.validateSystemEquationNumber()
        except IncorrectValueException as e:
            print(e.message)
            return self.enterSystemEquationNumber()

    def enterSystemEquationMethod(self):
        try:
            print('Введите номер метода:')
            return NonlinearEquationsValidator.validateSystemEquationMethod()
        except IncorrectValueException as e:
            print(e.message)
            return self.enterSystemEquationMethod()

    def enterStarts(self) -> object:
        try:
            print('Введите начальные приближения:')
            starts: list[float] = []
            for x in range(AMOUNT_OF_UNKNOWN):
                print(f'x{x + 1} = ', end='')
                starts.append(NonlinearEquationsValidator.validateNumber(input()))
            return starts
        except IncorrectValueException as e:
            print(e.message)
            return self.enterStarts()

    def enterFromFile(self):
        try:
            f = open(input('Введите путь к файлу:'), 'r')
            parameters = f.read().split(';')
            if len(parameters) != AMOUNT_OF_UNKNOWN + 1:
                raise IncorrectValueException(
                    f'Количество аргументов должно быть строго {AMOUNT_OF_UNKNOWN + 1}: начальные приближения '
                    'и точность вычислений (через ;).')
            starts = []
            for i in range(len(parameters) - 1):
                starts.append(NonlinearEquationsValidator.validateNumber(parameters[i]))
            eps = NonlinearEquationsValidator.validateEpsilon(parameters[len(parameters) - 1])
            return starts, eps
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
