import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import VENUE_TYPE_NAME, VENUE_TYPE_URI

from openapi_server.models.venue import Venue  # noqa: E501
from openapi_server import util

def venues_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of Venue

    Gets a list of all instances of Venue (more information in http://dbpedia.org/ontology/Venue) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[Venue]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=VENUE_TYPE_URI,
        rdf_type_name=VENUE_TYPE_NAME, 
        kls=Venue)

def venues_id_get(id):  # noqa: E501
    """Get a single Venue by its id

    Gets the details of a given Venue (more information in http://dbpedia.org/ontology/Venue) # noqa: E501

    :param id: The ID of the Venue to be retrieved
    :type id: str

    :rtype: Venue
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=VENUE_TYPE_URI,
        rdf_type_name=VENUE_TYPE_NAME, 
        kls=Venue)
