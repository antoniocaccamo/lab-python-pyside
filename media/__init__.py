import logging
from enum import Enum
import __future__
from typing import List


class MediaTypeEnum(Enum):
    Black = 0
    Hidden = 1
    Watch = 2
    Photo = 3
    Video = 5
    Web = 6


class BaseMedia:
    """

    """

    _duration: float = 5.0
    _days = [True, True, True, True, True, True, True]

    def __init__(self, media_type: MediaTypeEnum) -> None:
        self._media_type = media_type
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

    def __str__(self) -> str:
        return f"media_type {self._media_type} duration {self._duration:0.2f} days {self._days}"


class WatchMedia(BaseMedia):
    """

    """

    def __init__(self):
        super().__init__(MediaTypeEnum.Watch)


class MediaPlaylist:
    """

    """
    
    _play_list: List[BaseMedia] = list()

    def __init__(self) -> None:
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )
