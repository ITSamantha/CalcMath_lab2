import numexpr as ne

SYSTEMS_OF_EQUATIONS = \
    {
        1:
            {
                'SYSTEM': ['sin((x1)-0.6)-(x2)-1.6=0', '3*(x1)-cos((x2))-0.9=0'],
                'EQUIVALENT': ['x2=sin((x1)-0.6)-1.6', 'x1=(cos(x2)+0.9)/3'],
                'YACOBIAN': [['cos(x1-6)', '0'], ['0', '-sin(x2)/3']]
            },
        2:
            {
                'SYSTEM': ['(x1-3)**2-2*(x1)-(x2)+1=0', '(x1)-(x2)**3-27=0'],
                'EQUIVALENT': ['x2=((x1-3)**2-2*(x1)+1)', 'x1=((x2)**3+27)'],
                'YACOBIAN': [['2*(x1-3)-2', '0'], ['0', '3*(x2)**2']]
            },
        3:
            {
                'SYSTEM': ['0.1*(x1)**2+(x1)+0.2*(x2)**2-0.3=0', '0.2*(x1)**2+(x2)+0.1*(x1)*(x2)-0.7=0'],
                'EQUIVALENT': ['x2=0.70-0.20*(x1)**2-0.10*(x1)*(x2)', 'x1=0.30-0.10*(x1)**2-0.20*(x2)**2'],
                'YACOBIAN': [['-0.2*(x1)', '-0.4*(x2)'], ['-0.4*(x1)-0.1*(x2)', '-0.1*(x1)']]
            },
        4:
            {
                'SYSTEM': ['x1+x1*(x2)**3-9=0', 'x1*x2+x1*(x2)**2-6-x2=0'],
                'EQUIVALENT': ['x2=x1*x2+x1*(x2)**2-6', 'x1=-x1*(x2)**3+9'],
                'YACOBIAN': [['x2+x2**2', 'x1+2*x1*x2'], ['-(x2)**3', '-3*x1*(x2)**2']]
            }
    }


def calculateEquivalent(number_of_system, number_of_equivalent, x, y):
    return float(ne.evaluate(SYSTEMS_OF_EQUATIONS[number_of_system]['EQUIVALENT'][number_of_equivalent].split('=')[1],
                             local_dict={'x1': x, 'x2': y}))


def calculateYacobian(number_of_system, number_of_yacobian, number_of_dervivative, x=None, y=None):
    return float(
        ne.evaluate(SYSTEMS_OF_EQUATIONS[number_of_system]['YACOBIAN'][number_of_yacobian][number_of_dervivative],
                    local_dict={'x1': x, 'x2': y}))


def calculateFunction(number_of_system, x, y):
    return float(ne.evaluate(SYSTEMS_OF_EQUATIONS[number_of_system]['SYSTEM'][0].split('=')[1],
                             local_dict={'x1': x, 'x2': y}))
