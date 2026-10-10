class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"Vector with scal_proiz {self.scal_proiz, self.sloz, self.vich}"
    def scal_proiz(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)
    def sloz(self, other):
        return (self.x + other.x), (self.y + other.y), (self.z + other.z)
    def vich(self, other):
        return (self.x - other.x), (self.y - other.y), (self.z - other.z)
vector = Vector(1, 2, 3)
vector2 = Vector(2, 3, 4)

print(vector.scal_proiz(vector2), vector.sloz(vector2), vector.vich(vector2))
print(str(vector))