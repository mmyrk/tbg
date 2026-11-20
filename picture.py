from turtle import *

cube_count = int(input("Enter the number of cubes to draw: "))

for n10000 in range(cube_count):
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    n += 1
    right(45)
    forward(50)

done()

print("Turtle graphics completed.")