class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}j"

    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        real_part = (self.real * other.real + self.imag * other.imag) / denominator
        imag_part = (self.imag * other.real - self.real * other.imag) / denominator
        return ComplexNumber(real_part, imag_part)

with open('input.txt', 'r') as file:
    lines = file.readlines()
    real1, imag1, real2, imag2 = map(float, lines[0].split())

num1 = ComplexNumber(real1, imag1)
num2 = ComplexNumber(real2, imag2)

result = num1 / num2

with open('output.txt', 'w') as file:
    file.write(str(result))
