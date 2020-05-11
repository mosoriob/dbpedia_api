import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MEMBEROFPARLIAMENT_TYPE_NAME, MEMBEROFPARLIAMENT_TYPE_URI

from openapi_server.models.member_of_parliament import MemberOfParliament  # noqa: E501
from openapi_server import util

def memberofparliaments_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MemberOfParliament

    Gets a list of all instances of MemberOfParliament (more information in http://dbpedia.org/ontology/MemberOfParliament) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MemberOfParliament]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MEMBEROFPARLIAMENT_TYPE_URI,
        rdf_type_name=MEMBEROFPARLIAMENT_TYPE_NAME, 
        kls=MemberOfParliament)

def memberofparliaments_id_get(id):  # noqa: E501
    """Get a single MemberOfParliament by its id

    Gets the details of a given MemberOfParliament (more information in http://dbpedia.org/ontology/MemberOfParliament) # noqa: E501

    :param id: The ID of the MemberOfParliament to be retrieved
    :type id: str

    :rtype: MemberOfParliament
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MEMBEROFPARLIAMENT_TYPE_URI,
        rdf_type_name=MEMBEROFPARLIAMENT_TYPE_NAME, 
        kls=MemberOfParliament)
