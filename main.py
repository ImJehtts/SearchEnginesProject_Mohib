from tkinter import *
from tkinter import messagebox
import webbrowser
from tkinter import ttk

#Search bar functions
def searched():
   global ser
   ser = entrybox.get()

   restrict_file = open('restricted.txt', 'r', encoding="utf-8")
   restricted_word = restrict_file.readline()
   while restricted_word != "" and restricted_word.strip() not in ser.strip():
       restricted_word = restrict_file.readline()
   if restricted_word == "":
       currsearch.set(ser)
       listbox_history.insert(listbox_history.size(), ser)
       save_to_history(ser)
       currently_searched_bar.configure(validate="none")
       currently_searched_bar.configure(validate="key")
       restrict_file.close()
   else:
        messagebox.showerror(title="Restricted word searched", message="You are searching for a word that has been marked as restricted from being searched")
        ser = ""
        currsearch.set("")
        restrict_file.close()

def delete():
   entrybox.delete(len(entrybox.get()) - 1, END)

def clear():
   entrybox.delete(0, END)


def validate():
    return False

#Google search functions
def google_main():
   webbrowser.open("https://www.google.com")

def google_all_search():
   global ser
   webbrowser.open(f"https://www.google.com/search?q={ser}")

def google_images_search():
   global ser
   webbrowser.open(f"https://www.google.com/search?q={ser}&tbm=isch")

def google_video_search():
   global ser
   webbrowser.open(f"https://www.google.com/search?q={ser}&tbm=vid")

def google_news_search():
   global ser
   webbrowser.open(f"https://www.google.com/search?q={ser}&tbm=nws")

def google_maps_search():
   global ser
   webbrowser.open(f"https://www.google.com/maps?q={ser}")

def google_shopping_search():
   global ser
   webbrowser.open(f"https://www.google.com/search?q={ser}&tbm=shop")

#Bing search functions
def bing_main():
   webbrowser.open("https://www.bing.com")

def bing_all_search():
   global ser
   webbrowser.open(f"https://www.bing.com/search?q={ser}")

def bing_images_search():
  global ser
  webbrowser.open(f"https://www.bing.com/images/search?q={ser}")

def bing_video_search():
  global ser
  webbrowser.open(f"https://www.bing.com/videos/search?q={ser}")

def bing_news_search():
  global ser
  webbrowser.open(f"https://www.bing.com/news/search?q={ser}")

def bing_maps_search():
  global ser
  webbrowser.open(f"https://www.bing.com/maps?q={ser}")

def bing_shopping_search():
 global ser
 webbrowser.open(f"https://www.bing.com/shop?q={ser}")


#DuckDuckGo search functions
def duckduckgo_main():
  webbrowser.open("https://duckduckgo.com/")

def duckduckgo_all_search():
  global ser
  webbrowser.open(f"https://duckduckgo.com/?q={ser}&t=h_&ia=definition")

def duckduckgo_images_search():
 global ser
 webbrowser.open(f"https://duckduckgo.com/?q={ser}&t=h_&ia=images&iax=images")

def duckduckgo_video_search():
 global ser
 webbrowser.open(f"https://duckduckgo.com/?q={ser}&t=h_&iax=videos&ia=videos")

def duckduckgo_news_search():
 global ser
 webbrowser.open(f"https://duckduckgo.com/?q={ser}&t=h_&iar=news&ia=news")

def duckduckgo_maps_search():
    global ser
    webbrowser.open(f"https://duckduckgo.com/?q={ser}&t=h_&ia=news&iaxm=maps")


#Initialize main window
window = Tk()
window.geometry("745x735")
window.title("Multiple Engines in One")
window.resizable(False,False)


#Pictures needed and resized
magnify = PhotoImage(file='magnify.png')
x_button = PhotoImage(file='x_button.png')
trashcan = PhotoImage(file='trashcan.png')
addimg = PhotoImage(file='add.png')
google_logo = PhotoImage(file='google_logo.png')
bing_logo = PhotoImage(file='bing_logo.png')
duckduckgo_logo = PhotoImage(file='duckduckgo_logo.png')

searchpic = magnify.subsample(9, 9)
deletepic = x_button.subsample(9, 9)
clearpic = trashcan.subsample(9, 9)
addpic = addimg.subsample(9, 9)
googleicon = google_logo.subsample(7, 7)
bingicon = bing_logo.subsample(7, 7)
duckduckgoicon = duckduckgo_logo.subsample(7, 7)

window.iconphoto(True,searchpic)

#Variables
currsearch = StringVar()
ser = ''
vcmd = (window.register(validate))
restricted_list = []

#Frames
notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
notebook.add(tab1,text="Main")
tab1.config(background="#4b6043")
notebook.pack(expand=True, fill="both")

notebook.add(tab2,text="History&Restricted")
tab2.config(background="#4b6043")
notebook.pack(expand=True, fill="both")


search_bar_frame = Frame(tab1)
google_search_frame = Frame(tab1)
bing_search_frame = Frame(tab1)
duckduckgo_search_frame = Frame(tab1)
history_but_frame = Frame(tab2)
restricted_but_frame = Frame(tab2)

#Search Labels and Buttons for Main Tab
title_label = Label(tab1,
                   text="3 Browsers in One",
                   font = ("Times New Roman", 40),
                   fg="white",
                   bg="#4b6043")

current_search_label = Label(tab1,
                   text="Current search:",
                   font = ("Times New Roman", 30),
                   fg="white",
                   bg="#4b6043")

currently_searched_bar = Entry(tab1,
                   textvariable= currsearch,
                   font = ("Times New Roman", 30),
                   foreground="white",
                   background="#75975e",
                   width = 21,
                   relief=FLAT,
                   validatecommand=vcmd)
currently_searched_bar.update()
currently_searched_bar.configure(validate="key")


entrybox = Entry(tab1,
                font = ("Times New Roman", 40),
                fg="white",
                bg="#75975e",
                width = 27,
                relief=RAISED)

#Search Bar Buttons
search_button = Button(search_bar_frame,image=searchpic,command=searched).grid(row=0,column=0)
delete_button = Button(search_bar_frame,image=deletepic,command=delete).grid(row=0,column=1)
clear_button = Button(search_bar_frame,image=clearpic,padx= 5, command=clear).grid(row=0,column=2)

#buttons basic
buttonsbasics = {'font': ("Comic Sans",14),
                'fg':'white',
                'bg':'#87ab69',
                'activeforeground':'white',
                'activebackground':'#75975e',
                'width':10}

#Google Search Buttons
google_icon_logo = Button(tab1,
                         image=googleicon,
                         command=google_main,
                         bg = "#75975e",
                         activebackground="#75975e")

google_allbutton = Button(google_search_frame,text="ALL",**buttonsbasics,
                   command=google_all_search).grid(row=0,column=0)

google_imagesbutton = Button(google_search_frame,text="IMAGES", **buttonsbasics,
                      command=google_images_search).grid(row=1,column=0)

google_videosbutton = Button(google_search_frame,text="VIDEOS",**buttonsbasics,
                      command=google_video_search).grid(row=0,column=1)

google_newsbutton = Button(google_search_frame,text="NEWS",**buttonsbasics,
                    command=google_news_search).grid(row=1,column=1)

google_mapsbutton = Button(google_search_frame,text="MAPS",**buttonsbasics,
                          command=google_maps_search).grid(row=0,column=2)

google_shoppingbutton = Button(google_search_frame,text="SHOPPING",**buttonsbasics,
                          command=google_shopping_search).grid(row=1,column=2)

#Bing Search Buttons
bing_icon_logo = Button(tab1,
                       image=bingicon,
                        command=bing_main,
                        bg = "#75975e",
                        activebackground="#75975e")
bing_allbutton = Button(bing_search_frame,text="ALL",**buttonsbasics,
                  command=bing_all_search).grid(row=0,column=0)

bing_imagesbutton = Button(bing_search_frame,text="IMAGES", **buttonsbasics,
                     command=bing_images_search).grid(row=1,column=0)

bing_videosbutton = Button(bing_search_frame,text="VIDEOS",**buttonsbasics,
                     command=bing_video_search).grid(row=0,column=1)

bing_newsbutton = Button(bing_search_frame,text="NEWS",**buttonsbasics,
                   command=bing_news_search).grid(row=1,column=1)

bing_mapsbutton = Button(bing_search_frame,text="MAPS",**buttonsbasics,
                         command=bing_maps_search).grid(row=0,column=2)

bing_shoppingbutton = Button(bing_search_frame,text="SHOPPING",**buttonsbasics,
                         command=bing_shopping_search).grid(row=1,column=2)

#DuckDuckGo Search Buttons
duckduckgo_icon_logo = Button(tab1,
                      image=duckduckgoicon,
                       command=duckduckgo_main,
                        bg="#75975e",
                        activebackground="#75975e")
duckduckgo_allbutton = Button(duckduckgo_search_frame,text="ALL",**buttonsbasics,
                 command=duckduckgo_all_search).grid(row=0,column=0)

duckduckgo_imagesbutton = Button(duckduckgo_search_frame,text="IMAGES", **buttonsbasics,
                    command=duckduckgo_images_search).grid(row=1,column=0)

duckduckgo_videosbutton = Button(duckduckgo_search_frame,text="VIDEOS",**buttonsbasics,
                    command=duckduckgo_video_search).grid(row=0,column=1)

duckduckgo_newsbutton = Button(duckduckgo_search_frame,text="NEWS",**buttonsbasics,
                  command=duckduckgo_news_search).grid(row=1,column=1)

duckduckgo_mapsbutton = Button(duckduckgo_search_frame,text="MAPS",**buttonsbasics,
                        command=duckduckgo_maps_search).grid(row=0,column=2)

duckduckgo_lastlabel = Button(duckduckgo_search_frame,text="",
                       font=("Comic Sans",14),
                       bg='#4b6043',
                       width=10,
                       state=DISABLED,
                       relief= FLAT).grid(row=1,column=2)

#Packing and Placements for Main Tab
ICON_PLACEX_LEFT = 8
BUTTONS_FRAME_PLACEX_LEFT = 88
GOOGLE_Y = 360
BING_Y = 485
DUCKDUCKGO_Y = 610
title_label.pack()
current_search_label.place(x=6,y=100)
currently_searched_bar.place(x=256,y=100)
entrybox.place(x=6,y=175)
search_bar_frame.place(x=536,y=263)
google_icon_logo.place(x=ICON_PLACEX_LEFT,y=GOOGLE_Y)
bing_icon_logo.place(x=ICON_PLACEX_LEFT,y=BING_Y)
duckduckgo_icon_logo.place(x=ICON_PLACEX_LEFT,y=DUCKDUCKGO_Y)
google_search_frame.place(x=BUTTONS_FRAME_PLACEX_LEFT,y=GOOGLE_Y)
bing_search_frame.place(x=BUTTONS_FRAME_PLACEX_LEFT,y=BING_Y)
duckduckgo_search_frame.place(x=BUTTONS_FRAME_PLACEX_LEFT,y=DUCKDUCKGO_Y)


#Functions for History/Restricted Tab only

def deletehistory():
    for index_history in reversed(listbox_history.curselection()):
        listbox_history.delete((index_history))
    save_histfile_post_delete()

def clear_history():
    listbox_history.delete(0,END)
    open('history.txt','w',encoding="utf-8").close()


def deleterestricted():
    for index_restricted in reversed(listbox_restricted.curselection()):
        listbox_restricted.delete((index_restricted))
    save_restrictfile_post_delete()

def clear_restricted():
    listbox_restricted.delete(0, END)
    open('restricted.txt','w',encoding="utf-8").close()

def add_restricted():
    listbox_restricted.insert(listbox_restricted.size(),add_restrcit_words.get())
    save_to_restrict(add_restrcit_words.get())

def save_histfile_post_delete():
    contents = (listbox_history.get(0, END))
    hist_file = open('history.txt','w',encoding="utf-8")
    for line in range(len(contents)):
        hist_file.write(f"{contents[line]}\n")
    hist_file.close()

def save_to_history(just_searched):
    hist_file = open('history.txt', 'a', encoding="utf-8")
    hist_file.write(f"{just_searched}\n")
    hist_file.close()

def open_history():
    hist_file = open('history.txt', 'r', encoding="utf-8")
    for line in hist_file:
        listbox_history.insert(listbox_history.size(),line.strip())
    hist_file.close()

######################
def save_restrictfile_post_delete():
    contents = (listbox_restricted.get(0, END))
    restrict_file = open('restricted.txt','w',encoding="utf-8")
    for line in range(len(contents)):
        restrict_file.write(f"{contents[line]}\n")
    restrict_file.close()

def save_to_restrict(recent_searched):
    restrict_file = open('restricted.txt', 'a', encoding="utf-8")
    restrict_file.write(f"{recent_searched}\n")
    restrict_file.close()

def open_restrict():
    restrict_file = open('restricted.txt', 'r', encoding="utf-8")
    for line in restrict_file:
        listbox_restricted.insert(listbox_restricted.size(),line.strip())
    restrict_file.close()

#Search Labels and Buttons for History/Restricted Tab
history_list_frame = Frame(tab2)
history_scrollbar = Scrollbar(history_list_frame,orient=VERTICAL)
history_scrollbar.pack(side=RIGHT,fill=BOTH)

restricted_list_frame = Frame(tab2)
restricted_scrollbar = Scrollbar(restricted_list_frame,orient=VERTICAL)
restricted_scrollbar.pack(side=RIGHT,fill=BOTH)

historytitle_label = Label(tab2,
                   text="Search History",
                   font = ("Times New Roman", 34),
                   fg="black",
                   bg="#C0CFFA")

restrictedtitle_label = Label(tab2,
                   text="Restricted Words",
                   font = ("Times New Roman", 34),
                   fg="black",
                   bg="#ee6b6e")

listbox_history = Listbox(history_list_frame,
                  bg="#C0CFFA",
                  fg = "black",
                  font = ("Times New Roman",24),
                  width=20,
                  selectmode=MULTIPLE,
                  height = 14)#MAX 15

listbox_restricted= Listbox(restricted_list_frame,
                  bg="#ee6b6e",
                  fg = "black",
                  font = ("Times New Roman",24),
                  width=20,
                  selectmode=MULTIPLE,
                  height = 13)#MAX:13or14?

add_restrcit_words = Entry(tab2,
                font = ("Times New Roman", 24),
                fg="white",
                bg="#ee6b6e",
                width = 20,
                relief=RAISED)




#Buttons for History/Restricted Tab
delete_history_button = Button(history_but_frame,image=deletepic,command=deletehistory).grid(row=0,column=0)
clear_history_button = Button(history_but_frame,image=clearpic,command=clear_history,padx= 5).grid(row=0,column=1)

delete_restricted_button = Button(restricted_but_frame,image=deletepic,command=deleterestricted).grid(row=0,column=0)
clear_restricted_button = Button(restricted_but_frame,image=clearpic,command=clear_restricted,padx= 5).grid(row=0,column=1)
add_restricted_button = Button(restricted_but_frame,image=addpic,command=add_restricted,padx= 5).grid(row=0,column=2)

#Packing and Placements for History/Restricted Tab
historytitle_label.place(x=6,y=20)
restrictedtitle_label.place(x=400,y=19)

listbox_history.pack(side=LEFT,fill=BOTH)
listbox_history.config(yscrollcommand=history_scrollbar.set)
history_scrollbar.config(command=listbox_history.yview)
history_list_frame.place(x=6,y=81)

listbox_restricted.pack(side=LEFT,fill=BOTH)
listbox_restricted.config(yscrollcommand=restricted_scrollbar.set)
restricted_scrollbar.config(command=listbox_restricted.yview)
restricted_list_frame.place(x=400,y=124)

history_but_frame.place(x=101,y=644)
restricted_but_frame.place(x=495,y=644)

add_restrcit_words.place(x=400,y=82)

open_history()
open_restrict()

window.mainloop()


