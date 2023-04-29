import numexpr as ne
import numpy as np

EQUATIONS = {
    1:
        {
            'FUNCTION': 'x-sin(x)+cos(10*x)+5=0',
            'DERIVATIVE_FIRST': '1-cos(x)-10*sin(10*x)',
            'DERIVATIVE_SECOND': 'sin(x)-100*cos(10*x)',
            'FI': 'fi=la*(x-sin(x)+cos(10*x)+5)+x',
            'DERIVATIVE_FI': 'la(1-*cos(x)-10*sin(10*x))+1)'
        },
    2:
        {
            'FUNCTION': '3*x**3-12*x**2+19.2=0',
            'DERIVATIVE_FIRST': '9*x**2-24*x',
            'DERIVATIVE_SECOND': '18*x-24',
            'FI': 'fi=la*(3*x**3-12*x**2+19.2)+x',
            'DERIVATIVE_FI': 'la*(6*x**2-24*x)+1'
        },
    3: {
        'FUNCTION': 'x**5+(x+1)**4-x=0',
        'DERIVATIVE_FIRST': '5*x**4+4*(x+1)**3-1',
        'DERIVATIVE_SECOND': '20*x**3+12*(x+1)**2',
        'FI': 'fi=la*(x**5+(x+1)**4-x)+x',
        'DERIVATIVE_FI': 'la*(5*x**4+4*(x+1)**3-1)+1'
    }
}


def calculateFunctionValue(x, number_of_equation):
    return float(ne.evaluate(EQUATIONS[number_of_equation]['FUNCTION'].split('=')[0], local_dict={'x': x}))


def calculateDerivativeFirstValue(x, number_of_equation):
    return float(ne.evaluate(EQUATIONS[number_of_equation]['DERIVATIVE_FIRST'], local_dict={'x': x}))


def calculateDerivativeSecondValue(x, number_of_equation):
    return float(ne.evaluate(EQUATIONS[number_of_equation]['DERIVATIVE_SECOND'], local_dict={'x': x}))


def calculateFiValue(x, number_of_equation):
    return float(ne.evaluate(EQUATIONS[number_of_equation]['FI'].split('=')[1], local_dict={'x': x}))


def calculateFiDerivative(x, number_of_equation):
    return float(ne.evaluate(EQUATIONS[number_of_equation]['DERIVATIVE_FI'], local_dict={'x': x}))


# Условие сходимости метода касательных
def checkConvergenceCondition(a, b, number_of_equation):
    fun_1 = calculateFunctionValue(a, number_of_equation)
    fun_2 = calculateFunctionValue(b, number_of_equation)
    # Разные знаки на конце функции
    if fun_1 * fun_2 < 0:
        if checkFirstDerivativeFunction(a, b, number_of_equation):
            if checkSecondDerivativeFunction(a, b, number_of_equation):
                return True
            else:
                print('Вторая производная не сохраняет знак на отрезке.')
        else:
            print('Первая производная не сохраняет знак на отрезке или равна нулю в какой-то точке.')
        return False
    else:
        print(f'Функция на концах интервала имеет одинаковые знаки f(a)= {fun_1} и f(b) = {fun_2}.')
    return False


# Первая производна сохраняет знак на отрезке
def checkFirstDerivativeFunction(a, b, number_of_equation):
    isNegative = calculateDerivativeFirstValue(a, number_of_equation) < 0
    for val in np.arange(a, b, abs(b - a) / 50):
        fun_val = calculateDerivativeFirstValue(val, number_of_equation)
        if fun_val == 0 or (isNegative and fun_val > 0) or (not isNegative and fun_val < 0):
            return False
    return True


def checkSecondDerivativeFunction(a, b, number_of_equation):
    isNegative = calculateDerivativeSecondValue(a, number_of_equation) < 0
    for val in np.arange(a, b, abs(b - a) / 50):
        fun_val = calculateDerivativeSecondValue(val, number_of_equation)
        if (isNegative and fun_val > 0) or (not isNegative and fun_val < 0):
            return False
    return True


def calculateLambda(a, b, number_of_equation):
    return -1 / max(abs(calculateDerivativeFirstValue(a, number_of_equation)),
                    abs(calculateDerivativeFirstValue(b, number_of_equation)))
