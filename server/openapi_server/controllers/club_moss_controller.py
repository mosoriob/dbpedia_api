import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CLUBMOSS_TYPE_NAME, CLUBMOSS_TYPE_URI

from openapi_server.models.club_moss import ClubMoss  # noqa: E501
from openapi_server import util

def clubmosss_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ClubMoss

    Gets a list of all instances of ClubMoss (more information in http://dbpedia.org/ontology/ClubMoss) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ClubMoss]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CLUBMOSS_TYPE_URI,
        rdf_type_name=CLUBMOSS_TYPE_NAME, 
        kls=ClubMoss)

def clubmosss_id_get(id):  # noqa: E501
    """Get a single ClubMoss by its id

    Gets the details of a given ClubMoss (more information in http://dbpedia.org/ontology/ClubMoss) # noqa: E501

    :param id: The ID of the ClubMoss to be retrieved
    :type id: str

    :rtype: ClubMoss
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CLUBMOSS_TYPE_URI,
        rdf_type_name=CLUBMOSS_TYPE_NAME, 
        kls=ClubMoss)
