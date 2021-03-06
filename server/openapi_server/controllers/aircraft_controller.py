import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import AIRCRAFT_TYPE_NAME, AIRCRAFT_TYPE_URI

from openapi_server.models.aircraft import Aircraft  # noqa: E501
from openapi_server import util

def aircrafts_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Aircraft

    Gets a list of all instances of Aircraft (more information in http://dbpedia.org/ontology/Aircraft) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Aircraft]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=AIRCRAFT_TYPE_URI,
        rdf_type_name=AIRCRAFT_TYPE_NAME, 
        kls=Aircraft)

def aircrafts_id_get(id):  # noqa: E501
    """Get a single Aircraft by its id

    Gets the details of a given Aircraft (more information in http://dbpedia.org/ontology/Aircraft) # noqa: E501

    :param id: The ID of the Aircraft to be retrieved
    :type id: str

    :rtype: Aircraft
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=AIRCRAFT_TYPE_URI,
        rdf_type_name=AIRCRAFT_TYPE_NAME, 
        kls=Aircraft)
