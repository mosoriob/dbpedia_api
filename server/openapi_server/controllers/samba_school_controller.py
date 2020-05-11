import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SAMBASCHOOL_TYPE_NAME, SAMBASCHOOL_TYPE_URI

from openapi_server.models.samba_school import SambaSchool  # noqa: E501
from openapi_server import util

def sambaschools_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SambaSchool

    Gets a list of all instances of SambaSchool (more information in http://dbpedia.org/ontology/SambaSchool) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SambaSchool]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SAMBASCHOOL_TYPE_URI,
        rdf_type_name=SAMBASCHOOL_TYPE_NAME, 
        kls=SambaSchool)

def sambaschools_id_get(id):  # noqa: E501
    """Get a single SambaSchool by its id

    Gets the details of a given SambaSchool (more information in http://dbpedia.org/ontology/SambaSchool) # noqa: E501

    :param id: The ID of the SambaSchool to be retrieved
    :type id: str

    :rtype: SambaSchool
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SAMBASCHOOL_TYPE_URI,
        rdf_type_name=SAMBASCHOOL_TYPE_NAME, 
        kls=SambaSchool)
