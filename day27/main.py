import tkinter

def print_input():
    my_label.config(text=input.get())

window = tkinter.Tk()
window.title("A Damn good GUI")
window.minsize(width=500, height=300)
window.config(padx=30, pady=30)

# Label
my_label =tkinter.Label(text="I am a label", font=("Arial", 16))
my_label.grid(column=0, row=0) # pack is a layout manager others are place and grid
my_label["text"] = "New text to show"
my_label.config(text="More new text!")

# Button
button = tkinter.Button( text="Click this now!", command=print_input)
button.grid(column=3, row=0)

button2 = tkinter.Button( text="New Button", command=print_input)
button2.grid(column=2, row=2)



# Entry
input = tkinter.Entry()
input.grid(column=3, row=3)


window.mainloop()