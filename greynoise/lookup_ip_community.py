from connectors.core.connector import ConnectorError, get_logger

from greynoise import GreyNoise

from .constants import INTEGRATION_NAME, LOGGER_NAME

logger = get_logger(LOGGER_NAME)


def lookup_ip_community(config, params):
    ip_address = params.get("ip_address")
    if not ip_address:
        raise ConnectorError("Missing required input")

    api_key = config.get("api_key")

    api_client = GreyNoise(api_key=api_key, integration_name=INTEGRATION_NAME, offering="community")
    api_response = api_client.ip(ip_address)
    return api_response
