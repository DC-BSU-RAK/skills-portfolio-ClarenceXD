import tkinter as tk
import random
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

# Design
main = tk.Tk()
main.title("Math Quiz")
main.geometry("900x700")
main.resizable(False, False)
font_design_guide = ("Comic Sans MS", 12)
font_design_button = ("Comic Sans MS", 16)
font_design_entry = ("Comic Sans MS", 24)
font_design_label = ("Comic Sans MS", 32)


# Variables
questions_list = [] 
current_question = 0
user_tries = False
user_score = []

# Creates 5 frames/windows. I got help from the following links slide 108 - 112: https://docs.google.com/presentation/d/1ISu5TAaBbKspkNDV0S8Db4DPYMZP_MqtBwTxrgkddb4/edit?slide=id.g38bcb64a7d3_1_60#slide=id.g38bcb64a7d3_1_60
menu_frame = Frame(main)
menu_frame.place(x=0,y=0,width=900,height=700)
difficulty_frame = Frame(main)
difficulty_frame.place(x=0,y=0,width=900,height=700)
instruction_frame = Frame(main)
instruction_frame.place(x=0,y=0,width=900,height=700)
quiz_frame = Frame(main)
quiz_frame.place(x=0,y=0,width=900,height=700)
scoreboard_frame = Frame(main)
scoreboard_frame.place(x=0,y=0,width=900,height=700)

# background code
board_bg = Image.open("Assessment 1 - Skills Portfolio/Exercise 1 - Maths Quiz/assets/start_bg.png")
resized_bg = board_bg.resize((900, 700)) 
board_bg = ImageTk.PhotoImage(resized_bg)

start_bg = Image.open("Assessment 1 - Skills Portfolio/Exercise 1 - Maths Quiz/assets/Resized_image_table.png")
resized_bg = start_bg.resize((900, 700)) 
start_bg = ImageTk.PhotoImage(resized_bg)


def guide_menu():                     #help from and so on : https://www.youtube.com/watch?v=3yeRcxkth0I
    instruction_frame.tkraise()

    canvas = Canvas(instruction_frame, width=900, height=700)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=board_bg, anchor="nw")
    canvas.create_text(450, 125, text="Instructions", font=font_design_label, fill="white")
    canvas.create_text(
    450, 300,
    text="General Rules:\n- Only Addition (+) and Subtraction (-) questions.\n- You have 1 extra chance for each question if your first answer is wrong.\n\nDifficulty Levels:\nEasy: Numbers 1-9 (1-digit)\nModerate: Numbers 10-99 (2-digit)\nAdvanced: Numbers 1000-9999 (4-digit)\n\n",
    font=font_design_guide, fill="white", justify="left",)

    back = Button(instruction_frame,text="Back", width=15,height=3,font=font_design_button,bg="light gray", command=displaymenu)
    back.place(x=150, y=600, anchor="center")
    

def displaymenu():
    menu_frame.tkraise()

    canvas_menu = Canvas(menu_frame, width=900, height=700)
    canvas_menu.pack(fill="both", expand=True)
    canvas_menu.create_image(0, 0, image=start_bg, anchor="nw")
    canvas_menu.create_text(450, 125, text="Math Quiz", font=font_design_label, fill="black")


    Start = Button(menu_frame,text="Start", width=15,height=3,font=font_design_button,command=pick_difficulty_menu)
    Start.place(x=450, y=280, anchor="center")
    
    Instruction = Button(menu_frame,text="Instructions", width=15,height=3,font=font_design_button,command=guide_menu)
    Instruction.place(x=450, y=400, anchor="center")
    
    Quit = Button(menu_frame,text="Quit", width=15,height=3,font=font_design_button,command=main.destroy)
    Quit.place(x=450, y=520, anchor="center")

def pick_difficulty_menu():
    difficulty_frame.tkraise()

    canvas_menu = Canvas(difficulty_frame, width=900, height=700)
    canvas_menu.pack(fill="both", expand=True)
    canvas_menu.create_image(0, 0, image=start_bg, anchor="nw")
    canvas_menu.create_text(450, 125, text="Pick The Difficulty", font=font_design_label, fill="black")

    Easy = Button(difficulty_frame,text="Easy", width=15,height=3,font=font_design_button,bg="green",command= lambda:[gen_list(1,9), Quiz_time_menu()])
    Easy.place(x=450, y=280, anchor="center")

    Moderate = Button(difficulty_frame,text="Moderate", width=15,height=3,font=font_design_button,bg="yellow",command= lambda:[gen_list(10,99), Quiz_time_menu()])
    Moderate.place(x=450, y=400, anchor="center")

    Advanced = Button(difficulty_frame,text="Advanced", width=15,height=3,font=font_design_button,bg="red",command= lambda:[gen_list(1000,9999), Quiz_time_menu()])
    Advanced.place(x=450, y=520, anchor="center")

    back = Button(difficulty_frame,text="Back", width=15,height=3,font=font_design_button,bg="light gray",command=displaymenu)
    back.place(x=150, y=600, anchor="center")

# ANSWER. used https://www.geeksforgeeks.org/python/one-liner-for-python-if-elif-else-statements/
def calculate(first_num, second_num, operation):
    answer = (first_num + second_num) if operation == ("+") else (first_num - second_num)
    return answer

def decide_operation():
    return random.choice(["+","-"])

def random_int(min,max):            #creates a random int in range of min - max
    A1 = random.randint(min,max)
    B1 = random.randint(min,max)
    return A1, B1

def question_gen(min,max):  # creates questions stored in a dic format
    A1, B1 = random_int(min,max)
    operation = decide_operation() 
    answer = calculate(A1, B1, operation)
    question = {
        "first": A1,
        "second":B1,
        "ans": answer,
        "operation":operation
    }
    return question

# Creates 10 questions placed inside a list
def gen_list(l_min,l_max):     #Easy = 1-9   Moderate = 10-99   Advance = 1000-9999
    questions_list.clear()
    for a in range(10):
        i = question_gen(l_min,l_max)
        questions_list.append(i)


def Quiz_time_menu():
    quiz_frame.tkraise()
    global question , user_input , canvas_quiz
    


    canvas_quiz = Canvas(quiz_frame, width=900, height=700)
    canvas_quiz.pack(fill="both", expand=True)
    canvas_quiz.create_image(0, 0, image=board_bg, anchor="nw")
    canvas_quiz.create_text(450, 125, text="Quiz Time", font=font_design_label, fill="white")

    question =  canvas_quiz.create_text(450, 225, text="2 + 4 = fish", font=font_design_entry, fill="white")

    user_input = Entry(quiz_frame,font=("Arial", 18))
    user_input.place(x=450, y=280, anchor="center")

    Next = Button(quiz_frame,text="Next", width=12,height=2,font=font_design_button,bg="#CC8B51",fg="white",command=check_answer)
    Next.place(x=450, y=470, anchor="center")
    
    show_next_question()

def show_next_question():
    canvas_quiz.itemconfig(question, text=f'{current_question + 1}) {questions_list[current_question]["first"]} {questions_list[current_question]["operation"]} {questions_list[current_question]["second"]} = ?') #https://iqcode.com/code/python/how-to-change-text-in-a-canvas-tkinter
    user_input.delete('0', END) # deletes/clears entry https://stackoverflow.com/questions/27966626/how-to-clear-delete-the-contents-of-a-tkinter-text-widget

def check_answer():
    global user_tries , user_score
    # use try to check if user input str
    try:
        user_answer = int(user_input.get())
    except ValueError:
        messagebox.showwarning("Warning","Please Enter A Whole Number")
        return
    
    if user_tries == True and user_answer == questions_list[current_question]["ans"]:
        user_tries = False
        user_score.append(5)
        next_question() 
    elif user_answer == questions_list[current_question]["ans"]:
        user_tries = False
        user_score.append(10)
        next_question() 
    elif user_tries == False:
        user_tries = True
        messagebox.showwarning("Response","You are given 1 more chance")
    else:
        user_tries = False
        messagebox.showwarning("Response","Moving to the next question")
        next_question()

def next_question():
    global current_question
    current_question += 1
    show_next_question() if current_question <len(questions_list) else scoreboard() # show next question if current questions is less then total


def ending():
    total = sum(user_score)
    if total > 90:
        rank = "A+"
    elif total > 85:
        rank = "A"
    elif total > 80:
        rank = "B+"
    elif total > 75:
        rank = "B"
    elif total > 65:
        rank = "C"
    elif total > 40:
        rank = "D"
    else:
        rank = "F"
    return total , rank

def scoreboard():   #displays score/results
    global canvas_score
    scoreboard_frame.tkraise()
    total, rank = ending()
    
    canvas_score = Canvas(scoreboard_frame, width=900, height=700)
    canvas_score.pack(fill="both", expand=True)
    canvas_score.create_image(0, 0, image=board_bg, anchor="nw")
    canvas_score.create_text(450, 125, text="Score Board", font=font_design_label, fill="white")

    canvas_score.create_text(450, 175, text=f"Your Total Score: {total}/100",font=font_design_entry, fill="white")
    canvas_score.create_text(450, 255, text=f"Your Rank is {rank}",font=font_design_entry, fill="white")

    Next = Button(scoreboard_frame,text="Play Again", width=12,height=2,font=font_design_button,bg="#CC8B51",fg="white",command=lambda:[restart_variables(),displaymenu()])
    Next.place(x=450, y=470, anchor="center")

def restart_variables():
    global user_score, user_tries , current_question
    canvas_quiz.destroy()
    canvas_score.destroy()
    user_score = []
    user_tries = False
    current_question = 0    

displaymenu()
main.mainloop()


# useful links
# lambda button run 2 functions https://www.tutorialspoint.com/running-multiple-commands-when-a-button-is-pressed-in-tkinter
# helped with image https://www.geeksforgeeks.org/python/how-to-use-images-as-backgrounds-in-tkinter/

