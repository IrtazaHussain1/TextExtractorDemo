import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import csv
import json
# api for text extraction
import veryfi
# api configrations
client_id = "vrfOHDDnOc7blOlPtYKiKI1b0pdGffjzjRrgXZJ"
client_secret = "BchJJyLYIoek2N86921MS2GvLJCgdtckox5yMjB3s796IDHODFtKSrGa4XP0nOLoP5my81fWhl51PD4lRbDof7awWtZNsAxfFo8CEn603eL5SI9YfwTDZDy2G7LX4p39"
username = "hokejo5741"
api_key = "768fd6b5f23c7da36429610e691952b9"

# setting up client for api calls and SDK configration.
client  = veryfi.Client(client_id,client_secret,username,api_key)


data = {}


# extract text from the pdf file and add to
def ExtractText(file_name):
    global ext_text
    categories = ['Invoice','Airfare','Travel','Lodging','Job Suplies and Materials','Grocery']
    # json_result  = client.process_document(file_name,categories)

    file_name=file_name.split('/')[-1].split('.')[0]
    file_name=file_name+".json"
    with open(file_name,'w') as json_file:
        json_file.append({"hello":"ass"})

    


def BrowseFile():
    try:
        filename = filedialog.askopenfilename()
        print(filename)
        ExtractText(filename)
    except Exception as e:
        print(str(e))
    


def CreateWindow():
    window = Tk()
    # creating menu bar on top
    menubar = Menu(window)
    window.config(menu=menubar)

    # sub menu
    submenu = Menu(menubar, tearoff=0)

    menubar.add_cascade(label='File',menu=submenu)
    submenu.add_cascade(label="Open",command=BrowseFile)
    submenu.add_cascade(label="Exit",command=window.destroy)
    
    
    # widgets here
    lbl = Label(window,text='PDF Invocie To Data Extractor',fg='blue',font=('Arial',17))

    lbl.place(x=100,y=30)

    extract_button = Button(window,text="Extract",command=BrowseFile,bg="#fff",fg="#000")
    extract_button.pack(side=LEFT)
    extract_button.place(x=10,y=50)

    # adding frame for showing table 
    frame = Frame(window)
    frame.pack(side=LEFT,padx=20)
    # frame.place(x=20,y=100)
    print(data)
    provide_label = Label(frame,text='Company Name: {}'.format(data),bg='#fff',fg="#000")
    # add text to frame



    # add title to window
    window.title('Invoice Text Extractor')

    # geometry and frame set (width x height + xpos + ypos)
    window.geometry("500x500+100+200")
    window.resizable(False,False)



    # looping window to keep it open
    window.mainloop()




if __name__ == "__main__":
    CreateWindow();