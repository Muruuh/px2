class Rectangle:
    def __init__(self, a=0, b=0, name=""):
        self.a = a
        self.b = b
        self.name = name

    @classmethod
    def create_manually(cls):
        a = float(input("Тэгш өнцөгтийн уртыг (a) оруулна уу: "))
        b = float(input("Тэгш өнцөгтийн өргөнийг (b) оруулна уу: "))
        name = input("Тэгш өнцөгтийн нэрийг оруулна уу ")
        return cls(a, b, name)

    @classmethod
    def create_from_parameters(cls, a, b, name):
        return cls(a, b, name)

    @classmethod
    def create_from_file(cls, filename):
        with open(filename, 'r') as file:
            data = file.readline().split()
            a, b, name = map(float, data)
        return cls(a, b, name)

    @classmethod
    def create_from_object(cls, other_rectangle):
        return cls(other_rectangle.a, other_rectangle.b, other_rectangle.name)

    def get_length(self):
        return self.a

    def get_width(self):
        return self.b

    def get_name(self):
        return self.name


# Creating objects using different constructors
rectangle1 = Rectangle.create_manually()
rectangle2 = Rectangle.create_from_parameters(5, 8, "Rectangle2")
rectangle3 = Rectangle.create_from_file("rectangle_data.txt")
rectangle4 = Rectangle.create_from_object(rectangle2)

print(f"\nТэгш өнцөгт 1-ийн талаарх мэдээлэл:")
print(f"Урт: {rectangle1.get_length()}, Өргөн: {rectangle1.get_width()}, Name: {rectangle1.get_name()}")

print(f"\nТэгш өнцөгт 2-ийн талаарх мэдээлэл:")
print(f"Урт:{rectangle2.get_length()}, Өргөн: {rectangle2.get_width()}, Name: {rectangle2.get_name()}")

print(f"\nТэгш өнцөгт 3-ийн талаарх мэдээлэл:")
print(f"Урт:{rectangle3.get_length()}, Өргөн: {rectangle3.get_width()}, Name: {rectangle3.get_name()}")

print(f"\nТэгш өнцөгт 4-ийн талаарх мэдээлэл:")
print(f"Урт:{rectangle4.get_length()}, Өргөн: {rectangle4.get_width()}, Name: {rectangle4.get_name()}")
