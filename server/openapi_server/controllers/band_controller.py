import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BAND_TYPE_NAME, BAND_TYPE_URI

from openapi_server.models.band import Band  # noqa: E501
from openapi_server import util

def bands_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Band

    Gets a list of all instances of Band (more information in http://dbpedia.org/ontology/Band) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Band]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BAND_TYPE_URI,
        rdf_type_name=BAND_TYPE_NAME, 
        kls=Band)

def bands_id_get(id):  # noqa: E501
    """Get a single Band by its id

    Gets the details of a given Band (more information in http://dbpedia.org/ontology/Band) # noqa: E501

    :param id: The ID of the Band to be retrieved
    :type id: str

    :rtype: Band
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BAND_TYPE_URI,
        rdf_type_name=BAND_TYPE_NAME, 
        kls=Band)
