import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import TEMPLE_TYPE_NAME, TEMPLE_TYPE_URI

from openapi_server.models.temple import Temple  # noqa: E501
from openapi_server import util

def temples_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Temple

    Gets a list of all instances of Temple (more information in http://dbpedia.org/ontology/Temple) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Temple]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=TEMPLE_TYPE_URI,
        rdf_type_name=TEMPLE_TYPE_NAME, 
        kls=Temple)

def temples_id_get(id):  # noqa: E501
    """Get a single Temple by its id

    Gets the details of a given Temple (more information in http://dbpedia.org/ontology/Temple) # noqa: E501

    :param id: The ID of the Temple to be retrieved
    :type id: str

    :rtype: Temple
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=TEMPLE_TYPE_URI,
        rdf_type_name=TEMPLE_TYPE_NAME, 
        kls=Temple)
