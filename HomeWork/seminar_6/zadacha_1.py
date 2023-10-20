class Vector():
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __abs__(self):
        return (self.x**2+self.y**2+self.z**2)**0.5
    def __add__(self, other):
        if isinstance(other, Vector) == True:
            return Vector(self.x+other.x,self.y+other.y,self.z+other.z)
        else:
            return Vector(self.x+other,self.y+other,self.z+other)

    def __radd__(self, other):
        if isinstance(other, Vector) == True:
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            return Vector(self.x + other, self.y + other, self.z + other)
    def __sub__(self, other):
        if isinstance(other, Vector) == True:
            return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
        else:
            return Vector(self.x-other,self.y-other,self.z-other)
    def __rsub__(self, other):
        if isinstance(other, Vector) == True:
            return Vector(self.x-other.x,self.y-other.y,self.z-other.z)
        else:
            return Vector(self.x-other,self.y-other,self.z-other)
    def __mul__(self, other):
        if isinstance(other, Vector) == True:
            return Vector(self.x*other.x,self.y*other.y,self.z*other.z)
        else:
            return Vector(self.x*other,self.y*other,self.z*other)
    def __rmul__(self, other):
        if isinstance(other, Vector) == True:
            return Vector(self.x*other.x,self.y*other.y,self.z*other.z)
        else:
            return Vector(self.x*other,self.y*other,self.z*other)
    def __truediv__(self, other):
        if isinstance(other, Vector) == True:
            return Vector(self.x/other.x,self.y/other.y,self.z/other.z)
        else:
            return Vector(self.x/other,self.y/other,self.z/other)

    def __rtruediv__(self, other):
        if isinstance(other, Vector) == True:
            return Vector(self.x / other.x, self.y / other.y, self.z / other.z)
        else:
            return Vector(self.x / other, self.y / other, self.z / other)
    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'
v1 = Vector(1,2,3)
v2 = Vector(9,8,7)
v3 = v1 + 5 + v2
print(isinstance(v1, Vector))
print(v1.x, v1.x*v2.x)
print(abs(v2),abs(v1))
print(v3.x,v3.y, v3.z)
v3 = v1 - v2 - 33 + 42 - v2
print(v3.x,v3.y, v3.z)
v3 = v1/5 + 3 -v1 + v2 -v2*8 + 9*v1 + 5/v1
print(v3)