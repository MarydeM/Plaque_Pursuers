# Plaque Pursuers CSC 132 Final Project
# Contributers: Chloe, Mary
# Last Updated: 10/22/2020
##############################################################################

### the three pound signs means it is a note to delete later ###

### here is the website about making and deleting frames
### https://stackoverflow.com/questions/45905665/is-there-a-way-to-clear-all-widgets-from-a-tkinter-window-in-one-go-without-refe/45915006

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
        # adds the newly created button to a list
        button_list.append(button)

#Creates the main menu
class MainMenu():

    #calls functions that delete all of the previously made buttons and creates
    #new buttons for this class
    def __init__(self):
        self.delete_buttons()
        self.make_buttons()
    
    #creates buttons
    def make_buttons(self):
        # test buttons
        B1 = Gui("images/test.png", self.hello, 150, 300)
        B2 = Gui("images/test.png", self.hello, 650, 300)
        # back button, goes to Memory
        B2 = Gui("images/back_button.png", self.memory, 40, 40)
    
    ### test function
    def hello(self):
        ### These functions can be used to call the class assigned to the button
        ### Ex: the Memory game button would call the memory class
        print("hi, this is a test")
    
    #goes to the new class page
    def memory(self):
        Memory()
    
    #deletes all buttons on the page
    def delete_buttons(self):
        for item in button_list:
            item.destroy()
        
#Plays the card matching memory game
class Memory():
    
    def __init__(self):
        self.delete_buttons()
        self.make_buttons()
    
    #creates buttons
    def make_buttons(self):
        pass

    #deletes all buttons on the page    
    def delete_buttons(self):
        for item in button_list:
            item.destroy()

#Plays the pipes puzzle game
class Pipes():
    
    def __init__(self):
        self.make_buttons()
        
    def forget(self):
        pass
    
    #creates buttons
    def make_buttons(self):
        self.setup_game()
        B3 = Gui("images/Exit.png", self.back_menu, 50, 25)

    def setup_game(self):
        #set the variables for the pipe game
        grid_length, grid_width = 5, 7 #Length and width of the pipe grid
        pos_x, pos_y = 150, 150 #starting position of the Pipes
        Possible_Pipes = ["images/Pipe.png", "images/PipeSideways.png"]
        #creates a basic grid
        for length in range(grid_length):
            pos_x = 150
            for width in range(grid_width):
                #buttons are created that call the flip_pipe function
                PipeChoice = random.randint(0, 1)
                if(PipeChoice == 0):
                    Button = Gui("images/PipeSideways.png", self.flip_pipe, pos_x, pos_y)
                elif(PipeChoice == 1):
                    Button = Gui("images/Pipe.png", self.flip_pipe, pos_x, pos_y)
                pos_x += 75
            pos_y += 75

    def flip_pipe(self):
        #have the image flip whenever it is clicked here
        print ("test flip")
    
    #deletes all buttons on the page    
    def delete_buttons(self):
        for item in button_list:
            item.destroy()

#Plays the simon memory game
class Simon():
    
    def __init__(self):
        self.make_buttons()
    
    #creates buttons
    def make_buttons(self):
        pass
    
    #deletes all buttons on the page    
    def delete_buttons(self):
        for item in button_list:
            item.destroy()

#call this class when a game is won
class Candy():
    pass

################
# Main Program #
################
#will keep a list of created buttons to make them easier to delete
button_list = []

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
menu = MainMenu()

# display the GUI and wait for user interaction
window.mainloop()
