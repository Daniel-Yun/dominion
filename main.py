from tkinter import *
from PIL import *

gui = Tk()
gui.geometry("1920x1080")
gui.title("Dominion")
gui.config(bg='#FCF3CF')

# Player totals
total1 = IntVar()
total2 = IntVar()

# Card images
estate_temp = PhotoImage(file = r"Images\estate.png")
estate = estate_temp.subsample(3)
curse_temp = PhotoImage(file = r"Images\curse.png")
curse = curse_temp.subsample(3)
duchy_temp = PhotoImage(file = r"Images\duchy.png")
duchy = duchy_temp.subsample(3)
province_temp = PhotoImage(file = r"Images\province.png")
province = province_temp.subsample(3)

# Player 1 side
def button_click(number):
    global total1
    total1.set(total1.get() + number)

total_p1 = Label(gui, textvariable = total1, font = 'size, 75', bg = "#FCF3CF")
button_curse = Button(gui, command = lambda: button_click(-1), image = curse)
button_estate = Button(gui, command = lambda: button_click(1), image = estate)
button_duchy = Button(gui, command = lambda: button_click(3), image = duchy)
button_province = Button(gui, command = lambda: button_click(6), image = province)

button_curse.grid(row = 1, column = 0, padx = 5, pady = 5)
button_estate.grid(row = 1, column = 1, padx = 5, pady = 5)
button_duchy.grid(row = 1, column = 2, padx = 5, pady = 5)
button_province.grid(row = 1, column = 3, padx = 5, pady = 5)
total_p1.grid(row = 0, column = 5)

can = Canvas(gui, bg = 'black', height = 1080, width = 1)
can.place(relx = 0.5, rely = 0.5, anchor = CENTER)



# Player 2 side
def button_click_p2(number):
    global total2
    total2.set(total2.get() + number)


total_p2 = Label(gui, textvariable=total2, font='size, 30')












gui.mainloop()
