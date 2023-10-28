import tkinter as tk
from tkinter import ttk
import numpy as np
from scipy.stats import rankdata
from tkinter import* 
from tkinter import filedialog 
import os

students = []


def calculate_sub ():
    for student in students:
        total = sum(student['Results'])
        average = total / len(student['Results'])
        student['total'] = total
        student['average'] = average
        rankings = len({student['average']}) - rankdata({student['average']}).astype(int) + 1
        student['rank'] = rankings

def savefile():
    directory = "C:\\Users\\Admin.WASENTER\\Desktop\\python"
    filename = "userdata.txt"
    file_path = os.path.join(directory, filename)
    
    with open(file_path, 'w') as file:
        for student in students:
            file.write(f"Name: {student['name']}\n")
            file.write(f"Class: {student['class']}\n")
            file.write(f"ID: {student['ID']}\n")
            for i, subject in enumerate(student['Subject']):
                file.write(f"{subject}: {student['Results'][i]}\n")
            file.write(f"Total: {student['total']}\n")
            file.write(f"Average: {student['average']}\n")
            file.write(f"Rank: {student['rank']}\n\n")
        file.close()
def add_student():
    name = na.get()
    class_ = class_b.get()
    idn = d.get()
    results = [int(x) for x in it_entry.get().split(',')]

    Subject = ['IT','GEO','PY','ENG','MATH','BIO','HIS','CHEM','ECO','CIV']

    student = {
        'name': name,
        'class': class_,
        'ID': idn,
        'Subject': Subject,
        'Results': results,
        'total': 0,
        'average': 0,
        'rank': 0
    }
    students.append(student)
    name_entry.delete(0, tk.END)
    class_b.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    it_entry.delete(0, tk.END)
    



def show_info():
    h.destroy()
    n.destroy()
    c.destroy()
    i.destroy()
    geo.destroy()
    class_b.destroy()
    name_entry.destroy()
    id_entry.destroy()
    it_entry.destroy()
    bo.destroy()
    bos.destroy()

    def display_results():
        result_text.delete(1.0, tk.END)
        for student in students:
            result_text.insert(tk.END, f"Name: {student['name']}\n")
            result_text.insert(tk.END, f"Class: {student['class']}\n")
            result_text.insert(tk.END, f"ID: {student['ID']}\n")
            for i, subject in enumerate(student['Subject']):
                result_text.insert(tk.END, f"{subject}: {student['Results'][i]}\n")
            result_text.insert(tk.END, f"Total: {student['total']}\n")
            result_text.insert(tk.END, f"Average: {student['average']}\n")            
            result_text.insert(tk.END, f"Rank: {student['rank']} \n\n")


    by= tk.Label(text="Resalt table", font="ar 15 bold",  width="500", height="2", bg="#0000FF", fg="#ADD8E6" )
    by.pack()

    result_text = tk.Text(width=85, height=15,bg='#0C090A',fg='#E5E4E2')
    result_text.place(x=8, y=60)


    calculate_b = tk.Button(root,text="Culculate",command=calculate_sub,width="20",height='2',bg="#36454F",fg='#E5E4E2')
    calculate_b.place(x=10,y=310)

    display_b = tk.Button(root,text="Display",command=display_results,width="30",height='2',bg="#36454F",fg='#E5E4E2')
    display_b.place(x=180,y=310)

    calculate_s = tk.Button(root,text="Save",command=savefile,width="10",height='2',bg="#36454F",fg='#E5E4E2')
    calculate_s.place(x=610,y=310)

root = tk.Tk()
root.geometry("700x400")
root.title("Student info")
root.configure(bg="#00004F")

h=tk.Label(text="Students Info", font="ar 15 bold", bg="#0000FF", fg="#ADD8E6", width="500", height="3" )
h.pack()

n = tk.Label(text="Name :",fg='#ADD8E6',bg='#00004F')
c = tk.Label(text="Class :",fg='#ADD8E6',bg='#00004F')
i = tk.Label(text="Id Number :",fg='#ADD8E6',bg='#00004F')
geo = tk.Label(text="IT, GEO, PY, ENG, MATH, BIO, HIS, CHEM, ECO, CIV",fg='#ADD8E6',bg='#00004F')

c.place(x=10,y=160)
n.place(x=10,y=110)
i.place(x=10,y=210)
geo.place(x=375,y=110)

kuta=['9A','9B','10A','10B','11N','11S','12N','12S']
class_b=ttk.Combobox(root, values=kuta,width=27)
class_b.place(x=90 , y=160)

na = tk.StringVar()
d = tk.IntVar()


name_entry = tk.Entry(textvariable=na,width="30")
id_entry = tk.Entry(textvariable=d,width="30")
it_entry = tk.Entry(width="45")


name_entry.place(x=90,y=110)
id_entry.place(x=90,y=210)
it_entry.place(x=375,y=160)


bo = tk.Button(root,text="submit data",command=add_student,width="20",height='2',bg="#36454F",fg='#E5E4E2')
bo.place(x=500,y=200)

bos = tk.Button(root,text="Show resalt",command=show_info,width="0",height='2',bg="#36454F",fg='#E5E4E2')
bos.place(x=375,y=200)



root.mainloop()