import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CHRISTIANBISHOP_TYPE_NAME, CHRISTIANBISHOP_TYPE_URI

from openapi_server.models.christian_bishop import ChristianBishop  # noqa: E501
from openapi_server import util

def christianbishops_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ChristianBishop

    Gets a list of all instances of ChristianBishop (more information in http://dbpedia.org/ontology/ChristianBishop) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ChristianBishop]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CHRISTIANBISHOP_TYPE_URI,
        rdf_type_name=CHRISTIANBISHOP_TYPE_NAME, 
        kls=ChristianBishop)

def christianbishops_id_get(id):  # noqa: E501
    """Get a single ChristianBishop by its id

    Gets the details of a given ChristianBishop (more information in http://dbpedia.org/ontology/ChristianBishop) # noqa: E501

    :param id: The ID of the ChristianBishop to be retrieved
    :type id: str

    :rtype: ChristianBishop
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CHRISTIANBISHOP_TYPE_URI,
        rdf_type_name=CHRISTIANBISHOP_TYPE_NAME, 
        kls=ChristianBishop)
