import tkinter
from tkinter import *

def save_info ():

    ab=na.get()

    ac=cl.get()

    ad=d.get()

    ae=itt.get()

    af=ge.get()

    ag=p.get()

    ah=en.get()

    ai=ma.get()

    al=bi.get()

    amm=hi.get()

    an=ch.get()

    ao=ec.get()

    ap=ci.get()

    file = open("Student info" ,"w")

    file.write("Student name :"+ ab)

    file.write("  Class :"+ac)

    file.write("  ID number :"+str(ad))

    file.write("  IT :"+str(ae))

    file.write("  GEO :"+str(af))

    file.write("  PHY :"+str(ag))

    file.write("  ENG :"+str(ah))

    file.write("  MATH :"+str(ai))

    file.write("  BIO :"+str(al))

    file.write("  HIS :"+str(amm))

    file.write("  CHEM :"+str(an))

    file.write("  ECO :"+str(ao))

    file.write("  CIV :"+str(ap))

    file.write("  Total :"+str(total))

    file.write("  Average :"+str(ave))
    
    file.close()

    v=(ae + af + ag + ah + ai + al + amm + an + ao + ap)

    print(ab, ac, ad, ae, af, ag, ah, ai, al , amm, an , ao ,ap )

    return save_info

def total():
    ad=d.get()

    ae=itt.get()

    af=ge.get()

    ag=p.get()

    ah=en.get()

    ai=ma.get()

    al=bi.get()

    amm=hi.get()

    an=ch.get()

    ao=ec.get()

    ap=ci.get()

    u=(ae + af + ag + ah + ai + al + amm + an + ao + ap)

    print(u)

    return total

def average(numbers):
    average = total / len(numbers)
    return average
ave = average

print(ave)

root = Tk()

root.geometry("700x900")

root.title("Student info")

root.configure(bg="#FFFACD")

h=Label(text="Students Info", font="ar 15 bold", bg="#B22222", fg="#F0F8FF", width="500", height="3" )

h.pack()

n = Label(text="Name :")

c = Label(text="Class :")

i = Label(text="Id Number :")

geo = Label(text="Geo :")

it = Label(text="It :")

py = Label(text="Py :")

eng = Label(text="Eng :")

math = Label(text="Math :")

bio = Label(text="Bio :")

his = Label(text="His :")

chem = Label(text="Chem :")

civ = Label(text="Civc :")

eco = Label(text="Eco :")


c.place(x=10,y=260)
n.place(x=10,y=210)

i.place(x=10,y=310)

geo.place(x=400,y=210)

it.place(x=550,y=210)

py.place(x=550,y=260)

eng.place(x=400,y=260)

math.place(x=400,y=310)

bio.place(x=550,y=360)

his.place(x=550,y=310)

chem.place(x=400,y=360)

eco.place(x=550,y=410)

civ.place(x=400,y=410)

na = StringVar()

cl = StringVar()

d = IntVar()

itt = IntVar()

ge = IntVar()

p = IntVar()

en = IntVar()

ma = IntVar()

bi = IntVar()

hi = IntVar()

ch = IntVar()

ec = IntVar()

ci =  IntVar()

nm = Entry(textvariable=na,width="30")

cla = Entry(textvariable=cl,width="30")

di = Entry(textvariable=d,width="30")

ti = Entry(textvariable=itt,width="10")

eg = Entry(textvariable=ge,width="10")

yp = Entry(textvariable=p,width="10")

neg = Entry(textvariable=en,width="10")

am = Entry(textvariable=ma,width="10")

ib = Entry(textvariable=bi,width="10")

ih = Entry(textvariable=hi,width="10")

hc = Entry(textvariable=ch,width="10")

ce = Entry(textvariable=ec,width="10")

ic = Entry(textvariable=ci,width="10")

nm.place(x=90,y=210)

cla.place(x=90,y=260)

di.place(x=90,y=310)

ti.place(x=600,y=210)

eg.place(x=450,y=210)

yp.place(x=450,y=260)

neg.place(x=600,y=260)

am.place(x=450,y=310)

ib.place(x=600,y=360)

ih.place(x=600,y=310)

hc.place(x=450,y=360)

ce.place(x=600,y=410)

ic.place(x=450,y=410)

bo = Button(root,text="submit data",command=save_info,width="30",height='2',bg="grey")

bo.place(x=420,y=470)

root.mainloop()