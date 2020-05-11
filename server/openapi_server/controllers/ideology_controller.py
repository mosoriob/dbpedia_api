import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import IDEOLOGY_TYPE_NAME, IDEOLOGY_TYPE_URI

from openapi_server.models.ideology import Ideology  # noqa: E501
from openapi_server import util

def ideologys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Ideology

    Gets a list of all instances of Ideology (more information in http://dbpedia.org/ontology/Ideology) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Ideology]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=IDEOLOGY_TYPE_URI,
        rdf_type_name=IDEOLOGY_TYPE_NAME, 
        kls=Ideology)

def ideologys_id_get(id):  # noqa: E501
    """Get a single Ideology by its id

    Gets the details of a given Ideology (more information in http://dbpedia.org/ontology/Ideology) # noqa: E501

    :param id: The ID of the Ideology to be retrieved
    :type id: str

    :rtype: Ideology
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=IDEOLOGY_TYPE_URI,
        rdf_type_name=IDEOLOGY_TYPE_NAME, 
        kls=Ideology)
