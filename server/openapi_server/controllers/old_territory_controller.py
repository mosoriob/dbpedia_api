import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import OLDTERRITORY_TYPE_NAME, OLDTERRITORY_TYPE_URI

from openapi_server.models.old_territory import OldTerritory  # noqa: E501
from openapi_server import util

def oldterritorys_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of OldTerritory

    Gets a list of all instances of OldTerritory (more information in http://dbpedia.org/ontology/OldTerritory) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[OldTerritory]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=OLDTERRITORY_TYPE_URI,
        rdf_type_name=OLDTERRITORY_TYPE_NAME, 
        kls=OldTerritory)

def oldterritorys_id_get(id):  # noqa: E501
    """Get a single OldTerritory by its id

    Gets the details of a given OldTerritory (more information in http://dbpedia.org/ontology/OldTerritory) # noqa: E501

    :param id: The ID of the OldTerritory to be retrieved
    :type id: str

    :rtype: OldTerritory
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=OLDTERRITORY_TYPE_URI,
        rdf_type_name=OLDTERRITORY_TYPE_NAME, 
        kls=OldTerritory)
