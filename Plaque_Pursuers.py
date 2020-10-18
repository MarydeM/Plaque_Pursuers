# Plaque Pursuers CSC 132 Final Project
# Contributers: Chloe, Mary
# Last Updated: 10/21/2020
##############################################################################
#Imports Gui libraries
from tkinter import *

#Initializes GUI window and Buttons
class Gui(Frame):
    
    #main Frame Constructor
    ###I tried to set "command" to lambda as default, but I kept getting syntax errors.
    def __init__(self, parent, img, comnd, row, column, columnspan, \
                 rowspan, sticky = N+S+E+W):
        Frame.__init__(self, parent)
        self.img = img
        self.comnd = comnd
        self.row = row
        self.column = column
        self.columnspan = columnspan
        self.rowspan = rowspan
        self.sticky = sticky
        self.setupGUI()
        
    #mutators and grabers
    @property
    def comnd(self):                   
        return self._comnd    
                                      
    @comnd.setter                      
    def comnd(self, value):            
        self._comnd = value
        
    @property
    def img(self):                   
        return self._img         
                                      
    @img.setter                      
    def img(self, value):            
        self._img = value 
    
    @property
    def row(self):                   
        return self._row           
                                      
    @row.setter                      
    def row(self, value):            
        self._row = value
    
    @property
    def column(self):                   
        return self._column         
                                      
    @column.setter                      
    def column(self, value):            
        self._column = value
        
    @property
    def columnspan(self):                   
        return self._columnspan      
                                      
    @columnspan.setter                      
    def columnspan(self, value):            
        self._columnspan = value
    
    @property
    def rowspan(self):                   
        return self._rowspan 
                                      
    @rowspan.setter                      
    def rowspan(self, value):            
        self._rowspan = value
    
    @property
    def sticky(self):                   
        return self._sticky
                                      
    @sticky.setter                      
    def sticky(self, value):            
        self._sticky = value
        
    # sets up the GUI
    ###We need to add images and commands for buttons
    def setupGUI(self):
        img = PhotoImage(file = self.img)
        button = Button(self, bg = "white", image = img, borderwidth = 0, \
                        highlightthickness = 0, activebackground = "white",\
                        command = self.comnd)
        #sets button image's name
        button.image = img
        button.grid(row = self.row, column = self.column, rowspan = \
                    self.rowspan, columnspan = self.columnspan, sticky = \
                    self.sticky)
        self.pack(fill = BOTH, expand=1)

#Creates the main menu
class MainMenu(Gui):

    def __init__(self, parent):
        super().__init__(parent, "images/test.png", self.hello, 4, 4, 1, 1)
    
    # test function
    def hello(self):
        print("hi, this is a test")
        
#Plays the card matching memory game
class Memory(Gui):
    pass

#Plays the picture unscrambling game
class PictureScramble(Gui):
    pass

#Plays the pipes puzzle game
class Pipes(Gui):
    pass

#Plays the simon memory game
class Simon(Gui):
    pass


################
# Main Program #
################
#window resolution
#800x600 is Fullscreen on a rasp. pi
WIDTH, HEIGHT = 800, 600

# create the window
window = Tk()
#set the window WIDTHxHEIGHT
window.geometry("{}x{}".format(WIDTH, HEIGHT))
# set the window title
window.title("The Plaque Pursuers")
#set main background
window.image = PhotoImage(file="images/game_bg.png")
# generate the GUI
p = MainMenu(window)
# display the GUI and wait for user interaction
window.mainloop()
