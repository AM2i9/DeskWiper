from tkinter import *
from tkinter import filedialog
from wiper import *
import os

class GUI:

    def __init__(self,root):

        self.root = root
        self.directory = directory
        self.createWidgets()
        self.itemCount = 0

    def createWidgets(self):
        # Buttom to open Select folder dialouge
        self.openFolderButton = Button(self.root, text="Open Folder", command = lambda: self.openFolder())

        #Frame that contains the folder view
        self.folder_view_frame = Frame(self.root)
        self.folder_view_frame.pack(side=LEFT, fill = BOTH)

        # folder view itself
        self.folder_view = Listbox(self.folder_view_frame, width=50,height=30,bg = "white", font="Helvetica", fg="black")

        #Item count and directory that go below the folder view
        self.itemCountLabel = Label(self.folder_view_frame,text="0 items")
        self.directoryLabel = Label(self.folder_view_frame, text = "dir")

        #Folder view scrollbar
        self.folder_view_scrollbar = Scrollbar(self.folder_view_frame)

        #Updates folderview
        self.updateFolderView()

        self.folder_view.pack(side= LEFT, fill = BOTH)

        self.folder_view_scrollbar.pack(side=LEFT,fill = BOTH)
        self.folder_view.config(yscrollcommand = self.folder_view_scrollbar.set)
        self.folder_view_scrollbar.config(command=self.folder_view.yview)

        # Buttons
        self.scanButton = Button(self.root, text="Scan", command= lambda: print(scan(self.directory)))

        self.openFolderButton.pack(side=TOP)
        self.scanButton.pack(side=TOP)

    def openFolder(self): # Function to open file dialouge
        self.directory = filedialog.askdirectory()
        self.updateFolderView()
    
    def updateFolderView(self): # Updates folder view

        self.itemCount = len(os.listdir(self.directory)) # gets item count
        
        self.folder_view.delete(0,END) # Removes items from folder view

        for file in os.listdir(self.directory): # adds new items
            self.folder_view.insert(END, file)

        # These next lines remove the parts of the folder view and repack them with the right values and in the right place
        # Its 10pm, I don't have anymore braincells left to describe this
        self.itemCountLabel.destroy()
        self.directoryLabel.destroy()

        self.itemCountLabel = Label(self.folder_view_frame,text="{} items".format(self.itemCount))
        self.itemCountLabel.pack(side=BOTTOM,fill=X)

        self.directoryLabel = Label(self.folder_view_frame, text = self.directory)
        self.directoryLabel.pack(side=BOTTOM)

        self.folder_view.pack_forget()
        self.folder_view.pack(side= LEFT, fill = BOTH)

        self.folder_view_scrollbar.pack_forget()
        self.folder_view_scrollbar.pack(side=LEFT,fill = BOTH)
        self.folder_view.config(yscrollcommand = self.folder_view_scrollbar.set)
        self.folder_view_scrollbar.config(command=self.folder_view.yview)