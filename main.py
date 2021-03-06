# Program for spy chat 1.0
# from spy_details.py we are importing spy,Spy,chatmsg and friends
from spy_details import spy, Spy, ChatMsg, friends
# importing Steganography funcntion from steganogarphy for hiding text into the images
from steganography.steganography import Steganography
# importing termcolor for text formatting
from termcolor import colored
# welcome message to the user
print 'Welcome to SpyChat 1.0'
# default status messages
status_msg = ['Wassup', 'avaliable', 'Sleeping', 'Studying', 'busy']
# function for new status message
def new_status():
    # storing the new status message in a string variable
    new_status_msg = raw_input('Enter your new status:\n')
    return new_status_msg

# function to print current status message
def current_status_msg():
    # checking if user had any current status message
    if spy.current_status_msg is not None:
        print 'Your current status message is ' + spy.current_status_msg
    else:
        print 'You don\'t have any status message'


# function to add status
def add_status():
    # initially updated message is None
    updated_status_msg = None
    # call the current_status _msg() to print the current status of user
    current_status_msg()
    # ask the user if they want to set current status message from older ones
    status = raw_input('Do you want to select status message from the older(y/n):\n')
    # we have used upper in case user enter small y
    if status.upper() == 'Y':
        # setting the item position to one
        item_position = 1
        # loop to navigate over all the status messages
        for msg in status_msg:
            print '%d %s' % (item_position, msg)
            # updating the item position
            item_position += 1
        # ask the user to enter status choice and convert it to integer
        status_choice = int(raw_input("Enter the choice of your status message:\n"))
        # checking the index error
        if status_choice <= len(status_msg):
            # updating the message by retrieving it from list of status message
            updated_status_msg = status_msg[status_choice-1]
        else:
            print 'Not in avaliable statuses'
    elif status.upper() == 'N':
        # calling new status function to get new status message
        updated_status_msg = new_status()
        # to append the new updated messages to status messages list
        status_msg.append(updated_status_msg)
    else:
        print 'You might have entered the wrong choice, enter y or n'
    # if there is any updated message then its true
    if updated_status_msg:
        print 'New status message is %s' % updated_status_msg
    else:
        print 'You don\'t have new status message'
    # function returns updated message to the calling function
    return updated_status_msg


# function for checking if name is valid or not
def name_validation(name):
    # checks if spy name has some length
    if len(name) > 0:
        a = 0
        b = 0
        c = 0
        # loop to navigate over each character in spy.name
        for i in name:
            # checks if character is alphabet
            if i.isalpha():
                # 'pass' just pass the statement
                c += 1
            # checks if character is digit
            elif i.isdigit():
                a += 1
            # checks if character is space
            elif i.isspace():
                c += 1
            # now the rest of characters will fall into it
            else:
                b += 1
        # for printing only alphabetical name no digit no special character
        # if the string has spaces before and after then it removes it
        # if statement will only run if there is no digit and no special character
        if a <= 0 and b <= 0:
            return True
        else:
            print "String must have digits or special characters"
            return False
    else:
        print "Your name is too short ."
        return False


# function to check valid salutation.
def valid_salutation(salutation):
    if len(salutation) > 0:
        a = 0
        b = 0
        c = 0
        # loop to navigate over each character in salutation
        for i in salutation:
            # checks if character is alphabet
            if i.isalpha():
                c += 1
            # checks if character is digit
            elif i.isdigit():
                a += 1
            # checks if character is space
            elif i.isspace():
                c += 1
            elif i is '.':
                c += 1
            # now the rest of characters will fall into it
            else:
                b += 1
        # for printing only alphabetical name no digit and special characters
        # if the string has spaces before and after then it removes it
        # if statement will only run if there is no digit and no special character
        if a <= 0 and b <= 0:
            return True
        else:
            print "String must have digits or special characters"
            return False
    else:
        print "Your salutation is too short to be visible"
        return False


# function to print  spy rating
def spy_rating(rating):
    # if elif else series to check the standards for spy rating
    if 5 >= rating >= 4.5:
        print "Very High Standards"
    elif 4.5 > rating >= 4:
        print "High Standards"
    elif 4 > rating >= 3.5:
        print "Very Good Standards"
    elif 3.5 > rating >= 3:
        print "Good Standards"
    elif 3 > rating >= 2.5:
        print "Nice Standards"
    elif 2.5 > rating >= 0:
        print " low ,improve spy standards"
    else:
        print "Invalid standards"


# function to add a new friend to friend list
def add_friend():
    # initially setting details of friend to zero
    new_friend = Spy('', '', 0.0, 0)
    # asking the user to enter name
    new_friend.name = raw_input('Please tell your friend name:')
    # asking the user to enter salutation
    new_friend.salutation = raw_input('What should we call you Mr. or Ms.:')
    # asking the user to enter rating and converting it to float
    new_friend.rating = float(raw_input('Please tell your friends rating:'))
    # asking the user to enter age and converting it to integer
    new_friend.age = int(raw_input('Please tell your friends age:'))
    # check the standards of rating
    spy_rating(new_friend.rating)
    # checking the salutation
    # checks if user has right age to proceed, valid name and rating greater than user
    if 12 < new_friend.age < 50 and name_validation(new_friend.name) and 5 >= new_friend.rating >= spy.rating and \
            valid_salutation(new_friend.salutation):
        # stripping off spaces before and after his name
        new_friend.name = new_friend.name.strip(" ")
        new_friend.salutation = new_friend.salutation.strip(" ")
        # appending the new friend to friends list
        friends.append(new_friend)
        print 'Friend added'
    else:
        print 'Sorry we can\'t enter spy with that invalid details or your age might be low'
    # returning the no. of friends to the calling function
    return len(friends)


# function  to select a friend to start chatting with
def select_a_friend():
    position = 0
    # loop to navigate the list of friends
    for friend in friends:
        # printing the friend detail
        print '%d. %s %s aged %d having spy rating %.2f is online' % (position+1, friend.salutation, friend.name, friend.age, friend.rating)
        # updating the position of list item of friends
        position += 1
    # ask the user to select the friend and convert it into integer
    friend_choice = int(raw_input('Select one of your friend:\n'))
    # checking the index error
    if len(friends) >= friend_choice:
        pass
    else:
        print 'Wrong choice :_D'
        start_chat()
    # returning the index of friend choice
    return friend_choice-1


# function to check no text condition
def no_text(text, sent_by):
    # if we checking no text condition in encoding
    if sent_by is True:
        # this condition checks if there is no text
        if text == '':
            # asking the user if he wants to continue with no text message
            no_msg = raw_input('Do you want to continue without text message(y/n):\n')
            # if user sends that continue with no text message then assigning the same text to new_text
            if no_msg.upper() == 'Y':
                new_text = text
            # if user says no the asking user for text message to encode
            else:
                new_text = raw_input('What you want to say?')
        # if the text contains some message then assigning the same text to new_text
        else:
            new_text = text
        # returning the new_text to function call
        return new_text
    # if we checking no text condition in decoding
    else:
        if text == '':
            print 'Sender has send image with no text message inside it'
            # again calling start_chat()
            start_chat()
        else:
            pass


# function to encode the text in image
def encode(original_image, output_path, text):
    '''
        **** steganography can encode and convert .png or .jpg to .txt file with inside of
        text file various unicodes not understandable and can decode .txt file also******
        **** By this we can conclude that it may encode any file format to any other file format and
        ***** '''
    Steganography.encode(original_image, output_path, text)


# function to send messages
def send_msg():
    # calling function to select a friend and then storing the index of friends list to friend_choice
    friend_choice = select_a_friend()
    # asking the user to enter the name of original image with extension
    original_image = raw_input("Enter the name of your image with extension(like .jpg or .png):")
    # setting the path for the image with hidden text message
    output_path = raw_input("Enter the name of image to create with secret text(write extension):")
    # asking the user to enter the text message to be hide
    text = raw_input('What you wanna say to your comrade:')
    # function to check if there is no text message
    text = no_text(text, True)
    # Using the Steganography library hiding the message inside the image.
    # by calling the function we encode the text message into the original and
    # produce an output image with hidden text message
    encode(original_image, output_path, text)
    # declaring a new object of ChatMsg type class taking two arguments,
    # one is text message and another is boolean True stating that message sent ny me
    new_chat = ChatMsg(text, True)
    # appending the text message in chats of a selected friend
    friends[friend_choice].chats.append(new_chat)
    print 'Your secret image is ready!'

# function to check if other spy speaking  greater than 100 words

def average_chat(hidden_text, sender):
    if len(hidden_text) > 100:
        del friends[sender]

# function to check and send appropriate reply if spy has send secret message like this
# sos, save me, alert, help
def check_sos(text, sender, image_path):
    # list of sos type msg
    text = text.upper()
    sos_msg = ['SOS', 'SAVE ME', 'ALERT', 'HELP']
    # initialising a variable to zero
    flag = 0
    # loop to navigate through sos_msg list
    for sos in sos_msg:
        # checks if sos message
        if sos == text:
            flag += 1
        else:
            pass
    # if there is nay or more sos messages within a text then condition is true
    if flag > 0:
        new_text = raw_input("THIS IS AN EMERGENCY, SEND A VALID REPLY\n")
        encode(image_path, "yes.png", new_text)
        # declaring a new object of ChatMsg type class taking two arguments,
        # one is text message and another is boolean True stating that message sent by me
        new_chat = ChatMsg(new_text, True)
        # appending the text message in chats
        friends[sender].chats.append(new_chat)
    else:
        pass


# function to read a message
def read_msg():
    # selecting a friend by calling function and storing the index in sender variable
    sender = select_a_friend()
    # asking the user for the name of image
    output_path = raw_input('What is the name of file with extention?:')
    # decoding the hidden text message and storing it
    hidden_text = Steganography.decode(output_path)
    # function to check if there is no text message
    no_text(hidden_text, False)
    # declaring a new object of ChatMsg type class taking two arguments,
    # one is text message and another is boolean False stating that message was not sent ny me
    new_chat = ChatMsg(hidden_text, False)
    # appending the text message in chats of a selected friend
    friends[sender].chats.append(new_chat)
    # coloring the text
    text = colored(hidden_text, 'red')
    print 'Your secret message have been saved'
    print 'Secret message is:\n%s' % text
    # for checking if sos message is sent
    check_sos(hidden_text, sender, output_path)
    # calling average_chat() to see if spy is speaking too much
    average_chat(hidden_text, sender)


# function to read chat history with a particular friend
def read_chat_history():
    # function to select a friend of which to want to read chat history
    read_for = select_a_friend()
    # Printing new line
    print '\n'
    # navigating in all chats of a particular friend
    for chat in friends[read_for].chats:
        # checking if the chat message was sent by you
        if chat.sent_by_me:
            # assigning the time
            time = colored(chat.time.strftime("%d %B %Y, %a %H:%M"), 'blue', attrs=["dark", "bold"])
            # assigning the name, spy.name with red color and some attributes
            name = colored(spy.salutation + ' ' + spy.name, 'red', attrs=["dark", "bold"])
            # assigning the msg, chat.message with green color and some attributes
            msg = colored(chat.message, 'green', attrs=["dark", "bold"])
            # printing the message with time details
            print '[%s] %s said: %s' % (time, name, msg)
        else:
            # assigning the time
            time = colored(chat.time.strftime("%d %B %Y, %a %H:%M"), 'blue', attrs=["dark", "bold"])
            # assigning the name, spy.name with red color and some attributes
            name = colored(friends[read_for].salutation + ' ' + friends[read_for].name, 'red', attrs=["dark", "bold"])
            # assigning the msg, chat.message with green color and some attributes
            msg = colored(chat.message, 'green', attrs=["dark", "bold"])
            # printing the message with time details
            print '[%s] %s said: %s' % (time, name, msg)


# function to change user
def change_user():
    # take the input from user in  string
    spy.name = raw_input('Enter your name:')
    # call name_validation from validating name
    if name_validation(spy.name):
        # strip()- strip off the spaces before and after the string
        spy.name = spy.name.strip(" ")
        # asking for the salutation
        spy.salutation = raw_input('What should we call you Mr. or Ms.?:')
        # checking for the valid salutation
        result = valid_salutation(spy.salutation)
        if result is False:
            # if result turns to be false then exit the program
            print 'Error, wrong salutation'
            exit(1)
        else:
            pass
        # ask the user to enter age and convert the string to integer
        spy.age = int(raw_input('Enter your age:'))
        # ask the user to enter rating and convert the string to float
        spy.rating = float(raw_input('Enter your rating:'))
        # to check the standards of rating
        spy_rating(spy.rating)
        # call the start_chat func
        start_chat()
    else:
        print 'Enter a valid name'


# function to start chat with a friend
def start_chat():
    # adding the spy name and spy salutation into spy name
    # initially setting spy menu to True
    show_menu = True
    # checking if user has valid age
    if 12 < spy.age < 50:
        # printing the authentication message
        # using \ for printing multi line
        print 'Authentication complete! Welcome '\
         + spy.salutation + ' ' + spy.name + ', Age: ' + str(spy.age) + ', Rating: ' + str(spy.rating) + '. Thanks for being with us.'
        # while loop with condition show_menu to be True and stops as show_menu becomes False
        while show_menu:
            # storing the choices into menu_choice
            menu_choices = "What do you want to do?\n1.Current status message\n"\
             + "2. Add a status update\n3. Add a friend\n4. Send a secret message\n"\
             + "5. Read a secret message\n6. Read Chats from a user\n7. Change User\n8. Close spychat 1.0\n"
            # getting the menu choice from user and converting it to int and storing it to a variable
            menu_choice = int(raw_input(menu_choices))
            # condition to check if user has selected the right menu choice
            if menu_choice > 0:
                # first choice
                if menu_choice == 1:
                    # calling function to check the current status message
                    current_status_msg()
                # second choice
                elif menu_choice == 2:
                    # calling add_status function to add status message and returning
                    # the updated status message and storing it to current status message
                    spy.current_status_msg = add_status()
                # third choice
                elif menu_choice == 3:
                    # calling the function add friend and in return get the no. of friends
                    no_of_friends = add_friend()
                    # printing the no. of friends you have
                    print 'You have %d friends' % no_of_friends
                # fourth choice
                elif menu_choice == 4:
                    # calling send_msg function to send messages
                    send_msg()
                # fifth choice
                elif menu_choice == 5:
                    # calling read_msg function to read the messages sent to you
                    read_msg()
                # sixth choice
                elif menu_choice == 6:
                    # read chat history of a friend
                    read_chat_history()
                elif menu_choice == 7:
                    # function to change user
                    change_user()
                # in other cases setting show_menu to False and closing the application
                else:
                    show_menu = False
    # if you do not have valid age  then else will run
    else:
        print 'Sorry.You are not allowed, perhaps due to your age'


# Asks the user if they want to continue as existing user or want to enter a new username
existing = raw_input('Do you want to continue as ' + spy.salutation + ' ' + spy.name + ' (y/n)')
# checks the user input
# we have used upper() coz user can enter small y
if existing.upper() == "Y":
    # call the start_chat func
    start_chat()
# we have used upper() coz user can enter small n
elif existing.upper() == "N":
    # initializing spy details to zero r nothing
    spy = Spy('', '', 0, 0.0)
    # calling change user function
    change_user()
else:
    print 'Wrong choice '
