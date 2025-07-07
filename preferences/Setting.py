from media import MediaPlaylist
from preferences.Position import Position
from preferences.Size import Size


class Setting:
    __index: int
    _size: Size
    _position: Position
    _playlist : MediaPlaylist = None

    def __init__(self, index: int):
        self.__index = index

    @property
    def index(self):
        return self.__index

    @property
    def size(self) -> Size:
        return self._size

    @size.setter
    def size(self, value: Size):
        self._size = value

    @property
    def position(self) -> Position:
        return self._position

    @position.setter
    def position(self, value: Position):
        self._position = value

    @property
    def playlist(self) -> MediaPlaylist:
        return self._playlist

    @playlist.setter
    def playlist(self, value: MediaPlaylist):
        self._playlist = value