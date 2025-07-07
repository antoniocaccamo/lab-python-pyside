
from media import MediaPlaylist, PhotoMedia, WatchMedia, WebMedia
from preferences import Preference, Position, Setting, Size
from services import BaseService, MediaPlaylistIOService
from dependency_injector.wiring import Provide
import javaproperties
#from di import DIContainer
from services import MediaPlaylistIOService

class PreferenceService(BaseService):

    _media_playlist_io_service : MediaPlaylistIOService 
    _preference: Preference

    def __init__(self , media_playlist_io_service : MediaPlaylistIOService ):
        super().__init__()
        assert media_playlist_io_service, "MediaPlaylistIOService cannot be None"
        self._media_playlist_io_service = media_playlist_io_service
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
                    sz.width  = int(props[f"app.player.{index + 1}.size.width"])
                    sz.height = int(props[f"app.player.{index + 1}.size.height"])

                    pt = Position()
                    pt.left = int(props[f"app.player.{index + 1}.location.x"])
                    pt.top  = int(props[f"app.player.{index + 1}.location.y"])

                    st = Setting(index)
                    st.size = sz
                    st.position = pt

                    
                    st.playlist = self._media_playlist_io_service.load_playlist(
                        props[f"app.player.{index + 1}.sequence.file"]
                    )
                    self._preference.settings_add(st)

            except Exception as e:
                self.logger.error("error occurred:", e)

    @property
    def preference(self):
        return self._preference