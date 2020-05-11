import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SOCIETALEVENT_TYPE_NAME, SOCIETALEVENT_TYPE_URI

from openapi_server.models.societal_event import SocietalEvent  # noqa: E501
from openapi_server import util

def societalevents_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SocietalEvent

    Gets a list of all instances of SocietalEvent (more information in http://dbpedia.org/ontology/SocietalEvent) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SocietalEvent]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SOCIETALEVENT_TYPE_URI,
        rdf_type_name=SOCIETALEVENT_TYPE_NAME, 
        kls=SocietalEvent)

def societalevents_id_get(id):  # noqa: E501
    """Get a single SocietalEvent by its id

    Gets the details of a given SocietalEvent (more information in http://dbpedia.org/ontology/SocietalEvent) # noqa: E501

    :param id: The ID of the SocietalEvent to be retrieved
    :type id: str

    :rtype: SocietalEvent
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SOCIETALEVENT_TYPE_URI,
        rdf_type_name=SOCIETALEVENT_TYPE_NAME, 
        kls=SocietalEvent)
