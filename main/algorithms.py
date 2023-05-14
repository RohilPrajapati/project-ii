import math

def bisection(equation,a,b) -> dict:
    a = int(a)
    b = int(b)
    response = {}
    response['data_status']= True
    def func(num):
        result = eval(equation, {"builtins": None}, {"sin": math.sin, "cos": math.cos,'x':num})
        return float(result)
    
    
    if (func(a) >= 0 and func(b) < 0 ):
        pass
    elif (func(b) >= 0 and func(a) <0):
        # print(func(a))
        # print(func(b))
        a,b=b,a
    else:
        print(func(a))
        print(func(b))
        res = {
            'message':'You have not assumed right a and b',
            'status':False
        }
        return res
    error = 5
    c = a
    # print("xo\tfunc(x)\tyo\tfunc(y)\tx1\tx2\terror")

    iteration = []
    while (abs(error) > 0.005):
        row = {}
        # Find middle point
        
        # Check if middle point is root
        if (func(c) == 0.0):
            break
        # print(f"{a:.2f}\t{b:.2f}\t", end=" ")
        row['a'] = round(a, 4)
        row['f(a)'] = round(func(a),4)
        row['b']= round(b,4)
        row['f(b)'] = round(func(b),4)

        c = (a + b) / 2
        row['c'] =round(c,4)
        row['f(c)']=round(func(c),4)
        # row['mid_point']= c

        # Decide the side to repeat the steps
        error = (a - b) / a;
        if (func(c) * func(a) < 0):
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