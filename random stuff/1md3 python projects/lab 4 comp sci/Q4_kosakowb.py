#Bartosz Kosakowski
#400028494
#Lab 4 Question 4
###################

class Vector:
    """
    Takes a vector in list form and performs various functions with, such as
    addition or multiplication; vector must be a list and each element of type
    int or float
    """
    def __init__(self,vectorCoords):
        self.vector = vectorCoords
        if type(self.vector) is not list:
            raise AssertionError
        else:
            for i in range(len(self.vector)):
                if (type(self.vector[i]) is float) or (type(self.vector[i])) is int:
                    pass
                else:                                  
                    raise AssertionError
    """
    Returns to the user the number of dimensions of the vector
    """
    def dim(self):
        return len(self.vector)

    """
    Returns the specified component of the vector 
    """
    def __getitem__(self, i):
        if i < 1:
            raise AssertionError
        else:
            return(self.vector[i-1])

    """
    The i-th component of the vector, which is non-negative and not greater
    than the dimension of the vector, and where the index begins at 1, is changed to
    a new value, x
    """
    def __setitem__(self, i, x):
        if i < 0 or i > len(self.vector):
            raise AssertionError
        else:
            self.vector[i-1] = x
            
    """
    Returns a string, vectorStr, which shows the vector in a nicer format
    """
    def __str__(self):
        return 'Vector: ' + str(self.vector)

    """
    Takes two vectors of the same type (list) and of the same length,
    and adds them together
    """
    def __add__(self, other):
        self.vectorOut = []
        if (len(other.vector) != len(self.vector)) or (type(other.vector) is not list):
            raise AssertionError
        else:
            for idx in range(len(self.vector)):
                self.vectorOut.append(self.vector[idx] + other.vector[idx])
        return 'Vector: '+ str(self.vectorOut)
        
    """
    If the type of other is either int or float, the vector is multiplied
    by other
    """
    def __mul__(self, other):
        if type(other) is int or type(other) is float:
            for idx in range(len(self.vector)):
                self.vector[idx] = (self.vector[idx] * other)
        else:
            raise AssertionError
        return 'Vector: '+ str(self.vector)

