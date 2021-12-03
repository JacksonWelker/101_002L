step 1:
class Point(object):
    
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self):
        turtle.penup()
        turutle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(B)
        self.draw_action()
    
    def draw_action(self):
        tutule.dot()
 
step 2:
class Box(Point):
    
    def __init__(self, x1, y1, width, height, color):
        super().__init__(agr1, arg2m ... argn)
        self.yyy = yyy
        self.zzz = zzz
        
    def draw_action(self):
        tutle.dot()
step 3:
    
class BoxFilled(Box):
    
    def __init__(self, x1, y1m width, height, color fillcolor):
        super().__init__(arg1, arg2,.... argn)
        self.yyy = yyy
        
    def draw_aciton(self):
        tutle.dot()

step 4:

class Circle(Box):
    
    def __init(self, x, y, radius):
        self.center = point(x,y)
        self.radius = radius
    
    def type(self):
        circle.dot()

step 5:

class CircleFilled(BoxFilled):
        
    def __init__(self, x, y, radius):
        super().__init__(arg1, arg2,.... argn)
        self.yyy = yyy
        
    def draw_aciton(self):
        tutle.dot()



    
    

