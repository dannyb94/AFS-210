import random

class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist
        self.prev = None
        self.next = None

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other): #equal
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other): #not equal
        return not (self == other)

    def __lt__(self, other): #less than
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other): #greater than
        return ((self.title, self.artist) < (other.title, other.artist))
        

def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")

class Music:
    def __init__(self):
        self.atm = None
        self.head = None
        self.tail = None
        self.cnt = 0

    # List
    def listed(self):
        # cnt = 0
        # lt = self.size()
        # crnt = self.head
        # if lt == 0:
        #     print('There are no songs in your library.')
        # else:
        #     while cnt < lt:
        #         val = (Song.__str__(crnt))
        #         crnt = crnt.next
        #         cnt += 1
        #         print(val)

        
        crnt = self.head
        # print(crnt.__str__())
        # crnt = crnt.next

        # print(crnt.__str__())
        # crnt = crnt.next

        # print(crnt.__str__())
        # crnt = crnt.next


        # print(crnt.__str__())
        # crnt = crnt.next

        while crnt:
            # print(crnt.__str__())
            if crnt == self.tail:
                print(crnt.__str__())
                print("break")
                break
            else:
                # crnt = crnt.next
                # print("break")
                print(crnt.__str__())
                crnt = crnt.next
                # break

    # 
    def current(self):
        return self.atm

    # Add
    def addTo(self, title, artist):
        newNew = Song(title, artist)
        # self.cnt += 1
        if self.cnt == 0:
            # newNew = Song(title, artist)
            self.head = newNew
            self.tail = self.head
        else:
            self.tail.next = newNew
            newNew.prev = self.tail
            self.tail = newNew
            self.head.prev = self.tail
            self.tail.next = self.head
        self.cnt += 1

    # Delete
    def delete(self, title):
        # self.cnt -= 1
        # crnt = self.head
        # prev = self.head
        # if self.atm != None:
        #     if self.atm.title == title and self.atm.artist == artist:
        #         self.atm = None
            
        # while crnt:
        #         if crnt.title == title:
        #             if crnt == self.tail:
        #                 print("Deleted", Song.__str__(crnt))
        #                 prev.next = None
        #                 self.tail = prev
        #             else:
        #                 print("Deleted", Song.__str__(crnt))
        #                 prev.next = crnt.next
        #                 crnt.next = prev
        #             self.cnt -= 1
        #             return
        #         prev = crnt
        #         crnt = crnt.next

        crnt = self.head
        prev = self.head
        if self.cnt == 0:
            print('There are no songs in your library.')
        else:
            while crnt:
                if crnt.title == title:
                    if crnt == self.tail:
                        print("Deleted", Song.__str__(crnt))
                        prev.next = None
                        self.tail = prev
                    elif crnt == self.head:
                        print("Deleted", Song.__str__(crnt))
                        crnt.next.prev = None
                        self.head = crnt.next
                    else:
                        print("Deleted", Song.__str__(crnt))
                        prev.next = crnt.next
                        crnt.next = prev
                    self.cnt -= 1
                    return
                prev = crnt
                crnt = crnt.next

    # Play
    def play(self):
        if self.cnt == 0:
            print("Oh boo! There's nothing to play.")
        else:
            print(Song.__str__(self.head))

    # Skip
    def skip(self):
        crnt = self.atm
        if crnt is None:
            return "There's nothing playing at the moment. :("
        if crnt.next is None:
            self.atm = self.head
            return self.head
        else:
            self.atm = crnt.next
            return self.atm

    # Shuffle
    def shuffle(self):
        lt = self.size()
        if lt == 0:
            print('There are no songs in your library.')
        elif lt == 1:
            print("There's only one song in your library.")
        elif lt >= 2:
            self.head, self.tail = self.tail, self.head
        else:
            crnt = self.head
            cntng = 0
            while(cntng < lt):
                x = random.randint(0, lt - 1)
                swapNode = self.getAtIndex(x)
                temptitle, tempartist = Song.getTitle(swapNode), Song.getArtist(swapNode)
                swapNode.setTitle(Song.getTitle(crnt))
                swapNode.setArtist(Song.getArtist(crnt))
                crnt.setTitle(temptitle)
                crnt.setArtist(tempartist)
                crnt = crnt.next
                cntng += 1

    # Replay
    def replay(self):
        crnt = self.atm
        if crnt is None:
            return "Nothing to replay."
        elif crnt.prev is None:
            self.atm = self.tail
            return self.atm
        else:
            self.atm = crnt.prev
            return self.atm


music = Music()
music.addTo('Build', 'Justine Sky')
music.addTo('Easy', 'Mac Ayres')
music.addTo('Organic', 'Eric Bellinger')
music.addTo('Gone', 'Alex Isley, Jack Dine')


while True:
    menu()
    choice = int(input('Welcome to your personlaized music player! Select an option to begin: '))

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        # Add song to playlist
        title = input('Enter the title of song: ')
        artist = input('Enter the artist name: ')
        music.addTo(title, artist)
        print("New Song Added to Playlist")
    elif choice == 2:
        # Prompt user for Song Title 
        # remove song from playlist
        title = input("Enter the name of the song you wish to delete: ")
        music.delete(title)
        print("Song Removed from Playlist")
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print(music.play())
        print("Playing....")        
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        print("Skipping....")                     
        print(music.skip())
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        print("Replaying....")  
        print(music.replay())
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("Shuffling....")      
        print(music.shuffle())    
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        print("Currently playing: ", end=" ") 
        print(music.current())   
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        music.listed()
    elif choice == 0:
        print("Goodbye.")
        break

