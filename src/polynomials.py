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