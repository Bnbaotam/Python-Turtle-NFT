import turtle
# tao but de ve (chinh la doi tuong rua)
pen = turtle.Turtle()
# tao ham ve tam giac
def ve_tam_giac(x, y):

    #chon mau muon to
    pen.fillcolor("cornflowerblue")

    #bat dau to mau
    pen.begin_fill()

    # nhac but len
    pen.penup()

    # di chuyen den vi tri x va y tuong ung
    pen.goto(x, y)
    # dat but xuong
    pen.pendown()
    # dung vong lap for ve 3 canh tam giac
    for i in range(3):
    # ve doan thang dai 100
        pen.forward(100)
        # xoay trai 120 do
        pen.left(120)
        # ve tiep doan thang dai 100
        pen.forward(100)

    #ket thuc viec to mau
    pen.end_fill()

# Khi nhan chuot vao man hinh se goi ham ve_tam_giac de ve tam giac
turtle.onscreenclick(ve_tam_giac, 1)

# lang nghe xem khi nao nguoi dung click chuot vao man hinh
turtle.listen()

turtle.done()