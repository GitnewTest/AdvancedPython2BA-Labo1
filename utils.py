# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016

def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0
    """
    p = 0
    z = 1
    while p < n:
        z *= n - p
        p += 1
    return z
    

def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    d = b ** 2 - 4 * a * c
    if d > 0:
        root1 = (-b + d ** 0.5) / (2 * a)
        root2 = (-b - d ** 0.5) / (2 * a)
        return (root1, root2)
    elif d == 0:
        root = -b / (2 * a)
        return (root)
    else:
        return ()


def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    n = 50  #Nombre de pas
    h = (upper - lower) / n  #Aire des petits rectangles

    z = 0
    for i in range(n):
        x = lower + (i + 0.5) * h
        z += eval(function) * h
    return round(z,3)


if __name__ == '__main__':
    print(fact(5))
    print(roots(1, 0, 1))
    print(integrate('x ** 2 - 1', -1, 1))
