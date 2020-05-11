import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PREHISTORICALPERIOD_TYPE_NAME, PREHISTORICALPERIOD_TYPE_URI

from openapi_server.models.prehistorical_period import PrehistoricalPeriod  # noqa: E501
from openapi_server import util

def prehistoricalperiods_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of PrehistoricalPeriod

    Gets a list of all instances of PrehistoricalPeriod (more information in http://dbpedia.org/ontology/PrehistoricalPeriod) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[PrehistoricalPeriod]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PREHISTORICALPERIOD_TYPE_URI,
        rdf_type_name=PREHISTORICALPERIOD_TYPE_NAME, 
        kls=PrehistoricalPeriod)

def prehistoricalperiods_id_get(id):  # noqa: E501
    """Get a single PrehistoricalPeriod by its id

    Gets the details of a given PrehistoricalPeriod (more information in http://dbpedia.org/ontology/PrehistoricalPeriod) # noqa: E501

    :param id: The ID of the PrehistoricalPeriod to be retrieved
    :type id: str

    :rtype: PrehistoricalPeriod
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PREHISTORICALPERIOD_TYPE_URI,
        rdf_type_name=PREHISTORICALPERIOD_TYPE_NAME, 
        kls=PrehistoricalPeriod)
