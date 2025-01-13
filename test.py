import tkinter as tk
from tkinter.ttk import *



WIDTH = 800
HEIGHT = 600
root = tk.Tk()
root.title("Budget app")
excess = 0
totalprice = 0


def update_price():
    totalprice = 0
    monthlyIncome = int(mincome.get("1.0", tk.END))
    for i in listbox.get(1, tk.END):
        price = int(i.split()[-1])
        totalprice += price
    label5.config(text=totalprice)
    excess = monthlyIncome - totalprice
    label6.config(text=excess)
    return excess, totalprice

def add_bill():
    item = bitem.get("1.0", tk.END).strip()
    price = bprice.get("1.0", tk.END).strip()
    listbox.insert(tk.END, f"{item} {price}")
    bitem.delete("1.0", tk.END)
    bprice.delete("1.0", tk.END)
    update_price()

def delete_bill():
    selected_items = listbox.curselection()
    for index in selected_items[::-1]:
        listbox.delete(index)
    update_price()

def focus_next_widget(event):
    event.widget.tk_focusNext().focus()
    return "break"

listbox = tk.Listbox(root, width=WIDTH//16, height=HEIGHT//80)
listbox.grid(column=5,row=0, rowspan=(10),columnspan=(100),sticky="nsew")
listbox.insert(tk.END, "Bills:   Total:")
lbl = tk.Label(root, text="Monthly income")
mincome = tk.Text(root, height=2, width=15)
monthlyIncome = mincome.get("1.0", tk.END)
lbl.grid(column=0,row=0)
mincome.grid(column=0,row=1)
label1 = tk.Label(root, text="Bill name")
bitem = tk.Text(root, height=2, width=15)
label1.grid(column=0,row=2)
bitem.grid(column=0,row=3)
label2 = tk.Label(root, text="Bill price")
bprice = tk.Text(root, height=2, width=15)
label2.grid(column=0,row=4)
bprice.grid(column=0,row=5)
btn1 = tk.Button(root, text="Add item", command=add_bill)
btn1.grid(column=0,row=6)
btn2 = tk.Button(root, text="Delete item", command=delete_bill)
btn2.grid(column=0,row=7)
label3 = tk.Label(root, text="Total")
label3.grid(column=0,row=8)
label5 = tk.Label(root, text=totalprice)
label5.grid(column=0,row=9)
label4 = tk.Label(root, text="Excess")
label4.grid(column=0,row=10)
label6 = tk.Label(root, text=excess)
label6.grid(column=0,row=11)

mincome.bind("<Tab>", focus_next_widget)
bitem.bind("<Tab>", focus_next_widget)
bprice.bind("<Tab>", focus_next_widget)
root.bind("<Shift-Return>", lambda event: add_bill())
root.geometry(f"{WIDTH}x{HEIGHT}")
root.background = "gray"

root.mainloop()