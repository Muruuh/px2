class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imag - other.imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"


with open("input.txt", "r") as file:
    lines = file.readlines()
    real_part1, imag_part1 = map(float, lines[0].split())
    real_part2, imag_part2 = map(float, lines[1].split())

complex_num1 = ComplexNumber(real_part1, imag_part1)
complex_num2 = ComplexNumber(real_part2, imag_part2)


result = complex_num1 - complex_num2

with open("output.txt", "w") as file:
    file.write(str(result))
