import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TELEVISIONSEASON_TYPE_NAME, TELEVISIONSEASON_TYPE_URI

from openapi_server.models.television_season import TelevisionSeason  # noqa: E501
from openapi_server import util

def televisionseasons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of TelevisionSeason

    Gets a list of all instances of TelevisionSeason (more information in http://dbpedia.org/ontology/TelevisionSeason) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[TelevisionSeason]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TELEVISIONSEASON_TYPE_URI,
        rdf_type_name=TELEVISIONSEASON_TYPE_NAME, 
        kls=TelevisionSeason)

def televisionseasons_id_get(id):  # noqa: E501
    """Get a single TelevisionSeason by its id

    Gets the details of a given TelevisionSeason (more information in http://dbpedia.org/ontology/TelevisionSeason) # noqa: E501

    :param id: The ID of the TelevisionSeason to be retrieved
    :type id: str

    :rtype: TelevisionSeason
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TELEVISIONSEASON_TYPE_URI,
        rdf_type_name=TELEVISIONSEASON_TYPE_NAME, 
        kls=TelevisionSeason)
