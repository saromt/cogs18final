import string
import random
import nltk
import test_chatty

""" By providing the user with a story and specific characteristics for each character, I was able to create a ChatBot that was designed 
    to answer any curiousities that the user has about the people in the story. 
    I created a class and functions in order to execute the ChatBot and built upon some of the functions from A3."""

class Language(): #this is the class I created to assign the characteristics to each person
    
    #specific attributes
    def __init__(self, name, which_language, how_well_its_spoken, how_many, location):
        self.name = name
        self.which_language = which_language
        self.how_well_its_spoken = how_well_its_spoken
        self.how_many = how_many
        self.location = location
        
    
    #states which character speaks what language
    def print_language(self):
        print(self.name, 'knows how to speak', self.which_language)
        
    
    #states how many lanuguages a character speaks
    def print_amt(self):
        
        if self.how_many is 1:
            print(self.name, 'knows how to speak', self.how_many, 'language.')
            
        else:
            print(self.name, 'knows how to speak', self.how_many, 'languages.')
            
            
    #states how well the language is spoke
    def print_goodness(self):
        print(self.name, 'speaks', self.which_language, 'very', self.how_well_its_spoken,'.')
    
    #states where the characters learned the languages
    def print_edu(self):
        
        if self.location is 'school':
            print(self.name, 'learned', self.which_language, 'at', self.location)
            
        elif self.location is 'Mexico' or 'America':
            print(self.name, 'learned', self.which_language, 'in', self.location)
        

Adam = Language('Adam', 'Spanish', 'well', 1, 'Mexico.')
Bill = Language('Bill', 'English', 'nicely', 1, 'America.')
Callie = Language('Callie', 'French and Italian', 'elegantly', 2, 'school.')
Mylie = Language('Mylie', 'English and Khmer', 'smoothly', 2, 'school.')

def begin():
    #introduction
    print("Throughout high school, many language classes were offered. Four friends, Adam, Bill," + " " +
          "Callie, and Mylie, were all interested in submersing themselves in the culture and language classes, which included" + " "+
          "Spanish, English, French, Italian, and Khmer. Given that Adam was very interested in the Spanish culture," + " "+
          "he decided to study abroad in Mexico, where he learned to speak Spanish well. Bill, on the other hand, was very interested" + " "+
          "in perfecting his English. He stayed in America and learned to speak English nicely. Callie" + " "+
          "chose to take French and Italian classes at school. She was a very fast learner and picked up on both languages"+ " "+
          "quickly, speaking them elegantly as she progressed her studies. Mylie also took language classes at school."+
          "She decided to take English and Khmer classes, and spoke them smoothly by the end of the courses.")
    print(" ")
    
    #introduces what ChatBot is designed to do
    print("This ChatBot is designed to inform you about the different characters in this story. Through specifying exactly what you"+ " "+
            "want to know about each of them, the ChatBot will do its best to provide you with the information that you want.")
    print("Once you are done interacting with the ChatBot, simply say 'no' and the ChatBot will end.")
    print(" ")
    
    #ChatBot begins speaking
    print ("Hi! I am here to help you find out about my friends, Adam, Bill, Callie, and Mylie. Would you like to get started? (yes/no)")
    

def is_start(input_string): #accounts for user input and decides whether or not to provide more information to user
    
    if input_string.lower() == 'yes': 
        print("I can provide you information about what languages my friends speak, how well they speak, how many languages they speak, and where they learned the languages! To find out about each one, type in the keywords (language, amount, wellness, location) followed by the name of who you're curious about in the format - keyword, person")
    
    if input_string.lower() == 'no':
        print("Okay, goodbye!")

def is_whom(input_string): #function used if user wants to know more about each specific character; specified by keyword and name
    
    if input_string.lower() == 'language, adam':
        Adam.print_language()
    
    if input_string.lower() == 'language, bill':
        Bill.print_language()
    
    if input_string.lower() == 'language, callie':
        Callie.print_language()
    
    if input_string.lower() == 'language, mylie':
        Mylie.print_language()
    
    if input_string.lower() == 'amount, adam':
        Adam.print_amt()
    
    if input_string.lower() == 'amount, bill':
        Bill.print_amt()
    
    if input_string.lower() == 'amount, callie':
        Callie.print_amt()
    
    if input_string.lower() == 'amount, mylie':
        Mylie.print_amt()
 
    if input_string.lower() == 'wellness, adam':
        Adam.print_goodness()
    
    if input_string.lower() == 'wellness, bill':
        Bill.print_goodness()
    
    if input_string.lower() == 'wellness, callie':
        Callie.print_goodness()
    
    if input_string.lower() == 'wellness, mylie':
        Mylie.print_goodness()
    
    if input_string.lower() == 'location, adam':
        Adam.print_edu()
    
    if input_string.lower() == 'location, bill':
        Bill.print_edu()
    
    if input_string.lower() == 'location, callie':
        Callie.print_edu()
    
    if input_string.lower() == 'location, mylie':
        Mylie.print_edu()

#asks user if they want to continue asking about the characters
def go_on(input_string): 

    if input_string == 'yes':
        print("I can provide you information about what languages my friends speak, how well they speak, how many languages they speak, and where they learned the languages! To find out about each one, type in the keywords (language, amount, wellness, location) followed by the name of who you're curious about in the format - keyword, person")
    
    elif input_string == 'no':
        print("Okay, goodbye!") 
    
    print("Is there anything else I can help you with? (yes/no)")

#from A3 chatbot 
def prepare_text(input_string):
    """Helper method to make the input lower case and split multiple strings
    Got rid of remove_punctuation from org because some inputs need to contain '
    Parameters
    ----------
    input_string: string
        A string that user input 
    Returns
    -------
    out_list: list
        List representation of input after modifying
    """
    out_list = []
    temp_string = ''
    temp_string = input_string.lower()
    out_list = temp_string.split()
    return out_list

def end_chat(input_string):
    """Ends the chat if the input matches 'quit' or 'exit'
    Parameters
    ----------
    input_list: list
        the list that contains user input
    Returns
    -------
        boolean
    Whether the input was quit or exit or none 
    """
    for item in input_string:
        if item.lower() == 'quit' or item.lower() == 'exit':
            print ('The end!')
        else: 
            return False
def have_a_chat():
    """Main function to run our chatbot."""
    
    begin()
    
    chat = True
    
    while chat:

        # Get a message from the user
        msg = input('INPUT :\t')
        
        # Check if input is a 'start'
        start = True
        start = is_start(msg)
        
        msg = input('INPUT :\t')
        
        #Check is input is a 'who'
        who = is_whom(msg)
        
        #check if input is a 'go'
        go = go_on(msg)
        
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False
        
        print('')