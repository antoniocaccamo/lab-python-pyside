import __future__

from media import BaseMedia, MediaTypeEnum

class HiddenMedia(BaseMedia):
    """
    Represents a media type that is hidden, typically used for screensavers or blank displays.
    """

    def __init__(self) -> None:
        super().__init__(MediaTypeEnum.Hidden, None)

  