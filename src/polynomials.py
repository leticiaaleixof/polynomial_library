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

