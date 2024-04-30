class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __ne__(self, other):
        return self.real != other.real or self.imag != other.imag

    def __str__(self):
        return f"{self.real} + {self.imag}j"

def calculate_complex_numbers(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    complex_number_1 = map(float, lines[0].strip().split())
    complex_number_2 = map(float, lines[1].strip().split())

    complex_1 = ComplexNumber(*complex_number_1)
    complex_2 = ComplexNumber(*complex_number_2)

    result = complex_1 != complex_2

    with open(output_file, 'w') as f:
        f.write(str(result))

calculate_complex_numbers('input.txt', 'output.txt')
