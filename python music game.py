import random
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


#creates object of Song with properties of songtitle and artist
class Song_class:
    def __init__(self, songtitle, artist):
        self.songtitle = songtitle
        self.artist = artist
    def __repr__(self):
        return(f"Song Title: {song.songtitle} Artist: {song.artist}")

check()
#opens data.txt file
f = open("data.txt")
file_path = "data.txt"
song_list = []

with open(file_path, "r") as content:
    #assigns content of files to content (integer of lines in txt file)
    lines = content.readlines()

    for line in lines:
        #splits every line into songtitle and artist
        data = line.strip().split(",")
        #checks if there are 2 elements per line (separated by ,)
        if len(data) >= 2:
            #assigns first values per line to songtitle
            #and second value per line to artist
            songtitle, artist = data[0], data[1]
            song = Song_class(songtitle, artist)
            song_list.append(song)
            list_size = int(len(lines))
        else:
            print("No , separating songtitle and artist")

for song in song_list:
    print(f"Song Title: {song.songtitle} Artist: {song.artist}")

random_num = random.randint(0,list_size)
print("Random num", random_num)
print("Song list:", song_list)
for song in song_list:
    chosen_line = data + song.songtitle
    print("Chosen line", chosen_line)

