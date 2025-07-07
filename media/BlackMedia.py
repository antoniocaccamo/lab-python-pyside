import __future__

from media import BaseMedia, MediaTypeEnum

class BlackMedia(BaseMedia):
    """
    Represents a media type that is black, typically used for screensavers or blank displays.
    """

    def __init__(self) -> None:
        super().__init__(MediaTypeEnum.Black, None)

  