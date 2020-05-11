import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SOCCERCLUB_TYPE_NAME, SOCCERCLUB_TYPE_URI

from openapi_server.models.soccer_club import SoccerClub  # noqa: E501
from openapi_server import util

def soccerclubs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SoccerClub

    Gets a list of all instances of SoccerClub (more information in http://dbpedia.org/ontology/SoccerClub) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SoccerClub]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SOCCERCLUB_TYPE_URI,
        rdf_type_name=SOCCERCLUB_TYPE_NAME, 
        kls=SoccerClub)

def soccerclubs_id_get(id):  # noqa: E501
    """Get a single SoccerClub by its id

    Gets the details of a given SoccerClub (more information in http://dbpedia.org/ontology/SoccerClub) # noqa: E501

    :param id: The ID of the SoccerClub to be retrieved
    :type id: str

    :rtype: SoccerClub
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SOCCERCLUB_TYPE_URI,
        rdf_type_name=SOCCERCLUB_TYPE_NAME, 
        kls=SoccerClub)
