import math
from sympy import symbols,sympify,diff

def func(equation,num):
        result = eval(equation, {"builtins": None}, {"sin": math.sin, "cos": math.cos,'x':num})
        return float(result)

def bisection(equation,a,b) -> dict:
    a = int(a)
    b = int(b)
    response = {}
    response['data_status']= True
    
    if (func(equation,a) >= 0 and func(equation,b) < 0 ):
        pass
    elif (func(equation,b) >= 0 and func(equation,a) <0):
        a,b=b,a
    else:
        res = {
            'message':'You have not assumed right a and b',
            'status':False
        }
        return res
    error = 5
    c = a
    # print("xo\tfunc(x)\tyo\tfunc(y)\tx1\tx2\terror")
    response['header'] = [
        'iteration',
        'a',
        'f(a)',
        'b',
        'f(b)',
        'c',
        'f(c)',
        'error'
    ]
    iteration = []
    while (abs(error) > 0.005):
        row = {}
        # Find middle point
        
        # Check if middle point is root
        if (func(equation,c) == 0.0):
            break
        # print(f"{a:.2f}\t{b:.2f}\t", end=" ")
        row['a'] = round(a, 4)
        row['f(a)'] = round(func(equation,a),4)
        row['b']= round(b,4)
        row['f(b)'] = round(func(equation,b),4)

        c = (a + b) / 2
        row['c'] =round(c,4)
        row['f(c)']=round(func(equation,c),4)
        # row['mid_point']= c

        # Decide the side to repeat the steps
        error = (a - b) / a;
        if (func(equation,c) * func(equation,a) < 0):
            b = c
            # print(f"{a:.2f}\t{b:.2f}\t", end=" ")
            # row['c']= a
            # row['b']=b

        else:
            a = c
            # print(f"{a:.2f}\t{b:.2f}\t", end=" ")
            # row['new_x'] = a
            # row['new_x_val'] = b

        # print(f"{error:.3f}")
        row['error']= round(error,4)
        iteration.append(row)
    response['iteration']=iteration
    response['root']=c
    return response

def newton_raphson(equation,a):
    x = symbols('x')
    expr = sympify(equation)
    d_equation = diff(expr)
    d_str_eqn = str(d_equation)
    a = int(a)
    response = {}
    response['data_status']= True
    error = 5
    c = a
    # print("xo\tfunc(x)\tyo\tfunc(y)\tx1\tx2\terror")


    iteration = []
    response['header'] = [
        'iteration',
        'a',
        'f(a)',
        'c',
        'f(c)',
        'error'
    ]
    while (abs(error) > 0.005):
        row = {}
        # Find middle point
        
        # Check if middle point is root
        if (func(equation,c) == 0.0):
            break
        # print(f"{a:.2f}\t{b:.2f}\t", end=" ")
        row['a'] = round(a, 4)
        row['f(a)'] = round(func(equation,a),4)

        val = func(equation,a)
        d_val = func(d_str_eqn,a)
        c = a - (val/d_val)
        row['c'] =round(c,4)
        row['f(c)']=round(func(equation,c),4)
        # row['mid_point']= c


        # Decide the side to repeat the steps
        error = (a - c) / a;
        a = c

        # print(f"{error:.3f}")
        row['error']= round(error,4)
        iteration.append(row)
    response['iteration']=iteration
    response['root']=c
    return response

def false_position(equation,a,b):
    a = int(a)
    b = int(b)
    response = {}
    response['data_status']= True
    error = 5
    c = a
    # print("xo\tfunc(x)\tyo\tfunc(y)\tx1\tx2\terror")

    iteration = []

    response['header'] = [
        'iteration',
        'a',
        'f(a)',
        'b',
        'f(b)',
        'c',
        'f(c)',
        'error'
    ]

    while (abs(error) > 0.05):
        row = {}
        # Find middle point
        
        # Check if middle point is root
        if (func(equation,c) == 0.0):
            break
        # print(f"{a:.2f}\t{b:.2f}\t", end=" ")
        row['a'] = round(a, 4)
        row['f(a)'] = round(func(equation,a),4)
        row['b']= round(b,4)
        row['f(b)'] = round(func(equation,b),4)

        c = ((func(equation,a)*b) -(func(equation,b)*a)) / (func(equation,a)-func(equation,b))
        row['c'] =round(c,4)
        row['f(c)']=round(func(equation,c),4)
        # row['mid_point']= c

        # Decide the side to repeat the steps
        error = (a - b) / a;
        if (func(equation,c)>0):
            a = c


        else:
            b = c

        # print(f"{error:.3f}")
        row['error']= round(error,4)
        iteration.append(row)
        if abs(round(func(equation,c),4)) == 0.0000:
            break
    response['iteration']=iteration
    response['root']=c
    return response

def fixed_point(equation,a,b):
    a = int(a)
    b = int(b)
    response = {}
    response['data_status']= True
    if func(equation,a) * func(equation,b) >= 0:
        res = {
            'message':'You have not assumed right a and b. They should bracket the root.',
            'status':False
        }
        return res
 
    error = 5
    c = a
    # print("xo\tfunc(x)\tyo\tfunc(y)\tx1\tx2\terror")

    iteration = []

    response['header'] = [
        'iteration',
        'a',
        'f(a)',
        'b',
        'f(b)',
        'c',
        'f(c)',
        'error'
    ]
    while (abs(error) > 0.005):
        row = {}
        # Find middle point
        
        # Check if middle point is root
        if (func(equation,c) == 0.0):
            break
        # print(f"{a:.2f}\t{b:.2f}\t", end=" ")
        row['a'] = round(a, 4)
        row['f(a)'] = round(func(equation,a),4)
        row['b']= round(b,4)
        row['f(b)'] = round(func(equation,b),4)

        c = b - func(equation,b)*(b-a)/(func(equation,b)-func(equation,a))
        row['c'] =round(c,4)
        row['f(c)']=round(func(equation,c),4)
        # row['mid_point']= c

        # Decide the side to repeat the steps
        error = (a - b) / a;
        if func(equation,c) == 0.0:
            break
        if (func(equation,c) * func(equation,a) < 0):
            b = c
        else:
            a = c
        # print(f"{error:.3f}")
        row['error']= round(error,4)
        iteration.append(row)
        if abs(round(func(equation,c),4)) == 0.0000:
            break
    response['iteration']=iteration
    response['root']=c
    return response
