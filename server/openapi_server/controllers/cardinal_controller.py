import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CARDINAL_TYPE_NAME, CARDINAL_TYPE_URI

from openapi_server.models.cardinal import Cardinal  # noqa: E501
from openapi_server import util

def cardinals_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Cardinal

    Gets a list of all instances of Cardinal (more information in http://dbpedia.org/ontology/Cardinal) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Cardinal]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CARDINAL_TYPE_URI,
        rdf_type_name=CARDINAL_TYPE_NAME, 
        kls=Cardinal)

def cardinals_id_get(id):  # noqa: E501
    """Get a single Cardinal by its id

    Gets the details of a given Cardinal (more information in http://dbpedia.org/ontology/Cardinal) # noqa: E501

    :param id: The ID of the Cardinal to be retrieved
    :type id: str

    :rtype: Cardinal
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CARDINAL_TYPE_URI,
        rdf_type_name=CARDINAL_TYPE_NAME, 
        kls=Cardinal)
