import logging.config

from dependency_injector import containers, providers
from services import PreferenceService

class Container(containers.DeclarativeContainer):
    config = providers.Configuration(ini_files=["config.ini"])

    logging = providers.Resource(
        logging.config.fileConfig,
        fname="logging.ini",
    )

    preference_service = providers.Singleton(
        PreferenceService
    )
