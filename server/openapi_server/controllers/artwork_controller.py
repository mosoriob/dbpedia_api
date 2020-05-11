import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ARTWORK_TYPE_NAME, ARTWORK_TYPE_URI

from openapi_server.models.artwork import Artwork  # noqa: E501
from openapi_server import util

def artworks_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Artwork

    Gets a list of all instances of Artwork (more information in http://dbpedia.org/ontology/Artwork) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Artwork]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ARTWORK_TYPE_URI,
        rdf_type_name=ARTWORK_TYPE_NAME, 
        kls=Artwork)

def artworks_id_get(id):  # noqa: E501
    """Get a single Artwork by its id

    Gets the details of a given Artwork (more information in http://dbpedia.org/ontology/Artwork) # noqa: E501

    :param id: The ID of the Artwork to be retrieved
    :type id: str

    :rtype: Artwork
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ARTWORK_TYPE_URI,
        rdf_type_name=ARTWORK_TYPE_NAME, 
        kls=Artwork)
