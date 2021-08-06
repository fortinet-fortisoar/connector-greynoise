from connectors.core.connector import ConnectorError, get_logger

from greynoise import GreyNoise

from .constants import INTEGRATION_NAME, LOGGER_NAME

logger = get_logger(LOGGER_NAME)


def lookup_ip_complete(config, params):
    ip_address = params.get("ip_address")
    if not ip_address:
        raise ConnectorError("Missing required input")

    api_key = config.get("api_key")
    api_type = config.get("api_type")

    if api_type == "community":
        raise ConnectorError("This action is not support with Community API Key")
    else:
        api_client = GreyNoise(api_key=api_key, integration_name=INTEGRATION_NAME)

        context_response = api_client.ip(ip_address)
        riot_response = api_client.riot(ip_address)

        if context_response["seen"]:
            tags_response = api_client.metadata()
            updated_tags = build_tag_details(tags_response, context_response["tags"])
            context_response.pop("tags")
            context_response["tags"] = updated_tags

        if "riot" in riot_response and "seen" in context_response:
            api_response = context_response.copy()
            api_response.update(riot_response)
        else:
            api_response = context_response
        return api_response


def build_tag_details(metadata, tags):
    detailed_tags = []
    for tag in tags:
        for detailed_tag in metadata["metadata"]:
            if tag == detailed_tag["name"]:
                detailed_tags.append(detailed_tag)
    return detailed_tags
