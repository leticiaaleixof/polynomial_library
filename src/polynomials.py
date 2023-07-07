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