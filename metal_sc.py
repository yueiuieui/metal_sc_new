import easygui
import turtle
import os
import time
'''
This program is based on Python to achieve scratch code, open source based on MIT Licence'''
class scratch:
    x_listening=""
    def createcharacter(self,re):
            re=self
            turtle.register_shape(self)
            turtle.shape(self)
    class ui:
        def alert_notbool(line="",button="OK",tittle1="",image1=None):
            return easygui.msgbox(msg=line,tittle=tittle1,ok_button=button,image=image1,root=None)
        def alert(callback_varbool,line1="",image2=None,button1=("","")):
            callback_varbool=easygui.ccbox(msg=line1,choices=button1,image=image2)
    class io:
        def ask_suthor(authority=None):
            filecontent=None
            callback=3
            scratch.ui.alert(callback,line1="是否申请文件管理权限",image2=None,button1=("是的","不是"))
            if callback == 1:
                authority=True
            elif callback == 0:
                authority=False
        def readfile(filename,filepath):
            try:
                if authority == True:
                    filecontent=None
                    with open(filepath+filename,'rb') as f:
                        filecontent=f.read()
                elif authority == False:
                    raise "Error:No administrative authority"
            except NameError:
                print("Error:No administrative authority")
                exit(1)
    class pen:
        draw_bool=None
        def drawBegin():
            draw_bool=True
            turtle.pendown()
        def drawFinish():
            turtle.penup()
            draw_bool=False
        def pen_wight(self):
            turtle.width(self)
        def pen_color(self):
            turtle.pencolor(self)
        def typeit(line,movebool,fontname,fontsize):
            turtle.write(line, move=movebool, align="left", font=(fontname, fontsize, "normal"))
        def drawCircle(r,excent,line):
            turtle.circle(radius=r, extent=excent, steps=line)
    class move:
        turtle.degrees(fullcircle=360.00)
        def move(step,model):
            if model == 'forward':
                turtle.forward(step)
            elif model == 'backward':
                turtle.backward(step)
        def getx():
            x=turtle.xcor()
            print(x)
        def gety():
            y=turtle.ycor()
            print(y)
        def goto(x,y):
            turtle.goto(x,y)
        def setx_(self):
            turtle.setx(self)
            old_x=int(turtle.xcor())
        def setx_xpp(self):
            old_x=int(turtle.xcor())
            turtle.setx(old_x+self)
        def sety_(self):
            oldy=0
            turtle.sety(self)
        def sety_ypp(self):
            old_y=int(turtle.ycor())
            turtle.sety(oldy+self)   
        def turn(self):
            if self < 0:
                turtle.left(0-self)
            else:
                if self > 0:
                    turtle.right(self)
        def getplace():
            x=str(int(turtle.xcor()))
            y=str(int(turtle.ycor()))
            print(x+","+y)
    def create_radio(radioname):
        x_listening=radioname
    class CC:
        def hide():
            turtle.hideturtle()
        def show():
            turtle.showturtle()
        def set_bg(src):
            turtle.bgpic(src)
        def set_pic(picname):
            turtle.shape(picname)
    class chose:
        def wait_seconds(self):
            time.sleep(self)
        def ask(line,var):
            var=turtle.textinput("",line)
        def listening_key(fuction,key1):
            turtle.onkey(fuc=fuction,key=key1)
        def listening_mouse_enter(fuction1):
            turtle.onclicked(fuc=fuction1,btn=1, add=None)
        def clone_it():
            turtle.stamp()
   





    



            



        




    