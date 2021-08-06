from connectors.core.connector import ConnectorError, get_logger

from greynoise import GreyNoise

from .constants import INTEGRATION_NAME, LOGGER_NAME

logger = get_logger(LOGGER_NAME)


def get_tag_details(config, params):
    tag_name = params.get("tag_name")
    if not tag_name:
        raise ConnectorError("Missing required input")

    api_key = config.get("api_key")
    api_type = config.get("api_type")

    if api_type == "community":
        raise ConnectorError("This action is not support with Community API Key")
    else:
        api_client = GreyNoise(api_key=api_key, integration_name=INTEGRATION_NAME)
        api_response = api_client.metadata()

        tag_found = False
        for tag in api_response["metadata"]:
            if tag["name"] == tag_name:
                api_response = tag
                tag_found = True
                break

        if not tag_found:
            raise ConnectorError("Invalid Tag Name Provided")

        return api_response
