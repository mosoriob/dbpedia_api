import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SPACECRAFT_TYPE_NAME, SPACECRAFT_TYPE_URI

from openapi_server.models.spacecraft import Spacecraft  # noqa: E501
from openapi_server import util

def spacecrafts_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Spacecraft

    Gets a list of all instances of Spacecraft (more information in http://dbpedia.org/ontology/Spacecraft) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Spacecraft]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SPACECRAFT_TYPE_URI,
        rdf_type_name=SPACECRAFT_TYPE_NAME, 
        kls=Spacecraft)

def spacecrafts_id_get(id):  # noqa: E501
    """Get a single Spacecraft by its id

    Gets the details of a given Spacecraft (more information in http://dbpedia.org/ontology/Spacecraft) # noqa: E501

    :param id: The ID of the Spacecraft to be retrieved
    :type id: str

    :rtype: Spacecraft
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SPACECRAFT_TYPE_URI,
        rdf_type_name=SPACECRAFT_TYPE_NAME, 
        kls=Spacecraft)
