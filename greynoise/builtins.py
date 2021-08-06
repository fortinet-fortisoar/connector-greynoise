# FSR Autogenerated Content. DO NOT DELETE
from .get_all_tag_metadata import get_all_tag_metadata
from .get_tag_details import get_tag_details
from .gnql_query import gnql_query
from .lookup_ip_community import lookup_ip_community
from .lookup_ip_complete import lookup_ip_complete
from .lookup_ip_context import lookup_ip_context
from .lookup_ip_quick import lookup_ip_quick
from .lookup_ip_riot import lookup_ip_riot
from .stats_query import stats_query

supported_operations = {
    "lookup_ip_context": lookup_ip_context,
    "lookup_ip_riot": lookup_ip_riot,
    "lookup_ip_community": lookup_ip_community,
    "lookup_ip_quick": lookup_ip_quick,
    "gnql_query": gnql_query,
    "lookup_ip_complete": lookup_ip_complete,
    "stats_query": stats_query,
    "get_all_tag_metadata": get_all_tag_metadata,
    "get_tag_details": get_tag_details,
}
