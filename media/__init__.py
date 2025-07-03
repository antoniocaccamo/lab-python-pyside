import logging
from enum import Enum
import __future__
from typing import List
from uuid import uuid4


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

    def __str__(self) -> str:
        return f"media_type {self._media_type} | duration {self._duration:0.2f} | days {self._days}"


class WatchMedia(BaseMedia):
    """

    """

    def __init__(self):
        super().__init__(MediaTypeEnum.Watch)


class PhotoMedia(BaseMedia):
    """

    """

    def __init__(self, path: str ):
        assert path, "Path cannot be empty"
        super().__init__(MediaTypeEnum.Photo, path)

class VideoMedia(BaseMedia):
    """

    """

    def __init__(self, path: str ):
        assert path, "Path cannot be empty"
        super().__init__(MediaTypeEnum.Video, path)


class MediaPlaylist:
    """

    """
    _name = uuid4()
    _play_list: List[BaseMedia] = list()
    _loop_index=-1

    def __init__(self) -> None:
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )

    @property
    def play_list(self) -> List[BaseMedia]:
        return self._play_list

    def add_media(self, media: BaseMedia):
        self._play_list.append(media)
        self.logger.info(f"Added media: {media}")
   
    def get_current_media(self) -> BaseMedia:
        self._loop_index += 1
        idx = self._loop_index % len(self._play_list)
        return self._play_list[idx]
    
    def __str__(self) -> str:
        return f"playlist {self._name} | media count {len(self._play_list)} | current index {self._loop_index}"