print("Welcome to the music quiz game!")
print("Only these users are allowed to play: Fred, Billy, Jack")
#could use an array/list to name the users ^

#make an array/list to verify that the user's input = auth_users
auth_users = ["Fred", "Billy", "Jack", "fred", "billy", "jack"]
#make a function that asks the user for their name and denies
#and loops until the user inputs a correct user
def check():
    input_name = input("What is your name?")
    if input_name in auth_users:
        print("Authorised ")
        
    else:
        print("Unauthorised user try again!")
        check()

check()
f = open("data.txt")
content = f.readlines()

def line_func():
    valid_range = False
    list_size = len(content)
    print(list_size)
    while not valid_range:
        try:
            input_line = int(input("Choose line"))
            print(list_size)
            print(content)
            if input_line >= 0 and input_line <= list_size:
                valid_range = True
        except ValueError:
            print("Not a valid line number")
            
    input_line = input_line - 1
    print(content[input_line])
    line_func()
line_func()
