from connectors.core.connector import ConnectorError, get_logger

from greynoise import GreyNoise

from .constants import INTEGRATION_NAME, LOGGER_NAME

logger = get_logger(LOGGER_NAME)


def stats_query(config, params):
    query = params.get("query")
    if not query:
        raise ConnectorError("Missing required input")

    api_key = config.get("api_key")
    api_type = config.get("api_type")

    if api_type == "community":
        raise ConnectorError("This action is not supported with Community API Key")
    else:
        api_client = GreyNoise(api_key=api_key, integration_name=INTEGRATION_NAME)
        api_response = api_client.stats(query)
        return api_response
