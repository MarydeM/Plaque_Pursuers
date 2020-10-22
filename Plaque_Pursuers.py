# Plaque Pursuers CSC 132 Final Project
# Contributers: Chloe, Mary
# Last Updated: 10/22/2020
##############################################################################

### the three pound signs means it is a note to delete later ###

#Imports Gui libraries
from tkinter import *

#Initializes GUI window and Buttons
class Gui(Canvas):
    
    #main Frame Constructor
    ###I tried to set "command" to lambda as default, but I kept getting syntax errors.
    def __init__(self, img, comnd, xcoord, ycoord):
        Canvas.__init__(self)
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
        button = Button(window, bg = "white", image = img, borderwidth = 0, \
                        highlightthickness = 0, activebackground = "white",\
                        command = self.comnd)
        #sets button image's name
        button.image = img
        #places button using x and y coordinates
        button.place(x = self.xcoord, y = self.ycoord, anchor = "center")

#Creates the main menu
class MainMenu(Gui):

    def __init__(self):
        super().__init__(self, img, comnd, xcoord, ycoord)
        self.make_buttons()
    
    #creates buttons
    def make_buttons(self):
        B1 = MainMenu("images/test.png", self.hello, 100, 300)
        B1 = MainMenu("images/test.png", self.hello, 700, 300)
    
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

###generating the gui covers up the b.ackground. Fix needed
# generate the GUI
p = Canvas(window)
p.pack(expand = 1, fill = BOTH)

#Set background image
background_image = PhotoImage(file = "images/game_bg.png")
p.create_image(0, 0, anchor = NW, image = background_image)

#Set up main menue
MainMenu()

# display the GUI and wait for user interaction
window.mainloop()