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