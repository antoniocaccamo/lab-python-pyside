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