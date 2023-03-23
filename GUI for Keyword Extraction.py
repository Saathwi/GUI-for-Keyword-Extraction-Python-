#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
from tkinter import ttk
from rake_nltk import Rake
import numpy as np
import webbrowser
from googlesearch import search
r = Rake()

window= Tk()
window.title("Keyword Extractor")
window.geometry("700x600")

def key_word():
    global entry
    txt= entry.get()
    r.extract_keywords_from_text(txt)
    a=r.get_ranked_phrases()
    x=np.unique(a)
    label.configure(text=x)



entry= Label(window, text="Enter data:")
entry= Entry(window, width= 40)
entry.focus_set()
entry.pack()

ttk.Button(window, text= "Get Keywords",width= 20, command= key_word).pack(pady=20)

label=Label(window, text="Keywords/Phrases are:",width=100)
label.pack()


def callback(url):
    webbrowser.open_new_tab(url)


def google_search():
    global entry1
    txt= entry1.get()
    for j in search(txt, tld="co.in", num=5, stop=5, pause=2):
        link = Label(window, text=j,font=('Helveticabold', 15), fg="blue")
        link.bind("<Button-1>", lambda e:callback(j)) 
        link.pack()
      
entry1= Label(window, text="Enter the word to search:")
entry1= Entry(window, width= 40)
entry1.focus_set()
entry1.pack()

ttk.Button(window, text= "Search",width= 20, command= google_search).pack(pady=20)

label1=Label(window, text="Google links:",width=200)
label1.pack()

window.mainloop()


# In[ ]:





# In[ ]:




