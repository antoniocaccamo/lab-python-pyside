import __future__

from media import BaseMedia, MediaTypeEnum


class WebMedia(BaseMedia):

    """
    Represents a web-based media type, typically used for streaming or online content.
    """
    
    def __init__(self, path: str ):
        assert path, "Path cannot be empty"
        super().__init__(MediaTypeEnum.Web, path)