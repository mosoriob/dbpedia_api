import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PLANET_TYPE_NAME, PLANET_TYPE_URI

from openapi_server.models.planet import Planet  # noqa: E501
from openapi_server import util

def planets_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Planet

    Gets a list of all instances of Planet (more information in http://dbpedia.org/ontology/Planet) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Planet]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PLANET_TYPE_URI,
        rdf_type_name=PLANET_TYPE_NAME, 
        kls=Planet)

def planets_id_get(id):  # noqa: E501
    """Get a single Planet by its id

    Gets the details of a given Planet (more information in http://dbpedia.org/ontology/Planet) # noqa: E501

    :param id: The ID of the Planet to be retrieved
    :type id: str

    :rtype: Planet
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PLANET_TYPE_URI,
        rdf_type_name=PLANET_TYPE_NAME, 
        kls=Planet)
