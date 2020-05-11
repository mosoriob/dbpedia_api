import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import RUGBYCLUB_TYPE_NAME, RUGBYCLUB_TYPE_URI

from openapi_server.models.rugby_club import RugbyClub  # noqa: E501
from openapi_server import util

def rugbyclubs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of RugbyClub

    Gets a list of all instances of RugbyClub (more information in http://dbpedia.org/ontology/RugbyClub) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[RugbyClub]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=RUGBYCLUB_TYPE_URI,
        rdf_type_name=RUGBYCLUB_TYPE_NAME, 
        kls=RugbyClub)

def rugbyclubs_id_get(id):  # noqa: E501
    """Get a single RugbyClub by its id

    Gets the details of a given RugbyClub (more information in http://dbpedia.org/ontology/RugbyClub) # noqa: E501

    :param id: The ID of the RugbyClub to be retrieved
    :type id: str

    :rtype: RugbyClub
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=RUGBYCLUB_TYPE_URI,
        rdf_type_name=RUGBYCLUB_TYPE_NAME, 
        kls=RugbyClub)
