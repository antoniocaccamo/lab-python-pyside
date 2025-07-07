import __future__

from media import BaseMedia, MediaTypeEnum

class PhotoMedia(BaseMedia):
    """

    """

    def __init__(self, path: str ):
        assert path, "Path cannot be empty"
        super().__init__(MediaTypeEnum.Photo, path)