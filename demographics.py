from tkinter import *
from tkinter.messagebox import showerror

def get_demographic_fn():
    prompt = Tk()
    id, ppt_age, ppt_sex = StringVar(prompt), StringVar(prompt), StringVar(prompt)
    def quit_if_verified():
        age_val = ppt_age.get()
        if not age_val.isdigit():
            showerror("Input Error!",
                f"The inputted age: {age_val}\nis not a valid number!")
            return
        age_val = int(age_val)
        if age_val <= 0:
            showerror("Input Error!",
                f"The inputted age: {age_val}\nis invalid!")
            return
        sex_val = ppt_sex.get().upper()
        if sex_val not in ('M', 'F'):
            showerror("Input Error!",
                f"The inputted sex: {sex_val}\nis invalid!")
            return
        prompt.destroy()

    widgets = [
        Label(prompt, text='Participant ID:'),
        Entry(prompt, textvariable = id),
        Label(prompt, text='Please enter your age:'),
        Entry(prompt, textvariable = ppt_age),
        Label(prompt, text='Please enter your Sex (M/F):'),
        Entry(prompt, textvariable = ppt_sex),
        Button(prompt, text='Done', command = quit_if_verified),
    ]    
    for widget in widgets:
        widget.pack()

    prompt.mainloop()

    return f"{id.get()}-{ppt_sex.get().upper()}{ppt_age.get()}"

if __name__ == '__main__':
    print(get_demographic_fn())
