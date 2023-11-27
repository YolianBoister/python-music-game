print("Welcome to the music quiz game!")
print("Only these users are allowed to play: Fred, Billy, Jack")
#Could use an array/list to name the users ^

#make an array/list to verify that the user's input = auth_users
auth_users = ["Fred", "Billy", "Jack", "fred", "billy", "jack"]


def check():
    input_name = input("What is your name?")
    if input_name in auth_users:
        print("Authorised ")
        
    else:
        print("Unauthorised user try again!")
        check()
check()
print("Continued")
