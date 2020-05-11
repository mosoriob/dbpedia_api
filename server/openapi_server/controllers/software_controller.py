import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SOFTWARE_TYPE_NAME, SOFTWARE_TYPE_URI

from openapi_server.models.software import Software  # noqa: E501
from openapi_server import util

def softwares_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Software

    Gets a list of all instances of Software (more information in http://dbpedia.org/ontology/Software) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Software]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SOFTWARE_TYPE_URI,
        rdf_type_name=SOFTWARE_TYPE_NAME, 
        kls=Software)

def softwares_id_get(id):  # noqa: E501
    """Get a single Software by its id

    Gets the details of a given Software (more information in http://dbpedia.org/ontology/Software) # noqa: E501

    :param id: The ID of the Software to be retrieved
    :type id: str

    :rtype: Software
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SOFTWARE_TYPE_URI,
        rdf_type_name=SOFTWARE_TYPE_NAME, 
        kls=Software)
