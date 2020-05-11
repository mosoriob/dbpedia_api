import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CHRISTIANPATRIARCH_TYPE_NAME, CHRISTIANPATRIARCH_TYPE_URI

from openapi_server.models.christian_patriarch import ChristianPatriarch  # noqa: E501
from openapi_server import util

def christianpatriarchs_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ChristianPatriarch

    Gets a list of all instances of ChristianPatriarch (more information in http://dbpedia.org/ontology/ChristianPatriarch) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ChristianPatriarch]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CHRISTIANPATRIARCH_TYPE_URI,
        rdf_type_name=CHRISTIANPATRIARCH_TYPE_NAME, 
        kls=ChristianPatriarch)

def christianpatriarchs_id_get(id):  # noqa: E501
    """Get a single ChristianPatriarch by its id

    Gets the details of a given ChristianPatriarch (more information in http://dbpedia.org/ontology/ChristianPatriarch) # noqa: E501

    :param id: The ID of the ChristianPatriarch to be retrieved
    :type id: str

    :rtype: ChristianPatriarch
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CHRISTIANPATRIARCH_TYPE_URI,
        rdf_type_name=CHRISTIANPATRIARCH_TYPE_NAME, 
        kls=ChristianPatriarch)
