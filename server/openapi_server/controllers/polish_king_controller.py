import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import POLISHKING_TYPE_NAME, POLISHKING_TYPE_URI

from openapi_server.models.polish_king import PolishKing  # noqa: E501
from openapi_server import util

def polishkings_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PolishKing

    Gets a list of all instances of PolishKing (more information in http://dbpedia.org/ontology/PolishKing) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PolishKing]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=POLISHKING_TYPE_URI,
        rdf_type_name=POLISHKING_TYPE_NAME, 
        kls=PolishKing)

def polishkings_id_get(id):  # noqa: E501
    """Get a single PolishKing by its id

    Gets the details of a given PolishKing (more information in http://dbpedia.org/ontology/PolishKing) # noqa: E501

    :param id: The ID of the PolishKing to be retrieved
    :type id: str

    :rtype: PolishKing
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=POLISHKING_TYPE_URI,
        rdf_type_name=POLISHKING_TYPE_NAME, 
        kls=PolishKing)
