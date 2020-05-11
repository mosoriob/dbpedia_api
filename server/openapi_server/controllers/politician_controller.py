import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import POLITICIAN_TYPE_NAME, POLITICIAN_TYPE_URI

from openapi_server.models.politician import Politician  # noqa: E501
from openapi_server import util

def politicians_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Politician

    Gets a list of all instances of Politician (more information in http://dbpedia.org/ontology/Politician) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Politician]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=POLITICIAN_TYPE_URI,
        rdf_type_name=POLITICIAN_TYPE_NAME, 
        kls=Politician)

def politicians_id_get(id):  # noqa: E501
    """Get a single Politician by its id

    Gets the details of a given Politician (more information in http://dbpedia.org/ontology/Politician) # noqa: E501

    :param id: The ID of the Politician to be retrieved
    :type id: str

    :rtype: Politician
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=POLITICIAN_TYPE_URI,
        rdf_type_name=POLITICIAN_TYPE_NAME, 
        kls=Politician)
