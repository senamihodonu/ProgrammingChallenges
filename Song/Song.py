from matplotlib import artist
from matplotlib.pyplot import title


class Song():

    def __init__(self, title, artist, album, playtime):
        self.title = title
        self.artist = artist
        self.album = album
        self.playtime = playtime

    def getTitle(self):
        """returns the title of the song"""
        return self.title

    def setTitle(self, title):
        """sets the title of the song"""
        self.title = title

    def getArtist(self):
        """returns the artist of the song"""
        return self.artist

    def setArtist(self, artist):
        """sets the artist of the song"""
        self.artist = artist
    
    def getAlbum(self):
        """returns the title of the song"""
        return self.album

    def setAlbum(self, album):
        """sets the song album"""
        self.album = album
    
    def getPlaytime(self):
        """returns the playtime of the song"""
        return self.playtime

    def setPlaytime(self, playtime):
        """sets the playtime of the song"""
        self.playtime = playtime
    
    def toString(self):
        """sets the playtime of the song"""
        return f"{self.title}       |{self.artist}      | {self.album}      |{self.playtime}"

    
#newSong = Song()
# newSong = Song("Too long, too late", "SilverBlack", "World Angle", 3)

# newSong.toString()