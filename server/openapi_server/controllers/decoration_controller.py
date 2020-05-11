import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DECORATION_TYPE_NAME, DECORATION_TYPE_URI

from openapi_server.models.decoration import Decoration  # noqa: E501
from openapi_server import util

def decorations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Decoration

    Gets a list of all instances of Decoration (more information in http://dbpedia.org/ontology/Decoration) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Decoration]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DECORATION_TYPE_URI,
        rdf_type_name=DECORATION_TYPE_NAME, 
        kls=Decoration)

def decorations_id_get(id):  # noqa: E501
    """Get a single Decoration by its id

    Gets the details of a given Decoration (more information in http://dbpedia.org/ontology/Decoration) # noqa: E501

    :param id: The ID of the Decoration to be retrieved
    :type id: str

    :rtype: Decoration
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DECORATION_TYPE_URI,
        rdf_type_name=DECORATION_TYPE_NAME, 
        kls=Decoration)
