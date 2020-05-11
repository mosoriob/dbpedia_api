import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ARTISTDISCOGRAPHY_TYPE_NAME, ARTISTDISCOGRAPHY_TYPE_URI

from openapi_server.models.artist_discography import ArtistDiscography  # noqa: E501
from openapi_server import util

def artistdiscographys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ArtistDiscography

    Gets a list of all instances of ArtistDiscography (more information in http://dbpedia.org/ontology/ArtistDiscography) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ArtistDiscography]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ARTISTDISCOGRAPHY_TYPE_URI,
        rdf_type_name=ARTISTDISCOGRAPHY_TYPE_NAME, 
        kls=ArtistDiscography)

def artistdiscographys_id_get(id):  # noqa: E501
    """Get a single ArtistDiscography by its id

    Gets the details of a given ArtistDiscography (more information in http://dbpedia.org/ontology/ArtistDiscography) # noqa: E501

    :param id: The ID of the ArtistDiscography to be retrieved
    :type id: str

    :rtype: ArtistDiscography
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ARTISTDISCOGRAPHY_TYPE_URI,
        rdf_type_name=ARTISTDISCOGRAPHY_TYPE_NAME, 
        kls=ArtistDiscography)
