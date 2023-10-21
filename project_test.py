import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


def save_info():
    ab = na.get()
    ac = cl.get()
    ad = d.get()
    ae = itt.get()
    af = ge.get()
    ag = p.get()
    ah = en.get()
    ai = ma.get()
    al = bi.get()
    amm = hi.get()
    an = ch.get()
    ao = ec.get()
    ap = ci.get()

    file = open("Student info", "w")
    file.write("Student name :" + ab)
    file.write("  Class :" + ac)
    file.write("  ID number :" + str(ad))
    file.write("  IT :" + str(ae))
    file.write("  GEO :" + str(af))
    file.write("  PHY :" + str(ag))
    file.write("  ENG :" + str(ah))
    file.write("  MATH :" + str(ai))
    file.write("  BIO :" + str(al))
    file.write("  HIS :" + str(amm))
    file.write("  CHEM :" + str(an))
    file.write("  ECO :" + str(ao))
    file.write("  CIV :" + str(ap))
    file.write("  Total :" + str(total))
    file.write("  Average :" + str(ave))
    file.close()

    v = (ae + af + ag + ah + ai + al + amm + an + ao + ap)
    print(ab, ac, ad, ae, af, ag, ah, ai, al, amm, an, ao, ap)

def calculate_total():
    ad = d.get()
    ae = itt.get()
    af = ge.get()
    ag = p.get()
    ah = en.get()
    ai = ma.get()
    al = bi.get()
    amm = hi.get()
    an = ch.get()
    ao = ec.get()
    ap = ci.get()
    u = (ae + af + ag + ah + ai + al + amm + an + ao + ap)
    print(u)

def calculate_average(numbers):
    average = total / len(numbers)
    return average

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

root = Tk()

root.geometry("700x900")
root.title("Student info")
root.configure(bg="#FFFACD")

h = customtkinter.CTkLabel(root, text="Students Info", font="ar 15 bold", bg="#B22222", fg="#F0F8FF", width="500", height="3")
h.pack()

n = customtkinter.CTkLabel(root, text="Name:")
c = customtkinter.CTkLabel(root, text="Class:")
i = customtkinter.CTkLabel(root, text="Id Number:")
geo = customtkinter.CTkLabel(root, text="Geo:")
it = customtkinter.CTkLabel(root, text="It:")
py = customtkinter.CTkLabel(root, text="Py:")
eng = customtkinter.CTkLabel(root, text="Eng:")
math = customtkinter.CTkLabel(root, text="Math:")
bio = customtkinter.CTkLabel(root, text="Bio:")
his = customtkinter.CTkLabel(root, text="His:")
chem = customtkinter.CTkLabel(root, text="Chem:")
civ = customtkinter.CTkLabel(root, text="Civc:")
eco = customtkinter.CTkLabel(root, text="Eco:")

c.grid(row=0, column=0)
n.grid(row=1, column=0)
i.grid(row=2, column=0)
geo.grid(row=1, column=3)
it.grid(row=1, column=4)
py.grid(row=2, column=4)
eng.grid(row=2, column=3)
math.grid(row=2, column=5)
bio.grid(row=3, column=4)
his.grid(row=3, column=5)
chem.grid(row=3, column=3)
eco.grid(row=4, column=4)
civ.grid(row=4, column=3)

na =  customtkinter.CTkStringVar()
cl =  customtkinter.CTkStringVar()
d =   customtkinter.CTkIntVar()
itt = customtkinter.CTkIntVar()
ge =  customtkinter.CTkIntVar()
p =   customtkinter.CTkIntVar()
en =  customtkinter.CTkIntVar()
ma =  customtkinter.CTkIntVar()
bi =  customtkinter.CTkIntVar()
hi =  customtkinter.CTkIntVar()
ch =  customtkinter.CTkIntVar()
ec =  customtkinter.CTkIntVar()
ci =  customtkinter.CTkIntVar()

nm =  customtkinter.CTkEntry(root, textvariable=na, width="30")
cla = customtkinter.CTkEntry(root, textvariable=cl, width="30")
di =  customtkinter.CTkEntry(root, textvariable=d, width="30")
ti =  customtkinter.CTkEntry(root, textvariable=itt, width="10")
eg =  customtkinter.CTkEntry(root, textvariable=ge, width="10")
yp =  customtkinter.CTkEntry(root, textvariable=p, width="10")
neg = customtkinter.CTkEntry(root, textvariable=en, width="10")
am =  customtkinter.CTkEntry(root, textvariable=ma, width="10")
ib =  customtkinter.CTkEntry(root, textvariable=bi, width="10")
ih =  customtkinter.CTkEntry(root, textvariable=hi, width="10")
hc =  customtkinter.CTkEntry(root, textvariable=ch, width="10")
ce =  customtkinter.CTkEntry(root, textvariable=ec, width="10")
ic =  customtkinter.CTkEntry(root, textvariable=ci, width="10")

nm.grid(row=1, column=1)
cla.grid(row=2, column=1)
di.grid(row=3, column=1)
ti.grid(row=1, column=6)
eg.grid(row=1, column=5)
yp.grid(row=2, column=5)
neg.grid(row=2, column=6)
am.grid(row=2, column=7)
ib.grid(row=3, column=7)
ih.grid(row=3, column=6)
hc.grid(row=3, column=7)
ce.grid(row=4, column=6)
ic.grid(row=4, column=5)

bo = customtkinter.CTkButton(root, text="Submit Data", command=save_info, width="30", height='2', bg="grey")
bo.place(x=420, y=470)

root.mainloop()