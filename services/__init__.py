import logging
import __future__
import javaproperties

from media import MediaPlaylist, PhotoMedia, WatchMedia
from preferences import Preference, Size, Position, Setting


class BaseService:

    def __init__(self) -> None:
        self.logger = logging.getLogger(
            f"{__name__}.{self.__class__.__name__}",
        )


class PreferenceService(BaseService):
    _preference: Preference

    def __init__(self):
        super().__init__()

        with open("pref.properties", "r", encoding="utf-8") as f:
            self.logger.info(f"reading file: pref.properties ")
            try:
                props = javaproperties.load(f)
                sz = Size()
                sz.width = int(props["app.size.width"])
                sz.height = int(props["app.size.height"])

                pt = Position()
                pt.left = int(props["app.location.x"])
                pt.top = int(props["app.location.y"])

                self._preference = Preference()
                self._preference.computer_name = props["app.computer"]
                self._preference.size = sz
                self._preference.position = pt

                for index in range(0, int(props['app.player.video.windows.number'])):
                    sz = Size()
                    sz.width = int(props[f"app.player.{index + 1}.size.width"])
                    sz.height = int(props[f"app.player.{index + 1}.size.height"])

                    pt = Position()
                    pt.left = int(props[f"app.player.{index + 1}.location.x"])
                    pt.top = int(props[f"app.player.{index + 1}.location.y"])

                    st = Setting(index)
                    st.size = sz
                    st.position = pt
                    
                    self.logger.info(f"setting {index + 1}: dummy playlist")
                    playlist = MediaPlaylist()
                    playlist.add_media(WatchMedia())
                    playlist.add_media(PhotoMedia("media/photo1.jpg"))
                    
                    st.playlist = playlist


                    self._preference.settings_add(st)

            except Exception as e:
                self.logger.error("error occurred:", e)

    @property
    def preference(self):
        return self._preference
