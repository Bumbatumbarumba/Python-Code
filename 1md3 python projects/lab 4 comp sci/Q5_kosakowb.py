#Bartosz Kosakowski
#400028494
#Lab 4 Question 5
###################

"""
QUESTION 5
NOTE: I wasn't sure what the __rmul__ function was supposed to be,
since the lab was not very informative, so it's the same thing as
the modified __mul__ function
"""
#-=-=-=-=-=-=-= __mul__ function
def __mul__(self, other):
    self.dotProd = 0
    if type(other) != type(self):
        if type(other) is int or type(other) is float:
            for i in range(len(self.vector)):
                self.vector[i] = self.vector[i] * other
        else:
            raise AssertionError
        return 'Vector: ' + str(self.vector)
    else:
        if len(other.vector) != len(self.vector):
            raise AssertionError
        else:
            for i in range(len(self.vector)):
                self.dotProd = self.dotProd + (self.vector[i] * other.vector[i])
        return self.dotProd

    
#-=-=-=-=-=-= __rmul__ function
def __rmul__(self, other):
    self.dotProd = 0
    if type(other) != type(self):
        if type(other) is int or type(other) is float:
            for i in range(len(self.vector)):
                self.vector[i] = self.vector[i] * other
        else:
            raise AssertionError
        return 'Vector: ' + str(self.vector)
    else:
        if len(other.vector) != len(self.vector):
            raise AssertionError
        else:
            for i in range(len(self.vector)):
                self.dotProd = self.dotProd + (self.vector[i] * other.vector[i])
        return self.dotProd

