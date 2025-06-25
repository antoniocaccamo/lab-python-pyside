from typing import List


class Size:
    _width: int
    _height: int

    # def __init__(self, w : int , h : int):

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value) -> None:
        self._width = value

    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value) -> None:
        self._height = value


class Position:
    _top: int
    _left: int

    # def __init__(self, w : int , h : int):

    @property
    def top(self) -> int:
        return self._top

    @top.setter
    def top(self, value) -> None:
        self._top = value

    @property
    def left(self) -> int:
        return self._left

    @left.setter
    def left(self, value) -> None:
        self._left = value


class Setting:
    __index: int
    _size: Size
    _position: Position

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


class Preference:
    _computer_name: str
    _size: Size
    _position: Position
    _settings: List[Setting] = []

    @property
    def computer_name(self):
        return self._computer_name

    @computer_name.setter
    def computer_name(self, value):
        self._computer_name = value

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
    def settings(self):
        return self._settings

    def settings_add(self, setting: Setting):
        self._settings.append(setting)
