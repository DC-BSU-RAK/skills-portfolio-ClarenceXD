import PIL.ImageTk
import random
import tkinter as tk
import pygame
from tkinter import *

# Design
main = tk.Tk()
main.title("Alexa Tell me a Joke")
main.geometry("900x700")
main.resizable(False, False)
main.iconbitmap("Assessment 1 - Skills Portfolio/Exercise 2 - Alexa tell me a Joke/Resources/laugh.ico")

start_frame = Frame(main)
start_frame.place(x=0,y=0,width=900,height=700)
joke_frame = Frame(main)
joke_frame.place(x=0,y=0,width=900,height=700)


fonts = ("Comic Sans MS",16)
fonts_button = ("Comic Sans MS",12)
pygame.mixer.init()

# https://stackoverflow.com/questions/10748822/img-image-openfp-attributeerror-class-image-has-no-attribute-open
menu_bg = PIL.Image.open("Assessment 1 - Skills Portfolio/Exercise 2 - Alexa tell me a Joke/Resources/Menu.png")
m_menu_bg = PIL.ImageTk.PhotoImage(menu_bg)

joke_bg = PIL.Image.open("Assessment 1 - Skills Portfolio/Exercise 2 - Alexa tell me a Joke/Resources/joke.png")
m_joke_bg = PIL.ImageTk.PhotoImage(joke_bg)



def start_screen():
    start_frame.tkraise()

    bg_start = Label(start_frame, image=m_menu_bg)
    bg_start.place(x=0, y=0, width=900, height=700)

    start = Button(start_frame,text="Alexa tell me a Joke",font=fonts,bg="white",command= lambda:[joke_screen(),next_joke()])
    start.place(anchor=N,x=650,y=150)

list_joke = []
with open ('Assessment 1 - Skills Portfolio/Exercise 2 - Alexa tell me a Joke/randomJokes.txt', 'rt') as myfile:  # Open lorem.txt for reading text
    for i in range(37):
        contents = myfile.readline()              # Read the entire file to a string
        x = contents.strip("\n")        
        list_joke.append(x)
myfile.close()

def show_joke_punch():
    punch.config(text=f"You: {rng[1]}")

    # https://pythonprogramming.net/adding-sounds-music-pygame/
    pygame.mixer.music.load('Assessment 1 - Skills Portfolio/Exercise 2 - Alexa tell me a Joke/Resources/sitcom-laughing-1.mp3')
    pygame.mixer.music.play(0)

def next_joke():
    global rng

    rng = random.choice(list_joke).split('?') #The Following links helped https://java2blog.com/print-string-till-character-python/ https://www.w3schools.com/python/ref_random_choices.asp 
    joke.config(text=f"Alexa: {rng[0]}?")
    punch.config(text=f"You: ????")

def joke_screen():
    global joke,punch
    joke_frame.tkraise()

    bg_j = Label(joke_frame, image=m_joke_bg)
    bg_j.place(x=0, y=0, width=900, height=700)

    joke = Label(joke_frame,text="",font=fonts,wraplength=250,bg="white")
    joke.place(anchor=N,x=225,y=125)

    punch = Label(joke_frame,text="",font=fonts,wraplength=250,bg="white")
    punch.place(anchor=N,x=650,y=125)

    next_btn = Button(joke_frame,text="Next",font=fonts_button,command=next_joke)
    next_btn.place(anchor=N,x=450-75,y=400)    

    show_punch = Button(joke_frame,text="Whats the punch line?",font=fonts_button,command=show_joke_punch)
    show_punch.place(anchor=N,x=450+75,y=400)    

    quit = Button(joke_frame,text="Quit",font=fonts_button,command=main.destroy)
    quit.place(anchor=NW,x=0,y=0)

start_screen()
main.mainloop()