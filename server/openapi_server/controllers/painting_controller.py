import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PAINTING_TYPE_NAME, PAINTING_TYPE_URI

from openapi_server.models.painting import Painting  # noqa: E501
from openapi_server import util

def paintings_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Painting

    Gets a list of all instances of Painting (more information in http://dbpedia.org/ontology/Painting) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Painting]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PAINTING_TYPE_URI,
        rdf_type_name=PAINTING_TYPE_NAME, 
        kls=Painting)

def paintings_id_get(id):  # noqa: E501
    """Get a single Painting by its id

    Gets the details of a given Painting (more information in http://dbpedia.org/ontology/Painting) # noqa: E501

    :param id: The ID of the Painting to be retrieved
    :type id: str

    :rtype: Painting
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PAINTING_TYPE_URI,
        rdf_type_name=PAINTING_TYPE_NAME, 
        kls=Painting)
