import logging.config

from dependency_injector import containers, providers
from services import PreferenceService, MediaPlaylistIOService

class DIContainer(containers.DeclarativeContainer):
    config = providers.Configuration(ini_files=["config.ini"])

    logging = providers.Resource(
        logging.config.fileConfig,
        fname="logging.ini",
    )
    media_playlist_io_service = providers.Singleton(
        MediaPlaylistIOService
    )

    preference_service = providers.Singleton(
        PreferenceService,
        media_playlist_io_service=media_playlist_io_service
    )