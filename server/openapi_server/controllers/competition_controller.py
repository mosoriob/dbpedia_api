import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import COMPETITION_TYPE_NAME, COMPETITION_TYPE_URI

from openapi_server.models.competition import Competition  # noqa: E501
from openapi_server import util

def competitions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Competition

    Gets a list of all instances of Competition (more information in http://dbpedia.org/ontology/Competition) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Competition]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=COMPETITION_TYPE_URI,
        rdf_type_name=COMPETITION_TYPE_NAME, 
        kls=Competition)

def competitions_id_get(id):  # noqa: E501
    """Get a single Competition by its id

    Gets the details of a given Competition (more information in http://dbpedia.org/ontology/Competition) # noqa: E501

    :param id: The ID of the Competition to be retrieved
    :type id: str

    :rtype: Competition
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=COMPETITION_TYPE_URI,
        rdf_type_name=COMPETITION_TYPE_NAME, 
        kls=Competition)
