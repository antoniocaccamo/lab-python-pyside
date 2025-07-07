import __future__

from media import BaseMedia, MediaTypeEnum


class WatchMedia(BaseMedia):
    
    """    
    Represents a media type that is used for watch faces or similar applications.
    Typically does not have a specific path or content, as it is designed to display information
    rather than play media files"""

    def __init__(self):
        super().__init__(MediaTypeEnum.Watch)