import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import PROTOHISTORICALPERIOD_TYPE_NAME, PROTOHISTORICALPERIOD_TYPE_URI

from openapi_server.models.protohistorical_period import ProtohistoricalPeriod  # noqa: E501
from openapi_server import util

def protohistoricalperiods_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of ProtohistoricalPeriod

    Gets a list of all instances of ProtohistoricalPeriod (more information in http://dbpedia.org/ontology/ProtohistoricalPeriod) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[ProtohistoricalPeriod]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=PROTOHISTORICALPERIOD_TYPE_URI,
        rdf_type_name=PROTOHISTORICALPERIOD_TYPE_NAME, 
        kls=ProtohistoricalPeriod)

def protohistoricalperiods_id_get(id):  # noqa: E501
    """Get a single ProtohistoricalPeriod by its id

    Gets the details of a given ProtohistoricalPeriod (more information in http://dbpedia.org/ontology/ProtohistoricalPeriod) # noqa: E501

    :param id: The ID of the ProtohistoricalPeriod to be retrieved
    :type id: str

    :rtype: ProtohistoricalPeriod
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=PROTOHISTORICALPERIOD_TYPE_URI,
        rdf_type_name=PROTOHISTORICALPERIOD_TYPE_NAME, 
        kls=ProtohistoricalPeriod)
