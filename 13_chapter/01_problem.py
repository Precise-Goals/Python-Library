class Vec2D:
    def __init__(self, i, j):
        self.i = i
        self.j = j

    def show(self):
        print(f"2D Vector: {self.i}i + {self.j}j = 0")


class Vec3D(Vec2D):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k

    def show(self):
        print(f"3D Vector: {self.i}i + {self.j}j + {self.k}k = 0")


posVec = Vec2D(5, 7)
posVec.show()
hreVec = Vec3D(5, 7, 9)
hreVec.show()
