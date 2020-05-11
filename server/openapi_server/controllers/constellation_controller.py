import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CONSTELLATION_TYPE_NAME, CONSTELLATION_TYPE_URI

from openapi_server.models.constellation import Constellation  # noqa: E501
from openapi_server import util

def constellations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Constellation

    Gets a list of all instances of Constellation (more information in http://dbpedia.org/ontology/Constellation) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Constellation]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CONSTELLATION_TYPE_URI,
        rdf_type_name=CONSTELLATION_TYPE_NAME, 
        kls=Constellation)

def constellations_id_get(id):  # noqa: E501
    """Get a single Constellation by its id

    Gets the details of a given Constellation (more information in http://dbpedia.org/ontology/Constellation) # noqa: E501

    :param id: The ID of the Constellation to be retrieved
    :type id: str

    :rtype: Constellation
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CONSTELLATION_TYPE_URI,
        rdf_type_name=CONSTELLATION_TYPE_NAME, 
        kls=Constellation)
