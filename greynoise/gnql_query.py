from connectors.core.connector import ConnectorError, get_logger

from greynoise import GreyNoise

from .constants import INTEGRATION_NAME, LOGGER_NAME

logger = get_logger(LOGGER_NAME)


def gnql_query(config, params):
    query = params.get("query")
    max_results = str(params.get("max_results"))
    if not query:
        raise ConnectorError("Missing required input")

    if not max_results:
        max_results = "10"

    if not max_results.isnumeric():
        raise ConnectorError("Invalid input for Max Results Provided")

    api_key = config.get("api_key")
    api_type = config.get("api_type")

    if api_type == "community":
        raise ConnectorError("This action is not supported with Community API Key")
    else:
        api_client = GreyNoise(api_key=api_key, integration_name=INTEGRATION_NAME)
        api_response = api_client.query(query, size=max_results)
        return api_response
