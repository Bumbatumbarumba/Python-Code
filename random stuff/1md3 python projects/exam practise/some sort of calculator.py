class UnknownOperationError(Exception):
    pass

def const(c):
    return Expr('const',c,c)

class Expr:
    def __init__(self,op, a, b):
        self.operand1 = a
        self.operand2 = b
        self.op = op
    def __str__(self):
        if self.op == 'add':
            return str(self.operand1) + '+' +str(self.operand2)
        elif self.op == 'mult':
            return str(self.operand1) + '*' +str(self.operand2)
        elif self.op == 'const':
            return str(self.operand1)
        else:
            raise UnknownOperationError
    def eval(self):
        if self.op == 'add':
            return self.operand1.eval() + self.operand2.eval()
        elif self.op == 'mult':
            return self.operand1.eval() * self.operand2.eval()
        elif self.op == 'const':
            return str(self.operand1)
        else:
            raise UnknownOperationError
