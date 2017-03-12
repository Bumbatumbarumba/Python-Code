"""
copy paste bullshit as needed
"""


    def __mul__(self,other):
        self.dotProd = 0
        if  (type(other.vector) is not list):   
            if (len(other.vector) != len(self.vector)):
                raise AssertionError
            elif type(other.vector) if int or type(other.vector) is float:
                for i in range(len(self.vector)):
                    self.dotProd = self.dotProd + (self.vector[i] * other.vector[i])
        return self.dotProd
