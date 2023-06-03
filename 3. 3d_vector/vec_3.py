import math


class vec_3(object):
    def __init__(self, x, y, z):
        self._length = x
        self._width = y
        self._height = z
    
    def __str__(self):
        return f"[{self._length}; {self._width}; {self._height}]"
    
    def __add__(self, other):
        lengthAdd = self._length + other._length
        widthAdd = self._width + other._width
        heightAdd = self._height + other._height
        return vec_3(lengthAdd, widthAdd, heightAdd)
    
    def __sub__(self, other):
        lengthSub = self._length - other._length
        widthSub = self._width - other._width
        heightSub = self._height - other._height
        return vec_3(lengthSub, widthSub, heightSub)
    
    def __mul__(self, other):
        a = self._length * other._length
        b = self._width * other._width
        c = self._height * other._height
        return a+b+c
    
    def __eq__(self, other):
        a = (self._length == other._length)
        b = (self._width == other._width)
        c = (self._height == other._height)
        return a and b and c

    def __ne__(self, other):
        a = (self._length != other._length)
        b = (self._width != other._width)
        c = (self._height != other._height)
        return a or b or c

    def __abs__(self):
        a = self._length**2
        b = self._width**2
        c = self._height**2
        return (a+b+c)**0.5

    def __ge__(self, other):
        return abs(self) >= abs(other)

    def __le__(self, other):
        return abs(self) <= abs(other)

    def __gt__(self, other):
        return abs(self) > abs(other)

    def __lt__(self, other):
        return abs(self) < abs(other)

    def unit(self):
        try:
            a = self._length/abs(self)
            b = self._width/abs(self)
            c = self._height/abs(self)
            return vec_3(a, b, c)
        except ZeroDivisionError as errorMsg:
            print(errorMsg , f", the vector is {self}")

    def out_prod(self, other):
        a = self._width*other._height - other._width*self._height
        b = self._length*other._height - other._length*self._height
        c = self._length*other._width - other._length*self._width
        return vec_3(a, -b, c)

    def dist(self, other):
        return abs(self - other)

    def angle(self, other):
        try:
            return math.degrees(math.acos((self*other)/(abs(self)*abs(other))))
        except ZeroDivisionError as errorMsg:
            print(errorMsg , f", doesn't work for 0 vector")

    def proj(self, other):
        return (self*other)/abs(other)

    def rej(self, other):
        #TODO
        pass
    def parall(self, other):
        return abs(self.out_prod(other)) == 0

    def prepend(self, other):
        return self*other == 0

    def triangle_area(self, other):
        return abs(self.out_prod(other))/2

    def parallelogram_area(self, other):
        return abs(self.out_prod(other))

    def parallelepiped_vol(self, other1, other2):
        return abs(self.out_prod(other1)*other2)

    def prism_vol(self, other1, other2):
        return abs(self.out_prod(other1)*other2)/2

    def pyramid_vol(self, other1, other2):
        return abs(self.out_prod(other1)*other2)/3


class vec_2(vec_3):
    def __init__(self, x, y):
        super().__init__(x, y, 0)
    
    def rotate(self, theta):
        x = self._length * math.cos(theta) - self._width * math.sin(theta)
        y = self._length * math.sin(theta) + self._width * math.cos(theta)
        return vec_2(x, y)


a = vec_2(0, 4)
b = vec_3(0,0, 4)


print(a.rotate(math.pi/2))