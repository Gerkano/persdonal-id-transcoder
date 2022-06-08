from datetime import datetime
from tkinter import *

class PersonalID:

    def __init__(self, personal_code: str):
        self.personal_code = personal_code

    def date_validity(self) -> bool:
        cent1 = "18"
        cent2 = "19"
        cent3 = "20"
        year1 = self.personal_code[1:3]
        month1 = self.personal_code[3:5]
        day1 = self.personal_code[5:7]
        try:
            first_num = int(self.personal_code[0])
            if first_num == 1 or first_num == 2:
                year1 = cent1 + year1
            elif first_num == 3 or first_num == 4:
                year1 = cent2 + year1
            elif first_num == 5 or first_num == 6:
                year1 = cent3 + year1
            else:
                return False  

            if first_num<=6 and first_num>=1:
                try:
                    date_validity_check = datetime(int(year1), int(month1), int(day1))
                    print(date_validity_check)
                    return True
                except:
                    return False  
        except:
            return False  


    def control_number(self) -> bool:
        code_len = len(self.personal_code)
        count = 1
        count2 = 3
        num_sum1 = 0
        num_sum2 = 0
        
        if code_len == 11 and self.personal_code.isdigit():
            last_num = int(self.personal_code[10])        
            for number in range(code_len-1):
                num_sum1 = num_sum1 + (int(self.personal_code[number]) * count)
                count = count+1
                if count == 9:
                    count = 1
                    continue
    
            for number in range(code_len-1):
                num_sum2 = num_sum2 + (int(self.personal_code[number]) * count2)
                count2 = count2+1
                if count2 == 9:
                    count2 = 1
                    continue

            controlm1 = num_sum1 % 11
            controlm2 = num_sum2 % 11
        
            if controlm1 == 10:
                if controlm2 == 10:
                    return 0 == last_num
                else:
                    return controlm2 == last_num
            else:
                return controlm1 == last_num
        else:
            return False
            

    def conclusion(self) -> bool:
        if self.control_number() == True and self.date_validity() == True:
           print("Personal code is valid")
           return True
        else:
            print("Personal code is either incorrect or invalid")
            return False


window = Tk()
ui = StringVar()
menu = Menu(window)
window.config(menu=menu)
submenu = Menu(menu, tearoff = 0)
window.geometry("650x300")

def submit():
    ui.set(field.get())
    ip1 = PersonalID(ui.get())
    memory = ip1.conclusion()
    memory2 = ui.get()
    if ip1.conclusion() == True:
        result["text"] = f"{ui.get()} Personal code is valid"
        status["text"] = f"{ui.get()} Personal code is valid"
    else:
        result["text"] = f"{ui.get()} Personal code is not valid or incorrect, please try again"
        status["text"] = f"{ui.get()} Personal code is not valid or incorrect, please try again"
    return memory

def delete():
    result["text"] = ""
    field.delete(0, 5000)
    status["text"] = "nothing"

def restore(memory, memory2):
    if memory == True:
            result["text"] = f"{memory2} Personal code is valid"
            status["text"] = f"{memory2} Personal code is valid"
    else:
        result["text"] = f"{memory2} Personal code is not valid or incorrect, please try again"
        status["text"] = f"{memory2} Personal code is not valid or incorrect, please try again"

menu.add_cascade(labe="Menu", menu=submenu)
submenu.add_command(label="Delete", command=delete)
submenu.add_command(label="Restore", command=restore)
submenu.add_separator()
submenu.add_command(label="Exit", command=window.destroy)

field = Entry(window)
name = Label(window, text="Enter your personal code")
button = Button(window, text="PLEASE DO NOT PRESS THE BUTTON", command=submit)
button.bind(window, "<Return>", lambda event: submit())
result = Label(window, text="")
status = Label(window, text="nothing", bd=1, relief=SUNKEN, anchor=W)


name.pack()
field.pack()
button.pack()
result.pack()
status.pack(side=BOTTOM, fill=X)
window.mainloop()