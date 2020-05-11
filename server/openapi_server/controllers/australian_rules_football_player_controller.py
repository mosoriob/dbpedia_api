import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AUSTRALIANRULESFOOTBALLPLAYER_TYPE_NAME, AUSTRALIANRULESFOOTBALLPLAYER_TYPE_URI

from openapi_server.models.australian_rules_football_player import AustralianRulesFootballPlayer  # noqa: E501
from openapi_server import util

def australianrulesfootballplayers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of AustralianRulesFootballPlayer

    Gets a list of all instances of AustralianRulesFootballPlayer (more information in http://dbpedia.org/ontology/AustralianRulesFootballPlayer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[AustralianRulesFootballPlayer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AUSTRALIANRULESFOOTBALLPLAYER_TYPE_URI,
        rdf_type_name=AUSTRALIANRULESFOOTBALLPLAYER_TYPE_NAME, 
        kls=AustralianRulesFootballPlayer)

def australianrulesfootballplayers_id_get(id):  # noqa: E501
    """Get a single AustralianRulesFootballPlayer by its id

    Gets the details of a given AustralianRulesFootballPlayer (more information in http://dbpedia.org/ontology/AustralianRulesFootballPlayer) # noqa: E501

    :param id: The ID of the AustralianRulesFootballPlayer to be retrieved
    :type id: str

    :rtype: AustralianRulesFootballPlayer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AUSTRALIANRULESFOOTBALLPLAYER_TYPE_URI,
        rdf_type_name=AUSTRALIANRULESFOOTBALLPLAYER_TYPE_NAME, 
        kls=AustralianRulesFootballPlayer)
