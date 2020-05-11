import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CRIMINAL_TYPE_NAME, CRIMINAL_TYPE_URI

from openapi_server.models.criminal import Criminal  # noqa: E501
from openapi_server import util

def criminals_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Criminal

    Gets a list of all instances of Criminal (more information in http://dbpedia.org/ontology/Criminal) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Criminal]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CRIMINAL_TYPE_URI,
        rdf_type_name=CRIMINAL_TYPE_NAME, 
        kls=Criminal)

def criminals_id_get(id):  # noqa: E501
    """Get a single Criminal by its id

    Gets the details of a given Criminal (more information in http://dbpedia.org/ontology/Criminal) # noqa: E501

    :param id: The ID of the Criminal to be retrieved
    :type id: str

    :rtype: Criminal
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CRIMINAL_TYPE_URI,
        rdf_type_name=CRIMINAL_TYPE_NAME, 
        kls=Criminal)
