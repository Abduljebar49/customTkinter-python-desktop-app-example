import tkinter as tk
from tkinter import ttk
import os

xz=[]
lo=[]
sa=[]

def if_is():
    for aw in xz:
        qw=[]
        if aw['class'] == '11S':
            r= "C:\\Users\\Admin.WASENTER\\Desktop\\python"
            qw.append(r)
            print('correct')
        elif aw['class'] == '11N':
            t="C:\\Users\\Admin.WASENTER\\Desktop\\python"
            qw.append(t)
            print('correct')
        elif aw['class'] == '12S':
            m="C:\\Users\\Admin.WASENTER\\Desktop\\python"
            qw.append(m)
            print('correct')
        elif aw['class'] == '12N':
            ty="C:\\Users\\Admin.WASENTER\\Desktop\\python"
            qw.append(ty)
            print('correct')
        else:
            print('error')
        lo.append(qw)


        # label_login.config(text="Id number is not correct..", fg="red")
        # label_logi.config(text="NO Folder Has This Name .", fg="red")

def readd():
    directory = "C:\\Users\\Admin.WASENTER\\Desktop\\python"
    filename = "userdata.txt"
    file_path = os.path.join(directory, filename)
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                sa.append(line)
                print(line.strip())
        file.close()
    else:
        print("User information file not found.")      



def showin():
    ide = d.get()
    clas = class_b.get()
    aw={'id':ide,'class':clas}
    xz.append(aw)

    class_b.delete(0, tk.END)
    id_entry.delete(0, tk.END)

    h.destroy()
    class_b.destroy()
    id_entry.destroy()
    c.destroy()
    i.destroy()
    bo.destroy()

    def display_results():
        result_text.delete(1.0, tk.END)
    
        result_text.insert(tk.END, sa)
            
    result_text = tk.Text(width=65, height=15)
    result_text.place(x=0, y=60)
    
    by= tk.Label(text="Result table", font="ar 15 bold",  width="500", height="2", bg="#0000FF", fg="#ADD8E6" )
    by.pack()

    display_b = tk.Button(root,text="Display",command=display_results,width="30",height='2',bg="#36454F",fg='#E5E4E2')
    display_b.place(x=150,y=310)

    display_f = tk.Button(root,text="find",command=if_is,width="30",height='2',bg="#36454F",fg='#E5E4E2')
    display_f.place(x=150,y=360)

    display_r = tk.Button(root,text="read",command=readd,width="30",height='2',bg="#36454F",fg='#E5E4E2')
    display_r.place(x=150,y=410)

root = tk.Tk()

root.geometry("500x700")

root.title("Student info")

root.configure(bg="#00004F")

h=tk.Label(text="Students Info", font="ar 15 bold",bg="#0000FF", fg="#ADD8E6", width="500", height="3" )
h.pack()


sw = tk.StringVar()


kuta=['11N','11S','12N','12S']
class_b=ttk.Combobox(root, values=kuta,width=27,textvariable=sw)
class_b.place(x=160 , y=190)

d = tk.IntVar()
c = tk.Label(text="Select Your Class",fg='#ADD8E6',bg='#00004F')
i = tk.Label(text="Id Number",fg='#ADD8E6',bg='#00004F')
i.place(x=220,y=220)
c.place(x=205,y=160)
id_entry = tk.Entry(textvariable=d,width="30")
id_entry.place(x=160,y=250)

bo = tk.Button(root,text="Show me the info",command=showin,width="20",height='2',bg="#36454F",fg='#E5E4E2')
bo.place(x=177,y=290)

da =id_entry.get() 

ca = class_b.get()

frame_login = tk.Frame(root)

label_login = tk.Label(frame_login, text="", fg="red")
label_login.place(x=180,y=340)
frame_login.place(x=180,y=390)

root.mainloop()