import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BEER_TYPE_NAME, BEER_TYPE_URI

from openapi_server.models.beer import Beer  # noqa: E501
from openapi_server import util

def beers_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Beer

    Gets a list of all instances of Beer (more information in http://dbpedia.org/ontology/Beer) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Beer]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BEER_TYPE_URI,
        rdf_type_name=BEER_TYPE_NAME, 
        kls=Beer)

def beers_id_get(id):  # noqa: E501
    """Get a single Beer by its id

    Gets the details of a given Beer (more information in http://dbpedia.org/ontology/Beer) # noqa: E501

    :param id: The ID of the Beer to be retrieved
    :type id: str

    :rtype: Beer
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BEER_TYPE_URI,
        rdf_type_name=BEER_TYPE_NAME, 
        kls=Beer)
