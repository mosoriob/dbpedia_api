import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import FLAG_TYPE_NAME, FLAG_TYPE_URI

from openapi_server.models.flag import Flag  # noqa: E501
from openapi_server import util

def flags_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Flag

    Gets a list of all instances of Flag (more information in http://dbpedia.org/ontology/Flag) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Flag]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=FLAG_TYPE_URI,
        rdf_type_name=FLAG_TYPE_NAME, 
        kls=Flag)

def flags_id_get(id):  # noqa: E501
    """Get a single Flag by its id

    Gets the details of a given Flag (more information in http://dbpedia.org/ontology/Flag) # noqa: E501

    :param id: The ID of the Flag to be retrieved
    :type id: str

    :rtype: Flag
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=FLAG_TYPE_URI,
        rdf_type_name=FLAG_TYPE_NAME, 
        kls=Flag)
