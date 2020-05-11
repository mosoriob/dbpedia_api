import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PAINTER_TYPE_NAME, PAINTER_TYPE_URI

from openapi_server.models.painter import Painter  # noqa: E501
from openapi_server import util

def painters_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Painter

    Gets a list of all instances of Painter (more information in http://dbpedia.org/ontology/Painter) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Painter]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PAINTER_TYPE_URI,
        rdf_type_name=PAINTER_TYPE_NAME, 
        kls=Painter)

def painters_id_get(id):  # noqa: E501
    """Get a single Painter by its id

    Gets the details of a given Painter (more information in http://dbpedia.org/ontology/Painter) # noqa: E501

    :param id: The ID of the Painter to be retrieved
    :type id: str

    :rtype: Painter
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PAINTER_TYPE_URI,
        rdf_type_name=PAINTER_TYPE_NAME, 
        kls=Painter)
