#could use an array/list to name the users
print("Welcome to the music quiz game!")
print("Only these users are allowed to play: Fred, Billy, Jack.")

#makes an array/list to verify that the user's input = auth_users
auth_users = ["Fred", "Billy", "Jack", "fred", "billy", "jack"]

#makes a function that asks the user for their name and denies access
#until any of the values of auth_users are inputted.
def check():
    input_name = input("What is your name?")
    if input_name in auth_users:
        print("Authorised ")
        
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
                print("Not a valid line number")
        except ValueError:
            print("Not a valid line number")
    #user input is decreased so that: user input == line number
    input_line = input_line - 1
    #test prints
    print(content[input_line])
    print("finished")
    #loop for testing
    line_func()

check()

#opens data.txt file and assigns content of files to content (list)
f = open("data.txt")
content = f.readlines()

line_func()

