import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import LOCALITY_TYPE_NAME, LOCALITY_TYPE_URI

from openapi_server.models.locality import Locality  # noqa: E501
from openapi_server import util

def localitys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Locality

    Gets a list of all instances of Locality (more information in http://dbpedia.org/ontology/Locality) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Locality]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=LOCALITY_TYPE_URI,
        rdf_type_name=LOCALITY_TYPE_NAME, 
        kls=Locality)

def localitys_id_get(id):  # noqa: E501
    """Get a single Locality by its id

    Gets the details of a given Locality (more information in http://dbpedia.org/ontology/Locality) # noqa: E501

    :param id: The ID of the Locality to be retrieved
    :type id: str

    :rtype: Locality
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=LOCALITY_TYPE_URI,
        rdf_type_name=LOCALITY_TYPE_NAME, 
        kls=Locality)
