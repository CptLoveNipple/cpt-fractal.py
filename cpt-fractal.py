import turtle
import random
import Tkinter as tkinter
import time
from termcolor import colored

print("  ")
print("  ")
print("  ")
print colored("Note: You may close the drawing once it's   ", "red", "on_yellow")
print colored("completed by clicking anywhere on screen.   ", "red", "on_yellow")
time.sleep(5)
print("  ")
print("  ")
print colored("Welcome to the Spirographic Fractal Creator!", "green", "on_yellow")
print colored("                                            ", "blue", "on_yellow")
print colored("                                            ", "blue", "on_yellow")
print colored("Created in:                                 ", "blue", "on_yellow")
print colored("           Python 2.7.12                    ", "blue", "on_yellow")
print colored("           Using the Turtle module!         ", "blue", "on_yellow")
print colored("                                            ", "blue", "on_yellow")
print colored("                                            ", "blue", "on_yellow")
print colored("Created By:                                 ", "blue", "on_yellow")
print colored("           Malcolm B.                       ", "blue", "on_yellow")
print colored("       aka CptLoveNipple                    ", "green", "on_yellow")
print colored("                                            ", "blue", "on_yellow")
print colored("                                            ", "blue", "on_yellow")
print("  ")
print("  ")
time.sleep(5)
print("Simply answer the questions that are presented to   ")
print("you on screen.                                      ")
print("  ")
print("  ")
print("Make sure you input y or n when promted, and also   ")
print("make sure to spell each word correctly!             ")
print("  ")
print("  ")
print("Failure to spell a word correctly will cause things ")
print("to go all fucky. Please don't do that.              ")
print("  ")
print("  ")
time.sleep(7)

print("Random Mode? y/n")
crazy = raw_input()
crazy = str(crazy)
if crazy == 'y' :
    print("Would you like your random selection to be chaotic? y/n")
    chaos = raw_input()
    chaos = str(chaos)
    if chaos == 'y' :

        print("would you like to choose a  base shape? y/n")
        shape_select = raw_input()
        shape_select = str(shape_select)

        if shape_select == 'y':

            hex_side = int(6) #The _side values represent the number of sides
            tri_side = int(3) #that the chosen shape has. (eg. a hexagon has 6)
            oct_side = int(8)
            squ_side = int(4)

            hex_angle = int(120) #The _angle values represent the degree at which
            tri_angle = int(60) #each angle bends.
            oct_angle = int(135)
            squ_angle = int(90)

            print("Would you like a base shape of hexagon, triangle, octogon, or square?")
            my_shape = raw_input()
            my_shape = str(my_shape)

            if my_shape == 'hexagon' :
                side_select = int(hex_side) #The side_ and angle_ values are
                angle_select = int(hex_angle) #chosen here and called during
                                            #the draw of the selected shape.
            if my_shape == 'triangle' :
                side_select = int(tri_side)
                angle_select = int(tri_angle)

            if my_shape == 'octogon' :
                side_select = int(oct_side)
                angle_select = int(oct_angle)

            if my_shape == 'square' :
                side_select = int(squ_side)
                angle_select = int(squ_angle)

            turtle.setup(width = 2200, height = 2200, startx = None, starty = None) #Defines the turtle window size.

            passes_r = random.randint(7,20) #This is the number of times the drawn shape will repeat.
            angle_r1 = random.randint(1,180) #The following angle_ and chaos_ values are randomly
            angle_r2 = random.randint(1,180) #chosen here and called upon during the draw to
            angle_r3 = random.randint(1,180) #randomly create the fractal shape.
            angle_r4 = random.randint(1,180)
            angle_r5 = random.randint(1,180)
            angle_r6 = random.randint(1,180)
            angle_r7 = random.randint(1,180)
            angle_r8 = random.randint(1,180)
            chaos_r1 = random.randint(0,270)
            chaos_r2 = random.randint(0,270)
            chaos_r3 = random.randint(0,270)
            chaos_r4 = random.randint(0,270)
            chaos_r5 = random.randint(0,270)
            chaos_r6 = random.randint(0,270)
            chaos_r7 = random.randint(0,270)
            chaos_r8 = random.randint(0,270)

            shape_r = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
            turtle.shape(random.choice(shape_r)) #All of the _r values I've written dictate
            turtle.speed(0)                      #when the code is drawing random values.
            print("Calculating shape based on random input: ") + str(angle_r1) + ", " + str(angle_r2) + ", " + str(angle_r3) + ", " + str(angle_r4) + ", " + str(angle_r5) + ", " + str(angle_r6) + ", " + str(angle_r7) + ", " + str(angle_r8)
            #The "Calculating" print is showing the user which numbers the system randomly chose as turn angles.
            for _ in range(passes_r): #How many times the fractal will repeat.

                turtle.color('red')
                turtle.left(angle_select)

                for _ in range(side_select): #This range is how the selected shape is propogated.
                    turtle.forward(40)
                    turtle.left(chaos_r1)

                turtle.color('blue')
                turtle.left(angle_select) #By combining the side_ and angle_ values we create the shape selected.

                for _ in range(side_select):
                    turtle.forward(40)
                    turtle.left(chaos_r2)

                turtle.color('green')
                turtle.left(angle_select)

                for _ in range(side_select):
                    turtle.forward(40)
                    turtle.left(chaos_r3)

                turtle.color('yellow')
                turtle.left(angle_select)

                for _ in range(side_select):
                    turtle.forward(40)
                    turtle.left(chaos_r4)

                turtle.left(angle_select)

                for _ in range(side_select):
                    turtle.forward(40)
                    turtle.left(chaos_r5)

                turtle.color('green')
                turtle.left(angle_select)

                for _ in range(side_select):
                    turtle.forward(40)
                    turtle.left(chaos_r6)

                turtle.color('blue')
                turtle.left(angle_select)

                for _ in range(side_select):
                    turtle.forward(40)
                    turtle.left(chaos_r7)

                turtle.color('red')
                turtle.left(angle_select)

                for _ in range(side_select):
                    turtle.forward(40)
                    turtle.left(chaos_r8)

            turtle.hideturtle() #Hides the turtle after the draw so as to not cover the finished design.

        if shape_select == 'n':

            passes_r = random.randint(7,20)
            angle_r1 = random.randint(1,180) #Becuase a base shape is not being chosen
            angle_r2 = random.randint(1,180) #the system uses a completely random
            angle_r3 = random.randint(1,180) #set of values to create "chaotic" fractals.
            angle_r4 = random.randint(1,180)
            angle_r5 = random.randint(1,180)
            angle_r6 = random.randint(1,180)
            angle_r7 = random.randint(1,180)
            angle_r8 = random.randint(1,180)
            chaos_r1 = random.randint(0,270)
            chaos_r2 = random.randint(0,270)
            chaos_r3 = random.randint(0,270)
            chaos_r4 = random.randint(0,270)
            chaos_r5 = random.randint(0,270)
            chaos_r6 = random.randint(0,270)
            chaos_r7 = random.randint(0,270)
            chaos_r8 = random.randint(0,270)

            turtle.setup(width = 2200, height = 2200, startx = None, starty = None)

            shape_r = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
            turtle.shape(random.choice(shape_r))
            turtle.speed(0)

            print("Calculating shape based on random input: ") + str(angle_r1) + ", " + str(angle_r2) + ", " + str(angle_r3) + ", " + str(angle_r4) + ", " + str(angle_r5) + ", " + str(angle_r6) + ", " + str(angle_r7) + ", " + str(angle_r8)

            for _ in range(passes_r):

                turtle.color('red')
                turtle.left(angle_r1)

                for _ in range(4):
                    turtle.forward(50)
                    turtle.left(chaos_r1)

                turtle.color('blue')
                turtle.left(angle_r2)

                for _ in range(4):
                    turtle.forward(50)
                    turtle.left(chaos_r2)

                turtle.color('green')
                turtle.left(angle_r3)

                for _ in range(4):
                    turtle.forward(50)
                    turtle.left(chaos_r3)

                turtle.color('yellow')
                turtle.left(angle_r4)

                for _ in range(4):
                    turtle.forward(50)
                    turtle.left(chaos_r4)

                turtle.left(angle_r5)

                for _ in range(4):
                    turtle.forward(50)
                    turtle.left(chaos_r5)

                turtle.color('green')
                turtle.left(angle_r6)

                for _ in range(4):
                    turtle.forward(50)
                    turtle.left(chaos_r6)

                turtle.color('blue')
                turtle.left(angle_r7)

                for _ in range(4):
                    turtle.forward(50)
                    turtle.left(chaos_r7)

                turtle.color('red')
                turtle.left(angle_r8)

                for _ in range(4):
                    turtle.forward(50)
                    turtle.left(chaos_r8)

            turtle.hideturtle()

    elif chaos == 'n' :
        passes_r = random.randint(4,15)
        angle_r1 = random.randint(1,180) #If the user wants a fractal that is
        angle_r2 = random.randint(1,180) #random but not chaotic, then the
        angle_r3 = random.randint(1,180) #program uses a square as the base shape.
        angle_r4 = random.randint(1,180)
        angle_r5 = random.randint(1,180)
        angle_r6 = random.randint(1,180)
        angle_r7 = random.randint(1,180)
        angle_r8 = random.randint(1,180)

        shape_r = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
        turtle.shape(random.choice(shape_r)) #The program still randomizes the shape of the tutle itself.
        turtle.speed(0)

        print("Calculating shape based on random input: ") + str(angle_r1) + ", " + str(angle_r2) + ", " + str(angle_r3) + ", " + str(angle_r4) + ", " + str(angle_r5) + ", " + str(angle_r6) + ", " + str(angle_r7) + ", " + str(angle_r8)

        for _ in range(passes_r):

            turtle.color('red')
            turtle.left(angle_r1)

            for _ in range(4):
                turtle.forward(100)
                turtle.left(90)

            turtle.color('blue')
            turtle.left(angle_r2)

            for _ in range(4):
                    turtle.forward(100)
                    turtle.left(90)

            turtle.color('green')
            turtle.left(angle_r3)

            for _ in range(4):
                turtle.forward(100)
                turtle.left(90)

            turtle.color('yellow')
            turtle.left(angle_r4)

            for _ in range(4):
                turtle.forward(100)
                turtle.left(90)

            turtle.left(angle_r5)

            for _ in range(4):
                turtle.forward(100)
                turtle.left(90)

            turtle.color('green')
            turtle.left(angle_r6)

            for _ in range(4):
                turtle.forward(100)
                turtle.left(90)

            turtle.color('blue')
            turtle.left(angle_r7)

            for _ in range(4):
                turtle.forward(100)
                turtle.left(90)

            turtle.color('red')
            turtle.left(angle_r8)

            for _ in range(4):
                turtle.forward(100)
                turtle.left(90)

elif crazy == 'n' : #If the user does not want a randomly generated fractal
                    #then they must select all parameters manually.
    print("Enter number of repeats: # between 5 and 20 recommended.")
    passes = raw_input()
    passes = int(passes)

    if passes > 30 :
        print("Please select a number below 30.")
        passes = raw_input()
        passes = int(passes)

    if passes > 30 :
        print colored("Warning! Values higher than 30 may take a long time to process.", "red", "on_yellow")
        time.sleep(7)

    print("Enter Shape: Arrow, Turtle, Circle, Square, Triangle, or Classic")
    shape = raw_input().lower() #The .lower() function allows the user to input
                                #their selection with lowercase or capital letters.
    print("Enter Speed: (# 0 through 10: 0 is the fastest)")
    user_speed = raw_input() #All randomly generated draws use 0 because lower speeds
    user_speed = int(user_speed) #can take a very long time depending on number of passes.

    print("Enter Angle 1 (# between 1 and 180)")
    angle_1 = raw_input() #If the user selected 90 for all angles then the
    angle_1 = int(angle_1) #fractal would use a square shape as it's base.

    print("Enter Angle 2 (# between 1 and 180)")
    angle_2 = raw_input()
    angle_2 = int(angle_2)

    print("Enter Angle 3 (# between 1 and 180)")
    angle_3 = raw_input()
    angle_3 = int(angle_3)

    print("Enter Angle 4 (# between 1 and 180)")
    angle_4 = raw_input()
    angle_4 = int(angle_4)

    print("Enter Angle 5 (# between 1 and 180)")
    angle_5 = raw_input()
    angle_5 = int(angle_5)

    print("Enter Angle 6 (# between 1 and 180)")
    angle_6 = raw_input()
    angle_6 = int(angle_6)

    print("Enter Angle 7 (# between 1 and 180)")
    angle_7 = raw_input()
    angle_7 = int(angle_7)

    print("Enter Angle 8 (# between 1 and 180)")
    angle_8 = raw_input() #The program uses 8 angles because it was originally
    angle_8 = int(angle_8) #based soley on squares and I wanted a bit more variety. May change later.

    print("Turtle auto size y or n?") #Auto size defaults to 1.
    auto_size = raw_input().lower()
    auto_size = str(auto_size)
    if auto_size == 'y' :
        auto_size = str('auto')
        turtle.resizemode(auto_size)
    elif auto_size == 'n' :
        auto_size = str('noresize')
        print("what size? Enter a number from 1 to 10.")
        user_size = raw_input() #I don't personally like anyting but 1, but this
        user_size = int(user_size) #allows the user to have the option. I have had
        turtle.pensize(user_size) #a couple interesting results with higher selections,
                                  #so I do recommended you give them a shot.
    turtle.shape(shape)
    turtle.speed(user_speed)

    print("Calculating shape based on user input: ") + str(angle_1) + ", " + str(angle_2) + ", " + str(angle_3) + ", " + str(angle_4) + ", " + str(angle_5) + ", " + str(angle_6) + ", " + str(angle_7) + ", " + str(angle_8)

    for _ in range(passes):

        turtle.color('red')
        turtle.left(angle_1)

        for _ in range(4):
            turtle.forward(100)
            turtle.left(90)

        turtle.color('blue')
        turtle.left(angle_2)

        for _ in range(4):
            turtle.forward(100)
            turtle.left(90)

        turtle.color('green')
        turtle.left(angle_3)

        for _ in range(4):
            turtle.forward(100)
            turtle.left(90)

        turtle.color('yellow')
        turtle.left(angle_4)

        for _ in range(4):
            turtle.forward(100)
            turtle.left(90)

        turtle.left(angle_5)

        for _ in range(4):
            turtle.forward(100)
            turtle.left(90)

        turtle.color('green')
        turtle.left(angle_6)

        for _ in range(4):
            turtle.forward(100)
            turtle.left(90)

        turtle.color('blue')
        turtle.left(angle_7)

        for _ in range(4):
            turtle.forward(100)
            turtle.left(90)

        turtle.color('red')
        turtle.left(angle_8)

        for _ in range(4):
            turtle.forward(100)
            turtle.left(90)

turtle.hideturtle() #Hides the turtle after the draw so that the drawing is not covered.
turtle.exitonclick() #Program will close when the user clicks.
