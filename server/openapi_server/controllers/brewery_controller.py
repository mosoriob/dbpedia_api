import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BREWERY_TYPE_NAME, BREWERY_TYPE_URI

from openapi_server.models.brewery import Brewery  # noqa: E501
from openapi_server import util

def brewerys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Brewery

    Gets a list of all instances of Brewery (more information in http://dbpedia.org/ontology/Brewery) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Brewery]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BREWERY_TYPE_URI,
        rdf_type_name=BREWERY_TYPE_NAME, 
        kls=Brewery)

def brewerys_id_get(id):  # noqa: E501
    """Get a single Brewery by its id

    Gets the details of a given Brewery (more information in http://dbpedia.org/ontology/Brewery) # noqa: E501

    :param id: The ID of the Brewery to be retrieved
    :type id: str

    :rtype: Brewery
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BREWERY_TYPE_URI,
        rdf_type_name=BREWERY_TYPE_NAME, 
        kls=Brewery)
