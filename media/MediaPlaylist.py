import __future__

from media import BaseMedia, MediaTypeEnum


import logging
from typing import List
from uuid import uuid4


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