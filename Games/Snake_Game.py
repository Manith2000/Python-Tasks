import turtle #pygame is more powerful & complex
import time
import random

delay = 0.1 #since sometimes aniamtions are too fast
score = 0
high_score = 0

#setup screen
wn = turtle.Screen()
wn.title('Snake Game')
wn.bgcolor('Black')
wn.setup(width = 600,height = 600)
wn.tracer(0) #turns off screen updates


#Snake Head
head = turtle.Turtle() #creates turtle
head.speed(0) #animation speed is set to fastest
head.shape('square')
head.color('green')
head.penup()
head.goto(0,0)
head.direction = 'up'


#Snake Food
food = turtle.Turtle() #creates turtle
food.speed(0) #animation speed is set to fastest
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)

segments = [] #segments of snake


#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Score: 0 High Score: 0', align = 'center', font = ('Corbel',24,'normal'))


#Functions
def goup():
    if head.direction != 'down': #since when you press down the snake will run into it self and will crash
        head.direction = 'up'
def godown():
    if head.direction != 'up':
        head.direction = 'down'
def goright():
    if head.direction != 'left':
        head.direction = 'right'
def goleft():
    if head.direction != 'right':
        head.direction = 'left'

def move():
    y = head.ycor()
    x = head.xcor()
    if head.direction == 'up':
        head.sety(y + 20)
    if head.direction == 'down':
        head.sety(y - 20)
    if head.direction == 'right':
        head.setx(x + 20)
    if head.direction == 'left':
        head.setx(x - 20)

#Keyboard Bindings
wn.listen() #lsiten for clicks
wn.onkeypress(goup, 'w')
wn.onkeypress(godown, 's')
wn.onkeypress(goright, 'd')
wn.onkeypress(goleft, 'a')


#Main game loop
while True: #repeats again and again
    wn.update() #so every time through loop it updates the screen
    
    #check if border collision
    if head.xcor()>290 or head.ycor() < -290 or head.ycor() > 290 or  head.xcor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'

        #hide segments since snake died
        for segment in segments:
            segment.goto(1000,1000) #turtle module does not have a delete function for
        #clear segments list
        segments.clear()
        delay = 0.1
        score = 0
        pen.clear() #clears previously written by pen
        pen.write(f'Score: {score}  High Score: {high_score}', align = 'center', font = ('Corbel',24,'normal'))


    #check if you get the food
    if head.distance(food) < 20: #distance ebtween head and food. each turtle shape is 20x20 pixels so if less than 20 means they collided
        
        
        #move food to new position
        x = random.randint(-290,290) #since top and bottom are 300x300 size window. within screen
        y = random.randint(-290,290)
        food.goto(x,y)

        #add a new snake segment
        new_segment = turtle.Turtle()
        new_segment.speed(0) #animation speed is set to fastest
        new_segment.shape('square')
        new_segment.color('green')
        new_segment.penup()
        segments.append(new_segment)

        #shorten delay
        delay -= 0.01
        
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear() #clears previously written by pen
        pen.write(f'Score: {score}  High Score: {high_score}', align = 'center', font = ('Corbel',24,'normal'))

    #Move segments from end to beginning
    for i in range(len(segments)-1,0,-1): #iterate backwards
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y) #current segment must go to where the previous segment in the loop was (i.e. towards start of snake)
    
    if len(segments) > 0: #since for loop does not run if its 0
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y) #this is the very first segment

    move()

    #check for collision with segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            for segment in segments:
                segment.goto(1000,1000) #turtle module does not have a delete function for
            #clear segments list
            segments.clear()
            delay = 0.1
            score = 0
            pen.clear() #clears previously written by pen
            pen.write(f'Score: {score}  High Score: {high_score}', align = 'center', font = ('Corbel',24,'normal'))

    time.sleep(delay) #delays the program from moving almost instantenously 

wn.mainloop() #keeps window open by placing all our code above this
