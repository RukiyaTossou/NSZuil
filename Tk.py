from tkinter import *

def click():
    text['text'] = naam.get()


root = Tk()
text = Label(master= root,
              text= 'Welkom bij NS',
              font=('American', 16, 'bold'),
              background= 'yellow',
              foreground= 'blue',
              width= 20,
              height= 10,)
text.pack()

knop = Button(master=root, text= 'verzend')
knop.pack(pady =10, padx=12)

               )
naam= Entry(master=root)
naam.pack(padx=10, pady=20)

bericht= Entry(master=root)
bericht.pack(padx=10, pady=10)
root.mainloop()