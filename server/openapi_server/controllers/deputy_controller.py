import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import DEPUTY_TYPE_NAME, DEPUTY_TYPE_URI

from openapi_server.models.deputy import Deputy  # noqa: E501
from openapi_server import util

def deputys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Deputy

    Gets a list of all instances of Deputy (more information in http://dbpedia.org/ontology/Deputy) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Deputy]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=DEPUTY_TYPE_URI,
        rdf_type_name=DEPUTY_TYPE_NAME, 
        kls=Deputy)

def deputys_id_get(id):  # noqa: E501
    """Get a single Deputy by its id

    Gets the details of a given Deputy (more information in http://dbpedia.org/ontology/Deputy) # noqa: E501

    :param id: The ID of the Deputy to be retrieved
    :type id: str

    :rtype: Deputy
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=DEPUTY_TYPE_URI,
        rdf_type_name=DEPUTY_TYPE_NAME, 
        kls=Deputy)
