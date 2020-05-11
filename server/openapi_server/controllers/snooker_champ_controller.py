import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import SNOOKERCHAMP_TYPE_NAME, SNOOKERCHAMP_TYPE_URI

from openapi_server.models.snooker_champ import SnookerChamp  # noqa: E501
from openapi_server import util

def snookerchamps_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of SnookerChamp

    Gets a list of all instances of SnookerChamp (more information in http://dbpedia.org/ontology/SnookerChamp) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[SnookerChamp]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=SNOOKERCHAMP_TYPE_URI,
        rdf_type_name=SNOOKERCHAMP_TYPE_NAME, 
        kls=SnookerChamp)

def snookerchamps_id_get(id):  # noqa: E501
    """Get a single SnookerChamp by its id

    Gets the details of a given SnookerChamp (more information in http://dbpedia.org/ontology/SnookerChamp) # noqa: E501

    :param id: The ID of the SnookerChamp to be retrieved
    :type id: str

    :rtype: SnookerChamp
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=SNOOKERCHAMP_TYPE_URI,
        rdf_type_name=SNOOKERCHAMP_TYPE_NAME, 
        kls=SnookerChamp)
