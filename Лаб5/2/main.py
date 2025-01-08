class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def set_radius(self, radius=1):
        self.radius = radius

    def get_radius(self):
        return self.radius


c = Circle(5)
c.set_radius(10)
print(c.get_radius())
