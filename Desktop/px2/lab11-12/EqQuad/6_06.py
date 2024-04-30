import math

class EqQuad:
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def from_parameters(cls, a, b, c):
        return cls(a, b, c)

    @classmethod
    def from_file(cls, file_path):
        with open(file_path, 'r') as file:
            a, b, c = map(float, file.readline().split())
        return cls(a, b, c)

    @classmethod
    def from_copy(cls, other_obj):
        return cls(other_obj.a, other_obj.b, other_obj.c)

    def find_solutions(self):
        discriminant = self.b**2 - 4 * self.a * self.c

        if discriminant > 0:
            root1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
            root2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
            return root1, root2
        elif discriminant == 0:
            root = -self.b / (2 * self.a)
            return root,
        else:
            return "No real roots"

equation1 = EqQuad.from_parameters(4, -4, -3)
equation2 = EqQuad.from_parameters(1, -3, 2)  
equation3 = EqQuad.from_file('coefficients.txt')  
equation4 = EqQuad.from_copy(equation2)

print("1-р тэгшитгэлийн шийдэл:", equation1.find_solutions())
print("2-р тэгшитгэлийн шийдэл:", equation2.find_solutions())
print("3-р тэгшитгэлийн шийдэл:", equation3.find_solutions())
print("4-р тэгшитгэлийн шийдэл:", equation4.find_solutions())
