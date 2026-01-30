Playlist = []  # empty string array


class song:
    def __init__(self, title, artist, duration):
        self.title = title  # string variable
        self.artist = artist  # string variable
        self.duration = duration  # integer variable

    @property
    def GetTitle(self):
        return self.title

    @GetTitle.setter
    def GetTitle(self, value):
        self.title = value

    @property
    def GetArtist(self):
        return self.artist

    @GetArtist.setter
    def GetArtist(self, value):
        self.artist = value

    @property
    def GetDuration(self):
        return self.duration

    @GetDuration.setter
    def GetDuration(self, value):
        self.duration = value

    def GetDurationMinutes(self):
        duration_in_seconds = self.duration
        min = int(duration_in_seconds / 60)
        sec = duration_in_seconds % 60
        return min, sec


for count in range(3):
    print(f"\n")
    title = input(f"Enter song{count+1} title: ")
    artist = input(f"Enter artist name: ")
    duration = float(input(f"Enter duration: "))
    Playlist.append(song(title, artist, duration))

print()
for count in range(3):
    mins, secs = Playlist[count].GetDurationMinutes()
    print(
        f"Song{count+1} = {Playlist[count].GetTitle}, {Playlist[count].GetArtist}, {mins} minutes and {secs} seconds"
    )
