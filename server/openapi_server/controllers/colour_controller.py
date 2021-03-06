import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import COLOUR_TYPE_NAME, COLOUR_TYPE_URI

from openapi_server.models.colour import Colour  # noqa: E501
from openapi_server import util

def colours_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Colour

    Gets a list of all instances of Colour (more information in http://dbpedia.org/ontology/Colour) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Colour]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=COLOUR_TYPE_URI,
        rdf_type_name=COLOUR_TYPE_NAME, 
        kls=Colour)

def colours_id_get(id):  # noqa: E501
    """Get a single Colour by its id

    Gets the details of a given Colour (more information in http://dbpedia.org/ontology/Colour) # noqa: E501

    :param id: The ID of the Colour to be retrieved
    :type id: str

    :rtype: Colour
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=COLOUR_TYPE_URI,
        rdf_type_name=COLOUR_TYPE_NAME, 
        kls=Colour)
