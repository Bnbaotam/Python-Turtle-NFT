import turtle

myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")


def box(kich_thuoc):
    myPen.begin_fill()
    # 0 do.
    myPen.forward(kich_thuoc)
    myPen.left(90)
    # 90 do.
    myPen.forward(kich_thuoc)
    myPen.left(90)
    # 180 do.
    myPen.forward(kich_thuoc)
    myPen.left(90)
    # 270 so.
    myPen.forward(kich_thuoc)
    myPen.end_fill()
    myPen.setheading(0)


boxSize = 15
# Position myPen in top left area of the screen
myPen.penup()
myPen.forward(-100)
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0)


#Dung list de luu tru cac gia tri mau ung voi cac so 0, 1 , 2

bang_mau = ["#FFFFFF", "#FF0000", "#0000ff"]
pixels = [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]]

pixels.append([0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0])
pixels.append([0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0])
pixels.append([0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0])
pixels.append([0, 1, 1, 0, 0, 2, 2, 1, 1, 0, 0, 2, 2, 0])
pixels.append([1, 1, 1, 0, 0, 2, 2, 1, 1, 0, 0, 2, 2, 1])
pixels.append([1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1])
pixels.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
pixels.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
pixels.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
pixels.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
pixels.append([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
pixels.append([1, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1])
pixels.append([1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1])

for i in range(0, len(pixels)):
    for j in range(0, len(pixels[i])):

        #doi mau net ve
        myPen.color(bang_mau[pixels[i][j]])
        box(boxSize)
        myPen.penup()
        myPen.forward(boxSize)
        myPen.pendown()
    myPen.setheading(270)
    myPen.penup()
    myPen.forward(boxSize)
    myPen.setheading(180)
    myPen.forward(boxSize * len(pixels[i]))
    myPen.setheading(0)
    myPen.pendown()

turtle.done()