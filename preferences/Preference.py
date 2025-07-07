from preferences.Position import Position
from preferences.Setting import Setting
from preferences.Size import Size


from typing import List


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