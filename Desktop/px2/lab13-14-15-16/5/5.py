class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        real_sum = self.real + other.real
        imag_sum = self.imag + other.imag
        return ComplexNumber(real_sum, imag_sum)

    def __str__(self):
        return f"{self.real} + {self.imag}j"


with open("input.txt", "r") as file:
    lines = file.readlines()

real1, imag1 = map(float, lines[0].split())
real2, imag2 = map(float, lines[1].split())

complex_num1 = ComplexNumber(real1, imag1)
complex_num2 = ComplexNumber(real2, imag2)

result = complex_num1 + complex_num2

with open("output.txt", "w") as file:
    file.write(str(result))
