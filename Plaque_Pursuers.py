# Plaque Pursuers CSC 132 Final Project
# Contributers: Chloe, Mary
# Last Updated: 10/22/2020
##############################################################################

### the three pound signs means it is a note to delete later ###

#Imports libraries
import functools
from tkinter import *
import random
from time import sleep

#makes is so the motor abilities can be used or not
global gpio_on
gpio_on == False

#Initializes GUI window and Buttons that navigate menues
class Gui(Canvas):
    
    #main Frame Constructor
    def __init__(self, img, comnd, xcoord, ycoord, name = None):
        Canvas.__init__(self)
        self.img = img
        self.comnd = comnd
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.name = name
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
        
    @property
    def name(self):                   
        return self._name   
                                      
    @name.setter                      
    def name(self, value):            
        self._name = value
        
    # sets up indovidual buttons
    def setupGUI(self):
        img = PhotoImage(file = self.img)
        #creates button and gives it functionality
        button = Button(window, bg = None, image = img, borderwidth = 0, \
                        highlightthickness = 0, activebackground = None,\
                        command = self.comnd, name = self.name)
        #sets button image's name
        button.image = img
        #places button using x and y coordinates
        button.place(x = self.xcoord, y = self.ycoord, anchor = "center")
        # adds the newly created button to a list
        button_list.append(button)

    def changeImg(self, img):
        pass

###This needs to be moved to the Gui class, we need to add a image_index to ever other button as well###
class Game_Gui(Canvas):
    
    #main Frame Constructor
    def __init__(self, img_index, comnd, xcoord, ycoord, name = None):
        Canvas.__init__(self)
        self.img_index = img_index
        self.comnd = comnd
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.name = name
        self.setup_Pipe_GUI()
        
    #mutators and grabers
    @property
    def comnd(self):                   
        return self._comnd    
                                      
    @comnd.setter                      
    def comnd(self, value):            
        self._comnd = value
        
    @property
    def img_index(self):                   
        return self._img_index         
                                      
    @img_index.setter                      
    def img_index(self, value):            
        self._img_index = value 
    
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
        
    @property
    def name(self):                   
        return self._name   
                                      
    @name.setter                      
    def name(self, value):            
        self._name = value
        
    # sets up indovidual buttons
    def setup_Pipe_GUI(self):
        img = pipe_image_list[self.img_index - 1]
        #creates button and gives it functionality
        button = Button(window, bg = "white", image = img, borderwidth = 0, \
                        highlightthickness = 0, activebackground = "white",\
                        name = self.name)
        button.img_index = self.img_index
        button.configure(command = lambda: self.comnd(button))
        #sets button image's name
        button.image = img
        #places button using x and y coordinates
        button.place(x = self.xcoord, y = self.ycoord, anchor = "center")
        # adds the newly created button to a list
        button_list.append(button)

#Creates the main menu
class MainMenu():

    #calls functions that delete all of the previously made buttons and creates
    #new buttons for this class, happens every time a new menu is entered
    def __init__(self):
        self.delete_buttons()
        self.make_buttons()
        window.title("The Plaque Pursuers")
    
    #creates buttons
    def make_buttons(self):
        #left button goes to pipes game
        Gui("images/pipes.png", self.pipes, 200, 300)
        #right button goes to memory game
        Gui("images/memory.png", self.memory, 600, 300)
        # #middle button to move to simon
        # Gui("images/test.png", self.simon, 400, 300)
        #back button closes the game from this menu, typically just 
        #previous menu button
        Gui("images/back_button.png", self.quit_game, 40, 40)
    
    #goes to the new class page, Memory
    def memory(self):
        print("moving to memory")
        Memory()
        
    #goes to the new class page, Pipes
    def pipes(self):
        print("moving to pipes")
        Pipes()

    #goes to the class page, Simon
    def simon(self):
        print("moving to simon")
        Simon()

    #quits the program whenever the back button is pressed while on the menu
    def quit_game(self):
        window.destroy()
    
    #deletes all buttons on the page
    def delete_buttons(self):
        for item in button_list:
            item.destroy()
        #clears the buttons in the list
        button_list.clear()
        
#Plays the card matching memory game
class Memory():
    

    def __init__(self):
        window.title("The Plaque Pursuers: Memory Game")
        self.delete_buttons()
        #makes a list to contain all labels made
        global labels
        labels = []
        #makes a dictionary of the label names and locations
        global label_names
        label_names = {}
        # keeps a list of the cards that have been flipped
        global chosen_cards
        chosen_cards = []
        #keeps score of cards matched
        global score
        score = 0
        #gets card images
        self.get_images()
        self.make_buttons()
    
    #creates buttons and stores names
    def make_buttons(self):
        #makes back button
        Gui("images/back_button.png", self.main_menu, 40, 40)
        #creates golbal a dictionary with card names as keys and 
        #card location as values
        global cards
        cards = {}
        # Makes variable names using a, b, & c for rows and i for columns
        global card_names
        card_names = []
        for n in range(6):
            a = str("a" + str(n))
            b = str("b" + str(n))
            c = str("c" + str(n))
            card_names.append(a)
            card_names.append(b)
            card_names.append(c)
        #distance of cards from the left screen edge
        from_edge = 108
        #card location
        j = 0
        for i in range (6):
            #assigns an image to the front of the card with the same name
            #and location
            self.assign_images(card_names[j], from_edge, 140)
            #creates buttons with unique names to denote their location
            Gui("images/card_back.png", functools.partial(self.flip, \
                        card_names[j]), from_edge, 140, card_names[j])
            self.assign_images(card_names[j + 1], from_edge, 310)
            Gui("images/card_back.png", functools.partial(self.flip, \
                        card_names[j + 1]), from_edge, 310, card_names[j + 1])
            self.assign_images(card_names[j + 2], from_edge, 481)
            Gui("images/card_back.png", functools.partial(self.flip, \
                        card_names[j + 2]), from_edge, 481, card_names[j + 2])
            #adds card names and location in list, x coordinate, and y 
            #coordinate to the dictionary
            cards[card_names[j]] = [j, from_edge, 140]
            cards[card_names[j + 1]] = [j + 1, from_edge, 310]
            cards[card_names[j + 2]] = [j + 2, from_edge, 481]
            #iterates the x axis
            from_edge += 115
            #iterates card location
            j += 3
    
    #gets images to be used on the card fronts
    def get_images(self):
        #creates a list for images
        global images
        images = []
        #adds two of each image to the list
        for i in range (1, 10):
            images.append("images/candy" + str(i) + ".png")
            images.append("images/candy" + str(i) + ".png")
    
    #assigns images for the back of cards        
    def assign_images(self, name, x, y):
        #chooses a random image
        img = random.choice(images)
        picture = PhotoImage(file = img)
        # adds the name of the image as the value; uses the name of the card
        # location (i.e.: a0) as the key
        label_names[name] = img
        #makes a label with the image and turns "name" into an actual label
        name = Label(window, image = picture)
        #anchors image to label
        name.photo = picture
        name.place(x = x, y = y, anchor = "center")
        # Gui(image, functools.partial(None, name), x, y, name)
        #removes the image from the list so it can not be used again
        images.remove(img)
        # adds the name of the image as the value; uses the name of the card
        # location (i.e.: a0) as the key
        labels.append(name)    
        
    #flips a card over by recieving name as input
    #checks for a card match
    def flip(self, name):
        #finds card's location in the list with the dictionary
        card = cards.get(name)[0]
        #hide the card that has been clicked on to reveal its back
        button_list[card + 1].place_forget()
        #updates the window before flipping the cards back over
        window.update()
        self.score_counter(name)
        
    def score_counter(self, name):
        global score
        #keeps track of the cards that have been flipped
        if len(chosen_cards) < 2:
            chosen_cards.append(name)
            print (chosen_cards)
        #if two cards have been selected, check to see if the images match
        if len(chosen_cards) == 2:
            if label_names.get(chosen_cards[0]) == label_names.get(chosen_cards[1]):
                #if they match, iterate the score and clear the selected cards
                score += 1
                chosen_cards.clear()
            #if they do not match, flip cards back over
            else:
                #Places the card back side by taking the name (chosen_cards) as
                #a key, finding the values to that key (cards.get())
                #cards.get[0] = list location, cards.get[1] = x coordinate,
                #cards.get[2] = y coordinate
                button_list[cards.get(chosen_cards[0])[0] + 1].place\
                    (x = cards.get(chosen_cards[0])[1], \
                      y = cards.get(chosen_cards[0])[2], \
                      anchor = "center")
                button_list[cards.get(chosen_cards[1])[0] + 1].place\
                    (x = cards.get(chosen_cards[1])[1], \
                      y = cards.get(chosen_cards[1])[2], \
                      anchor = "center")
                chosen_cards.clear()
                #iterate score
                score += 1
            if score == 9:
                Candy()

    # deletes all labels and goes to the main menu
    def main_menu(self):
        global labels
        for item in labels:
            item.destroy()
        print("moving to menu")
        MainMenu()

    #deletes all buttons on the page    
    def delete_buttons(self):
        for item in button_list:
            item.destroy()
        #clears the buttons in the list
        button_list.clear()
        

#Plays the pipes puzzle game
class Pipes():
    
    def __init__(self):
        self.delete_buttons()
        self.make_buttons()
        
    def forget(self):
        pass
    
    #creates buttons
    def make_buttons(self):
        self.setup_game()
        Gui("images/back_button.png", self.back_menu, 40, 40)

    def setup_game(self):
        #set the variables for the pipe game:
        #Length and width of the pipe grid
        grid_length, grid_width = 5, 7 
        #starting position of the Pipes
        pos_x, pos_y = 150, 150 
        Possible_Pipes = [1, 2, 3, 4, 5, 6, 7]
        #creates a basic grid
        for length in range(grid_length):
            pos_x = 150
            for width in range(grid_width):
                #buttons are created that call the flip_pipe function
                PipeChoice = random.choice(Possible_Pipes)
                #button is created with the image index being put into the game_gui
                Button = Game_Gui(PipeChoice, flip_pipe, pos_x, pos_y)
                pos_x += 75
            pos_y += 75
            
    def back_menu(self):
        print("moving to menu")
        MainMenu()
        
    #deletes all buttons on the page    
    def delete_buttons(self):
        for item in button_list:
            item.destroy()
        #clears the buttons in the list 
        button_list.clear()

#flip button will be outside class so that button can be passed in
def flip_pipe(button):
    #have the image rotated whenever it is clicked here ###functionality needs to be added for "flow"###
    if(button.img_index == 1):
        button.img_index = 2
        button.configure(image = pipe_image_list[button.img_index - 1])
    elif(button.img_index == 2):
        button.img_index = 1
        button.configure(image = pipe_image_list[button.img_index - 1])
    elif(button.img_index == 3):
        button.img_index = 4
        button.configure(image = pipe_image_list[button.img_index - 1])
    elif(button.img_index == 4):
        button.img_index = 5
        button.configure(image = pipe_image_list[button.img_index - 1])
    elif(button.img_index == 5):
        button.img_index = 6
        button.configure(image = pipe_image_list[button.img_index - 1])
    elif(button.img_index == 6):
        button.img_index = 3
        button.configure(image = pipe_image_list[button.img_index - 1])
        
###May delete this later###
# #Plays the simon memory game
# class Simon():
    
#     def __init__(self):
#         self.delete_buttons()
#         self.make_buttons()
#         window.title("The Plaque Pursuers: Simon Says")
    
#     #creates buttons
#     def make_buttons(self):
#         Gui("images/back_button.png", self.back_menu, 40, 40)

#     def back_menu(self):
#         print("moving to menu")
#         MainMenu()
    
#     #deletes all buttons on the page    
#     def delete_buttons(self):
#         for item in button_list:
#             item.destroy()

#call this class when a game is won
class Candy():
    if gpio_on == False:
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

#calls the images for the pipe game after the canvas is created
pipe_image_list = [PhotoImage(file = "images/Pipe1.png"), PhotoImage(file = "images/Pipe2.png"), \
                   PhotoImage(file = "images/Pipe3.png"), PhotoImage(file = "images/Pipe4.png"), \
                   PhotoImage(file = "images/Pipe5.png"), PhotoImage(file = "images/Pipe6.png"), \
                   PhotoImage(file = "images/Pipe7.png")]

#Set background image
background_image = PhotoImage(file = "images/game_bg.png")
p.create_image(0, 0, anchor = NW, image = background_image)

#Sets up & enters the main menue
menu = MainMenu()

# display the GUI and wait for user interaction
window.mainloop()
