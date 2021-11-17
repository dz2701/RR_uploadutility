import tkinter as tk
import tkinter.messagebox
import json
from collections import OrderedDict

def parse_to_json():
    file_data = OrderedDict()
    file_data["title"] = str(title.get())
    file_data["author"] = str(author.get())
    file_data["pubdate"] = str(pubdate.get())
    noofim = int(imageno.get())
    number = int(jsonid.get())
    file_data["img"] = []
    for i in range (1,noofim+1):
        file_data["img"].append("https://firebasestorage.googleapis.com/v0/b/reserverecord-b2de5.appspot.com/o/images%2F{a}-{b}.png?alt=media&token=8a30dc10-a93e-460a-a0f4-2418d7956e04".format(a=number, b=i))
    file_data['captions'] = []
    if(st1.get()!=''):file_data['captions'].append(st1.get())
    if(st2.get()!=''):file_data['captions'].append(st2.get())
    if(st3.get()!=''):file_data['captions'].append(st3.get())
    if(st4.get()!=''):file_data['captions'].append(st4.get())
    file_data['content'] = str(content.get()).replace("\n", "\n")
    file_data['categories'] = []
    if(cat1.get()!=''):file_data['categories'].append(cat1.get())
    if(cat2.get()!=''):file_data['categories'].append(cat2.get())
    if(cat3.get()!=''):file_data['categories'].append(cat3.get())
    
    with open('../{}.json'.format(number), 'w', encoding="utf-8") as f:
        json.dump(file_data, f, ensure_ascii=False, indent="\t")
    print("ConversionFinished!")
    
    tkinter.messagebox.showinfo("Conversion Finished!", "Conversion has been Finished!")

master = tk.Tk()
master.title("RR JSON Generator")
master.geometry('400x450')
tk.Label(master, text="JSON ID:").grid(row=0)
tk.Label(master, text="Title").grid(row=1)
tk.Label(master, text="Author").grid(row=2)
tk.Label(master, text="PubDate(Month Date, Year)").grid(row=3)
tk.Label(master, text="# of images").grid(row=4)
tk.Label(master, text="Content: ").grid(row=5)
tk.Label(master, text="Caption for Image #1").grid(row=6)
tk.Label(master, text="Caption for Image #2").grid(row=7)
tk.Label(master, text="Caption for Image #3").grid(row=8)
tk.Label(master, text="Caption for Image #4").grid(row=9)
tk.Label(master, text="First Category").grid(row=10)
tk.Label(master, text="Second Category").grid(row=11)
tk.Label(master, text="Third Category").grid(row=12)


jsonid = tk.Entry(master)
title = tk.Entry(master)
author = tk.Entry(master)
pubdate = tk.Entry(master)
imageno = tk.Entry(master)
content = tk.Entry(master)
st1 = tk.Entry(master)
st2 = tk.Entry(master)
st3 = tk.Entry(master)
st4 = tk.Entry(master)
cat1 = tk.Entry(master)
cat2 = tk.Entry(master)
cat3 = tk.Entry(master)


jsonid.grid(row=0, column=1)
title.grid(row=1, column=1)
author.grid(row=2, column=1)
pubdate.grid(row=3, column=1)
imageno.grid(row=4, column=1)
content.grid(row=5, column=1)
st1.grid(row=6, column=1)
st2.grid(row=7, column=1)
st3.grid(row=8, column=1)
st4.grid(row=9, column=1)
cat1.grid(row=10, column=1)
cat2.grid(row=11, column=1)
cat3.grid(row=12, column=1)


tk.Button(master,text="Generate .json!",command=parse_to_json).grid(row=13, column=0, sticky=tk.W,pady=6)
tk.Button(master,text='Exit',command=master.quit).grid(row=14,column=0,sticky=tk.W,pady=6)

master.mainloop()
