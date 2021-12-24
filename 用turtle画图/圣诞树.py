import turtle
import random as r
from turtle import *

n = 100.0  # 树高

t = turtle.Turtle()  # 定义turtle对象

t.showturtle()
setup(600, 800)
# 定义速度
t.speed("fastest")
# 定义背景颜色
screensize(bg='black')
t.left(90)
t.forward(3 * n)  # 移动turtle到特定位置


def drawstars(width):
    t.color("red", "yellow")  # 定义最上端星星的颜色，外圈是orange，内部是yellow
    t.begin_fill()
    t.left(126)

    for i in range(5):  # 画五角星
        t.forward(width / 5)
        t.right(144)  # 五角星的角度
        t.forward(width / 5)
        t.left(72)  # 继续换角度
    t.end_fill()
    t.right(126)
    t.color('dark green')  # 其余的随机数情况下画空的树枝


drawstars(n)  # 调用函数，画最上面的星星


def drawlight():  # 定义画彩灯的方法
    if r.randint(0, 30) == 0:  # 如果觉得彩灯太多，可以把取值范围加大一些，对应的灯就会少一些
        t.color('tomato')  # 定义第一种颜色
        t.circle(r.randint(0, 10))
    elif r.randint(0, 30) == 1:
        t.color('orange')  # 定义第二种颜色
        t.circle(r.randint(0, 10))
    elif r.randint(0, 30) == 25:
        drawstars(r.randint(10, 20))
    else:
        t.color('dark green')  # 其余的随机数情况下画空的树枝


def drawsnow():  # 定义画雪花的方法
    t.ht()  # 隐藏笔头，ht=hideturtle
    t.pensize(2)  # 定义笔头大小
    for i in range(50):  # 画多少雪花
        t.pencolor("white")  # 定义画笔颜色为白色，其实就是雪花为白色
        t.pu()  # 提笔，pu=penup
        t.setx(r.randint(-350, 350))  # 定义x坐标，随机从-350到350之间选择
        t.sety(r.randint(-100, 350))  # 定义y坐标，注意雪花一般在地上不会落下，所以不会从太小的纵座轴开始
        t.pd()  # 落笔，pd=pendown
        dens = r.randint(4, 6)  # 雪花瓣数
        snowsize = r.randint(1, 10)  # 定义雪花大小
        for j in range(dens):  # 就是6，那就是画5次，也就是一个雪花五角星
            # t.forward(int(snowsize))  #int（）取整数
            t.fd(int(snowsize))
            t.backward(int(snowsize))
            # t.bd(int(snowsize))  #注意没有bd=backward，但有fd=forward，小bug
            t.right(int(360 / dens))  # 转动角度


t.color("dark green")  # 定义树枝的颜色
t.backward(n * 4.8)


def tree(d, s):  # 开始画树
    if d <= 0:
        return
    t.forward(s)
    tree(d - 1, s * .8)
    t.right(120)
    tree(d - 3, s * .5)
    drawlight()  # 同时调用小彩灯的方法
    t.color('dark green')  # 画笔颜色改回绿色
    t.right(120)
    tree(d - 3, s * .5)
    t.right(120)
    t.backward(s)


tree(15, n)
t.backward(n / 2)

for i in range(200):  # 循环画最底端的小装饰
    a = 200 - 400 * r.random()
    b = 10 - 20 * r.random()
    t.up()
    t.forward(b)
    t.left(90)
    t.forward(a)
    t.down()
    if r.randint(0, 1) == 0:
        t.color('tomato')
    else:
        t.color('wheat')
    t.circle(r.randint(2, 5))
    if r.randint(0, 1) == 1:
        drawstars(15)

    t.up()
    t.backward(a)
    t.right(90)
    t.backward(b)

t.color("dark red", "red")  # 定义字体颜色
t.write("Merry Christmas", align="center", font=("Comic Sans MS", 40, "bold"))  # 定义文字、位置、字体、大小

drawsnow()
turtle.mainloop()  # 完成,否则会直接关闭s
