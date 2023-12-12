#could use an array/list to name the users
print("Welcome to the music quiz game!")
print("Only these users are allowed to play: Fred, Billy, Jack.")

#makes an array/list to verify that the user's input = auth_users
auth_users = ["Fred", "Billy", "Jack", "fred", "billy", "jack"]

#makes a function that asks the user for their name and denies access
#until any of the values of auth_users are inputted.
def check():
    global debug_mode
    debug_mode = False
    input_name = input("What is your name?")
    if input_name in auth_users:
        print("Authorised ")
    elif input_name == ("debug"):
        debug_mode = True
        print("Debug mode enabled")
    else:
        print("Unauthorised user try again!")
        check()

#function for testing reading external text files.
#sets a value of False to a boolean that doesn't change until all
#input checks are passed.
def line_func():
    valid_range = False
    #counts number of items in content (list) and puts the output into
    #an integer variable.
    list_size = len(content)
    while not valid_range:
        try:
            input_line = int(input("Choose line"))
            #checks if input is in a range between 0 and the number of
            #lines in data.txt (list_size).
            if input_line >= 0 and input_line <= list_size:
                valid_range = True
            else:
                print("Out of range")
        except ValueError:
            print("Invalid value")
    #user input is decreased so that: user input == line number
    input_line = input_line - 1
    #test prints
    print("")
    print(content[input_line])
    print("Within range:",valid_range)
    print("Content of file:",content)
    print("")
    print("finished")
    #loop for testing
    line_func()

check()

#opens data.txt file and assigns content of files to content (list)
f = open("data.txt")
content = f.readlines()

if debug_mode == True:
    line_func()


