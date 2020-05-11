import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CONTINENT_TYPE_NAME, CONTINENT_TYPE_URI

from openapi_server.models.continent import Continent  # noqa: E501
from openapi_server import util

def continents_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Continent

    Gets a list of all instances of Continent (more information in http://dbpedia.org/ontology/Continent) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Continent]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CONTINENT_TYPE_URI,
        rdf_type_name=CONTINENT_TYPE_NAME, 
        kls=Continent)

def continents_id_get(id):  # noqa: E501
    """Get a single Continent by its id

    Gets the details of a given Continent (more information in http://dbpedia.org/ontology/Continent) # noqa: E501

    :param id: The ID of the Continent to be retrieved
    :type id: str

    :rtype: Continent
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CONTINENT_TYPE_URI,
        rdf_type_name=CONTINENT_TYPE_NAME, 
        kls=Continent)
