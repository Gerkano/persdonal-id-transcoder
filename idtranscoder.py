from datetime import datetime
from tkinter import *
import logging
logging.basicConfig(filename='Checks_log.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')

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
                    logging.info(date_validity_check)
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
                logging.info(f"Counter is: {count}")
                count = count+1
                if count == 10:
                    count = 1
                    continue
    
            for number in range(code_len-1):
                num_sum2 = num_sum2 + (int(self.personal_code[number]) * count2)
                logging.info(f"Counter two is: {count2}")
                count2 = count2+1
                if count2 == 10:
                    count2 = 1
                    continue

            controlm1 = num_sum1 % 11
            logging.info(f"Control number is: {controlm1}")
            controlm2 = num_sum2 % 11
            logging.info(f"Second control number is: {controlm2}")
        
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
        first_check = self.control_number()
        second_check = self.date_validity()
        logging.info(f"Check results: {first_check}, {second_check}")
        if first_check == True and second_check == True:
           return True
        else:
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
    logging.info(f"Entry: {memory2}")
    if memory == True:
        result["text"] = "Personal code is valid"
        status["text"] = "Veryfied"
    else:
        result["text"] = "Personal code is not valid or incorrect, please try again"
        status["text"] = "Not veryfied"
    logging.info(f"Memory entry: {memory}")
    return memory

def delete():
    result["text"] = ""
    field.delete(0, 5000)
    status["text"] = "Field entry empty"

def restore(memory):
    if memory == True:
        result["text"] = "Personal code is valid"
        status["text"] = "Veryfied"
    else:
        result["text"] = "Personal code is not valid or incorrect, please try again"
        status["text"] = "Not veryfied"

menu.add_cascade(labe="Menu", menu=submenu)
submenu.add_command(label="Delete", command=delete)
submenu.add_command(label="Restore", command=restore)
submenu.add_separator()
submenu.add_command(label="Exit", command=window.destroy)

field = Entry(window, show= '*')
name = Label(window, text="Enter your personal code")
button = Button(window, text="Confirm check", command=submit)
result = Label(window, text="")
status = Label(window, text="Field entry empty", bd=1, relief=SUNKEN, anchor=W)


name.pack()
field.pack()
button.pack()
result.pack()
status.pack(side=BOTTOM, fill=X)
window.mainloop()