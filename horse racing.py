from tkinter import *
import time
import random

winner = False
black_horse_x = 0
black_horse_y = 20

brown_horse_x = -28
brown_horse_y = 110

def start_game():
    global black_horse_x
    global brown_horse_x
    global winner

    while winner == False:
        time.sleep(0.05)
        random_move_black_horse = random.randint(0,20)
        random_move_brown_horse = random.randint(0,20)

        #Update the x positions of both horses
        black_horse_x += random_move_black_horse
        brown_horse_x += random_move_brown_horse

        move_horses(random_move_black_horse,random_move_brown_horse)
        main_screen.update()
        winner = check_winner()

    if winner == "Tie":
        Label(main_screen,text=winner,font=('calibri',20),fg="green").place(x=200,y=450)
    else:
        Label(main_screen,text=winner+" Wins!",font=('calibri bold',20),fg="green").place(x=200,y=450)

def move_horses(black_horse_random_move,brown_horse_random_move):
    canvas.move(black_horse,black_horse_random_move,0)
    canvas.move(brown_horse,brown_horse_random_move,0)

def check_winner():
    if black_horse_x >= 550 and brown_horse_x >= 550:
        return "Tie"
    if black_horse_x >= 550:
        return "Black Horse"
    if brown_horse_x >= 550:
        return "Brown Horse"
    return False

#setting up the main screen
main_screen = Tk()
main_screen.title("Horse Racing")
main_screen.geometry('600x500')
main_screen.config(background='white')

#Setting up the Canvas
canvas = Canvas(main_screen,width=600,height=200,bg="white")
canvas.pack(pady=20)

#Import the images 
black_horse_img = PhotoImage(file="./images/black-horse.png")
brown_horse_img = PhotoImage(file="./images/brown-horse.png")

#Resizing the images
black_horse_img = black_horse_img.zoom(3)
black_horse_img = black_horse_img.subsample(40)
brown_horse_img = brown_horse_img.zoom(6)
brown_horse_img = brown_horse_img.subsample(50)

#Adding images to the canvas
black_horse = canvas.create_image(black_horse_x,black_horse_y,anchor=NW,image=black_horse_img)
brown_horse = canvas.create_image(brown_horse_x,brown_horse_y,anchor=NW,image=brown_horse_img)

#Adding labels to the screen
l1 = Label(main_screen,text="Select your horse",font=('calibri bold',16),bg="white")
l1.place(x=230,y=280)
l2 = Label(main_screen,text="Please click play when ready!",font=("calibri",16),bg="white")
l2.place(x=200,y=330)

b1 = Button(main_screen,text='Play!',height=2,width=14,bg='white',font=('calibri',10),command=start_game)
b1.place(x=250,y=390)

main_screen.mainloop()

