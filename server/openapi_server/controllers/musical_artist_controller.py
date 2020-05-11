import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MUSICALARTIST_TYPE_NAME, MUSICALARTIST_TYPE_URI

from openapi_server.models.musical_artist import MusicalArtist  # noqa: E501
from openapi_server import util

def musicalartists_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MusicalArtist

    Gets a list of all instances of MusicalArtist (more information in http://dbpedia.org/ontology/MusicalArtist) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MusicalArtist]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MUSICALARTIST_TYPE_URI,
        rdf_type_name=MUSICALARTIST_TYPE_NAME, 
        kls=MusicalArtist)

def musicalartists_id_get(id):  # noqa: E501
    """Get a single MusicalArtist by its id

    Gets the details of a given MusicalArtist (more information in http://dbpedia.org/ontology/MusicalArtist) # noqa: E501

    :param id: The ID of the MusicalArtist to be retrieved
    :type id: str

    :rtype: MusicalArtist
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MUSICALARTIST_TYPE_URI,
        rdf_type_name=MUSICALARTIST_TYPE_NAME, 
        kls=MusicalArtist)
