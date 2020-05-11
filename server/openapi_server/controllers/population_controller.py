import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import POPULATION_TYPE_NAME, POPULATION_TYPE_URI

from openapi_server.models.population import Population  # noqa: E501
from openapi_server import util

def populations_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Population

    Gets a list of all instances of Population (more information in http://dbpedia.org/ontology/Population) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Population]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=POPULATION_TYPE_URI,
        rdf_type_name=POPULATION_TYPE_NAME, 
        kls=Population)

def populations_id_get(id):  # noqa: E501
    """Get a single Population by its id

    Gets the details of a given Population (more information in http://dbpedia.org/ontology/Population) # noqa: E501

    :param id: The ID of the Population to be retrieved
    :type id: str

    :rtype: Population
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=POPULATION_TYPE_URI,
        rdf_type_name=POPULATION_TYPE_NAME, 
        kls=Population)
