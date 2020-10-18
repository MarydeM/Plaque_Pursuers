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
    def __init__(self, parent, img, comnd, xcoord, ycoord):
        Frame.__init__(self, parent)
        self.img = img
        self.comnd = comnd
        self.xcoord = xcoord
        self.ycoord = ycoord
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
    def xcoord(self):                   
        return self._xcoord         
                                      
    @xcoord.setter                      
    def xcoord(self, value):            
        self._xcoord = value
    
    @property
    def ycoord(self):                   
        return self._ycoord      
                                      
    @ycoord.setter                      
    def ycoord(self, value):            
        self._ycoord = value
        
    # sets up indovidual buttons
    def setupGUI(self):
        img = PhotoImage(file = self.img)
        #creates button and gives it functionality
        button = Button(self, bg = "white", image = img, borderwidth = 0, \
                        highlightthickness = 0, activebackground = "white",\
                        command = self.comnd)
        #sets button image's name
        button.image = img
        #places button using x and y coordinates
        button.place(x = self.xcoord, y = self.ycoord, anchor = "center")
        self.pack(fill = BOTH, expand=1)

#Creates the main menu
class MainMenu(Gui):

    def __init__(self, parent):
        super().__init__(parent, "images/test.png", self.hello, 400, 300)
    
    ### test function
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

#call this class when a game is won
class Candy:
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

#Set background image.
###I have a higher resolution image, but I could not figure out how to shrink it to the window size
background_image = PhotoImage(file = "images/game_bg.png")
background_label = Label(window, image = background_image)
background_label.place(x = 0, y = 0, relwidth=1, relheight=1)

###generating the gui covers up the background. Fix needed
# generate the GUI
p = MainMenu(window)
p.pack()
# display the GUI and wait for user interaction
window.mainloop()
