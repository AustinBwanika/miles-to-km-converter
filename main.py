from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)

# Labels
miles_label = Label(text="Miles")
km_label = Label(text="Km")
equal_to = Label(text="is equal to")
answer_label = Label(text="0")


# Function
def conversion():
    answer = round(int(input_entry.get())*1.6,2)
    answer_label.config(text=f"{answer}")


# Entry
input_entry = Entry()



# Button

calculate = Button(text="Calculate", command=conversion)
# Display
input_entry.grid(column=10, row=4)
miles_label.grid(column=11, row=4)
answer_label.grid(column=10, row=5)
km_label.grid(column=11, row=5)
equal_to.grid(column=9, row=5)
calculate.grid(column=10,row=6)




window.mainloop()