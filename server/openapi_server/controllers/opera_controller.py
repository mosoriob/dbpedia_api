import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import OPERA_TYPE_NAME, OPERA_TYPE_URI

from openapi_server.models.opera import Opera  # noqa: E501
from openapi_server import util

def operas_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Opera

    Gets a list of all instances of Opera (more information in http://dbpedia.org/ontology/Opera) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Opera]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=OPERA_TYPE_URI,
        rdf_type_name=OPERA_TYPE_NAME, 
        kls=Opera)

def operas_id_get(id):  # noqa: E501
    """Get a single Opera by its id

    Gets the details of a given Opera (more information in http://dbpedia.org/ontology/Opera) # noqa: E501

    :param id: The ID of the Opera to be retrieved
    :type id: str

    :rtype: Opera
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=OPERA_TYPE_URI,
        rdf_type_name=OPERA_TYPE_NAME, 
        kls=Opera)
