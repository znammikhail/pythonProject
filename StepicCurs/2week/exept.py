
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print('division by ZERO')
    else:
        print('result is', result)
    finally:
        print('FINAL')

divide(10,0)
divide(5,3)
divide(2,[])