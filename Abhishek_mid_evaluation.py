from tkinter import *
from tkinter import ttk
from tkinter.filedialog import asksaveasfile



root=Tk()
root.geometry("300x300")
bold_font=("bold")
italic_font=("italic")
underline_font=("times 15 underline")
font_types = [
    "Helvetica",
    "Times",
    "Jokerman"]
font_sizes = [
    12,
    16,
    18,
    20,
    22,
    24,
    26,
    ]

def bolding():
    my_text.config(font=(my_font,my_size,"bold"))
def italicize():
    my_text.config(font=(my_font,my_size,"italic"))
def underlining():
    my_text.config(font=(my_font,my_size,"underline"))
def deleting():
    my_text.delete(1.0,END)
def saving():
    content=my_text.get("1.0","end-1c")
    files=[('Text Document','*.txt')]
    f = asksaveasfile(defaultextension=files , filetypes=[('Text Document','*.txt')])
    f.write(content)
    f.close()
def font_changing():
    global my_font
    global my_size
    my_font = selected_font.get()
    my_size = selected_size.get()
    my_text.config(font = (my_font,int(my_size)))
    




selected_font = StringVar()
selected_font.set(font_types[0])
selected_size = StringVar()
selected_size.set(font_sizes[0])




my_text = Text(root, width = 60 , height = 30,pady=5, padx=0,font = "Helvetica")
b_butt = Button(root,text="Bold",command=bolding)
i_butt = Button(root,text="Italic",command=italicize)
u_butt = Button(root,text="Underline",command=underlining)
c_butt = Button(root, text = "clear", command = deleting)
s_butt = Button(root,text="save",command =saving)
font_drop = OptionMenu(root,selected_font,*font_types)
size_drop = OptionMenu(root,selected_size,*font_sizes)
fontset_butt = Button(root,text="Change Font",comman = font_changing)



my_text.grid(column=0,row=1,columnspan=8000,padx=10,pady=10)
b_butt.grid(column=0,row=0)
i_butt.grid(column=1,row=0)
u_butt.grid(column=2,row=0)
c_butt.grid(column=3,row=0)
s_butt.grid(column=4,row=0)
font_drop.grid(column=5,row=0)
size_drop.grid(column=6,row=0)
fontset_butt.grid(column=7,row=0)




root.mainloop()
