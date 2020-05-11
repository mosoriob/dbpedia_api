import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MOSQUE_TYPE_NAME, MOSQUE_TYPE_URI

from openapi_server.models.mosque import Mosque  # noqa: E501
from openapi_server import util

def mosques_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Mosque

    Gets a list of all instances of Mosque (more information in http://dbpedia.org/ontology/Mosque) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Mosque]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MOSQUE_TYPE_URI,
        rdf_type_name=MOSQUE_TYPE_NAME, 
        kls=Mosque)

def mosques_id_get(id):  # noqa: E501
    """Get a single Mosque by its id

    Gets the details of a given Mosque (more information in http://dbpedia.org/ontology/Mosque) # noqa: E501

    :param id: The ID of the Mosque to be retrieved
    :type id: str

    :rtype: Mosque
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MOSQUE_TYPE_URI,
        rdf_type_name=MOSQUE_TYPE_NAME, 
        kls=Mosque)
