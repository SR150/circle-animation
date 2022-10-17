import tkinter
import math
#variables you can change
colours=['red','white','blue']#given in a list so they can be multicoloured
number=24#number of shapes
speed=1#variable that holds speed
distance=350#gives distance the circle comes from the center in pixels
showLine=True#show the path the dot takes


dotList=[]#stores dots for access
screenWidth=800
screenHeight=800
time=0#time used to calculate position
updateTime=50#time between updates in ms

root=tkinter.Tk()#setup screen
root.title('circle animation')
root.geometry(str(screenWidth)+"x"+str(screenHeight))
canvas = tkinter.Canvas(root, width=screenWidth, height=screenHeight)
canvas.pack()
canvas.configure(background='black')

class dot:
    radius=5
    colour=1
    angle=1
    shape=1#stores the shape so it can be referenced
    n=1#for testing
    def __init__(self,colour,angle,showline,distance):
        #set apropriate variables
        self.colour=colour
        self.angle=angle
        self.shape=(canvas.create_oval(screenWidth/2+self.radius,
                                       screenHeight/2+self.radius,
                                       screenWidth/2-self.radius,
                                       screenHeight/2-self.radius,
                                       fill=self.colour,
                                       width=2))
        
        if showLine:#if show line is on
            x1=math.cos(self.angle)*distance
            y1=math.sin(self.angle)*distance
            x2=math.cos(self.angle+math.pi)*distance
            y2=math.sin(self.angle+math.pi)*distance
            
            canvas.create_line(x1+screenWidth/2,
                               y1+screenHeight/2,
                               x2+screenWidth/2,
                               y2+screenHeight/2,
                               fill='white')
            
    def update(self,time,speed,distance):
        canvas.delete(self.shape)
        position=distance*math.sin(time*speed+self.angle)
        x=math.cos(self.angle)*position
        y=math.sin(self.angle)*position
        self.shape=(canvas.create_oval(screenWidth/2+self.radius+x,
                                       screenHeight/2+self.radius+y,
                                       screenWidth/2-self.radius+x,
                                       screenHeight/2-self.radius+y,
                                       fill=self.colour,
                                       width=2))
        #canvas.itemconfig(self.shape, fill=self.colour)
    
#create dots
c=0#keeps track of which colour is to be selected from the list of colours
for i in range (number):
    c=c+1
    if c==(len(colours)-1):#go back to the start of the colour list
        c=c-len(colours)
    dotList.append(dot(colours[c],math.pi/number*i,showLine,distance))
    
def update():#update position of all dots
    global time
    global speed
    global distance
    #find time
    time=time+updateTime/1000
    #set to update again
    root.after(updateTime,lambda:update())
    for dot in dotList:#update all objects
        dot.update(time,speed,distance)
    
root.after(updateTime,update)#start programm

root.mainloop()
