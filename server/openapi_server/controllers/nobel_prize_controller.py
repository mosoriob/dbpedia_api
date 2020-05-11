import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import NOBELPRIZE_TYPE_NAME, NOBELPRIZE_TYPE_URI

from openapi_server.models.nobel_prize import NobelPrize  # noqa: E501
from openapi_server import util

def nobelprizes_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of NobelPrize

    Gets a list of all instances of NobelPrize (more information in http://dbpedia.org/ontology/NobelPrize) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[NobelPrize]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=NOBELPRIZE_TYPE_URI,
        rdf_type_name=NOBELPRIZE_TYPE_NAME, 
        kls=NobelPrize)

def nobelprizes_id_get(id):  # noqa: E501
    """Get a single NobelPrize by its id

    Gets the details of a given NobelPrize (more information in http://dbpedia.org/ontology/NobelPrize) # noqa: E501

    :param id: The ID of the NobelPrize to be retrieved
    :type id: str

    :rtype: NobelPrize
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=NOBELPRIZE_TYPE_URI,
        rdf_type_name=NOBELPRIZE_TYPE_NAME, 
        kls=NobelPrize)
