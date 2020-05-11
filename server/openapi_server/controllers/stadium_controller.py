import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import STADIUM_TYPE_NAME, STADIUM_TYPE_URI

from openapi_server.models.stadium import Stadium  # noqa: E501
from openapi_server import util

def stadiums_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Stadium

    Gets a list of all instances of Stadium (more information in http://dbpedia.org/ontology/Stadium) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Stadium]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=STADIUM_TYPE_URI,
        rdf_type_name=STADIUM_TYPE_NAME, 
        kls=Stadium)

def stadiums_id_get(id):  # noqa: E501
    """Get a single Stadium by its id

    Gets the details of a given Stadium (more information in http://dbpedia.org/ontology/Stadium) # noqa: E501

    :param id: The ID of the Stadium to be retrieved
    :type id: str

    :rtype: Stadium
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=STADIUM_TYPE_URI,
        rdf_type_name=STADIUM_TYPE_NAME, 
        kls=Stadium)
