class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}j"

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return ComplexNumber(real_part, imag_part)
        else:
            raise TypeError("Үржүүлэх нь зөвхөн нийлмэл тоонуудын хувьд тодорхойлогддог.")

with open('input.txt', 'r') as input_file:
    lines = input_file.readlines()

complex_numbers = [list(map(float, line.split())) for line in lines]

complex_num1 = ComplexNumber(complex_numbers[0][0], complex_numbers[0][1])
complex_num2 = ComplexNumber(complex_numbers[1][0], complex_numbers[1][1])

result = complex_num1 * complex_num2

with open('output.txt', 'w') as output_file:
    output_file.write(str(result))
