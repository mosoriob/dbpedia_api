import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MARTIALARTIST_TYPE_NAME, MARTIALARTIST_TYPE_URI

from openapi_server.models.martial_artist import MartialArtist  # noqa: E501
from openapi_server import util

def martialartists_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MartialArtist

    Gets a list of all instances of MartialArtist (more information in http://dbpedia.org/ontology/MartialArtist) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MartialArtist]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MARTIALARTIST_TYPE_URI,
        rdf_type_name=MARTIALARTIST_TYPE_NAME, 
        kls=MartialArtist)

def martialartists_id_get(id):  # noqa: E501
    """Get a single MartialArtist by its id

    Gets the details of a given MartialArtist (more information in http://dbpedia.org/ontology/MartialArtist) # noqa: E501

    :param id: The ID of the MartialArtist to be retrieved
    :type id: str

    :rtype: MartialArtist
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MARTIALARTIST_TYPE_URI,
        rdf_type_name=MARTIALARTIST_TYPE_NAME, 
        kls=MartialArtist)
