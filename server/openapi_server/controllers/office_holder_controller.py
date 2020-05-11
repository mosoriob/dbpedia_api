import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import OFFICEHOLDER_TYPE_NAME, OFFICEHOLDER_TYPE_URI

from openapi_server.models.office_holder import OfficeHolder  # noqa: E501
from openapi_server import util

def officeholders_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of OfficeHolder

    Gets a list of all instances of OfficeHolder (more information in http://dbpedia.org/ontology/OfficeHolder) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[OfficeHolder]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=OFFICEHOLDER_TYPE_URI,
        rdf_type_name=OFFICEHOLDER_TYPE_NAME, 
        kls=OfficeHolder)

def officeholders_id_get(id):  # noqa: E501
    """Get a single OfficeHolder by its id

    Gets the details of a given OfficeHolder (more information in http://dbpedia.org/ontology/OfficeHolder) # noqa: E501

    :param id: The ID of the OfficeHolder to be retrieved
    :type id: str

    :rtype: OfficeHolder
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=OFFICEHOLDER_TYPE_URI,
        rdf_type_name=OFFICEHOLDER_TYPE_NAME, 
        kls=OfficeHolder)
