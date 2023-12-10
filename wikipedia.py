from tkinter import *
from tkinter.messagebox import showerror
from wikipedia import summary

# This function using for the answer of search
def get_answer():
    try:
        answer.delete(1.0, END)
        answer.insert(INSERT, summary(search_box.get()))
    except Exception as error:
        showerror('Error', error)

#f Fonts
font1 = ('Boulder', 20, 'bold')
font2 = ('Boulder', 25, 'bold')
font3 = ('Arial', 15)

# Main window / Object
root = Tk()
root.title('Python WikiPedia Application')
root.config(bg='lightblue')
root.geometry('750x630')
root.resizable(0, 0)

header = Label(root, text='WikiPedia with Python', fg='white', bg='black', font=font2, width=100, borderwidth=20)
header.pack()

# Top frame for search button and search box
top_frame = Frame(root, bg='lightblue')
top_frame.pack(side='top', fill='x', padx=55, pady=12)

# Bottom frame for show result / answer
bottom_frame = Frame(root, bg='lightblue')
bottom_frame.pack(side='top', fill='x', padx=10, pady=10)

# This is the search-box
search_box = Entry(top_frame, font=font2, width=25, bd=4)
search_box.pack(side='left', ipady=5)

# This is the search-button
search_button = Button(top_frame, text='SEARCH', font=font1, bd=4, command=get_answer)
search_button.pack(side='right')

# This is the result / answer
answer = Text(bottom_frame, font=font3, fg='black', width=70, height=100)
answer.pack(side='left', fill='y')

root.mainloop()