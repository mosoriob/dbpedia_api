import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import BASEBALLSEASON_TYPE_NAME, BASEBALLSEASON_TYPE_URI

from openapi_server.models.baseball_season import BaseballSeason  # noqa: E501
from openapi_server import util

def baseballseasons_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of BaseballSeason

    Gets a list of all instances of BaseballSeason (more information in http://dbpedia.org/ontology/BaseballSeason) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[BaseballSeason]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=BASEBALLSEASON_TYPE_URI,
        rdf_type_name=BASEBALLSEASON_TYPE_NAME, 
        kls=BaseballSeason)

def baseballseasons_id_get(id):  # noqa: E501
    """Get a single BaseballSeason by its id

    Gets the details of a given BaseballSeason (more information in http://dbpedia.org/ontology/BaseballSeason) # noqa: E501

    :param id: The ID of the BaseballSeason to be retrieved
    :type id: str

    :rtype: BaseballSeason
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=BASEBALLSEASON_TYPE_URI,
        rdf_type_name=BASEBALLSEASON_TYPE_NAME, 
        kls=BaseballSeason)
