import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import POLITICALFUNCTION_TYPE_NAME, POLITICALFUNCTION_TYPE_URI

from openapi_server.models.political_function import PoliticalFunction  # noqa: E501
from openapi_server import util

def politicalfunctions_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PoliticalFunction

    Gets a list of all instances of PoliticalFunction (more information in http://dbpedia.org/ontology/PoliticalFunction) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PoliticalFunction]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=POLITICALFUNCTION_TYPE_URI,
        rdf_type_name=POLITICALFUNCTION_TYPE_NAME, 
        kls=PoliticalFunction)

def politicalfunctions_id_get(id):  # noqa: E501
    """Get a single PoliticalFunction by its id

    Gets the details of a given PoliticalFunction (more information in http://dbpedia.org/ontology/PoliticalFunction) # noqa: E501

    :param id: The ID of the PoliticalFunction to be retrieved
    :type id: str

    :rtype: PoliticalFunction
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=POLITICALFUNCTION_TYPE_URI,
        rdf_type_name=POLITICALFUNCTION_TYPE_NAME, 
        kls=PoliticalFunction)
