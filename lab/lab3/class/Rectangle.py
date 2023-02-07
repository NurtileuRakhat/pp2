class Shape:
    def __init__(self) -> None:
        pass
    def area(self):
        return 0
class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        super().__init__()
        self.l = length
        self.w = width
    def area(self):
        return self.l * self.w
x = int(input())
y = int(input())
p = Rectangle(x,y)
print(p.area())

