import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import MIXEDMARTIALARTSEVENT_TYPE_NAME, MIXEDMARTIALARTSEVENT_TYPE_URI

from openapi_server.models.mixed_martial_arts_event import MixedMartialArtsEvent  # noqa: E501
from openapi_server import util

def mixedmartialartsevents_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of MixedMartialArtsEvent

    Gets a list of all instances of MixedMartialArtsEvent (more information in http://dbpedia.org/ontology/MixedMartialArtsEvent) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[MixedMartialArtsEvent]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=MIXEDMARTIALARTSEVENT_TYPE_URI,
        rdf_type_name=MIXEDMARTIALARTSEVENT_TYPE_NAME, 
        kls=MixedMartialArtsEvent)

def mixedmartialartsevents_id_get(id):  # noqa: E501
    """Get a single MixedMartialArtsEvent by its id

    Gets the details of a given MixedMartialArtsEvent (more information in http://dbpedia.org/ontology/MixedMartialArtsEvent) # noqa: E501

    :param id: The ID of the MixedMartialArtsEvent to be retrieved
    :type id: str

    :rtype: MixedMartialArtsEvent
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=MIXEDMARTIALARTSEVENT_TYPE_URI,
        rdf_type_name=MIXEDMARTIALARTSEVENT_TYPE_NAME, 
        kls=MixedMartialArtsEvent)
