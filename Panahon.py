class Songs:        #add yung (Playlist), di ko malagay me selp cazi di gagana sa gdb
    def __init__(self, title, artist, album, duration, year):
        self.title = title
        self.artist = artist
        self.album = album
        self.duration = duration
        self.year = year

    def __str__(self):
        return f"{self.title} - {self.artist}"

#Example lang diss ahh vvv

IPRAPK = Songs("Ikaw Pa Rin Ang Pipiliin Ko", "Cup of Joe","","","")

print(IPRAPK)
text = str(IPRAPK)

#BTW IDK KUNG GAGANA ITO PAGINADD YUNG ANO NI LYRIE AH, SABI NALNG KAY ME IS NOT.
