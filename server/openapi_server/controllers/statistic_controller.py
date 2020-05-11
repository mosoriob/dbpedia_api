import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import STATISTIC_TYPE_NAME, STATISTIC_TYPE_URI

from openapi_server.models.statistic import Statistic  # noqa: E501
from openapi_server import util

def statistics_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Statistic

    Gets a list of all instances of Statistic (more information in http://dbpedia.org/ontology/Statistic) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Statistic]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=STATISTIC_TYPE_URI,
        rdf_type_name=STATISTIC_TYPE_NAME, 
        kls=Statistic)

def statistics_id_get(id):  # noqa: E501
    """Get a single Statistic by its id

    Gets the details of a given Statistic (more information in http://dbpedia.org/ontology/Statistic) # noqa: E501

    :param id: The ID of the Statistic to be retrieved
    :type id: str

    :rtype: Statistic
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=STATISTIC_TYPE_URI,
        rdf_type_name=STATISTIC_TYPE_NAME, 
        kls=Statistic)
