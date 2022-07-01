from matplotlib import artist
from matplotlib.pyplot import title
from Song import Song
from tabulate import tabulate

"""
Program takes in song details, analyzes displays the songs in a
sorted in a table.
@snHD88
"""
class PlayList:
    def __init__(self):
        self.songs = []
        self.data = []
        self.playtime = []
        self.maxPlaytimes = []


    def add(self, song):
        """function to add song to playlist"""
        self.songs.append(song)

    def sPrint(self):
        """function to help analyze and display playlist details"""
        col_names =[" ", "Title", "Artist", "Album", "Playtime"]
        for s in range(len(self.songs)):
            self.data.append([s, self.songs[s].getTitle(), self.songs[s].getArtist(), self.songs[s].getAlbum(), self.songs[s].getPlaytime()])
            self.playtime.append(self.songs[s].getPlaytime())
        print(tabulate(self.data, headers=col_names, tablefmt="grid"))
        print("======================================")
        maxPlaytime = max(self.playtime)
        print("Song(s) with maximum playtime is:")
        for song in self.songs:
            if(maxPlaytime == song.getPlaytime()):
                print(song.toString())
        print("======================================")
        minPlaytime = min(self.playtime)
        print("Song(s) with minimum playtime is:")
        for song in self.songs:
            if(minPlaytime == song.getPlaytime()):
                print(song.toString())

    def length(self):
        return len(self.songs)
    


playlist = PlayList()

numSongs = input("Enter the number of songs: ")
for n in range(int(numSongs)):
    title = input("Enter title: ")
    artist = input("Enter artist: ")
    album = input("Enter album: ")
    playtime = input("Enter playtime: ")

    song = Song(title, artist, album, playtime)
    playlist.add(song)
    print(f"{title} added to playlist. Playlist size = {playlist.length()}")

playlist.sPrint()


