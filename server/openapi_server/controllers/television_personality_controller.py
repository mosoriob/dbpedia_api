import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TELEVISIONPERSONALITY_TYPE_NAME, TELEVISIONPERSONALITY_TYPE_URI

from openapi_server.models.television_personality import TelevisionPersonality  # noqa: E501
from openapi_server import util

def televisionpersonalitys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of TelevisionPersonality

    Gets a list of all instances of TelevisionPersonality (more information in http://dbpedia.org/ontology/TelevisionPersonality) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[TelevisionPersonality]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TELEVISIONPERSONALITY_TYPE_URI,
        rdf_type_name=TELEVISIONPERSONALITY_TYPE_NAME, 
        kls=TelevisionPersonality)

def televisionpersonalitys_id_get(id):  # noqa: E501
    """Get a single TelevisionPersonality by its id

    Gets the details of a given TelevisionPersonality (more information in http://dbpedia.org/ontology/TelevisionPersonality) # noqa: E501

    :param id: The ID of the TelevisionPersonality to be retrieved
    :type id: str

    :rtype: TelevisionPersonality
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TELEVISIONPERSONALITY_TYPE_URI,
        rdf_type_name=TELEVISIONPERSONALITY_TYPE_NAME, 
        kls=TelevisionPersonality)
