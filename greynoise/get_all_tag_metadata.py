from connectors.core.connector import ConnectorError, get_logger

from greynoise import GreyNoise

from .constants import INTEGRATION_NAME, LOGGER_NAME

logger = get_logger(LOGGER_NAME)


def get_all_tag_metadata(config, params):
    api_key = config.get("api_key")
    api_type = config.get("api_type")

    if api_type == "community":
        raise ConnectorError("This action is not support with Community API Key")
    else:
        api_client = GreyNoise(api_key=api_key, integration_name=INTEGRATION_NAME)
        api_response = api_client.metadata()
        return api_response
