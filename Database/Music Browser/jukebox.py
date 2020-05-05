import sqlite3 as sql
import tkinter as tk


class Scrollbox(tk.Listbox):

    def __init__(self, window, **kwargs):
        super().__init__(window, **kwargs)

        self.scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL, command=self.yview)

    def grid(self, row, column, sticky='nsw', rowspan=1, columnspan=1, **kwargs):
        super().grid(row=row, column=column, sticky=sticky, rowspan=rowspan, columnspan=columnspan, **kwargs)
        self.scrollbar.grid(row=row, column=column, sticky='nse', rowspan=rowspan)
        self['yscrollcommand'] = self.scrollbar.set


class Datalistbox(Scrollbox):

    def __init__(self, window, connection, table, field, sort_order=(), **kwargs):
        super().__init__(window, **kwargs)

        self.linked_box = None
        self.link_field = None
        self.cursor = connection.cursor()
        self.table = table
        self.field = field
        self.bind('<<ListboxSelect>>', self.on_select)

        self.sql_select = "SELECT " + self.field + ", _id " + "FROM " + self.table
        if sort_order:
            self.sql_order = " ORDER BY " + ','.join(sort_order)
        else:
            self.sql_order = " ORDER BY " + self.field

    def clear(self):
        self.delete(0, tk.END)

    def link(self, widget, link_field):
        self.linked_box = widget
        widget.link_field = link_field

    def requery(self, link_value=None):
        if link_value and self.link_field:
            sql = self.sql_select + " WHERE " + self.link_field + '=?' + self.sql_order
            self.cursor.execute(sql, (link_value, ))
        else:
            self.cursor.execute(self.sql_select)

        # clear listbox contents before loading
        self.clear()
        for value in self.cursor:
            self.insert(tk.END, value[0])

        if self.linked_box:
            self.linked_box.clear()

    def on_select(self, event):
        if self.linked_box:
            print(self is event.widget)     # TODO delete
            # lb = event.widget
            index = self.curselection()[0]
            value = self.get(index),

            # get the artist name from database row
            link_id = self.cursor.execute(self.sql_select + " WHERE " + self.field + "=?", value).fetchone()[1]
            self.linked_box.requery(link_id)

        # artist_id = db.execute("SELECT _id FROM artists WHERE artists.name=?", artist_name).fetchone()
        # artist_list = list()
        # for row in db.execute("SELECT name FROM albums WHERE albums.artist = ? ORDER BY albums.name", artist_id):
        #     artist_list.append(row[0])
        # albumLV.set(tuple(artist_list))
        # songsLV.set(("Choose an Album", ))


def get_songs(event):
    lb = event.widget
    index = lb.curselection()[0]
    album_name = (lb.get(index), )

    # get the song names from database
    album_id = db.execute("SELECT _id FROM albums WHERE albums.name=?", album_name).fetchone()
    song_list = list()
    for row in db.execute("SELECT title FROM song WHERE song.album=?", album_id):
        song_list.append(row[0])
    songsLV.set(tuple(song_list))


if __name__ == '__main__':

    db = sql.connect('music.db', detect_types=sql.PARSE_DECLTYPES)

    mainWindow = tk.Tk()
    mainWindow.title('Music Browser')
    mainWindow.geometry('1024x768')

    mainWindow.columnconfigure(0, weight=2)
    mainWindow.columnconfigure(1, weight=2)
    mainWindow.columnconfigure(2, weight=2)
    mainWindow.columnconfigure(3, weight=2)         # Spacer column in right

    mainWindow.rowconfigure(0, weight=1)
    mainWindow.rowconfigure(1, weight=5)
    mainWindow.rowconfigure(2, weight=5)
    mainWindow.rowconfigure(3, weight=1)

    # ______Labels_______#
    tk.Label(mainWindow, text='Artists').grid(row=0, column=0)
    tk.Label(mainWindow, text='Albums').grid(row=0, column=1)
    tk.Label(mainWindow, text='Songs').grid(row=0, column=2)

    # ______Artists Listbox______#
    artistList = Datalistbox(mainWindow, db, "artists", "name")
    artistList.grid(row=1, column=0, sticky='nsew', rowspan=2, padx=(30, 0))
    artistList.configure(border=2, relief='sunken')

    artistList.requery()
    # artistList.bind('<<ListboxSelect>>', get_albums)

    # The Scrollbox class replaces this code
    # artistScroll = tk.Scrollbar(mainWindow, orient=tk.VERTICAL, command=artistList.yview)
    # artistScroll.grid(row=1, column=0, sticky='nse', rowspan=2)
    # artistList['yscrollcommand'] = artistScroll.set

    # ______Albums List_________#
    albumLV = tk.Variable(mainWindow)
    albumLV.set(('Choose an artist', ))
    albumList = Datalistbox(mainWindow, db, "albums", "name", sort_order=('name', ))
    # albumList.requery()
    albumList.grid(row=1, column=1, sticky='nsew', padx=(30, 0))
    albumList.configure(border=2, relief='sunken')

    # albumList.bind('<<ListboxSelect>>', get_songs)
    artistList.link(albumList, "artist")
    # albumScroll = tk.Scrollbar(mainWindow, orient=tk.VERTICAL, command=albumList.yview)
    # albumScroll.grid(row=1, column=1, sticky='nse', rowspan=1)
    # albumList['yscrollcommand'] = albumScroll.set

    # _______Songs Listbox________#
    songsLV = tk.Variable(mainWindow)
    songsLV.set(('Choose an Album', ))
    songsList = Datalistbox(mainWindow, db, 'song', 'title')
    # songsList.requery()
    songsList.grid(row=1, column=2, sticky='nsew', padx=(30, 0))
    songsList.configure(border=2, relief='sunken')

    albumList.link(songsList, "album")

    # songsScroll = tk.Scrollbar(mainWindow, orient=tk.VERTICAL, command=songsList.yview)
    # songsScroll.grid(row=1, column=2, sticky='nse', rowspan=1)
    # songsList['yscrollcommand'] = songsScroll.set

    # ______mainloop______#
    mainWindow.mainloop()
    db.close()
