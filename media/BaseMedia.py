from media import MediaTypeEnum


import logging


class BaseMedia:
    """

    """

    _duration: float = 5.0
    _days = [True, True, True, True, True, True, True]
    _local_path: str

    def __init__(self, media_type: MediaTypeEnum, path : str = "") -> None:
        self._media_type = media_type
        self._local_path = path
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )

    @property
    def media_type(self):
        return self._media_type

    @property
    def duration(self) -> float:
        return self._duration

    @duration.setter
    def duration(self, value: float):
        self._duration = value

    def is_playable(self) -> bool:
        return True

    def local_path(self) -> str:
        return self._local_path

    def __str__(self) -> str:
        return f"media_type {self._media_type} | duration {self._duration:0.2f} | days {self._days}"