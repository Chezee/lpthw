from sys import exit                                #Import library


def gold_room():                                    #defining method
    print "This room is full of gold. How much do you take?"
    
    
    choice = raw_input("> ")                        #Making choice with raw_input
    a = choice.isdigit()
    if a == True:              #What the fuck is this?
        how_much = int(choice)                      #Converting it to 'int'
    else:
        dead("Man, learn to type a number.")        #If not number - you dead
    
    if how_much < 50:                               #Counting is you greedy
        print "Nice, you are not greedy, you win!"  
        exit(0)                                     
    else:
        dead("You greedy bastard!")
        

def bear_room():                                    #Defining method
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear."
    bear_moved = False                              
    
    while True:                                     #Making infinite loop. But what for? 
        choice = raw_input("> ")                    #What is 'True'?
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your legs off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what does it means"
            

def ctulhu_room():
    print "Here you see the great evil Ctulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    
    choice = raw_input("> ")
    
    if "flee" in choice:
        start()
    if "head" in choice:
        dead("That's was tasty")
    else: 
        ctulhu_room()
        

def dead(why):                                      #Defining 'dead' method with string 
    print why, "Good job!"                          #argument
    exit(0)


def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    
    choice = raw_input("> ")
    
    if choice == "left":
        bear_room()
    if choice == "right":
        ctulhu_room()
    else:
        dead("You stumble around the room until you starve.")
    

gold_room()