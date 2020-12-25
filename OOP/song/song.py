class Song:
    '''Class to represent a song
    
    Attributes:
        title(str): The title of the song
        artist (str): Name of the song's creator
        duration (int): The duration of the song in seconds'''

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title
    
    name = property(get_title)      # Creating a .name getter for find_object function.

 #help(Song.__init__)     #prints all the doc strings
 #print(Song.__doc__)     #prints doc strings of applied class


class Album:
    ''' Class to represent an album.
    Attributes:
        name (str): The name of the album.
        year (int): The year album was released.
        artist (str): The artists name respnsible for the album, defaults to VA
        tracks (List[Song]): A List of the song on the album.
        
    Methods:
        add_song: Used to add new song to the albums tracks list.'''

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = 'Various Artists'
        else:
            self.artist = artist
        
        self.tracks = []        # A list of Song objects

    def add_track(self, track: str, position=None):
        '''Adds a Song object to the track list.
        Searches for a song in self.tracks, if not found creates a Song object and appends
        it to the list.
        
        Args:
            track [str]: The title of a song to add.
            position (Optional[int]): If specified, the song will be added to that position
                in the track list - inserting it between other songs if necessary.
                Otherwise, the song will be added(appending) to the end of the list.'''
        
        song_found = find_object(track, self.tracks)
        if song_found is None:
            song_found = Song(track, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    '''Class to store artist details.
    
    Attributes:
        name (str): The name of the artist.
        albums(List[Albums]): A list of Albums by the artist.
            the list consists of Album objects.
    Methods:
        add_album: Used to add new album to the artists albums list'''

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        '''Add a new album to the list.
        
        Args:
            album (Album): Album object to add to the list'''
        
        self.albums.append(album)
    
    def add_song(self, name, year, title):
        '''Checks for an Album in the self.albums list, If the Album
        does not exist, a new Album object will be created and appended
        to self.albums list.
        This method will add a song to the Albums track list using the
        .add_song() method of Album class.
        
        Args:
            name (str): Name of the album
            year (int): The year album was produced
            title (str): The title of the song'''
        
        album_found = find_object(name, self.albums)
        if album_found is None:
            print(name + ': not found!')
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print('Found Album: ' + name)

        album_found.add_track(title)


def find_object(field, object_list):
    '''Checks if the passed field is same as the .name attribute
    of an object in a list of object.
    returns None if not found'''

    for item in object_list:
        if item.name == field:
            return item
    return None

def load_data():
    """Creates an empty list of Artist objects.
    Reads each line of a txt file and separates artist, album, year & song name.
    Checks if the artist already exists in the list, if not creates a new
    Artist object with that name and appends it to the artist list.
    If the Artist object already exists in the list, uses .add_song() method
    and passes album, year and song field.
    Returns a list of Artist objects after parsing the txt file."""

    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            #data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:      # If the artist is new.
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)

            new_artist.add_song(album_field, year_field, song_field)        # If the artist already exists in artist list.

    return artist_list

def create_checkfile(artist_list):
    '''Create a check file from the object data for comparison with the original file
    if checkfile.txt and albums.txt are the same, segrigation is successfull.'''

    with open('checkfile.txt', mode='w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print('{0.name}\t{1.name}\t{1.year}\t{2.title}'.format(new_artist, new_album, new_song), file=checkfile)


if __name__ == '__main__':
    artists = load_data()
    # for i in artists:
    #     print(i)
    print('There are {} artists'.format(len(artists)))

    create_checkfile(artists)