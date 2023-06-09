import matplotlib.pyplot as plt

class Polynomial:
  def __init__(self, polynomial):
    '''The initialization recieves a dict where the
    indexes are non-negative degrees and the values
    are the coeficients, or a string in the format:
    'ax^n + bx^(n-1) + ... + gx + h'. '''
    self.polynomial = polynomial


  def string_polynomial(self, polynomial = None):
    '''return the polynomial as a string.'''
    if polynomial == None:
      polynomial = self.polynomial
    p = [] #list with separate terms of the polynomial
    for i in polynomial:
      if polynomial[i] > 0 and polynomial[i] < 1:
        p.append(f'+{polynomial[i]}x^{i}')
      elif polynomial[i] < 0 and polynomial[i] > -1:
        p.append(f'{polynomial[i]}x^{i}')
      # cases where the coefficient is equal to 1 or -1 and it is unnecessary to show it
      if polynomial[i] == 1 and i != 0 and i != 1:
        p.append(f'+x^{i}')
      elif polynomial[i] == 1 and i == 1:
        p.append(f'+x')
      if polynomial[i] == -1 and i != 0 and i != 1:
        p.append(f'-x^{i}')
      elif polynomial[i] == -1 and i == 1:
        p.append(f'-x')
      if polynomial[i] > 1 and i != 0 and i != 1:
        p.append(f'+{polynomial[i]}x^{i}')
      elif polynomial[i] < -1 and i != 0 and i != 1:
        p.append(f'{polynomial[i]}x^{i}')
      # cases where the exponent is equal to 1, and it is unnecessary to show it
      if polynomial[i] > 1 and i == 1:
        p.append(f'+{polynomial[i]}x')
      elif polynomial[i] < -1 and i== 1:
        p.append(f'{polynomial[i]}x')
      if polynomial[i] == 0 and i == 0:
        p.append(' ')
      # cases where the exponent is equal to 0:
      if polynomial[i] > 0 and i == 0:
        p.append(f'+{polynomial[i]}')
      elif polynomial[i] < 0 and i == 0:
        p.append(f'{polynomial[i]}')
    delimiter = ''
    polynomial = delimiter.join(p)
    #if there is a "+" at the beginning of the polynomial, the sign will be erased
    if polynomial[0] == '+':
      polynomial = polynomial[1:]
    if polynomial[len(polynomial)-1] == ' ':
      polynomial = polynomial[:len(polynomial)-1]
    return polynomial
  

  def dict_polynomial(self, polynomial = None):
    '''Given a polynomial in string format, the code will
    return a dictionary representation of the polynomial.
    Args:
        polynomial (str): Polynomial string in the format
        'a_n*x^n + a_(n-1)*x^(n-1) + ... + a_1*x + a_0'.
    Returns:
        dict: Dictionary representation of the polynomial,
        where the keys are the exponents and the values
        are the coefficients.'''
    if polynomial == None:
      polynomial = self.polynomial
    # Preprocess the string to standardize the format
    polynomial_str = polynomial.replace('+x^', '+1:')
    if polynomial_str[:2] == 'x^':
      polynomial_str = polynomial_str.replace('x^', '1:')
    elif polynomial_str[:1] == 'x':
      polynomial_str = polynomial_str.replace('x', '1:1')
    polynomial_str = polynomial_str.replace('-x^', '-1:')
    polynomial_str = polynomial_str.replace('x^', ':')
    polynomial_str = polynomial_str.replace('x', ':1')
    terms = []
    p_list = polynomial_str.split('+')
    for negative in p_list:
      p_list = negative.replace('-', ' -')
      p_list = p_list.split(' ')
      terms += p_list
    if terms[0] == '':
      del terms[0]
    # add degree zero to the constant term:
    final_term = terms[len(terms)-1]
    if ':' not in final_term:
      final_term = final_term.replace(final_term, final_term +':0')
      terms[len(terms)-1] = final_term
    dictionary = {}
    for term in terms:
      term_parts = []
      term_parts.append(term)
      '''Convert the coefficient to float or int, depending on its value
      If the coefficient contains a decimal point, it is converted to float
      Otherwise, it is converted to int.'''
      for part in term_parts:
        term_parts = part.split(':')
        coefficient = term_parts[0]
        degree = term_parts[1]
        if float(coefficient)%1 == 0:
          dictionary[int(degree)] = int(float(coefficient))
        else:
          dictionary[int(degree)] = float(coefficient)
    return dictionary


  def value_at_x(self, x, polynomial = None) -> float:
    '''Calculates the value of the polynomial at a given x-coordinate.'''
    if polynomial == None:
      polynomial = self.polynomial
    if type(polynomial) == str:
      polynomial = self.dict_polynomial(polynomial)

    value = 0
    for degree in polynomial:
      value += polynomial[degree] * x ** degree
    return value
  
  
  def sum_of_two_polynomials(self, second_polynomial) -> dict:
    '''Calculates the sum of two polynomials.'''
    if type(self.polynomial) == str:
      polynomial = self.dict_polynomial(self.polynomial)
    else:
      polynomial = self.polynomial
    if type(second_polynomial) == str:
      second_polynomial = self.dict_polynomial(second_polynomial)

    sum = {}
    for degree, coefficient in polynomial.items():
      sum[degree] = sum.get(degree, 0) + coefficient
    for degree, coefficient in second_polynomial.items():
      sum[degree] = sum.get(degree, 0) + coefficient
    return sum


  def subtraction_of_two_polynomials(self, second_polynomial) -> dict:
    '''Calculates the subtraction of two polynomials.'''
    if type(self.polynomial) == str:
      polynomial = self.dict_polynomial(self.polynomial)
    else:
      polynomial = self.polynomial
    if type(second_polynomial) == str:
      second_polynomial = self.dict_polynomial(second_polynomial)

    subtraction = {}
    for degree, coefficient in polynomial.items():
      subtraction[degree] = subtraction.get(degree, 0) + coefficient
    for degree, coefficient in second_polynomial.items():
      subtraction[degree] = subtraction.get(degree, 0) - coefficient
    return subtraction
  

  def multiplying_two_polynomials(self, second_polynomial) -> dict:
    '''Calculates the multiplication of two polynomials.'''
    if type(self.polynomial) == str:
      polynomial = self.dict_polynomial(self.polynomial)
    else:
      polynomial = self.polynomial
    if type(second_polynomial) == str:
      second_polynomial = self.dict_polynomial(second_polynomial)

    product = {}
    for degree, coefficient in polynomial.items():
      for degree2, coefficient2 in second_polynomial.items():
        product[degree + degree2] = product.get(degree + degree2, 0) + coefficient * coefficient2
    return product


  def division_of_two_polynomials(self, divisor) -> dict:
    '''Performs the division of two polynomials and returns the quotient.'''
    if type(self.polynomial) == str:
      polynomial = self.dict_polynomial(self.polynomial)
    else:
      polynomial = self.polynomial
    if type(divisor) == str:
      divisor = self.dict_polynomial(divisor)

    quotient = {}
    remainder = polynomial.copy()
    dividend_degree = max(polynomial.keys())
    divisor_degree = max(divisor.keys())
    while dividend_degree >= divisor_degree:
      current_degree = dividend_degree - divisor_degree
      current_coefficient = remainder[dividend_degree] / divisor[divisor_degree]
      quotient[current_degree] = current_coefficient
      for degree, coefficient in divisor.items():
        remainder_degree = degree + current_degree
        remainder_coefficient = coefficient * current_coefficient
        if remainder_degree in remainder:
          remainder[remainder_degree] -= remainder_coefficient
        else:
          remainder[remainder_degree] = -remainder_coefficient

      del remainder[dividend_degree]
      if remainder:
        dividend_degree = max(remainder.keys())
      else:
        dividend_degree = 0

    return quotient
  

  def derivative(self) -> dict:
    '''Calculates the derivative of a polynomial.
    Returns:
      dict: The polynomial representing the derivative of
      the original polynomial.'''
    if type(self.polynomial) == str:
      polynomial = self.dict_polynomial(self.polynomial)
    else:
      polynomial = self.polynomial
    derivative = {}
    for degree in polynomial:
      if degree == 0:
        pass
      elif degree > 0:
        coefficient = polynomial[degree]*degree
        degree = degree-1
        derivative[degree] = coefficient
    return derivative
  

  def derivative_at_x(self, x) -> float:
    '''Calculates the derivative of a polynomial at a specific x-coordinate.'''
    derivative = self.derivative()
    return self.value_at_x(x, derivative)


  def polynomial_behavior(self, x):
    '''Determines the behavior of a polynomial at a given point.'''
    if self.derivative_at_x(x) > 0:
      print(f'The polynomial is increasing at the point x = {x}')
    elif self.derivative_at_x(x) < 0:
      print(f'The polynomial is decreasing at the point x = {x}')
    else:
      print(f'the polynomial has a stationary point at x = {x}')

    first_derivative = self.derivative()
    second_derivative = self.derivative(first_derivative)
    second_derivative_at_x = self.value_at_x(x, second_derivative)

    if second_derivative_at_x > 0:
      print(f'The polynomial is concave upward at the point x = {x}')
    elif second_derivative_at_x < 0:
      print(f'the polynomial is concave downwards at the point x = {x}')


  def newtons_method(self, x, max_iter = int(1e4), tol = 1e-6) -> float:
    '''Apply Newton's method to find the root of a polynomial.'''
    x_n = x
    polynomial_at_x = self.value_at_x(x)
    derivative_at_x = self.derivative_at_x(x)
    x_n1 = x - (polynomial_at_x / derivative_at_x)
    if derivative_at_x == 0:
      raise ValueError("Derivative equals zero. Newton's method does not converge.")

    for iter in range(max_iter):
      if abs(x_n1 - x_n) < tol:
        return x_n1
      x_n = x_n1
      polynomial_at_x = self.value_at_x(x_n)
      derivative_at_x = self.derivative_at_x(x_n)
      if derivative_at_x == 0:
        raise ValueError("Derivative equals zero. Newton's method does not converge.")
      x_n1 = x_n - (polynomial_at_x / derivative_at_x)
    raise ValueError("Maximum number of iterations reached.  Newton's method does not converge")
  

  def symbolic_integration(self, polynomial = None) -> dict:
    '''calculates the integration of a polynomial.
    Returns:
      dict: The polynomial representing the symbolic integral of the polynomial.'''
    if polynomial == None:
      polynomial = self.polynomial
    if type(polynomial) == str:
      polynomial = self.dict_polynomial(polynomial)
    integral = {}
    for term in polynomial:
      degree = term+1
      coefficient = polynomial[term]/degree
      integral[degree] = coefficient
    return integral
  

  def definite_integral(self, interval: list, polynomial = None) -> float:
    '''returns the definite integral using the fundamental theorem of calculus.'''
    if polynomial == None:
      polynomial = self.polynomial
    a = interval[0] # lower limit of integration
    b = interval[1] # upper limit of integration
    integral = self.symbolic_integrate(polynomial)
    return self.value_at_x(b, integral) - self.value_at_x(a, integral)


  def area_between_two_curves(self, second_polynomial, interval: list) -> float:
    ''' returns the area between the curves of two polynomials. '''
    return self.definite_integral(interval) - self.definite_integral(interval, second_polynomial)


  def x_points(self, interval: list, subintervals) -> list:
    """Calculates the x points of the integration interval.
      Args:
        - subintervals_length: Optional. The length of the subintervals.
      If not provided, the default value is used.
    """
    a = interval[0]
    b = interval[1]
    subinterval_length = (b - a)/subintervals
    x_points = []
    x = a
    while x <= b:
      x_points.append(x)
      x += subinterval_length
    return x_points


  def y_points(self, interval, subintervals, x_points = None) -> list:
    """Calculates the y points corresponding to the x points of the integration
    interval.
      Args:
        - x_points: Optional. A list containing the x points of the integration
        interval. If not provided, the default value is used.
    """
    if x_points == None:
      x_points = self.x_points(interval, subintervals)
    y_points = []
    for x in x_points:
      y_points.append(self.value_at_x(x))
    return y_points
  

  def riemann_sum(self, interval, subintervals) -> float:
    '''Calculates the numerical integral using the Riemann sum.'''
    if type(self.polynomial) == str:
      polynomial = self.dict_polynomial(self.polynomial)
    else:
      polynomial = self.polynomial
    a = interval[0]
    b = interval[1]
    subinterval_length = (b - a)/subintervals
    y_points = self.y_points(interval, subintervals)
    summation = 0
    for y in y_points:
      if y_points.index(y) < len(y_points)-1:
        summation += y
    integral = subinterval_length * summation
    return integral
  

  def trapezoidal_rule(self, interval, subintervals) -> float:
    '''Calculates the numerical integral using the trapezoidal rule.'''
    if type(self.polynomial) == str:
      polynomial = self.dict_polynomial(self.polynomial)
    else:
      polynomial = self.polynomial
    a = interval[0]
    b = interval[1]
    subinterval_length = (b - a)/subintervals
    y_points = self.y_points(interval, subintervals)
    summation = 0
    for index, y in enumerate(y_points):
      if index == 0 or index == len(y_points)-1:
        summation += y
      else:
        summation += 2 * y
    integral = (subinterval_length / 2) * summation
    return integral
  

  def simpsons_rule(self, interval, subintervals) -> float:
    '''Calculates the numerical integral using Simpson's rule.
      Returns:
        The value of the numerical integral calculated using Simpson's rule.
    '''
    if type(self.polynomial) == str:
      if type(self.polynomial) == str:
        polynomial = self.dict_polynomial(self.polynomial)
      else:
        polynomial = self.polynomial
    a = interval[0]
    b = interval[1]
    y_points = self.y_points(interval, subintervals)
    summation = 0
    for index, y in enumerate(y_points):
      if index == 0 or index == len(y_points)-1:
        summation += y
      elif index % 2 == 0:
        summation += 2 * y
      else:
        summation += 4 * y
    subinterval_length = (b - a)/subintervals
    numerical_integral = (subinterval_length/3) * summation
    return numerical_integral
  

  def polynomial_graph(self, interval: list):
    '''this function plots the graph of the polynomial over a given interval'''
    x_points = self.x_points(interval, 1000)
    plt.plot(x_points, self.y_points(interval, 10000, x_points), label='Polynomial')
    plt.axhline(0, color='black', linestyle='-')
    plt.legend(loc='upper left', fontsize='small')
    plt.show()


  def riemann_graph(self, interval: list, subintervals: int):
    '''This function plots the Riemann sum graph for the numerical integration
    using the specified number of subintervals. It shows the function curve and
    the Riemann sum bars.'''
    a = interval[0]
    b = interval[1]
    subinterval_length  = (b - a)/subintervals
    fig, ax = plt.subplots(figsize=(7, 6))
    x_points = self.x_points(interval, subintervals)
    ax.set_xlim(a, b)
    ax.plot(self.x_points(interval, 1000), self.y_points(interval, subintervals, self.x_points(interval, 1000)), color = 'black', label= 'Polynomial')
    ax.bar(x_points, self.y_points(interval, subintervals, x_points), width = subinterval_length,
           align = 'edge', edgecolor = 'darkblue', label= 'Riemann Sum')
    ax.legend(loc='upper left', fontsize='small')


  def trapezoidal_graph(self, interval: list, subintervals: int):
    ''' This function plots the trapezoidal rule graph for the numerical
    integration using the specified number of subintervals. It shows the
    function curve and the trapezoids.'''
    a = interval[0]
    b = interval[1]
    subintervals_length = (b - a)/1000
    x_points = self.x_points(interval, 1000)
    plt.plot(x_points, self.y_points(interval, subintervals, x_points), color = 'black', label= 'Polynomial')
    x_points = self.x_points(interval, subintervals)
    y_points = self.y_points(interval, subintervals, x_points)
    plt.plot(x_points, y_points)
    plt.fill_between(x_points, y_points, color='blue', alpha=0.1, label='trapezoids')
    for x, y in zip(x_points, y_points):
      plt.plot([x, x], [0, y], color='blue')
    plt.legend(loc='upper left', fontsize='small')
    plt.show()