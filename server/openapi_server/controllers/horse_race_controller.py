import connexion
import six
from openapi_server import query_manager
from openapi_server.utils.vars import HORSERACE_TYPE_NAME, HORSERACE_TYPE_URI

from openapi_server.models.horse_race import HorseRace  # noqa: E501
from openapi_server import util

def horseraces_get(label=None, page=None, per_page=None):  # noqa: E501
    """List all instances of HorseRace

    Gets a list of all instances of HorseRace (more information in http://dbpedia.org/ontology/HorseRace) # noqa: E501

    :param label: Filter by label
    :type label: str
    :param page: Page number
    :type page: int
    :param per_page: Items per page
    :type per_page: int

    :rtype: List[HorseRace]
    """


    return query_manager.get_resource(
        label=label,
        page=page,
        per_page=per_page,
        rdf_type_uri=HORSERACE_TYPE_URI,
        rdf_type_name=HORSERACE_TYPE_NAME, 
        kls=HorseRace)

def horseraces_id_get(id):  # noqa: E501
    """Get a single HorseRace by its id

    Gets the details of a given HorseRace (more information in http://dbpedia.org/ontology/HorseRace) # noqa: E501

    :param id: The ID of the HorseRace to be retrieved
    :type id: str

    :rtype: HorseRace
    """


    return query_manager.get_resource(id=id,
        rdf_type_uri=HORSERACE_TYPE_URI,
        rdf_type_name=HORSERACE_TYPE_NAME, 
        kls=HorseRace)
