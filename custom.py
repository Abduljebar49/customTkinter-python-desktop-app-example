import customtkinter as ck

ck.set_appearance_mode('light')
ck.set_default_color_theme('dark-blue')

root = ck.CTk()
root.geometry("500x500")


frame = ck.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both",expand=True)
h=ck.CTkLabel(master=frame,text="Students Info",text_color='white')

root.mainloop()
