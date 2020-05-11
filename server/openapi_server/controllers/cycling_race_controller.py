import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import CYCLINGRACE_TYPE_NAME, CYCLINGRACE_TYPE_URI

from openapi_server.models.cycling_race import CyclingRace  # noqa: E501
from openapi_server import util

def cyclingraces_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of CyclingRace

    Gets a list of all instances of CyclingRace (more information in http://dbpedia.org/ontology/CyclingRace) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[CyclingRace]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=CYCLINGRACE_TYPE_URI,
        rdf_type_name=CYCLINGRACE_TYPE_NAME, 
        kls=CyclingRace)

def cyclingraces_id_get(id):  # noqa: E501
    """Get a single CyclingRace by its id

    Gets the details of a given CyclingRace (more information in http://dbpedia.org/ontology/CyclingRace) # noqa: E501

    :param id: The ID of the CyclingRace to be retrieved
    :type id: str

    :rtype: CyclingRace
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=CYCLINGRACE_TYPE_URI,
        rdf_type_name=CYCLINGRACE_TYPE_NAME, 
        kls=CyclingRace)
