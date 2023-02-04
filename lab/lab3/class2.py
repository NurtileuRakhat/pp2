class Shape:
    def __init__(self) -> None:
        pass
    def area(self):
        return 0
class Sqare(Shape):
    def __init__(self,length) -> None:
        super().__init__()
        self.l = length
    def area(self):
        return self.l * self.l
x = int(input())
p = Sqare(x)
print(p.area())