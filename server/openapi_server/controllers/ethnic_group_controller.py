import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import ETHNICGROUP_TYPE_NAME, ETHNICGROUP_TYPE_URI

from openapi_server.models.ethnic_group import EthnicGroup  # noqa: E501
from openapi_server import util

def ethnicgroups_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of EthnicGroup

    Gets a list of all instances of EthnicGroup (more information in http://dbpedia.org/ontology/EthnicGroup) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[EthnicGroup]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=ETHNICGROUP_TYPE_URI,
        rdf_type_name=ETHNICGROUP_TYPE_NAME, 
        kls=EthnicGroup)

def ethnicgroups_id_get(id):  # noqa: E501
    """Get a single EthnicGroup by its id

    Gets the details of a given EthnicGroup (more information in http://dbpedia.org/ontology/EthnicGroup) # noqa: E501

    :param id: The ID of the EthnicGroup to be retrieved
    :type id: str

    :rtype: EthnicGroup
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=ETHNICGROUP_TYPE_URI,
        rdf_type_name=ETHNICGROUP_TYPE_NAME, 
        kls=EthnicGroup)
