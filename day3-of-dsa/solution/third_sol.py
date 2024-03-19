class Rectangle:
    def __init__(self, length, bredth):
        self.length = length
        self.bredth = bredth

    def set_dimensions(self, new_length, new_breadth):
        self.length = new_length
        self.bredth = new_breadth

    @property
    def dimensions(self):
        return self.length, self.bredth

    @dimensions.setter
    def dimensions(self, new_dimensions):
        new_length, new_breadth = new_dimensions
        self.length = new_length
        self.bredth = new_breadth

    def show_dimension(self):
        return f" Dimension of rectangle : length  {self.length} m and bredth {self.bredth}"
    def getArea(self):
        """Area of rectangle is given by lentgth in breadth"""
        return f"Area of rectangle is  {self.length*self.bredth}"

new_rect = Rectangle(10, 20)
print(new_rect.show_dimension())
new_rect.set_dimensions(15, 25)
print(new_rect.show_dimension())
print(new_rect.getArea())

