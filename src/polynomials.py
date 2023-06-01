
    '''
    Evaluates the value of the polynomial at a given x.
    '''
    def eval(self, x):
        value_at_x = 0
        for degree in self.coef_at_degree:
            value_at_x += self.coef_at_degree[degree] * x ** degree
        return value_at_x