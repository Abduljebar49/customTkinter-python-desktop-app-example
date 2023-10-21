import customtkinter
import pickle
import tkinter.ttk as ttk
customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"
# customtkinter.CTkLabel

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.fileName = "student_file.pkl"
        # self.store_student_array([],self.fileName);
        db = self.read_student_array(self.fileName)
        print(db)
        print('reading db above')
        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{850}x{400}")
        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=850, height=400 )
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Add Grade")
        self.tabview.add("Student Report")
        self.tabview.tab("Add Grade").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Student Report").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        # student = [nameValue,idValue,classInput,int(geoInput),int(itText),int(engInput),int(phyInput),int(mathsInput),int(histInput),int(civicInpt),int(ecoInput),int(ecoInput),int(chemInput),total,average]

        columns = ('Name', 'ID', 'Class', 'Geo','IT','Eng','Phy','Maths','Hist','Civic','Eco','Chem','total','average')
        self.table = ttk.Treeview(self.tabview.tab("Student Report"),
                                columns=columns,
                                height=17,
                                selectmode='browse',
                                show='headings')

        self.table.column("#1", anchor="c", minwidth=100, width=100)
        self.table.column("#2", anchor="c", minwidth=100, width=100)
        self.table.column("#3", anchor="c", minwidth=100, width=100)
        self.table.column("#4", anchor="w", minwidth=50, width=50)
        self.table.column("#5", anchor="w", minwidth=50, width=50)
        self.table.column("#6", anchor="w", minwidth=50, width=50)
        self.table.column("#7", anchor="w", minwidth=50, width=50)
        self.table.column("#8", anchor="w", minwidth=50, width=50)
        self.table.column("#9", anchor="w", minwidth=50, width=50)
        self.table.column("#10", anchor="w", minwidth=50, width=50)
        self.table.column("#11", anchor="w", minwidth=50, width=50)
        self.table.column("#12", anchor="w", minwidth=50, width=50)
        self.table.column("#13", anchor="w", minwidth=50, width=50)
        self.table.column("#14", anchor="w", minwidth=50, width=50)
        # columns = ('Name', 'ID', 'class', 'Geo','IT','Eng','Phy','Maths','Hist','Civic','Eco','Chem','total','average')

        self.table.heading('Name', text='Name')
        self.table.heading('ID', text='ID')
        self.table.heading('Class', text='Class')
        self.table.heading('Geo', text='Geo')
        self.table.heading('IT', text='IT')
        self.table.heading('Phy', text='Phy')
        self.table.heading('Maths', text='Maths')
        self.table.heading('Hist', text='Hist')
        self.table.heading('Civic', text='Civic')
        self.table.heading('Eco', text='Eco')
        self.table.heading('Chem', text='Chem')
        self.table.heading('total', text='total')
        self.table.heading('average', text='average')
        
        # self.table.set_children('value','value','value','value')
        self.table.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        st_list = self.read_student_array(self.fileName)
        for new in st_list:
            self.table.insert('', customtkinter.END, values=new)
            print(new)
        self.className = customtkinter.CTkLabel(self.tabview.tab("Add Grade"),text="Class")
        self.name = customtkinter.CTkLabel(self.tabview.tab("Add Grade"),text="Name")
        self.idNumber = customtkinter.CTkLabel(self.tabview.tab("Add Grade"),text="ID number")
        self.className.grid(row=0,column=0)
        self.name.grid(row=1,column=0)
        self.idNumber.grid(row=2,column=0)

        self.classValue = customtkinter.CTkEntry(self.tabview.tab("Add Grade"),placeholder_text="Enter Class Name")
        self.nameValue = customtkinter.CTkEntry(self.tabview.tab("Add Grade"),placeholder_text="Enter Name")
        self.idValue = customtkinter.CTkEntry(self.tabview.tab("Add Grade"),placeholder_text="Enter Id number")
        self.classValue.grid(row=0,column=1,padx=(20, 20), pady=(2, 2))
        self.nameValue.grid(row=1,column=1,padx=(20, 20), pady=(2, 2))
        self.idValue.grid(row=2,column=1,padx=(20, 20), pady=(2, 2))

        self.geoText = customtkinter.CTkLabel(self.tabview.tab("Add Grade"),text="Geography")
        self.itText = customtkinter.CTkLabel(self.tabview.tab("Add Grade"),text="IT")
        self.engText = customtkinter.CTkLabel(self.tabview.tab("Add Grade"),text="English")
        self.phyText = customtkinter.CTkLabel(self.tabview.tab("Add Grade"),text="Physics")
        self.mathsText = customtkinter.CTkLabel(self.tabview.tab("Add Grade"),text="Matheematics")
        self.histText = customtkinter.CTkLabel(self.tabview.tab("Add Grade"),text="History")
        self.chemText = customtkinter.CTkLabel(self.tabview.tab("Add Grade"),text="Chemistry")
        self.civicText = customtkinter.CTkLabel(self.tabview.tab("Add Grade"),text="Civic")
        self.ecoText = customtkinter.CTkLabel(self.tabview.tab("Add Grade"),text="Economics")

        self.geoValue = customtkinter.CTkEntry(self.tabview.tab("Add Grade"),placeholder_text="Enter Geo")
        self.itValue = customtkinter.CTkEntry(self.tabview.tab("Add Grade"),placeholder_text="Enter IT")
        self.engValue = customtkinter.CTkEntry(self.tabview.tab("Add Grade"),placeholder_text="Enter Eng")
        self.phyValue = customtkinter.CTkEntry(self.tabview.tab("Add Grade"),placeholder_text="Enter Physics")
        self.mathsValue = customtkinter.CTkEntry(self.tabview.tab("Add Grade"),placeholder_text="Enter Maths")
        self.histValue = customtkinter.CTkEntry(self.tabview.tab("Add Grade"),placeholder_text="Enter Hist")
        self.chemValue = customtkinter.CTkEntry(self.tabview.tab("Add Grade"),placeholder_text="Enter Chem")
        self.civicValue = customtkinter.CTkEntry(self.tabview.tab("Add Grade"),placeholder_text="Enter Civ")
        self.ecoValue = customtkinter.CTkEntry(self.tabview.tab("Add Grade"),placeholder_text="Enter Eco")

        self.geoText.grid(row=3,column=2,padx=(20, 20), pady=(2, 2))
        self.geoValue.grid(row=3,column=3,padx=(20, 20), pady=(2, 2))
        self.itText.grid(row=3,column=4,padx=(20, 20), pady=(2, 2))
        self.itValue.grid(row=3,column=5,padx=(20, 20), pady=(2, 2))
        
        self.engText.grid(row=4,column=2,padx=(20, 20), pady=(2, 2))
        self.engValue.grid(row=4,column=3,padx=(20, 20), pady=(2, 2))
        self.phyText.grid(row=4,column=4,padx=(20, 20), pady=(2, 2))
        self.phyValue.grid(row=4,column=5,padx=(20, 20), pady=(2, 2))

        self.mathsText.grid(row=5,column=2,padx=(20, 20), pady=(2, 2))
        self.mathsValue.grid(row=5,column=3,padx=(20, 20), pady=(2, 2))
        self.histText.grid(row=5,column=4,padx=(20, 20), pady=(2, 2))
        self.histValue.grid(row=5,column=5,padx=(20, 20), pady=(2, 2))

        self.chemText.grid(row=6,column=2,padx=(20, 20), pady=(2, 2))
        self.chemValue.grid(row=6,column=3,padx=(20, 20), pady=(2, 2))
        self.civicText.grid(row=6,column=4,padx=(20, 20), pady=(2, 2))
        self.civicValue.grid(row=6,column=5,padx=(20, 20), pady=(2, 2))

        self.ecoText.grid(row=7,column=2,padx=(20, 20), pady=(2, 2))
        self.ecoValue.grid(row=7,column=3,padx=(20, 20), pady=(2, 2))

        self.submitButton = customtkinter.CTkButton(self.tabview.tab("Add Grade"),text="submit data",command=self.save_info)
        self.refreshButton = customtkinter.CTkButton(self.tabview.tab("Student Report"),text="Refresh data",command=self.refresh_data)
        self.submitButton.grid(row=8,column=5,padx=(20, 20), pady=(2, 2))
        self.refreshButton.grid(row=7,column=4,padx=(20, 20), pady=(2, 2))
    def refresh_data(self):
        for item in self.table.get_children():
            self.table.delete(item)
        st_list = self.read_student_array(self.fileName)
        for new in st_list:
            self.table.insert('', customtkinter.END, values=new)
                  
    def save_info(self):
        chemInput = self.chemValue.get()
        geoInput = self.geoValue.get()
        itText   = self.itValue.get()
        engInput = self.engValue.get()
        phyInput = self.phyValue.get()
        mathsInput = self.mathsValue.get()
        histInput = self.histValue.get()
        civicInpt = self.civicValue.get()
        ecoInput = self.ecoValue.get()
        
        classInput = self.classValue.get()
        idValue = self.idValue.get()
        nameValue = self.nameValue.get()
        total = int(chemInput) + int(geoInput) + int(itText) + int(engInput) + int(phyInput) + int(mathsInput) + int(histInput) + int(civicInpt) + int(ecoInput)
        average = total/9
        student = [nameValue,idValue,classInput,int(geoInput),int(itText),int(engInput),int(phyInput),int(mathsInput),int(histInput),int(civicInpt),int(ecoInput),int(chemInput),total,average]
        oldStudent = self.read_student_array(self.fileName)
        oldStudent.append(student)
        self.store_student_array(oldStudent,'student_file.pkl')


    def store_student_array(self,student_array,filename):
        with open(filename,'wb') as file:
            pickle.dump(student_array,file)

    def read_student_array(self,filename):
        try:
            with open(filename,'rb') as file:
                student_array = pickle.load(file)
                return student_array
        except:
            self.store_student_array([],self.fileName)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        
if __name__ == "__main__":
    app = App()
    app.mainloop()
