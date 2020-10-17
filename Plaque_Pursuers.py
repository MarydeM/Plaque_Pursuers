# Plaque Pursuers CSC 132 Final Project
# Contributers: Chloe, Nathaniel, Mary
# Last Updated: 10/21/2020
##############################################################################
#Imports Gui libraries
from tkinter import *

#Initializes GUI window and Buttons
class Gui(Frame):
    
    #main Frame Constructor
    def __init__(self, parent, row, column, columnspan, rowspan, sticky = N+S+E+W):
        Frame.__init__(self, parent)
        self.row = row
        self.column = column
        self.columnspan = columnspan
        self.rowspan = rowspan
        self.sticky = sticky
        self.setupGUI()
        
    #mutators and grabers
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
        self.display.grid(row = self.row, column = self.column, columnspan \
                          = self.columnspan, sticky = self.sticky)
        #pack the GUI
        self.pack(fill = BOTH, expand=1)

     #borrowed this from The Reckoner for reference   
# img = PhotoImage(file="images/rpr.gif")
#         button = Button(self, bg="white", image=img, borderwidth = 0, \
#                         highlightthickness = 0, activebackground = "white",\
#                         command = lambda: self.process(")"))
#         button.image = img #sets button image's name
#         button.grid(row = 1, column = 1, sticky = N+S+E+W)

#Creates the main menu
class MainMenu(Gui):

    def __init__(self, parent):
        super().__init__(parent, 4, 4, 4, 4)
        
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
WIDTH, HEIGHT = 800, 600 #800x600 is Fullscreen on a rasp. pi

# create the window
window = Tk()
#set the window WIDTHxHEIGHT
window.geometry("{}x{}".format(WIDTH, HEIGHT))
# set the window title
window.title("The Plaque Pursuers")
# generate the GUI
p = MainMenu(window)
# display the GUI and wait for user interaction
window.mainloop()
