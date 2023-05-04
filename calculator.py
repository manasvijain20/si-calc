from tkinter import *
window = Tk()
window.title("Simple Interest Calculator")
window.geometry("600x500")
window.configure(bg='#708090')

def simple_interest():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    i = (p*r*t)/100
    interest = round(i, 2)
    show_label.destroy()
    message = Label(result_frame, text="Interest on Rs "+str(p)+" at the rate of interest "+str(r)+" for "+str(t)+" years is Rs."+str(interest), bg="white", font=("Calibri", 14), width=55)
    message.place(x=20, y=40)
    message.pack()
#Heading
heading_label = Label(window, text="Simple Interest Calculator", fg="#F0FFFF", bg="#708090", font=("Calibri",20), bd=5)
heading_label.place(x=50, y=20)

#Entry boxes 
principal_label=Label(window, text="Principal ", fg="#708090", bg="#F0FFFF", bd=5, font=("Calibri",15))
principal_label.place(x=30, y=120)
principal_entry = Entry(window, text="", bd=2, width=23)
principal_entry.place(x=148, y=127)

rate_label=Label(window, text="Rate ", fg="#708090", bg="#F0FFFF", bd=5, font=("Calibri",15))
rate_label.place(x=30, y=170)
rate_entry = Entry(window, text="", bd=2, width=23)
rate_entry.place(x=148, y=177)

time_label=Label(window, text="Time ", fg="#708090", bg="#F0FFFF", bd=5, font=("Calibri",15))
time_label.place(x=30, y=220)
time_entry = Entry(window, text="", bd=2, width=23)
time_entry.place(x=148, y=227)

#button 
calculate_button = Button(window, text="CALCULATE", fg="#708090", bg="#F0FFFF", bd=4, command=simple_interest)
calculate_button.place(x=280, y=300)

#Result Frame and Label
result_frame = LabelFrame(window, text="Result", bg="#708090", font=("Calibri", 16))
result_frame.pack(padx=20, pady=20)
result_frame.place(x=30, y=350)

show_label = Label(result_frame, text="Your result will be displayed here", bg="#F0FFFF", fg="#708090", font=("Calibri", 14), width=55)
show_label.place(x=30, y=370)
show_label.pack()
window.mainloop()

#colors
#bg
#708090

#F0FFFF
