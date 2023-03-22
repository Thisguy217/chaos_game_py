import turtle
from random import choice
from tqdm import tqdm

def main():
    draw_sierpinski(points = 1000, distance = 2, shape="Pentagon")
    turtle.getscreen().getcanvas().postscript(file='output.eps')
    window.exitonclick()

#Turtle Initialization
window = turtle.Screen()
window.bgcolor("black")
size = 5
dotColor = "green"
t = turtle.Turtle()

t.speed(0)

#Triangle
POINT_A_Triangle = [0,200]
POINT_B_Triangle = [-200,-100]
POINT_C_Triangle = [200,-100]

#Square
POINT_A_Square = [200,200]
POINT_B_Square = [-200,-200]
POINT_C_Square = [200,-200]
POINT_D_Square = [-200,200]

#Pentagon
POINT_A_Pentagon = [161,117]
POINT_B_Pentagon = [-61,-190]
POINT_C_Pentagon = [-200,0]
POINT_D_Pentagon = [-61,190]
POINT_E_Pentagon = [161,-117]

#Hexagon
POINT_A_Hexagon = [173,100]
POINT_B_Hexagon = [0,200]
POINT_C_Hexagon = [-173,100]
POINT_D_Hexagon = [-173,-100]
POINT_E_Hexagon = [0,-200]
POINT_F_Hexagon = [173,-100]

def MidPointCalc(first, second, midValue):
    return (first + second) / midValue

def RandomPointGenerator(shape="Triangle"):
    if shape == "Triangle":
        return choice(['A','B','C'])
    elif shape == "Square":
        return choice(['A','B','C','D'])
    elif shape == "Pentagon":
        return choice(['A','B','C','D','E'])
    elif shape == "Hexagon":
        return choice(['A','B','C','D','E','F'])
    else:
        return 'A'

def MoveToPointMath(endPoint, currentX, currentY, distance = 2, shape = "Triangle"):
    if shape == "Triangle":
        if endPoint == 'A':
            xCoordinate = MidPointCalc(POINT_A_Triangle[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_A_Triangle[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
        elif endPoint == 'B':
            xCoordinate = MidPointCalc(POINT_B_Triangle[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_B_Triangle[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
        elif endPoint == 'C':
            xCoordinate = MidPointCalc(POINT_C_Triangle[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_C_Triangle[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
    elif shape == "Square":
        if endPoint == 'A':
            xCoordinate = MidPointCalc(POINT_A_Square[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_A_Square[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
        elif endPoint == 'B':
            xCoordinate = MidPointCalc(POINT_B_Square[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_B_Square[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
        elif endPoint == 'C':
            xCoordinate = MidPointCalc(POINT_C_Square[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_C_Square[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
        elif endPoint == 'D':
            xCoordinate = MidPointCalc(POINT_D_Square[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_D_Square[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
    elif shape == "Pentagon":
        if endPoint == 'A':
            xCoordinate = MidPointCalc(POINT_A_Pentagon[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_A_Pentagon[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
        elif endPoint == 'B':
            xCoordinate = MidPointCalc(POINT_B_Pentagon[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_B_Pentagon[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
        elif endPoint == 'C':
            xCoordinate = MidPointCalc(POINT_C_Pentagon[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_C_Pentagon[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
        elif endPoint == 'D':
            xCoordinate = MidPointCalc(POINT_D_Pentagon[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_D_Pentagon[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
        elif endPoint == 'E':
            xCoordinate = MidPointCalc(POINT_E_Pentagon[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_E_Pentagon[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
    elif shape == "Hexagon":
        if endPoint == 'A':
            xCoordinate = MidPointCalc(POINT_A_Hexagon[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_A_Hexagon[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
        elif endPoint == 'B':
            xCoordinate = MidPointCalc(POINT_B_Hexagon[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_B_Hexagon[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
        elif endPoint == 'C':
            xCoordinate = MidPointCalc(POINT_C_Hexagon[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_C_Hexagon[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
        elif endPoint == 'D':
            xCoordinate = MidPointCalc(POINT_D_Hexagon[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_D_Hexagon[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
        elif endPoint == 'E':
            xCoordinate = MidPointCalc(POINT_E_Hexagon[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_E_Hexagon[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
        elif endPoint == 'F':
            xCoordinate = MidPointCalc(POINT_F_Hexagon[0], currentX, distance)
            yCoordinate = MidPointCalc(POINT_F_Hexagon[1], currentY, distance)
            t.goto(xCoordinate,yCoordinate)
            t.dot(size, dotColor)
    
def draw_sierpinski(points = 100, distance = 2, shape="Triangle"):
    index = 0;
    t.left(90)
    t.penup()
    if shape == "Triangle":
        t.goto(POINT_A_Triangle[0],POINT_A_Triangle[1])
        t.dot(size, dotColor)
        t.goto(POINT_B_Triangle[0],POINT_B_Triangle[1])
        t.dot(size, dotColor)
        t.goto(POINT_C_Triangle[0],POINT_C_Triangle[1])
        t.dot(size, dotColor)
        t.goto(0,0)
        for _ in tqdm(range(0,points)):
            letter = RandomPointGenerator()
            MoveToPointMath(letter, t.xcor(), t.ycor(), distance, shape)
            index+=1
    elif shape == "Square":
        t.goto(POINT_A_Square[0],POINT_A_Square[1])
        t.dot(size, dotColor)
        t.goto(POINT_B_Square[0],POINT_B_Square[1])
        t.dot(size, dotColor)
        t.goto(POINT_C_Square[0],POINT_C_Square[1])
        t.dot(size, dotColor)
        t.goto(POINT_D_Square[0],POINT_D_Square[1])
        t.dot(size, dotColor)
        t.goto(0,0)
        for _ in tqdm(range(0,points)):
            letter = RandomPointGenerator()
            MoveToPointMath(letter, t.xcor(), t.ycor(), distance, shape)
            index+=1
    elif shape == "Pentagon":
        t.goto(POINT_A_Pentagon[0],POINT_A_Pentagon[1])
        t.dot(size, dotColor)
        t.goto(POINT_B_Pentagon[0],POINT_B_Pentagon[1])
        t.dot(size, dotColor)
        t.goto(POINT_C_Pentagon[0],POINT_C_Pentagon[1])
        t.dot(size, dotColor)
        t.goto(POINT_D_Pentagon[0],POINT_D_Pentagon[1])
        t.dot(size, dotColor)
        t.goto(POINT_E_Pentagon[0],POINT_E_Pentagon[1])
        t.dot(size, dotColor)
        t.goto(0,0)
        for _ in tqdm(range(0,points)):
            letter = RandomPointGenerator()
            MoveToPointMath(letter, t.xcor(), t.ycor(), distance, shape)
            index+=1
    elif shape == "Hexagon":
        t.goto(POINT_A_Hexagon[0],POINT_A_Hexagon[1])
        t.dot(size, dotColor)
        t.goto(POINT_B_Hexagon[0],POINT_B_Hexagon[1])
        t.dot(size, dotColor)
        t.goto(POINT_C_Hexagon[0],POINT_C_Hexagon[1])
        t.dot(size, dotColor)
        t.goto(POINT_D_Hexagon[0],POINT_D_Hexagon[1])
        t.dot(size, dotColor)
        t.goto(POINT_E_Hexagon[0],POINT_E_Hexagon[1])
        t.dot(size, dotColor)
        t.goto(POINT_F_Hexagon[0],POINT_F_Hexagon[1])
        t.dot(size, dotColor)
        t.goto(0,0)
        for _ in tqdm(range(0,points)):
            letter = RandomPointGenerator()
            MoveToPointMath(letter, t.xcor(), t.ycor(), distance, shape)
            index+=1
            
if __name__ == "__main__":
    main()
