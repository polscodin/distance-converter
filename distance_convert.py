from tkinter import *
import tkinter.font as font
window = Tk()
window.geometry("900x200")
window.title("kilometers converter")


def conversion():
    weight = float(value.get())

    gram_weight = weight*1000
    pound_weight = weight*0.621371
    ounce_weight = weight*100000

    t1.delete("1.0",END)
    t1.insert(END,gram_weight)

    t2.delete("1.0",END)
    t2.insert(END,pound_weight)

    t3.delete("1.0",END)
    t3.insert(END,ounce_weight)





title1 = Label(window,text="Kilometer -> mile",font=font.Font(size=30),fg="grey")


weight = Label(window,text="Enter distance in km : ",font=font.Font(size=10))
weight.grid(row=1,column=0)

value = StringVar()

kg_weight = Entry(window,textvariable=value,width=15,fg="Red")
kg_weight.grid(row=1,column=1)



g = Label(window,text="Meters : ",padx=30).grid(row=3,column=0)
p = Label(window,text="Mile : ",padx=30).grid(row=3,column=2)
o = Label(window,text="Centimeters : ",padx=30).grid(row=3,column=4)

t1 = Text(window,height=1,width=20)
t2 = Text(window,height=1,width=20)
t3 = Text(window,height=1,width=20)
t1.grid(row=3,column=1)
t2.grid(row=3,column=3)
t3.grid(row=3,column=5)

convert_button = Button(window,text="Convert",pady=10,padx=20,font=font.Font(size=10),width=3,height=1,fg="black",bg="grey",command=conversion)
convert_button.grid(row=1,column=2)




window.mainloop()