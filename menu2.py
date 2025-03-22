from tkinter import*
from tkinter.ttk import*
new=Tk()
new.title("🍕<Pizza hut>🍕")
title=Label(new,text="")
title.grid(row=0,column=3,columnspan=7,pady=25)
h=Label(new,text="🍕Select a Pizza🍕")
h.grid(row=1,column=0,padx=10)
k=Label(new,text="Select the amount 😁😁😁")
k.grid(row=3,column=0,padx=10)
z=IntVar()
a=["Pepperoni","Cheese","Sweet Chilli","⭐Tripple Layered Pizza⭐"]
u=Combobox(new,textvariable=z,width=15)
u["values"]=tuple(range(101))
u.grid(row=3,column=1)
hi = Listbox(new, width=40)  
for pizza in a:
    hi.insert(END, pizza)  
hi.grid(row=1, column=1)

endVal=IntVar()
g=Radiobutton(new,text="S")
g1=Radiobutton(new,text="M")
g2=Radiobutton(new,text="L")
g3=Radiobutton(new,text="XL")
g.grid(row=2,column=3)
g1.grid(row=3,column=3)
g2.grid(row=4,column=3)
g3.grid(row=5,column=3)


c=Label(new,anchor="center")
c.grid(row=6,column=1,pady=25)

new.mainloop()