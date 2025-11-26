from tkinter import * 
from tkinter import ttk
from tkinter import messagebox

# Design
main = Tk()
main.title("Student Manager")
main.geometry("1200x600")
main.resizable(False, False)
main.iconbitmap("Assessment 1 - Skills Portfolio/Exercise 3 - Student Manager/resources/BSU ico.ico")

manager = ttk.Notebook(main)

style = ttk.Style(main)
style.configure('TNotebook.Tab', width=5555)
style.theme_use('clam')

student_list_tk = Frame(main,bg="white")
student_add_tk = Frame(main,bg="white")
student_high_tk = Frame(main,bg="white")
student_low_tk = Frame(main,bg="white")

manager.add(student_list_tk,text="Student Record")
manager.add(student_add_tk,text="Student Add")
manager.add(student_high_tk,text="Student Highest")
manager.add(student_low_tk,text="Student Lowest")


# Variables
lists = []
student_list = []
fonts_title = ("Comic Sans MS",18)
fonts_entry = ("Comic Sans MS",12)
fonts_label = ("Comic Sans MS",10)
fonts_add = ("Comic Sans MS",14)
# https://stackoverflow.com/questions/3277503/how-to-read-a-file-line-by-line-into-a-list

def open_file():
    global lists
    lists=[]
    with open('Assessment 1 - Skills Portfolio/Exercise 3 - Student Manager/resources/studentMarks.txt', 'rt') as txt:
        next(txt)
        for line in txt:
            lists.append(line.rstrip())   

# overall cal
def overall_marks(m1,m2,m3,e1):
    total = int(m1) + int(m2) + int(m3) + int(e1)
    overall = (total/160) * 100
    return overall
def get_total(m1,m2,m3):
    return int(m1) + int(m2) +int(m3)

def update_list():
    global student_list
    student_list = []
    open_file()
    # adds each student into a dic then into a list
    for x in lists:
        student_dic = {
            "code": str(x).split(",")[0],
            "name": str(x).split(",")[1],
            "c_mark1": str(x).split(",")[2],
            "c_mark2": str(x).split(",")[3],
            "c_mark3": str(x).split(",")[4],
            "e_mark": str(x).split(",")[5],
            "total": "",
            "overall": "",
            "grade":"",
        }

        student_list.append(student_dic)
    # adds overall to each student
    for i in student_list:
        i["overall"] = overall_marks(i["c_mark1"],i["c_mark2"],i["c_mark3"],i["e_mark"])

    for y in student_list:
        y["total"] = get_total(y["c_mark1"],y["c_mark2"],y["c_mark3"])

    for x in student_list:
        if x["overall"] >= 70:
            x["grade"] = "A"

        elif x["overall"] >= 60:
            x["grade"] = "B"

        elif x["overall"] >= 50:
            x["grade"] = "C"

        elif x["overall"] >= 40:
            x["grade"] = "D"

        else:
            x["grade"] = "F"

update_list()
#Student Record
heading_rec = Label(student_list_tk,text="Student Record",bg="white",font=fonts_title)
heading_rec.place(anchor=N,x=600,y=0)

search_label = Label(student_list_tk,bg="white",font=fonts_label,text="Search By Code:")
search_label.place(anchor=N,x=840+50,y=30)

search = Entry(student_list_tk,bg="white",font=fonts_entry)
search.place(anchor=N,x=1000+50,y=30)

search_btn = Button(student_list_tk,text="🔍",font=("Comic Sans MS",8),command=lambda: one_student())
search_btn.place(anchor=N,x=1100+50,y=30)

asc = Button(student_list_tk,font=("Comic Sans Ms",8),text="Ascending",command=lambda: load_table(True))
asc.place(anchor=NW,x=230,y=65)

dsc = Button(student_list_tk,font=("Comic Sans Ms",8),text="Descending",command=lambda: load_table(False))
dsc.place(anchor=NW,x=145,y=65)

display_table = Button(student_list_tk,font=("Comic Sans Ms",8),text="Reload Table",command=lambda: load_table(False))
display_table.place(anchor=NW,x=1087,y=65)

delete_table_btn = Button(student_list_tk,text="Delete Selected",font=("Comic Sans MS",8),command=lambda: delete())
delete_table_btn.place(anchor=NW,x=35,y=65)

edit_student_btn = Button(student_list_tk,text="Edit Selected",font=("Comic Sans MS",8),command=lambda: edit())
edit_student_btn.place(anchor=NW,x=310,y=65)

table_list = ttk.Treeview(student_list_tk, column=("code", "name","Mark1","Mark2","Mark3","total","Exam1","Overall","Grade"), show='headings', height=20)


student_count_display = Label(student_list_tk,text="Student Count: x",bg="white",font=fonts_label)

student_count_display.place(anchor=NW,x=35,y=530)

# Creates window to edit student info
def edit():
    global stored, c_entry,n_entry,cm1,cm2,cm3,em1
    selection = table_list.selection()[0]
#helped with pop up window https://stackoverflow.com/questions/41946222/how-do-i-create-a-popup-window-in-tkinter
    if selection:
        stored = selection
        pop_window = Toplevel()
        pop_window.title("Update Student")
        pop_window.geometry("500x500")
        # Labels
        code=Label(pop_window,font=fonts_title,text="Code: ").place(anchor=NW,x=35,y=25)
        name=Label(pop_window,font=fonts_title,text="Name: ").place(anchor=NW,x=35,y=75)
        mark1=Label(pop_window,font=fonts_title,text="Coursework Mark 1: ").place(anchor=NW,x=35,y=125)
        mark2=Label(pop_window,font=fonts_title,text="Coursework Mark 2: ").place(anchor=NW,x=35,y=175)
        mark3=Label(pop_window,font=fonts_title,text="Coursework Mark 3: ").place(anchor=NW,x=35,y=225)
        exam1=Label(pop_window,font=fonts_title,text="Exam Mark 1: ").place(anchor=NW,x=35,y=275)
        #Entry
        c_entry =Entry(pop_window,font=fonts_entry)
        c_entry.place(anchor=NW,x=275,y=25)
        n_entry =Entry(pop_window,font=fonts_entry)
        n_entry.place(anchor=NW,x=275,y=75)
        cm1 =Entry(pop_window,font=fonts_entry)
        cm1.place(anchor=NW,x=275,y=125)
        cm2 = Entry(pop_window,font=fonts_entry)
        cm2.place(anchor=NW,x=275,y=175)
        cm3 =Entry(pop_window,font=fonts_entry)
        cm3.place(anchor=NW,x=275,y=225)
        em1 = Entry(pop_window,font=fonts_entry)
        em1.place(anchor=NW,x=275,y=275)

        change_btn=Button(pop_window,font=fonts_entry,text="Update Student Info",command=lambda:edit_one_student())
        change_btn.place(anchor=N,x=250,y=300)


                
    else:
        messagebox.showwarning("Selection Problem", "Please Select a Student")
    
def edit_one_student():
    for x in student_list:
        if x["code"] == stored:
            new_code = c_entry.get()
            new_name = n_entry.get()
            new_mark1 =cm1.get()
            new_mark2 =cm2.get()
            new_mark3 =cm3.get()
            new_exam1 =em1.get()

    for y in student_list:
        if y["code"] == new_code:
            messagebox.showerror("Code Error", "Please Enter A Appropriate Code.")
            return


    with open('Assessment 1 - Skills Portfolio/Exercise 3 - Student Manager/resources/studentMarks.txt', 'r') as txt:
        lines = txt.readlines()

    temp_lines = []

    for x in lines:         #skips first line allows rest
        # store each line skipping the stored code
        if x[:4] != stored:
            temp_lines.append(x.strip("\n"))
    
    updated_info = (f"{new_code},{new_name},{new_mark1},{new_mark2},{new_mark3},{new_exam1}")
    temp_lines.append(updated_info)
    with open('Assessment 1 - Skills Portfolio/Exercise 3 - Student Manager/resources/studentMarks.txt', 'w') as txt:
        txt.write("\n".join(temp_lines))


    load_table(False)

    
    

def delete():
    selected_item = table_list.selection()
    if selected_item:
        yes_or_no = messagebox.askyesno("Delete Student Info", "Are you sure you want to delete this student") 
        if yes_or_no ==True:
            selected_item = table_list.selection()[0]
            remove_student(selected_item)
            table_list.delete(selected_item)
            load_table(False)
    else:
        messagebox.showwarning("Selection Problem", "Please Select a Student")


#rewrites whole txt https://stackoverflow.com/questions/4710067/how-to-delete-a-specific-line-in-a-text-file-using-python
def remove_student(code):
    temp_lines = []

    with open('Assessment 1 - Skills Portfolio/Exercise 3 - Student Manager/resources/studentMarks.txt', 'r') as txt:
        lines = txt.readlines()

    sub_count = int(lines[0]) 
    sub_count -= 1               

    for x in lines[1:]:         #skips first line allows rest
        # store each line skipping the code
        if x[:4] != code:
            temp_lines.append(x.strip("\n"))
    #.join used to add \n in between the list and not the end
    with open('Assessment 1 - Skills Portfolio/Exercise 3 - Student Manager/resources/studentMarks.txt', 'w') as txt:
        txt.write(str(sub_count) + "\n")
        txt.write("\n".join(temp_lines))

# helps with creating table https://www.tutorialspoint.com/delete-and-edit-items-in-tkinter-treeview
def load_table(ascending):

    
    # resets the table information is case of recall
    for x in table_list.get_children():
        table_list.delete(x)

    table_list.column("#1", anchor=CENTER,width=125)
    table_list.heading("#1", text="Code",)
    table_list.column("#2", anchor=CENTER,width=125)
    table_list.heading("#2", text="Name",)
    table_list.column("#3", anchor=CENTER,width=125)
    table_list.heading("#3", text="Mark 1",)
    table_list.column("#4", anchor=CENTER,width=125)
    table_list.heading("#4", text="Mark 2",)
    table_list.column("#5", anchor=CENTER,width=125)
    table_list.heading("#5", text="Mark 3",)

    table_list.column("#6", anchor=CENTER,width=125,)
    table_list.heading("#6", text="Total Marks",)

    table_list.column("#7", anchor=CENTER,width=125)
    table_list.heading("#7", text="Exam 1",)
    table_list.column("#8", anchor=CENTER,width=125)
    table_list.heading("#8", text="Overall",)
    table_list.column("#9", anchor=CENTER,width=125,)
    table_list.heading("#9", text="Grade",)
    update_list() #get newest info

#found during research on sort https://stackoverflow.com/questions/403421/how-do-i-sort-a-list-of-objects-based-on-an-attribute-of-the-objects
    if ascending == True:

        student_list.sort(key=lambda x: x["overall"])
    else:
        student_list.sort(key=lambda x: x["overall"], reverse=True)


    for x in student_list:
        table_list.insert("","end",iid=x["code"],values=(
        x["code"],
        x["name"],
        x["c_mark1"],
        x["c_mark2"],
        x["c_mark3"],
        x["total"],
        x["e_mark"],
        str(x["overall"]) + "%",
        x["grade"]
        ))

    table_list.place(anchor=N,x=600,y=100)

    with open('Assessment 1 - Skills Portfolio/Exercise 3 - Student Manager/resources/studentMarks.txt', 'r') as txt:
        first_line = txt.readline()
    student_count_display.config(text=f"Student Count: {first_line}")



#creates table delete info and adds only needed
def one_student(): #search function
    load_table(True) #updates student_lists
    for x in table_list.get_children():
        table_list.delete(x)
    find = search.get()

    for i in student_list:
        if i["code"] == find:
            table_list.insert("","end",iid=i["code"],values=(
            i["code"],
            i["name"],
            i["c_mark1"],
            i["c_mark2"],
            i["c_mark3"],
            i["total"],
            i["e_mark"],
            str(i["overall"]) + "%",
            i["grade"]
            ))




#Add student to Record
heading_add = Label(student_add_tk,text="Add a Student",bg="white",font=fonts_title)
heading_add.place(anchor=N,x=600,y=0)

# left
heading_code = Label(student_add_tk,font=fonts_add,text="Student Code: ",bg="white")
heading_code.place(anchor=NW,x=450-175,y=50)

code_entry = Entry(student_add_tk,font=fonts_entry,highlightcolor="#1e90ff",highlightthickness=1)
code_entry.place(anchor=NW,x=450-175,y=100)

heading_mark1 = Label(student_add_tk,font=fonts_add,text="Coursework Mark 1: ",bg="white")
heading_mark1.place(anchor=NW,x=450-175,y=150)

mark1_entry = Entry(student_add_tk,font=fonts_entry,highlightcolor="#1e90ff",highlightthickness=1)
mark1_entry.place(anchor=NW,x=450-175,y=200)

heading_mark3 = Label(student_add_tk,font=fonts_add,text="Coursework Mark 3: ",bg="white")
heading_mark3.place(anchor=NW,x=450-175,y=250)

mark3_entry = Entry(student_add_tk,font=fonts_entry,highlightcolor="#1e90ff",highlightthickness=1)
mark3_entry.place(anchor=NW,x=450-175,y=300)

# right

heading_name = Label(student_add_tk,font=fonts_add,text="Name: ",bg="white")
heading_name.place(anchor=NW,x=450+250,y=50)

name_entry = Entry(student_add_tk,font=fonts_entry,highlightcolor="#1e90ff",highlightthickness=1)
name_entry.place(anchor=NW,x=450+250,y=100)

heading_mark2 = Label(student_add_tk,font=fonts_add,text="Coursework Mark 2: ",bg="white")
heading_mark2.place(anchor=NW,x=450+250,y=150)

mark2_entry = Entry(student_add_tk,font=fonts_entry,highlightcolor="#1e90ff",highlightthickness=1)
mark2_entry.place(anchor=NW,x=450+250,y=200)

heading_exam1 = Label(student_add_tk,font=fonts_add,text="Exam Mark 1: ",bg="white")
heading_exam1.place(anchor=NW,x=450+250,y=250)

exam1_entry = Entry(student_add_tk,font=fonts_entry,highlightcolor="#1e90ff",highlightthickness=1)
exam1_entry.place(anchor=NW,x=450+250,y=300)

add_btn = Button(student_add_tk,text="Add to Record",font=("Comic Sans MS",18),command=lambda: add_student())
add_btn.place(anchor=N,x=600,y=400)


manager.pack(expand=1, fill="both",  pady=0)


def add_student():
    update_list()
    #Code Below will be updated to grab values from text boxs on the frame
    code = code_entry.get()
    name = name_entry.get()
    m1 = mark1_entry.get()
    m2 = mark2_entry.get()
    m3 = mark3_entry.get()
    e1 = exam1_entry.get()

    #check 1:https://www.w3schools.com/python/ref_func_all.asp
    checker = [code,name,m1,m2,m3,e1]
    i = all(checker)
    if i == False:
        messagebox.showwarning("Input Error", "Please Enter the Appropriate Information.")
        return
    #check 2: is code already used 
    for x in student_list:
        if code == x["code"]:
            messagebox.showwarning("Duplicate Code", "Student Code already in use. Please retry.")
            return
    # check 3 : is input a number
    try:
        int(code)
        int(m1)
        int(m2)
        int(m3)
        int(e1)
    except ValueError:
        messagebox.showerror("Input Error","Please Enter the Appropriate Informaton.")
        return

    with open('Assessment 1 - Skills Portfolio/Exercise 3 - Student Manager/resources/studentMarks.txt', 'r') as txt:
        lines = txt.readlines()

    sub_count = int(lines[0]) 
    sub_count += 1        

    temp_lines = []

    for x in lines[1:]:       
        
        if x[:4] != code:
            temp_lines.append(x.strip("\n"))
    temp_lines.append(f"{code},{name},{m1},{m2},{m3},{e1}")
    #.join used to add \n in between the list and not the end
    with open('Assessment 1 - Skills Portfolio/Exercise 3 - Student Manager/resources/studentMarks.txt', 'w') as txt:
        txt.write(str(sub_count) + "\n")
        txt.write("\n".join(temp_lines))
    code_entry.delete(0,END)
    name_entry.delete(0,END)
    mark1_entry.delete(0,END)
    mark2_entry.delete(0,END)
    mark3_entry.delete(0,END)
    exam1_entry.delete(0,END)
    load_table(False)

# highest student frame
heading_high = Label(student_high_tk,text="Top Student",bg="white",font=fonts_title)
heading_high.place(anchor=N,x=600,y=0)

high_btn = Button(student_high_tk,text="Display Top Student",font=("Comic Sans MS",18),command=lambda:find_highest())
high_btn.place(anchor=N,x=600,y=400)
    
highest_table = ttk.Treeview(student_high_tk, column=("code", "name","Mark1","Mark2","Mark3","total","Exam1","Overall","Grade"), show='headings', height=6)

# lowest student frame
heading_low = Label(student_low_tk,text="lowest Marked Student",bg="white",font=fonts_title)
heading_low.place(anchor=N,x=600,y=0)

low_btn = Button(student_low_tk,text="Display Lowest Marked Student",font=("Comic Sans MS",18),command=lambda:find_lowest())
low_btn.place(anchor=N,x=600,y=400)
    
lowest_table = ttk.Treeview(student_low_tk, column=("code", "name","Mark1","Mark2","Mark3","total","Exam1","Overall","Grade"), show='headings', height=6)


def find_lowest():
    update_list()
    # resets the table information is case of recall
    for x in lowest_table.get_children():
        lowest_table.delete(x)

    temp_L = []
    for x in student_list:
        temp_L.append(x["overall"]) 
    highest = min(temp_L)


    lowest_table.column("#1", anchor=CENTER,width=125)
    lowest_table.heading("#1", text="Code",)
    lowest_table.column("#2", anchor=CENTER,width=125)
    lowest_table.heading("#2", text="Name",)
    lowest_table.column("#3", anchor=CENTER,width=125)
    lowest_table.heading("#3", text="Mark 1",)
    lowest_table.column("#4", anchor=CENTER,width=125)
    lowest_table.heading("#4", text="Mark 2",)
    lowest_table.column("#5", anchor=CENTER,width=125)
    lowest_table.heading("#5", text="Mark 3",)

    lowest_table.column("#6", anchor=CENTER,width=125)
    lowest_table.heading("#6", text="Total Marks",)

    lowest_table.column("#7", anchor=CENTER,width=125)
    lowest_table.heading("#7", text="Exam 1",)
    lowest_table.column("#8", anchor=CENTER,width=125)
    lowest_table.heading("#8", text="Overall",)
    lowest_table.column("#9", anchor=CENTER,width=125)
    lowest_table.heading("#9", text="Grade",)



    for i in student_list:
        if highest == i["overall"]:
            lowest_table.insert("", "end", values=(
            i["code"],
            i["name"],
            i["c_mark1"],
            i["c_mark2"],
            i["c_mark3"],
            i["total"],
            i["e_mark"],
            str(i["overall"]) + "%",
            i["grade"]
            ))

    lowest_table.place(anchor=N,x=600,y=100)

def find_highest():
    update_list()
    # resets the table information is case of recall
    for x in highest_table.get_children():
        highest_table.delete(x)

    temp_L = []
    for x in student_list:
        temp_L.append(x["overall"]) 
    highest = max(temp_L)


    highest_table.column("#1", anchor=CENTER,width=125)
    highest_table.heading("#1", text="Code",)
    highest_table.column("#2", anchor=CENTER,width=125)
    highest_table.heading("#2", text="Name",)
    highest_table.column("#3", anchor=CENTER,width=125)
    highest_table.heading("#3", text="Mark 1",)
    highest_table.column("#4", anchor=CENTER,width=125)
    highest_table.heading("#4", text="Mark 2",)
    highest_table.column("#5", anchor=CENTER,width=125)
    highest_table.heading("#5", text="Mark 3",)

    highest_table.column("#6", anchor=CENTER,width=125)
    highest_table.heading("#6", text="Total Marks",)

    highest_table.column("#7", anchor=CENTER,width=125)
    highest_table.heading("#7", text="Exam 1",)
    highest_table.column("#8", anchor=CENTER,width=125)
    highest_table.heading("#8", text="Overall",)
    highest_table.column("#9", anchor=CENTER,width=125)
    highest_table.heading("#9", text="Grade",)



    for i in student_list:
        if highest == i["overall"]:
            highest_table.insert("", "end", values=(
            i["code"],
            i["name"],
            i["c_mark1"],
            i["c_mark2"],
            i["c_mark3"],
            i["total"],
            i["e_mark"],
            str(i["overall"]) + "%",
            i["grade"]
            ))

    highest_table.place(anchor=N,x=600,y=100)

load_table(False)

main.mainloop()