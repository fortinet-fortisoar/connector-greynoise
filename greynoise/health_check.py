from connectors.core.connector import get_logger

from greynoise import GreyNoise

from .constants import INTEGRATION_NAME, LOGGER_NAME

logger = get_logger(LOGGER_NAME)


def health_check(config=None, *args, **kwargs):
    api_key = config.get("api_key")
    api_client = GreyNoise(api_key=api_key, integration_name=INTEGRATION_NAME)
    api_client.test_connection()

    return "Connector is Available"
