# -----------------------------------------------------------------------------
# Hello there! And welcome to the nightmare I call my code!
# Please, don't steal my code and claim it as your own, not that
# this is code that you would want to claim as your own
# © Patrick Brennan (AM2i9)
# https://github.com/AM2i9/DeskWiper
#-------------------------------------------------------------------------------

from tkinter import *
from tkinter import filedialog,messagebox
from wiper import *
import os

class GUI:

    def __init__(self,root):

        self.root = root
        self.directory = directory
        self.createWidgets()
        self.itemCount = 0

        self.file_extensions = []
        self.movableExtensions = []
        self.destinations = {}

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
        self.scanButton = Button(self.root, text="Start", command= lambda: self.start())

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

        # Ok, its a week later and now I can explain it
        # These next few lines recreate the directory label and count under the item list
        self.itemCountLabel.destroy()
        self.directoryLabel.destroy()

        self.itemCountLabel = Label(self.folder_view_frame,text="{} items".format(self.itemCount))
        self.itemCountLabel.pack(side=BOTTOM,fill=X)

        self.directoryLabel = Label(self.folder_view_frame, text = self.directory)
        self.directoryLabel.pack(side=BOTTOM)

        #Recreates the folder view
        self.folder_view.pack_forget()
        self.folder_view.pack(side= LEFT, fill = BOTH)

        # Recreates the scrollbar
        self.folder_view_scrollbar.pack_forget()
        self.folder_view_scrollbar.pack(side=LEFT,fill = BOTH)
        self.folder_view.config(yscrollcommand = self.folder_view_scrollbar.set)
        self.folder_view_scrollbar.config(command=self.folder_view.yview)

    def start(self): # Function to start the movement process
        self.file_extensions = scan(self.directory)
        self.DirSelectionScreen()

    def DirSelectionScreen(self): # Under this function is alllllllllllllllll of the things that happen when you click start

        class entryBox(GUI): # For later in the code. It was easier to create a class to do this for each individual extension
            def __init__(self, BFrame, extension,x,y):

                self.extension = extension

                self.dir = ""
                self.frame = Frame(BFrame)
                self.frame.grid(row=y,column=x,padx=10,pady=10)

                label = Label(self.frame, text = extension)
                self.entry = Entry(self.frame, textvariable = self.dir)

                # Button to open a file dialoge
                selectButton = Button(self.frame, text="...", command = lambda: self.setEntry(filedialog.askdirectory()))

                label.pack(side=LEFT)
                self.entry.pack(side=LEFT)
                selectButton.pack(side=LEFT)

            def setEntry(self,value): # Sets the text of the entry, for once you have selected one
                self.entry.delete(0,END)
                self.entry.insert(0,value)

                self.dir = value

        def A(self): # Part A! I could not come up with a better name for this, and I was tired, so here we are
            # Part A is where you select the file extensions you wish to move
            self.dirSelection = Toplevel()
            self.dirSelection.title("DeskWiper")

            self.movableExtensions = []

            prompt = Label(self.dirSelection, text="Please enter which file extensions you would like to move:")
            prompt.pack(side=TOP)

            ok_button = Button(self.dirSelection,text="Ok", command = lambda: select_extenstions(self))
            ok_button.pack(side=BOTTOM)

            AFrame = Frame(self.dirSelection)
            AFrame.pack()

            self.selected_extensions = []

            x = 0
            y = 0

            # Creates a checkbox grid for each extension
            for extension in self.file_extensions:
                
                intvar = IntVar()

                self.selected_extensions.append(intvar)

                chkbox = Checkbutton(AFrame, text=extension, var=self.selected_extensions[self.selected_extensions.index(intvar)])

                chkbox.grid(column=x,row=y)

                x = x + 1

                if x > 3:
                    y = y + 1
                    x = 0

        def B(self): # And here we are at the sequel. Honestly, I think these function names are better than most movie names
            # In part B, you select where you would like to move the extensions you selected in part A
            destroyTopLevel(self)
            self.dirSelection = Toplevel()
            self.dirSelection.title("DeskWiper")

            ok_button = Button(self.dirSelection, text="Move Files", command=lambda: startMove(self))
            label = Label(self.dirSelection, text="Please select where you would like to move the files:")
            label.pack(side=TOP)

            ok_button.pack(side=BOTTOM)
            BFrame = Frame(self.dirSelection)
            BFrame.pack(side=BOTTOM)

            self.entryFrames = []

            x = 0
            y = 0

            # Once again, creating a grid
            for extension in self.movableExtensions:
                self.entryFrames.append(entryBox(BFrame, extension,x,y))

                x = x + 1
                if x > 1:
                    y = y + 1
                    x = 0

        def startMove(self): #Well... A second Start... oh well

            # WeLl Of CoUrSe WeRe GoNnA aSk YoU "ARE YOU SURE YOU WISH TO DESTROY YOUR ORGANIZED DESKTOP?!?!"
            if messagebox.askokcancel("Starting move...","Are you sure you wish to continue? This will move all of your selected items."):
                destroyTopLevel(self)
                getDestinations(self)
                self.move()

        def getDestinations(self): # Getting the directories from part B
            for entry in self.entryFrames:
                self.destinations[entry.extension] = entry.dir

        def destroyTopLevel(self): # Destroy the windows created by A and B
            self.dirSelection.destroy()

        def select_extenstions(self): # Get the selected extensions from part A, and then run part B

            self.movableExtensions = []

            for extension in self.selected_extensions:
                self.selected_extensions[self.selected_extensions.index(extension)] = extension.get()

            for ex in self.file_extensions:

                if self.selected_extensions[self.file_extensions.index(ex)] > 0:
                    self.movableExtensions.append(ex)

            B(self)

        A(self) # It all begins at the end

    def move(self): # FINALLY. THE FUNCTION THAT ACTUALLY STARTS THE MOVE
        print("move")
        if not moveFiles(self.directory,self.movableExtensions,self.destinations):
            messagebox.showerror("ERROR","An error occured in moving your files") # Yup. Just not gonna tell you the error
        else:
            messagebox.showinfo("Success", "Your files have been moved.")


