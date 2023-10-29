import customtkinter
import pickle
import tkinter.ttk as ttk
import tkinter as tk
from tkinter import messagebox
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
        self.geometry(f"{886}x{440}")
        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=850, height=400 )
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Search Student")
        self.tabview.add("Add Grade")
        self.tabview.add("Student Report")
        self.tabview.tab("Add Grade").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Student Report").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Search Student").grid_columnconfigure(0, weight=3)  # configure grid of individual tabs
        # student = [nameValue,idValue,classInput,int(geoInput),int(itText),int(engInput),int(phyInput),int(mathsInput),int(histInput),int(civicInpt),int(ecoInput),int(ecoInput),int(chemInput),total,average]

        self.columns = ('Name', 'ID', 'Class', 'Geo','IT','Eng','Phy','Maths','Hist','Civic','Eco','Chem','total','average','rank')
        self.table = ttk.Treeview(self.tabview.tab("Student Report"),
                                columns=self.columns,
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
        self.table.column("#15", anchor="w", minwidth=50, width=50)
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
        self.table.heading('rank', text='rank')
        
        # self.table.set_children('value','value','value','value')
        self.table.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

        self.refresh_data()
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
        self.refreshButton.grid(row=8,column=3)

        #search tab section codes
        self.logo_label = customtkinter.CTkLabel(self.tabview.tab("Search Student"), text="Search Student by ID", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0,  column=0, columnspan=4, padx=20, pady=(20, 10))
        self.search_text = customtkinter.CTkEntry(self.tabview.tab("Search Student"),width=300,height=35, placeholder_text="Enter student name here")
        self.search_text.grid(row=2, column=0, columnspan=4, )

        self.button_container = customtkinter.CTkFrame(self.tabview.tab("Search Student"))
        self.button_container.grid(row=3,column=0)
        self.main_button_1 = customtkinter.CTkButton(master=self.button_container,command=self.search_student,height=35,text="Search", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button_1.grid(row=3, column=0,  padx=(20, 20), pady=(20, 20))
        self.main_button = customtkinter.CTkButton(master=self.button_container,command=self.reset_search,height=35,text="Reset", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.main_button.grid(row=3, column=2,  padx=(20, 20), pady=(20, 20))

    def reset_search(self):
        print('enter')
        self.reset_entry(self.search_text)
        try:
            self.error_label.grid_remove()   
        except:
            print('')
        try:
            self.table_search.grid_remove()
        except:
            print('')
    def reset_entry(self, entry):
        entry.delete(0, tk.END)  # Delete the current text from index 0 to the end
        entry.insert(0, "") 

    def add_rank_and_sort(self,arr):
        arr.sort(key=lambda x: x[13], reverse=True)
        for i, student in enumerate(arr):
            student.append(i + 1)  # Add rank as the 11th item
        arr.sort(key=lambda x: x[14])
        return arr

    def refresh_data(self):
        for item in self.table.get_children():
            self.table.delete(item)
        st_list = self.read_student_array(self.fileName)
        ordered = self.add_rank_and_sort(st_list)
        for new in ordered:
            self.table.insert('', customtkinter.END, values=new)

    def add_data_from_search(self,array):
        for item in self.table_search.get_children():
            self.table_search.delete(item)
        for new in array:
            self.table_search.insert('', customtkinter.END, values=new)        

    def search_student(self):
        text = self.search_text.get()
        if(text == ''):
            self.dialogText("Input required","You should write an input to search")
            return
        st_list = self.read_student_array(self.fileName)
        found_items = []
        for array in st_list:
            if text in array[1]:
                found_items.append(array)
        if(len(found_items)>0):
            self.table_search = ttk.Treeview(self.tabview.tab("Search Student"),
                                columns=self.columns,
                                height=len(found_items),
                                selectmode='browse',
                                show='headings')
            self.table_search.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)            
            self.table_search.column("#1", anchor="c", minwidth=100, width=100)
            self.table_search.column("#2", anchor="c", minwidth=100, width=100)
            self.table_search.column("#3", anchor="c", minwidth=100, width=100)
            self.table_search.column("#4", anchor="w", minwidth=50, width=50)
            self.table_search.column("#5", anchor="w", minwidth=50, width=50)
            self.table_search.column("#6", anchor="w", minwidth=50, width=50)
            self.table_search.column("#7", anchor="w", minwidth=50, width=50)
            self.table_search.column("#8", anchor="w", minwidth=50, width=50)
            self.table_search.column("#9", anchor="w", minwidth=50, width=50)
            self.table_search.column("#10", anchor="w", minwidth=50, width=50)
            self.table_search.column("#11", anchor="w", minwidth=50, width=50)
            self.table_search.column("#12", anchor="w", minwidth=50, width=50)
            self.table_search.column("#13", anchor="w", minwidth=50, width=50)
            self.table_search.column("#14", anchor="w", minwidth=50, width=50) 
            self.table_search.heading('Name', text='Name')
            self.table_search.heading('ID', text='ID')
            self.table_search.heading('Class', text='Class')
            self.table_search.heading('Geo', text='Geo')
            self.table_search.heading('IT', text='IT')
            self.table_search.heading('Phy', text='Phy')
            self.table_search.heading('Maths', text='Maths')
            self.table_search.heading('Hist', text='Hist')
            self.table_search.heading('Civic', text='Civic')
            self.table_search.heading('Eco', text='Eco')
            self.table_search.heading('Chem', text='Chem')
            self.table_search.heading('total', text='total')
            self.table_search.heading('average', text='average')
            self.add_data_from_search(found_items)
            if(self.error_label):
                self.error_label.grid_remove()
        else:
            print('no found item')

            self.error_label = customtkinter.CTkLabel(self.tabview.tab("Search Student"), text="No Record Found",text_color='red', font=customtkinter.CTkFont(size=20, weight="bold"))
            self.error_label.grid(row=5,  column=0, columnspan=4, padx=20, pady=(20, 10))
            if(self.table_search):
                self.table_search.grid_remove()

    def dialogText(self,title,description):
        messagebox.showinfo(title, description)


    def register_successful(self):
        # dialog = customtkinter.CTkDz(text="Type in a number:", title="CTkInputDialog")

        messagebox.showinfo("Registration Successful", "Congratulations! You have successfully registered.")
        self.reset_entry(self.chemValue)
        self.reset_entry(self.geoValue)
        self.reset_entry(self.itValue)
        self.reset_entry(self.engValue)
        self.reset_entry(self.phyValue)
        self.reset_entry(self.mathsValue)
        self.reset_entry(self.civicValue)
        self.reset_entry(self.histValue)
        self.reset_entry(self.ecoValue)
        self.reset_entry(self.classValue)
        self.reset_entry(self.idValue)
        self.reset_entry(self.nameValue)
        
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
        average = round(total/9,2)
        student = [nameValue,idValue,classInput,int(geoInput),int(itText),int(engInput),int(phyInput),int(mathsInput),int(histInput),int(civicInpt),int(ecoInput),int(chemInput),total,average]
        oldStudent = self.read_student_array(self.fileName)
        oldStudent.append(student)
        self.store_student_array(oldStudent,'student_file.pkl')
        self.register_successful()

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
