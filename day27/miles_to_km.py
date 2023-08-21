from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

def convert_miles_km():
    miles = entry.get()    
    km = float(miles) * 1.609
    label_result.config(text=f"{km}")
# Entry
entry = Entry(width=7)
entry.insert(END, string="Miles to convert")
entry.grid(column=1, row=0)

# Label
label_miles = Label(text="Miles")
label_miles.grid(column=3, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_result = Label(text=0, justify="center")
label_result.grid(column=1, row=1)

label_km = Label(text="Km")
label_km.grid(column=3, row=1)

# Button
button = Button(text="Calculate", command=convert_miles_km)
button.grid(column=1, row=2)

window.mainloop()