class Matrix:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __add__(self, other):
        return Matrix(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
    
    def __mul__(self, other):
        # mnożenie macierzy
        a = self.a * other.a + self.b * other.c
        b = self.a * other.b + self.b * other.d
        c = self.c * other.a + self.d * other.c
        d = self.c * other.b + self.d * other.d
        return Matrix(a, b, c, d)

    def __str__(self):
        custom_string = f"""({self. a} {self.b})
({self. c} {self.d})"""
        return custom_string
    
    def __repr__(self):
        return f"Matrix({self.a}, {self.b}, {self.c}, {self.d})"


A = Matrix(1,2,3,4)
I = Matrix(1,0,0,1)

print(A*I)
print(I+I)