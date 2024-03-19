class Circle:
    
    def __init__(self, radius):
        self.radius=radius
    @property
    def setradius(self):
        return self.radius
    @setradius.setter
    def setradius(self,new_radius):
        self.radius=new_radius
        
    def getArea(self):
        """The area of a circle is given by the formula A = pi*r^2"""
        return f"The area of circle is {round((22/7)*self.radius,2)} "
    def getCircumference(self):
        """The circumfernence of circle is given by the formula  C = 2*pi*r"""
        return f"The circumfernence of circle is : {round(2*(22/7)*self.radius,2)}"
    
first_circle=Circle(10)
first_circle.setradius=29
print(first_circle.radius)
print(first_circle.getArea())
print(first_circle.getCircumference())