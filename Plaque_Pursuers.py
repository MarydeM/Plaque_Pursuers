# Plaque Pursuers CSC 132 Final Project
# Contributers: Chloe, Mary
# Last Updated: 11/05/2020
##############################################################################

#Imports libraries
import functools
from tkinter import *
import random
from time import sleep

#makes is so the motor abilities can be used or not
global gpio_on
#set false when not on rasp py
gpio_on = False

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
        
    # sets up individual buttons
    def setupGUI(self):
        img = PhotoImage(file = self.img)
        #creates button and gives it functionality
        button = Button(window, bg = "white", image = img, borderwidth = 0, \
                        highlightthickness = 0, activebackground = None,\
                        command = self.comnd, name = self.name)
        #sets button image's name
        button.image = img
        #places button using x and y coordinates
        button.place(x = self.xcoord, y = self.ycoord, anchor = "center")
        # adds the newly created button to a list
        button_list.append(button)

class Game_Gui(Canvas):
    
    #main Frame Constructor
    def __init__(self, img_index, location, pipe_connected,comnd, xcoord, ycoord, name = None):
        Canvas.__init__(self)
        self.img_index = img_index
        self.location = location
        self.pipe_connected = pipe_connected
        self.comnd = comnd
        self.xcoord = xcoord
        self.ycoord = ycoord
        self.name = name
        self.setup_Pipe_GUI()
        
    #mutators and grabers
    @property
    def location(self):
        return self._location

    @location.setter                      
    def location(self, value):            
        self._location = value

    @property
    def pipe_connected(self):                   
        return self._pipe_connected         
                                      
    @pipe_connected.setter                      
    def pipe_connected(self, value):            
        self._pipe_connected = value
        
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
        
    # sets up indovidual buttons for the pipe puzzle
    def setup_Pipe_GUI(self):
        img = pipe_image_list[self.img_index - 1]
        #creates button and gives it functionality
        button = Button(window, bg = "white", image = img, borderwidth = 0, \
                        highlightthickness = 0, activebackground = "white",\
                        name = self.name)
        #if it is connected == 1, otherwise == 0
        button.pipe_connected = self.pipe_connected
        #to change the image of a pipe
        button.img_index = self.img_index
        #location in the grid of the pipe
        button.location = self.location
        button.configure(command = lambda: self.comnd(button))
        #sets button image's name
        button.image = img
        #places button using x and y coordinates
        button.place(x = self.xcoord, y = self.ycoord, anchor = "center")
        # adds the newly created button to a list
        button_list.append(button)
        made_pipes.append(button)

#Creates the main menu
class MainMenu():

    #calls functions that delete all of the previously made buttons and creates
    #new buttons for this class, happens every time a new menu is entered
    def __init__(self):
        self.delete_buttons()
        self.make_buttons()
    
    #creates buttons
    def make_buttons(self):
        #left button goes to pipes game
        Gui("images/pipes.png", self.pipes, 200, 250)
        #right button goes to memory game
        Gui("images/memory.png", self.memory, 600, 250)
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
        self.delete_buttons()
        #makes a list to contain all labels made
        global labels
        labels = []
        #makes a dictionary of the label names and images
        global label_names
        label_names = {}
        # keeps a list of the cards that have been flipped
        global chosen_cards
        chosen_cards = []
        #keeps score of cards matched
        global score
        score = 0
        #counts lives
        global lives
        global lives_left
        lives_left = 15
        #gets card images
        self.get_images()
        self.make_buttons()
    
    #creates buttons and stores names
    def make_buttons(self):
        #makes back button
        Gui("images/back_button.png", self.main_menu, 40, 40)
        #makes life counter
        global lives_left
        global lives
        lives = Label(window, text = "Lives Left \n" + str(lives_left), \
                      bg = "white", borderwidth = 2, relief = "raised")
        lives.place(x = 735, y = 40)
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
        from_edge = 140
        #card location
        j = 0
        for i in range (6):
            #assigns an image to the front of the card with the same name
            #and location
            self.assign_images(card_names[j], from_edge, 90)
            #creates buttons with unique names to denote their location
            Gui("images/card_back.png", functools.partial(self.flip, \
                        card_names[j]), from_edge, 90, card_names[j])
            self.assign_images(card_names[j + 1], from_edge, 245)
            Gui("images/card_back.png", functools.partial(self.flip, \
                        card_names[j + 1]), from_edge, 245, card_names[j + 1])
            self.assign_images(card_names[j + 2], from_edge, 400)
            Gui("images/card_back.png", functools.partial(self.flip, \
                        card_names[j + 2]), from_edge, 400, card_names[j + 2])
            #adds card names and location in list, x coordinate, and y 
            #coordinate to the dictionary
            cards[card_names[j]] = [j, from_edge, 90]
            cards[card_names[j + 1]] = [j + 1, from_edge, 245]
            cards[card_names[j + 2]] = [j + 2, from_edge, 400]
            #iterates the x axis
            from_edge += 108
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
        #makes a label with the image and turns "lab" into the actual label
        lab = Label(window, image = picture)
        #anchors image to label
        lab.photo = picture
        lab.place(x = x, y = y, anchor = "center")
        # adds the name of the image and the label as the value; uses the \
        #name of the card location (i.e.: a0) as the key
        label_names[name] = [img, lab]
        #removes the image from the list so it can not be used again
        images.remove(img)
        # adds the label to a list for easy deletion later
        labels.append(lab)
        
    #flips a card over by recieving name as input
    #checks for a card match
    def flip(self, name):
        global lives_left
        #finds card's location in the list with the dictionary
        card = cards.get(name)[0]
        #hide the card that has been clicked on to reveal its back, only while
        #the game is being played
        if lives_left > 0:
            button_list[card + 1].place_forget()
            #updates the window before flipping the cards back over
            window.update()
            self.score_counter(name)
        
    def score_counter(self, name):
        global score
        #keeps track of the cards that have been flipped
        if len(chosen_cards) < 2:
            chosen_cards.append(name)
        #if two cards have been selected, check to see if the images match
        if len(chosen_cards) == 2:
            if label_names.get(chosen_cards[0])[0] == label_names.get(chosen_cards[1])[0]:
                #if they match, highlight the cards chosen
                label_names.get(chosen_cards[0])[1].config(borderwidth = 4, \
                            relief = "groove")
                label_names.get(chosen_cards[1])[1].config(borderwidth = 4, \
                            relief = "groove")
                #iterate the score and clear the selected cards
                score += 1
                chosen_cards.clear()
            #if they do not match, flip cards back over
            else:
                sleep(1)
                #Places the card's back side by taking the name (chosen_cards) as
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
                # Take away a life
                global lives_left
                lives_left -= 1
                lives.configure(text = "Lives Left \n" + str(lives_left))
            #Tell the player the game is over
            if lives_left == 0:
                lives.configure(text = "Game \n Over")
            #Dispense candy when the GPIO is on
            if score == 9:
                Candy.dispense()

    # deletes all labels and goes to the main menu
    def main_menu(self):
        global labels
        for item in labels:
            item.destroy()
        lives.destroy()
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
        #sets up image list to be used for the Pipe puzzle
        global pipe_image_list
        pipe_image_list = [PhotoImage(file = "images/Pipe1.png"), PhotoImage(file = "images/Pipe2.png"), \
                   PhotoImage(file = "images/Pipe3.png"), PhotoImage(file = "images/Pipe4.png"), \
                   PhotoImage(file = "images/Pipe5.png"), PhotoImage(file = "images/Pipe6.png"), \
                   PhotoImage(file = "images/Pipe7.png"), PhotoImage(file = "images/Pipe1_light.png"), \
                   PhotoImage(file = "images/Pipe2_light.png"), PhotoImage(file = "images/Pipe3_light.png"), \
                   PhotoImage(file = "images/Pipe4_light.png"), PhotoImage(file = "images/Pipe5_light.png"), \
                   PhotoImage(file = "images/Pipe6_light.png"), PhotoImage(file = "images/Pipe7_light.png"), \
                   PhotoImage(file = "images/sink.png"), PhotoImage(file = "images/sink_light.png"), \
                   PhotoImage(file = "images/flow.png"), PhotoImage(file = "images/start_flow.png"), \
                           PhotoImage(file = "images/back_to_menu.png")]
        #clear the main menu and create the pipe game
        self.delete_buttons()
        self.make_buttons()
    
    #creates buttons
    def make_buttons(self):
        #create a background for the pipes using a rectangle
        global rect
        rect = p.create_rectangle(110, 60, 790, 440, fill = "white")
        self.setup_game()
        #create the back to menu button
        Gui("images/back_button.png", self.back_menu, 40, 40)
        #create the flow
        Gui("images/flow.png", None, 150, 100)
        #Sink, 40 is end goal, it is an arbitrary number
        global sink
        sink = Game_Gui(15, 40, False, flip_pipe, 750, 100)
        #flow is the start the flow button
        flow = Game_Gui(18, -50, False, Flow, 450, 30)

    def setup_game(self):
        #if the pipes reach the goal pipe_win will be set to true
        global pipe_win
        pipe_win = False
        #set the variables for the pipe game:
        #Length and width of the pipe grid
        grid_length, grid_width = 5, 7 
        #starting position of the Pipes
        pos_x, pos_y = 225, 100
        #1==vertical, 2==horizontal, 3==down to right,4==up to right, 5==left to up, 6==left to down,
        #7==up to down and left to right.
        Possible_Pipes = [1, 2, 3, 4, 5, 6, 7]
        #there will be a number of possible boards to use as a base, to ensure there is at least
        #one valid path to the sink
        Boards = [1, 2, 3]
        #location == where on the 5x7 board the button is
        location = 1
        #randomly choose a board to use as a base
        board_choice = random.choice(Boards)
        #creates a basic grid
        for length in range(grid_length):
            pos_x = 225
            for width in range(grid_width):
                #buttons are created that call the flip_pipe function
                PipeChoice = random.choice(Possible_Pipes)
                #button is created with the image index being put into the game_gui
                #if the board is board1, create this board
                if(board_choice == 1):
                    if(location <= 2):
                        Button = Game_Gui(1, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 3):
                        Button = Game_Gui(3, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 10):
                        Button = Game_Gui(2, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 17):
                        Button = Game_Gui(6, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 18):
                        Button = Game_Gui(6, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 12) or (location == 13):
                        Button = Game_Gui(6, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 7):
                        Button = Game_Gui(5, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 19):
                        Button = Game_Gui(3, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 11):
                        Button = Game_Gui(5, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 20):
                        Button = Game_Gui(6, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 13):
                        Button = Game_Gui(6, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 14):
                        Button = Game_Gui(3, location, False, flip_pipe, pos_x, pos_y)
                    #fill rest
                    else:
                        Button = Game_Gui(PipeChoice, location, False, flip_pipe, pos_x, pos_y)
                #2nd board choice
                elif(board_choice == 2):
                    if(location == 1):
                        Button = Game_Gui(3, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 7) or (location == 8):
                        Button = Game_Gui(6, location, False, flip_pipe, pos_x, pos_y)
                    elif(location <= 13) and (location >= 10):
                        Button = Game_Gui(4, location, False, flip_pipe, pos_x, pos_y)
                    elif(location <= 21) and (location >= 16):
                        Button = Game_Gui(5, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 9):
                        Button = Game_Gui(7, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 14):
                        Button = Game_Gui(2, location, False, flip_pipe, pos_x, pos_y)
                    #fill rest
                    else:
                        Button = Game_Gui(PipeChoice, location, False, flip_pipe, pos_x, pos_y)
                #board option #3
                elif(board_choice == 3):
                    if(location == 1):
                        Button = Game_Gui(3, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 7):
                        Button = Game_Gui(7, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 8):
                        Button = Game_Gui(6, location, False, flip_pipe, pos_x, pos_y)
                    elif(location <= 21) and (location >= 16):
                        Button = Game_Gui(5, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 9):
                        Button = Game_Gui(7, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 14):
                        Button = Game_Gui(1, location, False, flip_pipe, pos_x, pos_y)
                    elif(location == 24):
                        Button = Game_Gui(7, location, False, flip_pipe, pos_x, pos_y)
                    elif(location >= 25) and (location <= 27):
                        Button = Game_Gui(3, location, False, flip_pipe, pos_x, pos_y)
                    #fill rest
                    else:
                        Button = Game_Gui(PipeChoice, location, False, flip_pipe, pos_x, pos_y)
                #increases the location in the grid by one
                location += 1
                #moves x cord by 75 for next x
                pos_x += 75
            #moves y cord by 75 for next y
            pos_y += 75

    #return to main menu if back button is pressed
    def back_menu(self):
        #delete the rectangle
        global rect
        p.delete(rect)
        print("moving to menu")
        #clear the made_pipes list
        made_pipes.clear()
        #return to menu
        MainMenu()
        
    #deletes all buttons on the page    
    def delete_buttons(self):
        for item in button_list:
            item.destroy()
        #clears the buttons in the list 
        button_list.clear()

#flip button will be outside class so that button can be passed in
def flip_pipe(button):
    #if the game is won, do not allow for the pipes to be clicked
    global pipe_win
    if(pipe_win == False):
        #the image index is one above the actual number in the index!!
        #have the image rotated whenever it is clicked here
        #end goal/the sink, does nothing when pressed
        if(button.location == 40):
            return
        #if a pipe is clicked, the image will change to the roatated pipe
        #vertical to horiontal
        if(button.img_index == 1):
            button.img_index = 2 
            button.configure(image = pipe_image_list[button.img_index - 1])
        #horizontal to vertical
        elif(button.img_index == 2):
            button.img_index = 1
            button.configure(image = pipe_image_list[button.img_index - 1])
        #S and E to N and E
        elif(button.img_index == 3):
            button.img_index = 4
            button.configure(image = pipe_image_list[button.img_index - 1])
        #N and E to N and W
        elif(button.img_index == 4):
            button.img_index = 5
            button.configure(image = pipe_image_list[button.img_index - 1])
        #N and W to S and W
        elif(button.img_index == 5):
            button.img_index = 6
            button.configure(image = pipe_image_list[button.img_index - 1])
        #S and W back to S and E
        elif(button.img_index == 6):
            button.img_index = 3
            button.configure(image = pipe_image_list[button.img_index - 1])

#the flow button will activate this function
def Flow(button):
    global pipe_win
    #when the game is won, change to True
    #go through the for loop multiple times so the flow and move
    for number in range(0, 10):
        #go through the for loop every time a button is pressed to know if a true statement needs to change
        for check in made_pipes:
            if(check.location == 7):
                #if pipe below
                if(made_pipes[check.location + 6].img_index == 8) or \
                    (made_pipes[check.location + 6].img_index == 12) or \
                    (made_pipes[check.location + 6].img_index == 14):
                    #if current pipe can take from below
                    if(made_pipes[check.location - 1].img_index == 2) or \
                        (made_pipes[check.location - 1].img_index == 9) or \
                        (made_pipes[check.location - 1].img_index == 3) or \
                        (made_pipes[check.location - 1].img_index == 10) or \
                        (made_pipes[check.location - 1].img_index == 7) or \
                        (made_pipes[check.location - 1].img_index == 14):
                        #skip if already won
                        if(pipe_win == True): 
                            break
                        made_pipes[check.location - 1].pipe_connected == True
                        check.img_index += 7
                        check.configure(image = pipe_image_list[check.img_index - 1])
                        pipe_win = True
                        #index 37 is the final button
                        made_pipes[35].img_index = 16
                        made_pipes[35].configure(image = pipe_image_list[made_pipes[35].img_index - 1])
                        print("You win")
                        #break out of loop if you win
                        break
                #if pipe to the left
                if(made_pipes[check.location - 2].img_index == 9) or \
                    (made_pipes[check.location - 2].img_index == 10) or \
                    (made_pipes[check.location - 2].img_index == 14):
                    #if current pipe can take from left
                    if(made_pipes[check.location - 1].img_index == 2) or \
                        (made_pipes[check.location - 1].img_index == 9) or \
                        (made_pipes[check.location - 1].img_index == 7) or \
                        (made_pipes[check.location - 1].img_index == 14):
                        #skip if already won
                        if(pipe_win == True): 
                            break
                        made_pipes[check.location - 1].pipe_connected == True
                        check.img_index += 7
                        check.configure(image = pipe_image_list[check.img_index - 1])
                        pipe_win = True
                        #index 37 is the final button
                        made_pipes[35].img_index = 16
                        made_pipes[35].configure(image = pipe_image_list[made_pipes[35].img_index - 1])
                        print("You win")
                        #break out of loop if you win
                        break
            #check to the left of the current checking pipe
            #if true to left, make true except when on edge
            try:
                if(made_pipes[check.location - 1].location != 1):
                    if(made_pipes[check.location - 2].pipe_connected == True) and \
                        (made_pipes[check.location - 1].location != 29) or \
                        (made_pipes[check.location - 1].location != 22) or \
                        (made_pipes[check.location - 1].location != 15) or \
                        (made_pipes[check.location - 1].location != 8):
                        #check left most pipe
                        if(made_pipes[check.location - 2].img_index == 9) \
                            or (made_pipes[check.location - 2].img_index == 10) \
                            or (made_pipes[check.location - 2].img_index == 11) \
                            or (made_pipes[check.location - 2].img_index == 14):
                            #if image is horizontal no flow
                            if(made_pipes[check.location - 1].img_index == 2):
                                if(made_pipes[check.location - 1].location != 29) or \
                                (made_pipes[check.location - 1].location != 22) or \
                                (made_pipes[check.location - 1].location != 15) or \
                                (made_pipes[check.location - 1].location != 8):
                                    made_pipes[check.location - 1].pipe_connected = True
                                    made_pipes[check.location - 1].img_index = 9
                                    check.configure(image = pipe_image_list[check.img_index - 1])
                            #west and north pipe
                            elif(made_pipes[check.location - 1].img_index == 5):
                                if(made_pipes[check.location - 1].location != 29) or \
                                (made_pipes[check.location - 1].location != 22) or \
                                (made_pipes[check.location - 1].location != 15) or \
                                (made_pipes[check.location - 1].location != 8):
                                    made_pipes[check.location - 1].pipe_connected = True
                                    made_pipes[check.location - 1].img_index = 12
                                    check.configure(image = pipe_image_list[check.img_index - 1])
                            #west and south pipe
                            elif(made_pipes[check.location - 1].img_index == 6):
                                if(made_pipes[check.location - 1].location != 29) or \
                                (made_pipes[check.location - 1].location != 22) or \
                                (made_pipes[check.location - 1].location != 15) or \
                                (made_pipes[check.location - 1].location != 8):
                                    made_pipes[check.location - 1].pipe_connected = True
                                    made_pipes[check.location - 1].img_index = 13
                                    check.configure(image = pipe_image_list[check.img_index - 1])
                            #4 way
                            elif(made_pipes[check.location - 1].img_index == 7):
                                if(made_pipes[check.location - 1].location != 29) or \
                                (made_pipes[check.location - 1].location != 22) or \
                                (made_pipes[check.location - 1].location != 15) or \
                                (made_pipes[check.location - 1].location != 8):
                                    made_pipes[check.location - 1].pipe_connected = True
                                    made_pipes[check.location - 1].img_index = 14
                                    check.configure(image = pipe_image_list[check.img_index - 1])
                            if(made_pipes[check.location - 2].img_index != 9) and \
                                    (made_pipes[check.location - 2].img_index != 10) and \
                                    (made_pipes[check.location - 2].img_index != 11) and \
                                    (made_pipes[check.location - 2].img_index != 14):
                                    made_pipes[check.location - 1].pipe_connected = False
            except:
                pass
            #check first spot
            try:
                if(made_pipes[check.location - 1].location == 1):
                    if(made_pipes[0].img_index == 2):
                        made_pipes[0].pipe_connected = True
                        made_pipes[0].img_index = 9
                        made_pipes[0].configure(image = pipe_image_list[check.img_index - 1])
                    if(made_pipes[0].img_index == 5):
                        made_pipes[0].pipe_connected = True
                        made_pipes[0].img_index = 12
                        made_pipes[0].configure(image = pipe_image_list[check.img_index - 1])
                    if(made_pipes[0].img_index == 6):
                        made_pipes[0].pipe_connected = True
                        made_pipes[0].img_index = 13
                        made_pipes[0].configure(image = pipe_image_list[check.img_index - 1])
                    if(made_pipes[0].img_index == 7):
                        made_pipes[0].pipe_connected = True
                        made_pipes[0].img_index = 14
                        made_pipes[0].configure(image = pipe_image_list[check.img_index - 1])
            except:
                pass
            #if true above, make true
            try:
                if(made_pipes[check.location - 8].pipe_connected == True):
                    if(made_pipes[check.location - 1].location > 7):
                        if(made_pipes[check.location - 8].img_index == 8) or (made_pipes[check.location - 8].img_index == 10)\
                            or (made_pipes[check.location - 8].img_index == 13) \
                            or (made_pipes[check.location - 8].img_index == 14):
                            #if image is vertical no flow
                            if(made_pipes[check.location - 1].img_index == 1):
                                made_pipes[check.location - 1].pipe_connected = True
                                made_pipes[check.location - 1].img_index = 8
                                check.configure(image = pipe_image_list[check.img_index - 1])
                            #west and north pipe
                            elif(made_pipes[check.location - 1].img_index == 5):
                                made_pipes[check.location - 1].pipe_connected = True
                                made_pipes[check.location - 1].img_index = 12
                                check.configure(image = pipe_image_list[check.img_index - 1])
                            #east and north pipe
                            elif(made_pipes[check.location - 1].img_index == 4):
                                made_pipes[check.location - 1].pipe_connected = True
                                made_pipes[check.location - 1].img_index = 11
                                check.configure(image = pipe_image_list[check.img_index - 1])
                            #4 way
                            elif(made_pipes[check.location - 1].img_index == 7):
                                made_pipes[check.location - 1].pipe_connected = True
                                made_pipes[check.location - 1].img_index = 14
                                check.configure(image = pipe_image_list[check.img_index - 1])
                            if(made_pipes[check.location - 8].img_index != 8) and \
                                (made_pipes[check.location - 8].img_index != 10) and \
                                (made_pipes[check.location - 8].img_index != 13) and \
                                (made_pipes[check.location - 8].img_index != 14):
                                made_pipes[check.location - 1].pipe_connected = False
            except:
                pass
            #if true below, make true
            try:
                if(made_pipes[check.location + 6].pipe_connected == True):
                    #check pipe below
                    if(made_pipes[check.location + 6].img_index == 8) or (made_pipes[check.location + 6].img_index == 11)\
                        or (made_pipes[check.location + 6].img_index == 12) \
                        or (made_pipes[check.location + 6].img_index == 14):
                        #if image is vertical no flow
                        if(made_pipes[check.location - 1].img_index == 1):
                            made_pipes[check.location - 1].pipe_connected = True
                            made_pipes[check.location - 1].img_index = 8
                            check.configure(image = pipe_image_list[check.img_index - 1])
                        #west and south pipe
                        elif(made_pipes[check.location - 1].img_index == 6):
                            made_pipes[check.location - 1].pipe_connected = True
                            made_pipes[check.location - 1].img_index = 13
                            check.configure(image = pipe_image_list[check.img_index - 1])
                        #east and south pipe
                        elif(made_pipes[check.location - 1].img_index == 3):
                            made_pipes[check.location - 1].pipe_connected = True
                            made_pipes[check.location - 1].img_index = 10
                            check.configure(image = pipe_image_list[check.img_index - 1])
                        #4 way
                        elif(made_pipes[check.location - 1].img_index == 7):
                            made_pipes[check.location - 1].pipe_connected = True
                            made_pipes[check.location - 1].img_index = 14
                            check.configure(image = pipe_image_list[check.img_index - 1])
                        if(made_pipes[check.location + 6].img_index != 8) and \
                            (made_pipes[check.location + 6].img_index != 10) and \
                            (made_pipes[check.location + 6].img_index != 13) and \
                            (made_pipes[check.location + 6].img_index != 14):
                            made_pipes[check.location - 1].pipe_connected = False
            except:
                pass
            try:
                #if right true, except on right edge
                if(made_pipes[check.location].pipe_connected == True) and \
                    (made_pipes[check.location].location != made_pipes[34].location) or \
                    (made_pipes[check.location].location != made_pipes[28].location) or \
                    (made_pipes[check.location].location != made_pipes[21].location) or \
                    (made_pipes[check.location].location != made_pipes[14].location) or \
                    (made_pipes[check.location].location != made_pipes[7].location):
                    #check right most pipe
                    if(made_pipes[check.location].img_index == 9) or (made_pipes[check.location].img_index == 12)\
                        or (made_pipes[check.location].img_index == 13) \
                        or (made_pipes[check.location].img_index == 14):
                        #if image is horizontal no flow
                        if(made_pipes[check.location - 1].img_index == 2):
                            made_pipes[check.location - 1].pipe_connected = True
                            made_pipes[check.location - 1].img_index = 9
                            check.configure(image = pipe_image_list[check.img_index - 1])
                        #north and east
                        elif(made_pipes[check.location - 1].img_index == 4):
                            made_pipes[check.location - 1].pipe_connected = True
                            made_pipes[check.location - 1].img_index = 11
                            check.configure(image = pipe_image_list[check.img_index - 1])
                        #east and south pipe
                        elif(made_pipes[check.location - 1].img_index == 3):
                            made_pipes[check.location - 1].pipe_connected = True
                            made_pipes[check.location - 1].img_index = 10
                            check.configure(image = pipe_image_list[check.img_index - 1])
                        #4 way
                        elif(made_pipes[check.location - 1].img_index == 7):
                            made_pipes[check.location - 1].pipe_connected = True
                            made_pipes[check.location - 1].img_index = 14
                            check.configure(image = pipe_image_list[check.img_index - 1])
                        if(made_pipes[check.location].img_index != 9) and \
                                (made_pipes[check.location].img_index != 12) and \
                                (made_pipes[check.location].img_index != 13) and \
                                (made_pipes[check.location].img_index != 14):
                                made_pipes[check.location - 1].pipe_connected = False
            except:
                pass
            try:
                if(made_pipes[check.location - 1].img_index > 7):
                    made_pipes[check.location - 1].pipe_connected = True
                if(made_pipes[check.location - 1].img_index <= 7):
                    made_pipes[check.location - 1].pipe_connected = False
            except:
                pass
    #after updating all the pipes
    window.update()
    #check if game is won, and if so dispense candy
    if(pipe_win == True):
        #have a slight pause here
        sleep(0.5)
        #show that the player is returning to menu
        returning = Game_Gui(19, -60, False, flip_pipe, 400, 240)
        window.update()
        print("dispensing candy")
        Candy.dispense()
        #wait 5 seconds after winning before returning to menu
        sleep(5)
        #delete the rectangle
        global rect
        p.delete(rect)
        #return to Menu
        Pipes().back_menu()
    #if the game is not over, change back to regular pipes so the game can continue
    if(pipe_win == False):
        #have a slight pause before cleaning up
        sleep(1.5)
        #for loop, clean up any flow if game not over
        for number in range(0, 6):
            for check in made_pipes:
                if(check.img_index > 7) and (check.img_index < 15):
                    made_pipes[check.location - 1].pipe_connected = False
                    made_pipes[check.location - 1].img_index -= 7
                    check.configure(image = pipe_image_list[check.img_index - 1])
    
#call this class when a game is won
class Candy():
    def dispense():
        if gpio_on == False:
            pass
        
        if gpio_on == True:
            import RPi.GPIO as GPIO
            
            #set up pins and assign numbers to them  
            GPIO.setmode(GPIO.BCM)
            
            ControlPin = [18, 21, 24, 27]
            
            for pin in ControlPin:
                GPIO.setup(pin, GPIO.OUT)
                GPIO.output(pin, 0)
            
            #create sequences that will rotate the motor
            a = [1, 0, 0, 0]
            b = [1, 1, 0, 0]
            c = [0, 1, 0, 0]
            d = [0, 1, 1, 0]
            e = [0, 0, 1, 0]
            f = [0, 0, 1, 1]
            g = [0, 0, 0, 1]
            h = [1, 0, 0, 1]
            #put all of the sequences in a master sequence
            seq = [a, b, c, d, e, f, g, h]
            
            #512 is one full turn on the motor
            for i in range (512):
                #goes through the sequences on the appropiate pins
                for halfstep  in range(8):
                    for pin in range(4):
                        GPIO.output(ControlPin[pin], seq[halfstep][pin])
                    sleep(0.001)
                   
            GPIO.cleanup()

################
# Main Program #
################
#will keep a list of created buttons to make them easier to delete
button_list = []
#list of created pipes for the pipe puzzle
made_pipes = []

#window resolution
#800x480 is Fullscreen on a rasp. pi
WIDTH, HEIGHT = 800, 480

# create the window
window = Tk()
#set the window WIDTHxHEIGHT
window.geometry("{}x{}".format(WIDTH, HEIGHT))
# set the window title
window.title("The Plaque Pursuit")

# generate the GUI
p = Canvas(window)
p.pack(expand = 1, fill = BOTH)

#Set background image
background_image = PhotoImage(file = "images/game_bg.png")
p.create_image(0, 0, anchor = NW, image = background_image)

#Sets up & enters the main menue
menu = MainMenu()

# display the GUI and wait for user interaction
window.mainloop()
